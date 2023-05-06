#
# @lc app=leetcode id=1498 lang=python3
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
#
# algorithms
# Medium (37.89%)
# Likes:    2602
# Dislikes: 232
# Total Accepted:    61.2K
# Total Submissions: 148.2K
# Testcase Example:  '[3,5,6,7]\n9'
#
# You are given an array of integers nums and an integer target.
#
# Return the number of non-empty subsequences of nums such that the sum of the
# minimum and maximum element on it is less or equal to target. Since the
# answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: nums = [3,5,6,7], target = 9
# Output: 4
# Explanation: There are 4 subsequences that satisfy the condition.
# [3] -> Min value + max value <= target (3 + 3 <= 9)
# [3,5] -> (3 + 5 <= 9)
# [3,5,6] -> (3 + 6 <= 9)
# [3,6] -> (3 + 6 <= 9)
#
#
# Example 2:
#
#
# Input: nums = [3,3,6,8], target = 10
# Output: 6
# Explanation: There are 6 subsequences that satisfy the condition. (nums can
# have repeated numbers).
# [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
#
#
# Example 3:
#
#
# Input: nums = [2,3,3,4,6,7], target = 12
# Output: 61
# Explanation: There are 63 non-empty subsequences, two of them do not satisfy
# the condition ([6,7], [7]).
# Number of valid subsequences (63 - 2 = 61).
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= target <= 10^6
#
#
#
from bisect import bisect_left
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 1000000007
        nums.sort()
        lo = hi = bisect_left(nums, (target // 2) + 1) - 1
        res = 0
        power = 1
        while lo >= 0:
            while hi < len(nums) - 1 and nums[lo] + nums[hi + 1] <= target:
                hi += 1
                power = (power * 2) % MOD
            res += power
            res %= MOD
            power = (power * 2) % MOD
            lo -= 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numSubseq, Solution()),
        [
            ([[3, 5, 6, 7], 9], 4),
            ([[3, 3, 6, 8], 10], 6),
            ([[2, 3, 3, 4, 6, 7], 12], 61),
            ([[3, 2, 4, 1, 5], 6], 21),
            ([[3, 5, 6, 7], 10], 9),
            ([[1] * 1000, 2], 688423209),
        ],
    )
