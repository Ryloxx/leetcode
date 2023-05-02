#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.25%)
# Likes:    13653
# Dislikes: 437
# Total Accepted:    799.6K
# Total Submissions: 1.8M
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers nums and an integer k, return the total number of
# subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -1000 <= nums[i] <= 1000
# -10^7 <= k <= 10^7
#
#
#
from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = defaultdict(int, {0: 1})
        current_sum = res = 0
        for n in nums:
            current_sum += n
            res += memo[current_sum - k]
            memo[current_sum] += 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.subarraySum, Solution()),
        [
            [[[1, 1, 1], 2], 2],
            [[[1, 2, 3], 3], 2],
        ],
    )
