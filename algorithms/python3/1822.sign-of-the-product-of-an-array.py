#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#
# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
#
# algorithms
# Easy (65.94%)
# Likes:    1474
# Dislikes: 160
# Total Accepted:    213.7K
# Total Submissions: 323.9K
# Testcase Example:  '[-1,-2,-3,-4,3,2,1]'
#
# There is a function signFunc(x) that returns:
#
#
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
#
#
# You are given an integer array nums. Let product be the product of all values
# in the array nums.
#
# Return signFunc(product).
#
#
# Example 1:
#
#
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144)
# = 1
#
#
# Example 2:
#
#
# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) =
# 0
#
#
# Example 3:
#
#
# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) =
# -1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# -100 <= nums[i] <= 100
#
#
#
# from functools import reduce
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for x in nums:
            if not x:
                return 0
            if x < 0:
                res *= -1
        return res

    # def arraySign(self, nums: List[int]) -> int:
    #     return -1 if (res := reduce(lambda acc, e: acc * e,
    #                                 nums)) < 0 else 0 if res == 0 else 1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.arraySign, Solution()),
        [
            ([[-1, -2, -3, -4, 3, 2, 1]], 1),
            ([[1, 5, 0, 2, -3]], 0),
            ([[-1, 1, -1, 1, -1]], -1),
        ],
    )
