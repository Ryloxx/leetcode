#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (37.59%)
# Likes:    4728
# Dislikes: 375
# Total Accepted:    515.1K
# Total Submissions: 1.4M
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# You are given an m x n integer array grid. There is a robot initially located
# at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either
# down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that
# the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach
# the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to
# 2 * 10^9.
#
#
# Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
#
# Constraints:
#
#
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.
#
#
#

from types import MethodType
from typing import List
import algo_input

# @lc code=start


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        if not n:
            return 0
        m = len(obstacleGrid[0])
        if not m:
            return 0
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        prev_r, next_r = [0] * m, [0] * m
        next_r[0] = 1
        for y in range(n):
            for x in range(m):
                top = prev_r[x]
                left = next_r[x - 1] if x > 0 else 1 if (y, x) == (0, 0) else 0
                next_r[x] = 0 if obstacleGrid[y][x] else top + left
            prev_r, next_r = next_r, prev_r
        return prev_r[-1]


# @lc code=end
algo_input.run(
    MethodType(Solution.uniquePathsWithObstacles, Solution()),
    [[[[[0, 0, 0], [0, 1, 0], [0, 0, 0]]], 2], [[[[0, 1], [0, 0]]], 1]],
)
