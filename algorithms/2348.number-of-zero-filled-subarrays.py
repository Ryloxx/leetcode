#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#
# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
#
# algorithms
# Medium (57.31%)
# Likes:    1595
# Dislikes: 50
# Total Accepted:    81.7K
# Total Submissions: 124.1K
# Testcase Example:  '[1,3,0,0,2,0,0,4]'
#
# Given an integer array nums, return the number of subarrays filled with 0.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
# Example 1:
#
#
# Input: nums = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation:
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0.
# Therefore, we return 6.
#
# Example 2:
#
#
# Input: nums = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0.
# Therefore, we return 9.
#
#
# Example 3:
#
#
# Input: nums = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#
from itertools import chain
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = seq_len = 0
        for n in chain(nums, [-1]):
            if n:
                res += (seq_len * (seq_len + 1)) // 2
                seq_len = 0
            else:
                seq_len += 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.zeroFilledSubarray, Solution()),
        [
            ([[1, 3, 0, 0, 2, 0, 0, 4]], 6),
            ([[0, 0, 0, 2, 0, 0]], 9),
            ([[2, 10, 2019]], 0),
        ],
    )
