#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#
# https://leetcode.com/problems/maximum-erasure-value/description/
#
# algorithms
# Medium (52.44%)
# Likes:    904
# Dislikes: 15
# Total Accepted:    44.1K
# Total Submissions: 83.7K
# Testcase Example:  '[4,2,4,5,6]'
#
# You are given an array of positive integers nums and want to erase a subarray
# containing unique elements. The score you get by erasing the subarray is
# equal to the sum of its elements.
#
# Return the maximum score you can get by erasing exactly one subarray.
#
# An array b is called to be a subarray of a if it forms a contiguous
# subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some
# (l,r).
#
#
# Example 1:
#
#
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
#
#
# Example 2:
#
#
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
#
#
#
# from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = right = res = current_sum = 0
        memo = [0] * (10**4 + 1)
        while right < len(nums):
            while memo[nums[right]]:
                current_sum -= nums[left]
                memo[nums[left]] = 0
                left += 1
            current_sum += nums[right]
            memo[nums[right]] = 1
            res = max(res, current_sum)
            right += 1
        return res

    # 2nd solution
    # def maximumUniqueSubarray(self, nums: List[int]) -> int:
    #     res = current_sum = 0
    #     memo, last_seen = defaultdict(int), defaultdict(lambda: -1)
    #     left = -1
    #     for right, num in enumerate(nums):
    #         current_sum += num
    #         left = max(left, last_seen[num])
    #         res = max(res, current_sum - memo[left])
    #         memo[right] = current_sum
    #         last_seen[num] = right
    #     return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maximumUniqueSubarray, Solution()),
        [
            [[[4, 2, 4, 5, 6]], 17],
            [[[1, 1, 1, 1]], 1],
            [[[0, 0, 0, 0]], 0],
            [[[5, 2, 1, 2, 5, 2, 1, 2, 5]], 8],
            [[[558, 508, 782, 32, 187, 103, 370, 607, 619, 267, 984, 10]], 5027
             ],
        ],
    )
