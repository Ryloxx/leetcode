#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
#
# algorithms
# Medium (48.42%)
# Likes:    1219
# Dislikes: 62
# Total Accepted:    67.4K
# Total Submissions: 139.1K
# Testcase Example:  '[5,0,3,8,6]'
#
# Given an integer array nums, partition it into two (contiguous) subarrays
# left and right so that:
#
#
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
#
#
# Return the length of left after such a partitioning.
#
# Test cases are generated such that partitioning exists.
#
#
# Example 1:
#
#
# Input: nums = [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
#
#
# Example 2:
#
#
# Input: nums = [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^6
# There is at least one valid answer for the given input.
#
#
#
from itertools import accumulate
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def partitionDisjoint(self, nums: List[int]) -> int:
        right = reversed(list(accumulate(reversed(nums), func=min)))
        next(right, None)
        for length, (M, m) in enumerate(zip(accumulate(nums, func=max), right),
                                        1):
            if M <= m:
                return length
        return len(nums)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.partitionDisjoint, Solution()),
        [
            [[[5, 0, 3, 8, 6]], 3],
            [[[1, 1, 1, 0, 6, 12]], 4],
            [[[5, 4, 3, 2, 1, 0]], 6],
            [[[0, 0]], 1],
            [[[1, 0]], 2],
            [[[0, 1]], 1],
            [[[0, 1, 2]], 1],
            [[[2, 1, 0]], 3],
            [[[0, 0, 0]], 1],
        ],
    )
