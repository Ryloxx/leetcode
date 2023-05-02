#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (48.73%)
# Likes:    11177
# Dislikes: 483
# Total Accepted:    766K
# Total Submissions: 1.6M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#
from functools import cache
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        @cache
        def f(x):
            if x not in nums:
                return 0
            return f(x - 1) + 1

        return max(map(f, nums), default=0)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestConsecutive, Solution()),
        [
            [[[0, 0, 0, 0, 0, 1]], 2],
            [[[0]], 1],
            [[[]], 0],
            [[[8, 9, 10, 5, 6, 7]], 6],
            [[[100, 4, 200, 1, 3, 2]], 4],
            [[[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], 9],
        ],
    )
