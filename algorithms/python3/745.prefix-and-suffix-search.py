#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#
# https://leetcode.com/problems/prefix-and-suffix-search/description/
#
# algorithms
# Hard (36.56%)
# Likes:    1099
# Dislikes: 334
# Total Accepted:    51.4K
# Total Submissions: 139.8K
# Testcase Example:  '["WordFilter","f"]\n[[["apple"]],["a","e"]]'
#
# Design a special dictionary with some words that searchs the words in it by a
# prefix and a suffix.
#
# Implement the WordFilter class:
#
#
# WordFilter(string[] words) Initializes the object with the words in the
# dictionary.
# f(string prefix, string suffix) Returns the index of the word in the
# dictionary, which has the prefix prefix and the suffix suffix. If there is
# more than one valid index, return the largest of them. If there is no such
# word in the dictionary, return -1.
#
#
#
# Example 1:
#
#
# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]
#
# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix =
# "a" and suffix = 'e".
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 15000
# 1 <= words[i].length <= 10
# 1 <= prefix.length, suffix.length <= 10
# words[i], prefix and suffix consist of lower-case English letters only.
# At most 15000 calls will be made to the function f.
#
#
#
from itertools import accumulate
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {(prefix, suffix): idx
                     for idx, w in enumerate(words) for prefix in accumulate(w)
                     for suffix in (w[x:] for x in range(len(w)))}

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.get((prefix, suffix), -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(
            WordFilter.f,
            WordFilter(
                ["apple", "boots", "rock", "loots", "brick", "role", "book"])),
        [
            [["boo", "ook"], 6],
            [["a", "e"], 0],
            [["ap", "le"], 0],
            [["", "oots"], -1],
            [["b", "ts"], 1],
            [["b", "k"], 6],
            [["boo", "k"], 6],
            [["boo", "oots"], 1],
            [["boo", "oot"], -1],
            [["brick", ""], -1],
            [["brick", "k"], 4],
        ],
    )
    run(
        MethodType(
            WordFilter.f,
            WordFilter([
                "cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa",
                "abcaccbcaa", "accabaccaa", "cabcbbbcca", "ababccabcb",
                "caccbbcbab", "bccbacbcba"
            ])),
        [[["ab", "abcaccbcaa"], 4], [["ac", "accabaccaa"], 5],
         [["bccbacbcba", "a"], 9], [["a", "aa"], 5],
         [["cabaaba", "abaaaa"], 0], [["cacc", "accbbcbab"], 8],
         [["ccbcab", "bac"], 1], [["bac", "cba"], 2], [["bcbb", "aa"], 3],
         [["ccbca", "cbcababac"], 1]],
    )
