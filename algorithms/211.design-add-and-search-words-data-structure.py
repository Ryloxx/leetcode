#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (42.93%)
# Likes:    6318
# Dislikes: 360
# Total Accepted:    490.7K
# Total Submissions: 1.1M
# Testcase Example:  '["WordDictionary","addWord","addWord",
# "addWord","search","search","search","search"]\n' +
# '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports adding new words and finding if a
# string matches any previously added string.
#
# Implement the WordDictionary class:
#
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched
# later.
# bool search(word) Returns true if there is any string in the data structure
# that matches word or false otherwise. word may contain dots '.' where dots
# can be matched with any letter.
#
#
#
# Example:
#
#
# Input
#
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 3 dots in word for search queries.
# At most 10^4 calls will be made to addWord and search.
#
#
#
# from collections import defaultdict
from itertools import chain
from algo_input import run, wrapp_class


# @lc code=start
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for i in chain(word, "#"):
            curr = curr.setdefault(i, {})

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the
        dot character '.' to represent any one letter.
        """

        def dfs(curr, w, i=0):
            if i >= len(w):
                return "#" in curr
            if w[i] in curr:
                return dfs(curr[w[i]], w, i + 1)
            return w[i] == "." and any(dfs(x, w, i + 1) for x in curr.values())

        return dfs(self.root, word)


# class WordDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = defaultdict(set)

#     def addWord(self, word: str) -> None:
#         """
#         Adds a word into the data structure.
#         """
#         self.root[len(word)].add(word)

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the data structure. A word could contain
#         the dot character '.' to represent any one letter.
#         """
#         bucket = len(word)
#         if bucket not in self.root:
#             return False
#         if word in self.root[bucket]:
#             return True
#         if "." not in word:
#             return False
#         a = self.root[bucket]
#         for i, c in enumerate(word):
#             if c != ".":
#                 a = [x for x in a if x[i] == c]
#                 if not a:
#                     return False
#         return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
if __name__ == "__main__":
    run(
        wrapp_class(WordDictionary),
        [
            ([[],
              [
                  ["addWord", ["bad"]],
                  ["addWord", ["dad"]],
                  ["addWord", ["mad"]],
                  ["search", ["pad"]],
                  ["search", ["bad"]],
                  ["search", [".ad"]],
                  ["search", ["b.."]],
              ]], [None, None, None, False, True, True, True]),
        ],
    )
