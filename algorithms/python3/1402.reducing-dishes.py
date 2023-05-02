#
# @lc app=leetcode id=1402 lang=python3
#
# [1402] Reducing Dishes
#
# https://leetcode.com/problems/reducing-dishes/description/
#
# algorithms
# Hard (72.03%)
# Likes:    2339
# Dislikes: 239
# Total Accepted:    87.9K
# Total Submissions: 115.9K
# Testcase Example:  '[-1,-8,0,5,-7]'
#
# A chef has collected data on the satisfaction level of his n dishes. Chef can
# cook any dish in 1 unit of time.
#
# Like-time coefficient of a dish is defined as the time taken to cook that
# dish including previous dishes multiplied by its satisfaction level i.e.
# time[i] * satisfaction[i].
#
# Return the maximum sum of like-time coefficient that the chef can obtain
# after dishes preparation.
#
# Dishes can be prepared in any order and the chef can discard some dishes to
# get this maximum value.
#
#
# Example 1:
#
#
# Input: satisfaction = [-1,-8,0,5,-9]
# Output: 14
# Explanation: After Removing the second and last dish, the maximum total
# like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
# Each dish is prepared in one unit of time.
#
# Example 2:
#
#
# Input: satisfaction = [4,3,2]
# Output: 20
# Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)
#
#
# Example 3:
#
#
# Input: satisfaction = [-1,-4,-5]
# Output: 0
# Explanation: People do not like the dishes. No dish is prepared.
#
#
#
# Constraints:
#
#
# n == satisfaction.length
# 1 <= n <= 500
# -1000 <= satisfaction[i] <= 1000
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        dp = m = 0
        length = len(satisfaction)
        satisfaction.sort()
        for i in range(length):
            m += satisfaction[i]
            dp += (i + 1) * satisfaction[i]
        res = max(dp, 0)
        for i in range(1, length):
            dp = dp - m
            m -= satisfaction[i - 1]
            res = max(res, dp)
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxSatisfaction, Solution()),
        [
            ([[-1, -8, 0, 5, -9]], 14),
            ([[4, 3, 2]], 20),
            ([[-1, -4, -5]], 0),
        ],
    )
