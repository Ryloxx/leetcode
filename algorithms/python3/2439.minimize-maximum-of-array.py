#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#
# https://leetcode.com/problems/minimize-maximum-of-array/description/
#
# algorithms
# Medium (33.49%)
# Likes:    1461
# Dislikes: 360
# Total Accepted:    39.5K
# Total Submissions: 89.9K
# Testcase Example:  '[3,7,1,6]'
#
# You are given a 0-indexed array nums comprising of n non-negative integers.
#
# In one operation, you must:
#
#
# Choose an integer i such that 1 <= i < n and nums[i] > 0.
# Decrease nums[i] by 1.
# Increase nums[i - 1] by 1.
#
#
# Return the minimum possible value of the maximum integer of nums after
# performing any number of operations.
#
#
# Example 1:
#
#
# Input: nums = [3,7,1,6]
# Output: 5
# Explanation:
# One set of optimal operations is as follows:
# 1. Choose i = 1, and nums becomes [4,6,1,6].
# 2. Choose i = 3, and nums becomes [4,6,2,5].
# 3. Choose i = 1, and nums becomes [5,5,2,5].
# The maximum integer of nums is 5. It can be shown that the maximum number
# cannot be less than 5.
# Therefore, we return 5.
#
#
# Example 2:
#
#
# Input: nums = [10,1]
# Output: 10
# Explanation:
# It is optimal to leave nums as is, and since 10 is the maximum value, we
# return 10.
#
#
#
# Constraints:
#
#
# n == nums.length
# 2 <= n <= 10^5
# 0 <= nums[i] <= 10^9
#
#
#
from math import ceil
from typing import List
from algo_input import run
from types import MethodType

# @lc code=start


class Solution:

    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            res = max(res, ceil(prefix / (i + 1)))
        return res

    # def minimizeArrayValue(self, nums: List[int]) -> int:

    #     def is_good(val):
    #         bank = 0
    #         for n in nums:
    #             bank += max(0, val - n) - max(0, n - val)
    #             if bank < 0:
    #                 return False
    #         return True

    #     lo, hi = 0, max(nums, default=0)
    #     while lo < hi:
    #         mid = (lo + hi) // 2
    #         if is_good(mid):
    #             hi = mid
    #         else:
    #             lo = mid + 1
    #     return lo


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minimizeArrayValue, Solution()),
        [
            ([[3, 7, 1, 1, 1, 1, 1, 1, 1]], 5),
            ([[3, 7, 1, 6]], 5),
            ([[10, 1]], 10),
            ([[1, 10]], 6),
            ([[13, 13, 20, 0, 8, 9, 9]], 16),
            ([[6, 9, 3, 8, 14]], 8),
            ([[]], 0),
            ([[0]], 0),
        ],
    )
