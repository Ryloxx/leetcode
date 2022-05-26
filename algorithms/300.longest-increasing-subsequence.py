#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (49.38%)
# Likes:    11950
# Dislikes: 235
# Total Accepted:    861.9K
# Total Submissions: 1.7M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting
# some or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
#
# Example 1:
#
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
#
# Example 3:
#
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
#
#

from bisect import bisect_left
from types import MethodType
from typing import List
from algo_input import run


# @lc code=start
class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if not res or res[-1] < i:
                res.append(i)
                continue
            res[bisect_left(res, i)] = i
        return len(res)


# @lc code=end

if __name__ == "__main__":
    run(MethodType(Solution.lengthOfLIS, Solution()), [
        [[[10, 9, 2, 5, 3, 7, 101, 18]], 4],
        [[[0, 1, 0, 3, 2, 3]], 4],
        [[[7, 7, 7, 7, 7, 7, 7]], 1],
        [[list(range(2500))], 2500],
    ])
