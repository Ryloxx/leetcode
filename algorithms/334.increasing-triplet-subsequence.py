#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (41.52%)
# Likes:    5775
# Dislikes: 261
# Total Accepted:    351.5K
# Total Submissions: 824.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given an integer array nums, return true if there exists a triple of indices
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
# indices exists, return false.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
#
#
# Example 2:
#
#
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
#
#
# Example 3:
#
#
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] ==
# 4 < nums[5] == 6.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^5
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#
# Follow up: Could you implement a solution that runs in O(n) time complexity
# and O(1) space complexity?
#
from bisect import bisect_left
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:
        res = []
        for i in nums:
            if not res or res[-1] < i:
                res.append(i)
                if len(res) == 3:
                    return True
                continue
            res[bisect_left(res, i)] = i
        return False


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.increasingTriplet, Solution()),
        [
            ([[1, 2, 3, 4, 5]], True),
            ([[20, 100, 10, 12, 5, 13]], True),
            ([[5, 4, 3, 2, 1]], False),
            ([[2, 1, 5, 0, 4, 6]], True),
        ],
    )
