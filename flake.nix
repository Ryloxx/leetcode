{
  outputs = { self, nixpkgs, flake-utils }:

    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = pkgs.python310Packages;
        nodePackages = pkgs.nodePackages;
      in
      {
        devShells.default = pkgs.mkShell {
          name = "leetcode";
          venvDir = "./.venv";
          buildInputs = with pythonPackages;[
            python
            black
            flake8
            venvShellHook
          ] ++
          (with nodePackages; [
            prettier
          ]) ++ (with pkgs;[
            pipenv
            rustup
            nodejs_18
            lint-staged
            husky
          ]);
          postShellHook = ''
            echo "pipenv install..."
            pipenv sync --dev > .dev_shell_out
          '';
        };
      });
}
