#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (40.71%)
# Likes:    3757
# Dislikes: 2281
# Total Accepted:    570.3K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and abs(i
# - j) <= k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
#
# Example 3:
#
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
#
#
#
from collections import Counter
# from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(N) time complexity
    # O(min(N, K)) space complexity
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = Counter()

        for idx in range(len(nums)):
            if memo[nums[idx]] > 0:
                return True
            memo[nums[idx]] += 1
            if idx >= k:
                memo[nums[idx - k]] -= 1
                if memo[nums[idx - k]] <= 0:
                    del memo[nums[idx - k]]
        return False

    # O(N) time complexity
    # O(N) space complexity
    #  def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     memo = defaultdict(lambda: -float('inf'))

    #     for idx, n in enumerate(nums):
    #         if idx - memo[n] <= k:
    #             return True
    #         memo[n] = idx
    #     return False


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.containsNearbyDuplicate, Solution()),
        [
            ([[1, 2, 3, 1], 3], True),
            ([[1, 0, 1, 1], 1], True),
            ([[1, 2, 3, 1, 2, 3], 2], False),
            ([[1, 2, 1, 4, 2, 3], 2], True),
        ],
    )
