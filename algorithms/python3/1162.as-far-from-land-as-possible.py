#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#
# https://leetcode.com/problems/as-far-from-land-as-possible/description/
#
# algorithms
# Medium (48.55%)
# Likes:    3048
# Dislikes: 78
# Total Accepted:    102.4K
# Total Submissions: 205.1K
# Testcase Example:  '[[1,0,1],[0,0,0],[1,0,1]]'
#
# Given an n x n grid containing only values 0 and 1, where 0 represents water
# and 1 represents land, find a water cell such that its distance to the
# nearest land cell is maximized, and return the distance. If no land or water
# exists in the grid, return -1.
#
# The distance used in this problem is the Manhattan distance: the distance
# between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
#
#
# Example 1:
#
#
# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with
# distance 2.
#
#
# Example 2:
#
#
# Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: The cell (2, 2) is as far as possible from all the land with
# distance 4.
#
#
#
# Constraints:
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
#
#
#
from itertools import product
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        s = {(y, x) for y, x in product(range(m), range(n)) if grid[y][x]}
        seen = set()
        res = -1
        while s:
            seen.update(s)
            s = {(y, x)
                 for _y, _x in s for d_y, d_x in directions
                 for y, x in [[_y + d_y, _x + d_x]]
                 if (y, x) not in seen and 0 <= y < m and 0 <= x < n}
            res += 1
        return res or -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxDistance, Solution()),
        [
            ([[[1, 0, 1], [0, 0, 0], [1, 0, 1]]], 2),
            ([[[1, 0, 0], [0, 0, 0], [0, 0, 0]]], 4),
            ([[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]], -1),
            ([[[1, 1, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1],
               [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]], 1),
            ([[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]], -1),
        ],
    )
