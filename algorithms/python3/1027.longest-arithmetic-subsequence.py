#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Subsequence
#
# https://leetcode.com/problems/longest-arithmetic-subsequence/description/
#
# algorithms
# Medium (48.11%)
# Likes:    2149
# Dislikes: 99
# Total Accepted:    87.3K
# Total Submissions: 182K
# Testcase Example:  '[3,6,9,12]'
#
# Given an array nums of integers, return the length of the longest arithmetic
# subsequence in nums.
#
# Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ...,
# nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence
# seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= i <
# seq.length - 1).
#
#
# Example 1:
#
#
# Input: nums = [3,6,9,12]
# Output: 4
# Explanation:
# The whole array is an arithmetic sequence with steps of length = 3.
#
#
# Example 2:
#
#
# Input: nums = [9,4,7,2,10]
# Output: 3
# Explanation:
# The longest arithmetic subsequence is [4,7,10].
#
#
# Example 3:
#
#
# Input: nums = [20,1,15,3,10,5,8]
# Output: 4
# Explanation:
# The longest arithmetic subsequence is [20,15,10,5].
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 1000
# 0 <= nums[i] <= 500
#
#
#
# from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [[1] * 1001 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                r = nums[i] - nums[j] + 500
                dp[i][r] = dp[j][r] + 1
        return max(map(max, dp))

    # Using hashmap
    # def longestArithSeqLength(self, nums: List[int]) -> int:
    #     dp = defaultdict(int)
    #     for i in range(len(nums)):
    #         for j in range(i):
    #             r = nums[i] - nums[j]
    #             dp[i, r] = dp[j, r] + 1
    #     return max(dp.values()) + 1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestArithSeqLength, Solution()),
        [
            [[[9, 4, 7, 2, 10]], 3],
            [[[3, 6, 9, 12]], 4],
            [[[20, 1, 15, 3, 10, 5, 8]], 4],
        ],
    )
