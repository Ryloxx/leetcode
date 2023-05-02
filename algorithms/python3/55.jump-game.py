#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (38.47%)
# Likes:    14375
# Dislikes: 750
# Total Accepted:    1.3M
# Total Submissions: 3.2M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for current in range(target, -1, -1):
            jump = nums[current]
            if current + jump >= target:
                target = current
        return not target


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.canJump, Solution()),
        [
            ([[3, 2, 1, 0, 4]], False),
            ([[2, 3, 1, 1, 4]], True),
            ([[0]], True),
            ([[1, 2, 3]], True),
            ([[1]], True),
            ([[2, 0]], True),
            ([[
                2, 0, 6, 9, 8, 4, 5, 0, 8, 9, 1, 2, 9, 6, 8, 8, 0, 6, 3, 1, 2,
                2, 1, 2, 6, 5, 3, 1, 2, 2, 6, 4, 2, 4, 3, 0, 0, 0, 3, 8, 2, 4,
                0, 1, 2, 0, 1, 4, 6, 5, 8, 0, 7, 9, 3, 4, 6, 6, 5, 8, 9, 3, 4,
                3, 7, 0, 4, 9, 0, 9, 8, 4, 3, 0, 7, 7, 1, 9, 1, 9, 4, 9, 0, 1,
                9, 5, 7, 7, 1, 5, 8, 2, 8, 2, 6, 8, 2, 2, 7, 5, 1, 7, 9, 6
            ]], False),
        ],
    )
