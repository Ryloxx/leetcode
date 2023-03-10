#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (52.88%)
# Likes:    11918
# Dislikes: 135
# Total Accepted:    617K
# Total Submissions: 1.1M
# Testcase Example:  '"horse"\n"ros"'
#
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
#
# Insert a character
# Delete a character
# Replace a character
#
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#
# Constraints:
#
#
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        a = len(word1)
        b = len(word2)
        dp = [[0 for y in range(b + 1)] for x in range(a + 1)]
        for i in range(1, a + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, b + 1):
            dp[0][i] = dp[0][i - 1] + 1
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minDistance, Solution()),
        [
            (["horse", "ros"], 3),
            (["intention", "execution"], 5),
        ],
    )
