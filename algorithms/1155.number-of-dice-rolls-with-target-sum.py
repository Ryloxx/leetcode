#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (47.76%)
# Likes:    2367
# Dislikes: 92
# Total Accepted:    120.1K
# Total Submissions: 247.8K
# Testcase Example:  '1\n6\n3'
#
# You have n dice and each die has k faces numbered from 1 to k.
#
# Given three integers n, k, and target, return the number of possible ways
# (out of the k^n total ways) to roll the dice so the sum of the face-up
# numbers equals target. Since the answer may be too large, return it modulo
# 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.
#
#
# Example 2:
#
#
# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
#
#
# Example 3:
#
#
# Input: n = 30, k = 30, target = 500
# Output: 222616187
# Explanation: The answer must be returned modulo 10^9 + 7.
#
#
#
# Constraints:
#
#
# 1 <= n, k <= 30
# 1 <= target <= 1000
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(2)]
        k = min(k, target)
        for i in range(1, k + 1):
            dp[0][i] = 1
        for _ in range(1, n):
            s = 0
            for i in range(1, target + 1):
                dp[1][i] = s = (s + dp[0][i - 1] -
                                dp[0][max(0, i - k - 1)]) % MOD
            dp[0], dp[1] = dp[1], dp[0]
        return dp[0][-1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numRollsToTarget, Solution()),
        [
            [[2, 6, 7], 6],
            [[1, 6, 3], 1],
            [[10, 10, 20], 92368],
            [[30, 30, 500], 222616187],
        ],
    )
