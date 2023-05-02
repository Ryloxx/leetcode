#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#
# https://leetcode.com/problems/wiggle-subsequence/description/
#
# algorithms
# Medium (45.01%)
# Likes:    2923
# Dislikes: 104
# Total Accepted:    147.4K
# Total Submissions: 322.9K
# Testcase Example:  '[1,7,4,9,2,5]'
#
# A wiggle sequence is a sequence where the differences between successive
# numbers strictly alternate between positive and negative. The first
# difference (if one exists) may be either positive or negative. A sequence
# with one element and a sequence with two non-equal elements are trivially
# wiggle sequences.
#
#
# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences
# (6, -3, 5, -7, 3) alternate between positive and negative.
# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences.
# The first is not because its first two differences are positive, and the
# second is not because its last difference is zero.
#
#
# A subsequence is obtained by deleting some elements (possibly zero) from the
# original sequence, leaving the remaining elements in their original order.
#
# Given an integer array nums, return the length of the longest wiggle
# subsequence of nums.
#
#
# Example 1:
#
#
# Input: nums = [1,7,4,9,2,5]
# Output: 6
# Explanation: The entire sequence is a wiggle sequence with differences (6,
# -3, 5, -7, 3).
#
#
# Example 2:
#
#
# Input: nums = [1,17,5,10,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that achieve this length.
# One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,4,5,6,7,8,9]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#
#
# Follow up: Could you solve this in O(n) time?
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 0
        while i < len(nums) - 2 and nums[i] == nums[i + 1]:
            i += 1
        last, res, switch = None, 0, nums[i + 1] > nums[i]
        for i in range(i, len(nums)):
            n = nums[i]
            if (last is None or (switch and last > n)
                    or (not switch and last < n)):
                res += 1
                switch = not switch
            last = n
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.wiggleMaxLength, Solution()),
        [
            [[[1, 1, 7, 4, 9, 2, 5]], 6],
            [[[0, 0, 0]], 1],
            [[[1, 17, 5, 10, 13, 15, 10, 5, 16, 8]], 7],
            [[[1, 7, 4, 9, 2, 5]], 6],
            [[[1, 2, 3, 4, 5, 6, 7, 8, 9]], 2],
            [[[84]], 1],
            [[[0, 0]], 1],
            [[[0, 1]], 2],
            [[[1, 14, 7, 14, 9, 14, 5]], 7],
            [[[2, 1, 7, 4, 9, 2, 5]], 7],
            [[[3, 3, 3, 2, 5]], 3],
        ],
    )
