#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (40.11%)
# Likes:    11878
# Dislikes: 315
# Total Accepted:    1.2M
# Total Submissions: 2.9M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def bisect_left(self, arr, target):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if target <= arr[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = self.bisect_left(
            nums, target), self.bisect_left(nums, target + 1) - 1
        return [start, end
                ] if start < len(nums) and nums[start] == target else [-1, -1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.searchRange, Solution()),
        [
            [[[5, 7, 7, 8, 8, 10], 8], [3, 4]],
            [[[5, 7, 7, 8, 8, 10], 6], [-1, -1]],
            [[[], 0], [-1, -1]],
            [[[1], 1], [0, 0]],
            [[[2, 2], 2], [0, 1]],
        ],
    )
