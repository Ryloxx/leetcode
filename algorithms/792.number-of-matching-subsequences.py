#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (50.57%)
# Likes:    3276
# Dislikes: 158
# Total Accepted:    143.8K
# Total Submissions: 282.5K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given a string s and an array of strings words, return the number of words[i]
# that is a subsequence of s.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
#
# Example 1:
#
#
# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s:
# "a", "acd", "ace".
#
#
# Example 2:
#
#
# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.
#
#
#
from collections import Counter
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # M = len(s), N = len(words), K = len(words[i])
    # O(M + N * K) time complexity
    # O(M) space complexity
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        memo = [[-1] * 26]
        for i in range(len(s) - 1, -1, -1):
            memo.append(list(memo[-1]))
            memo[-1][ord(s[i]) - ord('a')] = i + 1
        res = len(words)
        words = Counter(words)
        for w in words:
            i = 0
            for c in w:
                i = memo[len(s) - i][ord(c) - ord('a')]
                if i < 0:
                    res -= words[w]
                    break
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numMatchingSubseq, Solution()),
        [
            [["qsjdklf", ["", "", "", ""]], 4],
            [["abcde", ["a", "bb", "acd", "ace", "ee"]], 3],
            [["", ["", "bb", "acd", "ace"]], 1],
            [["g" * (5 * 10**4 - 1) + "c", ["g" * 49 + "c"] * 5000], 5000],
            [["dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]], 2],
        ],
    )
