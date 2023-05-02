#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (58.94%)
# Likes:    6763
# Dislikes: 1130
# Total Accepted:    545.4K
# Total Submissions: 900.4K
# Testcase Example:  '[10,15,20]'
#
# You are given an integer array cost where cost[i] is the cost of i^th step on
# a staircase. Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
#
# Example 1:
#
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
#
#
# Example 2:
#
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
#
#
#
# Constraints:
#
#
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999
#
#
#
# from functools import cache
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(N) time complexity
    # O(1) space complexity
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        while not cost:
            return 0
        cost.append(0)
        for c in range(len(cost) - 3, -1, -1):
            cost[c] += min(cost[c + 1], cost[c + 2])
        return min(cost[0], cost[1])

    # O(N) time complexity
    # O(N) space complexity
    # def minCostClimbingStairs(self, cost: List[int]) -> int:

    #     @cache
    #     def dp(i):
    #         if i >= len(cost):
    #             return 0
    #         return cost[i] + min(dp(i + 2), dp(i + 1))

    #     return min(dp(0), dp(1))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minCostClimbingStairs, Solution()),
        [
            [[[]], 0],
            [[[0, 2, 1, 3]], 1],
            [[[10, 15, 20]], 15],
            [[[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]], 6],
        ],
    )
