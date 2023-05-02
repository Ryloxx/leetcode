#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#
# https://leetcode.com/problems/word-subsets/description/
#
# algorithms
# Medium (52.59%)
# Likes:    1021
# Dislikes: 132
# Total Accepted:    51.8K
# Total Submissions: 99K
# Testcase Example:  '["amazon","apple","facebook","google","leetcode"]\n
# ["e","o"]'
#
# You are given two string arrays words1 and words2.
#
# A string b is a subset of string a if every letter in b occurs in a including
# multiplicity.
#
#
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
#
#
# A string a from words1 is universal if for every string b in words2, b is a
# subset of a.
#
# Return an array of all the universal strings in words1. You may return the
# answer in any order.
#
#
# Example 1:
#
#
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 =
# ["e","o"]
# Output: ["facebook","google","leetcode"]
#
#
# Example 2:
#
#
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 =
# ["l","e"]
# Output: ["apple","google","leetcode"]
#
#
#
# Constraints:
#
#
# 1 <= words1.length, words2.length <= 10^4
# 1 <= words1[i].length, words2[i].length <= 10
# words1[i] and words2[i] consist only of lowercase English letters.
# All the strings of words1 are unique.
#
#
#
from collections import Counter, defaultdict
from typing import List
from algo_input import run, any_order
from types import MethodType


# @lc code=start
class Solution:
    # N = len(words1), K = len(words1[i]), M = len(words2), Q = len(words2[i])
    # O(M * Q + N * K) time complexity
    # O(1) space complexity
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        base = Counter()
        for w in words2:
            temp = defaultdict(int)
            for c in w:
                temp[c] += 1
                base[c] = max(base[c], temp[c])
        return [w for w in words1 if not base - Counter(w)]


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.wordSubsets, Solution()), [
        [[["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"]],
         ["facebook", "google"]],
        [[["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]],
         ["facebook", "google", "leetcode"]],
        [[["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]],
         ["apple", "google", "leetcode"]],
        [[["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"]],
         ["google", "leetcode"]],
    ],
        comparator=any_order)
