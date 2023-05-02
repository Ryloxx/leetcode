#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#
# https://leetcode.com/problems/unique-paths-iii/description/
#
# algorithms
# Hard (79.72%)
# Likes:    3625
# Dislikes: 151
# Total Accepted:    137.1K
# Total Submissions: 171.1K
# Testcase Example:  '[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]'
#
# You are given an m x n integer array grid where grid[i][j] could be:
#
#
# 1 representing the starting square. There is exactly one starting square.
# 2 representing the ending square. There is exactly one ending square.
# 0 representing empty squares we can walk over.
# -1 representing obstacles that we cannot walk over.
#
#
# Return the number of 4-directional walks from the starting square to the
# ending square, that walk over every non-obstacle square exactly once.
#
#
# Example 1:
#
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#
#
# Example 2:
#
#
# Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
#
#
# Example 3:
#
#
# Input: grid = [[0,1],[2,0]]
# Output: 0
# Explanation: There is no path that walks over every empty square exactly
# once.
# Note that the starting and ending square can be anywhere in the grid.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 20
# 1 <= m * n <= 20
# -1 <= grid[i][j] <= 2
# There is exactly one starting cell and one ending cell.
#
#
#
from itertools import product
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # O(3**(M * N)) time complexity
    # O(M * N) space complexity
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = start_y = start_x = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for y, x in product(range(m), range(n)):
            if grid[y][x] == 1:
                start_y, start_x = y, x
                grid[y][x] = 0
            count += grid[y][x] == 0

        def dfs(y, x):
            if not (0 <= y < m and 0 <= x < n):
                return 0
            nonlocal count
            if not count and grid[y][x] == 2:
                return 1
            if grid[y][x] != 0:
                return 0
            count -= 1
            prev, grid[y][x] = grid[y][x], -1
            res = sum(dfs(y + dy, x + dx) for dy, dx in directions)
            grid[y][x] = prev
            count += 1
            return res

        return dfs(start_y, start_x)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.uniquePathsIII, Solution()),
        [
            ([[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]], 2),
            ([[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]], 4),
            ([[[0, 1], [2, 0]]], 0),
        ],
    )
