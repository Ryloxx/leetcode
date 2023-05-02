#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#
# https://leetcode.com/problems/binary-trees-with-factors/description/
#
# algorithms
# Medium (43.67%)
# Likes:    1410
# Dislikes: 139
# Total Accepted:    52.3K
# Total Submissions: 112K
# Testcase Example:  '[2,4]'
#
# Given an array of unique integers, arr, where each integer arr[i] is strictly
# greater than 1.
#
# We make a binary tree using these integers, and each number may be used for
# any number of times. Each non-leaf node's value should be equal to the
# product of the values of its children.
#
# Return the number of binary trees we can make. The answer may be too large so
# return the answer modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
#
# Example 2:
#
#
# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2,
# 5], [10, 5, 2].
#
#
# Constraints:
#
#
# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 10^9
# All the values of arr are unique.
#
#
#
from functools import reduce
from math import sqrt
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def numFactoredBinaryTrees(self, nums: List[int]) -> int:
        nums.sort()
        MOD, dp = (7 + 10**9), {}
        for idx in range(len(nums)):
            n = nums[idx]
            dp[n] = 1
            limit = sqrt(n)
            for i in range(idx):
                a = nums[i]
                if a > limit:
                    break
                if n % a:
                    continue
                b = n // a
                if b not in dp:
                    continue
                dp[n] = (dp[n] + (dp[a] * dp[b] *
                                  (1 if a == b else 2) % MOD)) % MOD
        return reduce(lambda acc, curr: (acc + curr) % MOD, dp.values())


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numFactoredBinaryTrees, Solution()),
        [
            [[[2, 4, 8, 64]], 34],
            [[[2, 4]], 3],
            [[[2, 4, 5, 10]], 7],
            [[[
                46, 144, 5040, 4488, 544, 380, 4410, 34, 11, 5, 3063808, 5550,
                34496, 12, 540, 28, 18, 13, 2, 1056, 32710656, 31, 91872, 23,
                26, 240, 18720, 33, 49, 4, 38, 37, 1457, 3, 799, 557568, 32,
                1400, 47, 10, 20774, 1296, 9, 21, 92928, 8704, 29, 2162, 22,
                1883700, 49588, 1078, 36, 44, 352, 546, 19, 523370496, 476, 24,
                6000, 42, 30, 8, 16262400, 61600, 41, 24150, 1968, 7056, 7, 35,
                16, 87, 20, 2730, 11616, 10912, 690, 150, 25, 6, 14, 1689120,
                43, 3128, 27, 197472, 45, 15, 585, 21645, 39, 40, 2205, 17, 48,
                136
            ]], 509730797],
        ],
    )
