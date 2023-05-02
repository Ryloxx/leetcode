#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
#
# algorithms
# Medium (33.59%)
# Likes:    2278
# Dislikes: 40
# Total Accepted:    60.9K
# Total Submissions: 174.6K
# Testcase Example:  '[1,1,4,2,3]\n5'
#
# You are given an integer array nums and an integer x. In one operation, you
# can either remove the leftmost or the rightmost element from the array nums
# and subtract its value from x. Note that this modifies the array for future
# operations.
#
# Return the minimum number of operations to reduce x to exactly 0 if it is
# possible, otherwise, return -1.
#
#
# Example 1:
#
#
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to
# reduce x to zero.
#
#
# Example 2:
#
#
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
#
#
# Example 3:
#
#
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and
# the first two elements (5 operations in total) to reduce x to zero.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= x <= 10^9
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:
        ax = sum(nums) - x
        if not ax:
            return len(nums)
        if ax < 0:
            return -1
        current, left, res = 0, 0, float('inf')
        for right, i in enumerate(nums):
            current += i
            while current > ax:
                current -= nums[left]
                left += 1
            if current == ax:
                res = min(res, len(nums) - (right - left + 1))

        return res if res != float('inf') else -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minOperations, Solution()),
        [
            [[[1, 1, 4, 2, 3], 5], 2],
            [[[2, 3, 1, 1, 1], 5], 2],
            [[[1, 1, 1], 3], 3],
            [[[5, 6, 7, 8, 9], 4], -1],
            [[[3, 2, 20, 1, 1, 3], 10], 5],
            [[[
                4, 4, 4, 4, 7, 3, 8, 2, 1, 6, 7, 3, 10, 1, 10, 5, 7, 2, 6, 10,
                5, 6, 10, 4, 5, 8, 4, 2, 10, 5, 8, 1, 9, 10, 3, 8, 8, 2, 1, 4,
                4, 7, 6, 6, 9, 4, 6, 7, 2, 5, 1, 9, 7, 5, 4, 10, 5, 1, 2, 9, 5,
                3, 1, 3, 7, 2, 5, 3, 1, 3, 3, 4, 4, 9, 6, 2, 6, 7, 1, 2, 8, 1,
                7, 2, 7, 4, 1, 7, 4, 7, 5, 4, 4, 8, 8, 4, 8, 6, 10, 6
            ], 99], 18],
            [[[
                10, 4, 3, 1, 4, 2, 4, 3, 8, 4, 4, 7, 10, 6, 8, 10, 9, 9, 3, 1,
                3, 7, 3, 2, 8, 4, 6, 8, 3, 3, 3, 3, 2, 7, 8, 2, 10, 2, 5, 6, 2,
                1, 9, 1, 4, 9, 3, 3, 1, 1, 8, 7, 10, 9, 8, 6, 7, 1, 8, 7, 5, 7,
                2, 9, 8, 9, 4, 7, 8, 2, 4, 5, 9, 9, 9, 9, 5, 9, 9, 9, 5, 1, 1,
                4, 1, 10, 4, 2, 9, 9, 2, 4, 5, 8, 1, 1, 4, 3, 9, 4
            ], 64], 13],
            [[[
                1, 7, 4, 4, 3, 1, 1, 1, 1, 4, 2, 2, 1, 9, 8, 4, 4, 1, 6, 2, 7,
                5, 7, 6, 5, 8, 1, 5, 1, 7, 8, 8, 10, 8, 2, 7, 3, 1, 6, 7, 9, 8,
                5, 7, 4, 3, 7, 2, 5, 4, 8, 4, 4, 10, 2, 1, 3, 5, 5, 1, 10, 9,
                1, 7, 6, 10, 4, 8, 6, 2, 6, 7, 6, 8, 6, 1, 6, 2, 8, 3, 9, 2, 8,
                3, 4, 5, 3, 4, 3, 5, 5, 5, 6, 5, 8, 3, 5, 5, 5, 4
            ], 75], 16],
            [[[1 for x in range(10**5)], 10**5], 10**5],
            [[[1 + x % 2 for x in range(10**5)], 10**5], 66_667],
        ],
    )
