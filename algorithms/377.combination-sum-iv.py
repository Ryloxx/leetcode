#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (49.49%)
# Likes:    4122
# Dislikes: 453
# Total Accepted:    276.1K
# Total Submissions: 547.1K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an array of distinct integers nums and a target integer target, return
# the number of possible combinations that add up to target.
#
# The test cases are generated so that the answer can fit in a 32-bit
# integer.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
#
#
# Example 2:
#
#
# Input: nums = [9], target = 3
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
#
#
#
# Follow up: What if negative numbers are allowed in the given array? How does
# it change the problem? What limitation we need to add to the question to
# allow negative numbers?
#
#
# from functools import cache
from itertools import takewhile
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # N = len(nums), M = target

    # O(N + MlogM + M * min(N, M)) time complexity
    # O(M) space complexity, same as the second solution but on average it uses
    # less space
    def combinationSum4(self, nums: List[int], target: int) -> int:
        m = 0
        for i in range(len(nums)):
            if nums[i] <= target:
                m = max(m, nums[i])
                nums[i] = nums[i] % target
            else:
                nums[i] = float('inf')
        nums.sort()
        if m <= 0:
            return 0
        dp = [0] * m
        dp[0] = 1
        for x in range(1, target + 1):
            dp[x % m] = sum(dp[(x - j) % m]
                            for j in takewhile(lambda j: j <= x, nums))
        return dp[target % m]

    # O(M * N) time complexity
    # O(M) space complexity
    # def combinationSum4(self, nums: List[int], target: int) -> int:

    #     @cache
    #     def dp(x):
    #         if x < 0:
    #             return 0
    #         if x == 0:
    #             return 1
    #         return sum(dp(x - i) for i in nums)

    #     return dp(target)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.combinationSum4, Solution()),
        [
            [[[
                3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                20, 21, 22, 23, 24, 25
            ], 10], 9],
            [[[1, 2, 3], 4], 7],
            [[[
                3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                20, 21, 22, 23, 24, 25
            ], 1], 0],
            [[[9], 3], 0],
            [[list(range(1, 200)), 31], 1073741824],
        ],
    )
