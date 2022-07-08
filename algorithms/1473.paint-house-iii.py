#
# @lc app=leetcode id=1473 lang=python3
#
# [1473] Paint House III
#
# https://leetcode.com/problems/paint-house-iii/description/
#
# algorithms
# Hard (50.82%)
# Likes:    889
# Dislikes: 70
# Total Accepted:    23K
# Total Submissions: 41.8K
# Testcase Example:  '[0,0,0,0,0]\n[[1,10],[10,1],[10,1],[1,10],[5,1]]
# \n5\n2\n3'
#
# There is a row of m houses in a small city, each house must be painted with
# one of the n colors (labeled from 1 to n), some houses that have been painted
# last summer should not be painted again.
#
# A neighborhood is a maximal group of continuous houses that are painted with
# the same color.
#
#
# For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2},
# {3,3}, {2}, {1,1}].
#
#
# Given an array houses, an m x n matrix cost and an integer target
# where:
#
#
# houses[i]: is the color of the house i, and 0 if the house is not painted
# yet.
# cost[i][j]: is the cost of paint the house i with the color j + 1.
#
#
# Return the minimum cost of painting all the remaining houses in such a way
# that there are exactly target neighborhoods. If it is not possible, return
# -1.
#
#
# Example 1:
#
#
# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m =
# 5, n = 2, target = 3
# Output: 9
# Explanation: Paint houses of this way [1,2,2,1,1]
# This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
# Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
#
#
# Example 2:
#
#
# Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m =
# 5, n = 2, target = 3
# Output: 11
# Explanation: Some houses are already painted, Paint the houses of this way
# [2,2,1,2,2]
# This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
# Cost of paint the first and last house (10 + 1) = 11.
#
#
# Example 3:
#
#
# Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n
# = 3, target = 3
# Output: -1
# Explanation: Houses are already painted with a total of 4 neighborhoods
# [{3},{1},{2},{3}] different of target = 3.
#
#
#
# Constraints:
#
#
# m == houses.length == cost.length
# n == cost[i].length
# 1 <= m <= 100
# 1 <= n <= 20
# 1 <= target <= m
# 0 <= houses[i] <= n
# 1 <= cost[i][j] <= 10^4
#
#
#
from functools import cache
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(T * M * N**2) time complexity
    # O(T * M * N) space complexity
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int,
                target: int) -> int:

        @cache
        def dp(i=0, last=-1, neigh=0):
            if i >= len(houses):
                if neigh == target:
                    return 0
                return float('inf')
            if neigh > target:
                return float('inf')
            return min(
                dp(i + 1, x, neigh + (x != last)) +
                (cost[i][x] if x != houses[i] - 1 else 0)
                for x in [range(n), [houses[i] - 1]][houses[i] != 0])

        return res if (res := dp()) != float('inf') else -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minCost, Solution()),
        [
            [[[0], [[1]], 1, 1, 1], 1],
            [[[1], [[1]], 1, 1, 1], 0],
            [[[0] * 100, [[1, 10] * 10 for _ in range(100)], 100, 20, 1], 100],
            [[[0] * 100, [[1, 10] * 10 for _ in range(100)], 100, 20, 0], -1],
            [[[0] * 100, [[1, 10] for _ in range(100)], 100, 2, 100], 550],
            [[[0] * 100, [[1, 10] * 10
                          for _ in range(100)], 100, 20, 100], 100],
            [[[0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5,
              2, 3], 11],
            [[[3, 1, 2, 3], [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3,
              3], -1],
            [[[0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5,
              2, 3], 9],
        ],
    )
