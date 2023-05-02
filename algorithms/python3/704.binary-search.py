#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (55.13%)
# Likes:    8847
# Dislikes: 185
# Total Accepted:    1.7M
# Total Submissions: 3M
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
#
# Example 2:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo if nums[lo] == target else -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.search, Solution()),
        [
            ([[-1, 0, 3, 5, 9, 12], 9], 4),
            ([[-1, 0, 3, 5, 9, 12], 2], -1),
        ],
    )
