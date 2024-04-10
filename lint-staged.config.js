const { statSync, readdirSync } = require("fs");
const path = require("path");
/**
 * @param {string} filePath
 */
const findRustRootDir = (filePath) => {
  let current_path = filePath;
  let prev_path = "";
  while (prev_path != current_path) {
    const s = statSync(current_path);
    if (s.isDirectory()) {
      const files = readdirSync(current_path);
      if (
        files.some((fileName) => {
          return fileName === "Cargo.toml";
        })
      ) {
        return current_path;
      }
    }
    prev_path = current_path;
    current_path = path.resolve(current_path, "../");
  }
  throw new Error("file is not part of a rust project");
};

module.exports = {
  "*.py": ["black", "flake8"],
  "*.rs":
    /**
     * @param {string[]} allRustFiles
     */
    (allRustFiles) => {
      console.log(allRustFiles);
      return Array.from(new Set(allRustFiles.map(findRustRootDir))).map(
        (root) => `./clippy-dirty.sh -u -b files -r ${root} -- -- -D warnings`,
      );
    },
  "**/*.{js,jsx,ts,tsx}": "prettier --write",
};
