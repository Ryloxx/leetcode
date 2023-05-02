#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (60.76%)
# Likes:    7588
# Dislikes: 283
# Total Accepted:    350.8K
# Total Submissions: 571.3K
# Testcase Example:  '"bbbab"'
#
# Given a string s, find the longest palindromic subsequence's length in s.
#
# A subsequence is a sequence that can be derived from another sequence by
# deleting some or no elements without changing the order of the remaining
# elements.
#
#
# Example 1:
#
#
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def longestPalindromeSubseq(self, s: str) -> int:
        if len(set(s)) == 1:
            return len(s)
        dp = [[1 if x == y else 0 for y in range(len(s))]
              for x in range(len(s))]
        for left in range(1, len(s)):
            for i in range(len(s) - left):
                j = i + left
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][-1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestPalindromeSubseq, Solution()),
        [
            (["bbbab"], 4),
            (["cbbd"], 2),
        ],
    )
