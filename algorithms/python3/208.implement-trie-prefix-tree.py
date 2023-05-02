#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (61.18%)
# Likes:    9435
# Dislikes: 116
# Total Accepted:    768.2K
# Total Submissions: 1.2M
# Testcase Example:  '["Trie","insert","search","search",
# "startsWith","insert","search"]\n' +
# '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
#
# Implement the Trie class:
#
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
#
#
#
# Example 1:
#
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and
# startsWith.
#
#
#
from algo_input import run, wrapp_class


# @lc code=start
class Trie:

    def __init__(self):
        self.data = {}

    def insert(self, word: str) -> None:
        node = self.data
        for c in word:
            node = node.setdefault(c, {})
        node["#"] = True

    def search(self, word: str) -> bool:
        node = self.data
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return "#" in node

    def startsWith(self, prefix: str) -> bool:
        node = self.data
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
if __name__ == "__main__":
    run(
        wrapp_class(Trie),
        [
            ([[],
              [
                  ["insert", ["apple"]],
                  ["search", ["apple"]],
                  ["search", ["app"]],
                  ["startsWith", ["app"]],
                  ["insert", ["app"]],
                  ["search", ["app"]],
              ]], [None, True, False, True, None, True]),
        ],
    )
