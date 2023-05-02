#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
#
# algorithms
# Medium (57.08%)
# Likes:    1941
# Dislikes: 86
# Total Accepted:    111.7K
# Total Submissions: 190.5K
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of size n, return the minimum number of moves
# required to make all array elements equal.
#
# In one move, you can increment or decrement an element of the array by 1.
#
# Test cases are designed so that the answer will fit in a 32-bit integer.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one
# element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
#
#
# Example 2:
#
#
# Input: nums = [1,10,2,9]
# Output: 16
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = nums[len(nums) // 2]
        return sum(abs(n - i) for i in nums)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minMoves2, Solution()),
        [
            [[[1, 2, 3]], 2],
            [[[2]], 0],
            [[[2, 2, 2, 2, 2]], 0],
            [[[2, 100]], 98],
            [[[1, 10, 2, 9]], 16],
            [[[
                45, 60, 92, 13, 38, 62, 65, 11, 30, 30, 73, 1, 42, 12, 60, 93,
                76, 18, 5, 78, 13, 29, 17, 30, 66, 64, 52, 95, 77, 28, 89, 3,
                35, 56, 53, 9, 91, 54, 15, 35, 20, 18, 25, 76, 35, 69, 24, 98,
                90, 19, 71, 36, 62, 57, 91, 35, 79, 87, 68, 59, 6, 50, 63, 79,
                93, 47, 89, 3, 27, 50, 5, 58, 53, 47, 58, 62, 49, 23, 10, 79,
                100, 60, 11, 37, 95, 93, 23, 41, 96, 10, 48, 95, 10, 21, 1, 29,
                83, 11, 32, 14
            ]], 2541],
        ],
    )
