#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (64.32%)
# Likes:    12974
# Dislikes: 387
# Total Accepted:    1.7M
# Total Submissions: 2.6M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
#
#
#
from collections import defaultdict
from typing import List
from algo_input import run, any_order
from types import MethodType


# @lc code=start
class Solution:

    # O(NK) time complexity
    # O(N * K) space complexity
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = defaultdict(list)
        for w in strs:
            a = [0] * 26
            for c in w:
                a[ord(c) - ord('a')] += 1
            memo[tuple(a)].append(w)
        return list(memo.values())

    # O(NKlogK) time complexity
    # O(N * K) space complexity
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     memo = defaultdict(list)
    #     for w in strs:
    #         memo[tuple(sorted(w))].append(w)
    #     return list(memo.values())


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.groupAnagrams, Solution()), [
        ([["eat", "tea", "tan", "ate", "nat", "bat"]
          ], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([[""]], [[]]),
        ([["a"]], [["a"]]),
        ([["", ""]], [["", ""]]),
        ([["ddddddddddg", "dgggggggggg"]], [["dgggggggggg"], ["ddddddddddg"]]),
        ([[
            "ara", "god", "moo", "mig", "wan", "cut", "wow", "lie", "jim",
            "sox", "toe", "rep", "ill", "got", "set", "bud", "sue", "day",
            "bib", "run", "mar", "bib", "zoe", "fog", "lad", "pea", "oct",
            "red"
        ]], [["lad"], ["pea"], ["fog"], ["mar"], ["sue"], ["run"], ["bud"],
             ["got"], ["wan"], ["god"], ["zoe"], ["cut"], ["oct"], ["day"],
             ["moo"], ["red"], ["bib", "bib"], ["toe"], ["mig"], ["wow"],
             ["jim"], ["ara"], ["ill"], ["lie"], ["sox"], ["set"], ["rep"]]),
    ],
        comparator=lambda a, b: any_order(*[["".join(sorted(x)) for x in y]
                                            for y in [a, b]]))
