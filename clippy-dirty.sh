#!/usr/bin/env bash

set -e

function print-help {
    echo "USAGE"
    echo "    clippy-dirty [options] [--] [clippy-options]"
    echo
    echo "OPTIONS"
    echo "    -b files  Shows messages only for the files you've modified"
    echo "              (this is the default behavior)"
    echo
    echo "    -b lines  Shows messages only for the lines you've modified"
    echo "              (it's more restrictive than '-b files')"
    echo
    echo "    -u        Ignore untracked files"
    echo
    echo "    -h        Prints this help"
    echo
    echo "Arguments after '--' get passed into clippy:"
    echo "    clippy-dirty -- -p workspace-crate"
    echo "    clippy-dirty -- --all-targets --all-features"
    echo "    clippy-dirty -- -- -D clippy::new_without_default"
    echo "    clippy-dirty -b lines -- -- -D clippy::new_without_default"
    echo
    echo "Same for environmental variables:"
    echo "    RUSTFLAGS=\"-D warnings\" clippy-dirty"
}

# Invokes `git status` and prepares a list of all the modified
# (created / updated / deleted) files, both tracked and untracked.
#
# Output
#   files: string[]
function find-dirty-files {
    files=()

    while read -r _ a _ _ _ _ _ _ b _; do
        local file

        # When a file is untracked, we get its name in `$a` and when it's
        # tracked, inside `$b`.
        if [[ -z "$b" ]]; then
            if [[ "${show_untracked}" == "no" ]]; then
                continue;
            fi

            file="$a"
        else
            file="$b"
        fi

        # When a directory is untracked, `git status` returns path to the
        # directory instead of concrete file name - in such cases we've got to
        # manually traverse the entire directory.
        if [[ -d "$file" ]]; then
            while read -r file; do
                files+=("$file")
            done < <(find "$file" -type f)
        else
            files+=("$file")
        fi
    done < <(git status --porcelain=2)
}

# Escapes slashes, quotes etc. inside the file name so that it can be passed
# straight into jq.
function jq-escape-file {
    printf "%s" "$1" | jq -R -s '.'
}

# Builds a condition that gets passed into `jq` for when `-b files` has been
# enabled.
#
# Input
#   files: string[]
#
# Output
#   jq_where: string
function build-condition-for-dirty-files {
    jq_where="false"

    for file in "${files[@]}"; do
        jq_file=$(jq-escape-file "$file")
        jq_where="$jq_where or .file_name == $jq_file"
    done
}

# Builds a condition that gets passed into `jq` for when `-b lines` has been
# enabled.
#
# Input
#   files: string[]
#
# Output
#   jq_where: string
function build-condition-for-dirty-lines {
    jq_where="false"

    for file in "${files[@]}"; do
        # Since we can't invoke `git blame` on untracked files, when we find
        # one, we're not trying to track down particular lines and just accept
        # messages for the entire file

        if [[ -z $(git ls-files "$file") ]]; then
            jq_file=$(jq-escape-file "$file")
            jq_where="$jq_where or .file_name == $jq_file"
        else
            while read -r commit _ line _; do
                if [[ ! "$commit" == "0000000000000000000000000000000000000000" ]]; then
                    continue
                fi

                jq_file=$(jq-escape-file "$file")
                jq_where="$jq_where or (.file_name == $jq_file and .line_start >= $line and .line_end <= $line)"
            done < <(git blame --incremental "$file")
       fi
    done
}

# Input:
#   jq_where: string
function launch-clippy {
    while read -r msg; do
        echo -e "$msg"
    done < <(
        cargo -C $root -Z unstable-options clippy --quiet --message-format=json-diagnostic-rendered-ansi "$@" | jq "
            select(. | type == \"object\")
            | select(has(\"message\"))
            | select(any(.message.spans[]; $jq_where))
            | .message.rendered
        " --unbuffered --raw-output
    )
}

# ------------------ #
# Check dependencies #

for app in "cargo" "git" "jq"; do
    if ! [[ -x "$(command -v ${app})" ]]; then
      echo "error: '$app' is not installed" >&2
      exit 1
    fi
done

# --------------- #
# Parse arguments #

basis="files"
show_untracked="yes"
root=.
while getopts "b:r:hu" opt; do
    case "$opt" in
       "b")
           basis="$OPTARG"
           ;;

       "r")
           root="$OPTARG"
           ;;

        "h")
            print-help
            exit
            ;;

        "u")
            show_untracked="no"
            ;;

        *)
            echo "error: '$OPTARG' is not a valid argument" >&2
            exit 1
            ;;
    esac
done

shift $((OPTIND -1))

if [[ ! "$basis" =~ ^(files|lines)$ ]]; then
    echo "error: unknown basis '$basis'" >&2
    echo "hint: please try '-h' for help" >&2
    exit 2
fi

# --------------------------- #
# Let's get the party started #

echo '[+] Searching for dirty files'

find-dirty-files

if [[ ${#files[@]} -eq 0 ]]; then
    echo "warn: No files are dirty, nothing to do"
    exit 0
fi

echo " -  Found ${#files[@]} files"

if [[ "$basis" == "files" ]]; then
    build-condition-for-dirty-files
else
    echo
    echo '[+] Searching for dirty lines'
    build-condition-for-dirty-lines
fi

echo
echo '[+] Launching clippy'
echo

launch-clippy "$@"