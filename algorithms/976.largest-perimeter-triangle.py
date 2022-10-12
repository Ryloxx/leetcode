#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#
# https://leetcode.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (55.18%)
# Likes:    2185
# Dislikes: 298
# Total Accepted:    158.3K
# Total Submissions: 289.8K
# Testcase Example:  '[2,1,2]'
#
# Given an integer array nums, return the largest perimeter of a triangle with
# a non-zero area, formed from three of these lengths. If it is impossible to
# form any triangle of a non-zero area, return 0.
#
#
# Example 1:
#
#
# Input: nums = [2,1,2]
# Output: 5
#
#
# Example 2:
#
#
# Input: nums = [1,2,1]
# Output: 0
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^6
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.largestPerimeter, Solution()),
        [
            ([[2, 1, 2]], 5),
            ([[1, 2, 1]], 0),
        ],
    )
