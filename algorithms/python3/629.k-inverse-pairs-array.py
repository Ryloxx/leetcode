#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#
# https://leetcode.com/problems/k-inverse-pairs-array/description/
#
# algorithms
# Hard (37.29%)
# Likes:    989
# Dislikes: 131
# Total Accepted:    29.6K
# Total Submissions: 76.2K
# Testcase Example:  '3\n0'
#
# For an integer array nums, an inverse pair is a pair of integers [i, j] where
# 0 <= i < j < nums.length and nums[i] > nums[j].
#
# Given two integers n and k, return the number of different arrays consist of
# numbers from 1 to n such that there are exactly k inverse pairs. Since the
# answer can be huge, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 3, k = 0
# Output: 1
# Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has
# exactly 0 inverse pairs.
#
#
# Example 2:
#
#
# Input: n = 3, k = 1
# Output: 2
# Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
# 0 <= k <= 1000
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    MOD = 10**9 + 7

    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(k + 1):
                if not j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (
                        (dp[i][j - 1] + dp[i - 1][j]) % Solution.MOD -
                        (dp[i - 1][j - i] if i <= j else 0)) % Solution.MOD
        return (dp[n][k] - (dp[n][k - 1] if k > 0 else 0)) % Solution.MOD


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.kInversePairs, Solution()),
        [
            [[5, 2], 9],
            [[6, 2], 14],
            [[3, 0], 1],
            [[3, 1], 2],
            [[5, 1], 4],
            [[1000, 1000], 663677020],
        ],
    )
