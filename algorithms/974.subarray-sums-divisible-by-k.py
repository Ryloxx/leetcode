#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (53.59%)
# Likes:    3975
# Dislikes: 157
# Total Accepted:    132.8K
# Total Submissions: 247.9K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an integer array nums and an integer k, return the number of non-empty
# subarrays that have a sum divisible by k.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
#
#
# Example 2:
#
#
# Input: nums = [5], k = 9
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# 2 <= k <= 10^4
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def subarraysDivByK(self, A: List[int], K: int):

        curr_sum = count = 0
        mods = [1] + [0] * (K - 1)

        for num in A:
            curr_sum += num
            mod = curr_sum % K
            count += mods[mod]
            mods[mod] += 1
        return count


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.subarraysDivByK, Solution()),
        [
            ([[4, 5, 0, -2, -3, 1], 5], 7),
            ([[5], 9], 0),
        ],
    )
