#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/
#
# algorithms
# Hard (43.65%)
# Likes:    1810
# Dislikes: 36
# Total Accepted:    44.2K
# Total Submissions: 72.8K
# Testcase Example:  '[1,3,5,2,7,5]\n1\n5'
#
# You are given an integer array nums and two integers minK and maxK.
#
# A fixed-bound subarray of nums is a subarray that satisfies the following
# conditions:
#
#
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
#
#
# Return the number of fixed-bound subarrays.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
#
#
# Example 2:
#
#
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10
# possible subarrays.
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^5
# 1 <= nums[i], minK, maxK <= 10^6
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = m = M = -1
        res = 0
        for idx, x in enumerate(nums):
            if not (minK <= x <= maxK):
                left = idx
                continue
            if x == minK:
                m = idx
            if x == maxK:
                M = idx
            res += max(0, min(m, M) - left)
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.countSubarrays, Solution()),
        [
            ([[1, 3, 5, 2, 7, 5], 1, 5], 2),
            ([[1, 1, 1, 1], 1, 1], 10),
            ([[0, 0, 0, 0], 1, 1], 0),
            ([[1], 1, 1], 1),
            ([[1, 5], 1, 5], 1),
        ],
    )
