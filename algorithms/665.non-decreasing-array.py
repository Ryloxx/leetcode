#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Medium (21.57%)
# Likes:    3774
# Dislikes: 671
# Total Accepted:    178.7K
# Total Submissions: 817.8K
# Testcase Example:  '[4,2,3]'
#
# Given an array nums with n integers, your task is to check if it could become
# non-decreasing by modifying at most one element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for
# every i (0-based) such that (0 <= i <= n - 2).
#
#
# Example 1:
#
#
# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
#
#
# Example 2:
#
#
# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^4
# -10^5 <= nums[i] <= 10^5
#
#
#
from itertools import accumulate, repeat
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        nums += list(accumulate(repeat(2, 3), initial=10**5 + 2))
        token = False
        if nums[0] > nums[1]:
            token = True
            nums[0] = nums[1]
        for idx in range(len(nums) - 4):
            a, b, c, d = nums[idx], nums[idx + 1], nums[idx + 2], nums[idx + 3]
            if b > c:
                if token:
                    return False
                if a <= c:
                    nums[idx + 1] = a
                elif b <= d:
                    nums[idx + 2] = b
                else:
                    return False
                token = True
        return True


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.checkPossibility, Solution()),
        [
            [[[1, 4, 1, 2]], True],
            [[[1, 1, 1]], True],
            [[[1, 3, 2]], True],
            [[[4, 2, 3]], True],
            [[[4, 2, 2]], True],
            [[[4, 2, 1]], False],
            [[[1, 2, 3]], True],
            [[[1, 2, 3, 3]], True],
            [[[4, 2, 3, 3]], True],
        ],
    )
