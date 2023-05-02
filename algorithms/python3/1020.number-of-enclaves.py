#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#
# https://leetcode.com/problems/number-of-enclaves/description/
#
# algorithms
# Medium (65.10%)
# Likes:    2395
# Dislikes: 43
# Total Accepted:    101.8K
# Total Submissions: 154.5K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# You are given an m x n binary matrix grid, where 0 represents a sea cell and
# 1 represents a land cell.
#
# A move consists of walking from one land cell to another adjacent
# (4-directionally) land cell or walking off the boundary of the grid.
#
# Return the number of land cells in grid for which we cannot walk off the
# boundary of the grid in any number of moves.
#
#
# Example 1:
#
#
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is
# not enclosed because its on the boundary.
#
#
# Example 2:
#
#
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.
#
#
#
from itertools import chain, product
from types import MethodType
from typing import List

from algo_input import run


# @lc code=start
class Solution:

    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(y, x):
            if not (0 <= y < m and 0 <= x < n) or not grid[y][x]:
                return
            grid[y][x] = 0
            for dy, dx in directions:
                dfs(y + dy, x + dx)

        for y, x in chain(product([0, m - 1], range(n)),
                          product(range(m), [0, n - 1])):
            dfs(y, x)
        return sum(x for y in grid for x in y)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numEnclaves, Solution()),
        [
            ([[[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]], 3),
            ([[[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]], 0),
            ([[[0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
               [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
               [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1],
               [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
               [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
               [0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
               [1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
               [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]]], 11),
        ],
    )
