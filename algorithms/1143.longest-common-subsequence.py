#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (58.65%)
# Likes:    9820
# Dislikes: 114
# Total Accepted:    619.8K
# Total Submissions: 1.1M
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
# A common subsequence of two strings is a subsequence that is common to both
# strings.
#
#
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#
# Constraints:
#
#
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s = False
        right = 0
        l1, l2 = len(text1), len(text2)
        row = [0] * l1 * 2
        for i in range(l2):
            left, s = 0, not s
            for j in range(l1):
                up, topleft = row[
                    j + l1 *
                    (not s)], row[j - 1 + l1 *
                                  (not s)] + 1 if i > 0 and j > 0 else 1
                right = topleft if text2[i] == text1[
                    j] else left if left > up else up
                left = row[j + l1 * s] = right
        return right


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestCommonSubsequence, Solution()),
        [
            (["abcde", "ace"], 3),
            (["abc", "abc"], 3),
            (["abc", "def"], 0),
        ],
    )
