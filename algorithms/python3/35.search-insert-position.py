#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.15%)
# Likes:    12360
# Dislikes: 536
# Total Accepted:    2M
# Total Submissions: 4.7M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
#
#
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
#
# Example 2:
#
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
#
# Example 3:
#
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
#
#
#
# from bisect import bisect_left
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # Lazy
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     return bisect_left(nums, target)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.searchInsert, Solution()),
        [
            ([[1, 3, 5, 6], 5], 2),
            ([[1, 3, 5, 6], 2], 1),
            ([[1, 3, 5, 6], 7], 4),
        ],
    )
