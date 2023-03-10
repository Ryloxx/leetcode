#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#
# https://leetcode.com/problems/domino-and-tromino-tiling/description/
#
# algorithms
# Medium (48.42%)
# Likes:    2655
# Dislikes: 825
# Total Accepted:    88.5K
# Total Submissions: 166.9K
# Testcase Example:  '3'
#
# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You
# may rotate these shapes.
#
# Given an integer n, return the number of ways to tile an 2 x n board. Since
# the answer may be very large, return it modulo 10^9 + 7.
#
# In a tiling, every square must be covered by a tile. Two tilings are
# different if and only if there are two 4-directionally adjacent cells on the
# board such that exactly one of the tilings has both squares occupied by a
# tile.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def numTilings(self, n: int) -> int:
        if not n:
            return 1
        MOD = 10**9 + 7
        dp = [0] * 1001
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        for i in range(4, n + 1):
            dp[i] = 2 * dp[i - 1] + dp[i - 3]
            dp[i] %= MOD
        return dp[n]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numTilings, Solution()),
        [
            ([3], 5),
            ([1], 1),
            ([4], 11),
        ],
    )
