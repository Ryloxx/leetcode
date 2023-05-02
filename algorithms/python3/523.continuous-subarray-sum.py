#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (27.31%)
# Likes:    3960
# Dislikes: 390
# Total Accepted:    363.6K
# Total Submissions: 1.3M
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# Given an integer array nums and an integer k, return true if nums has a
# continuous subarray of size at least two whose elements sum up to a multiple
# of k, or false otherwise.
#
# An integer x is a multiple of k if there exists an integer n such that x = n
# * k. 0 is always a multiple of k.
#
#
# Example 1:
#
#
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up
# to 6.
#
#
# Example 2:
#
#
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose
# elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
#
#
# Example 3:
#
#
# Input: nums = [23,2,6,4,7], k = 13
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9
# 0 <= sum(nums[i]) <= 2^31 - 1
# 1 <= k <= 2^31 - 1
#
#
#
from itertools import accumulate
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        memo = {0: 0}
        for idx, i in enumerate(accumulate(nums)):
            if memo.setdefault(i % k, idx + 1) < idx:
                return True
        return False


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.checkSubarraySum, Solution()),
        [
            ([[7919] * 15, 15], True),
            ([[23, 2, 6, 4, 7, 10], 6], True),
            ([[23, 2, 4, 6, 7], 6], True),
            ([[23, 2, 6, 4, 7], 13], False),
            ([[1, 0], 2], False),
            ([[5, 0, 0, 0], 3], True),
        ],
    )
