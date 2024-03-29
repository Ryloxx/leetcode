#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#
# https://leetcode.com/problems/where-will-the-ball-fall/description/
#
# algorithms
# Medium (66.54%)
# Likes:    2373
# Dislikes: 142
# Total Accepted:    99.3K
# Total Submissions: 138.9K
# Testcase Example:
# '[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]'
#
# You have a 2-D grid of size m x n representing a box, and you have n balls.
# The box is open on the top and bottom sides.
#
# Each cell in the box has a diagonal board spanning two corners of the cell
# that can redirect a ball to the right or to the left.
#
#
# A board that redirects the ball to the right spans the top-left corner to the
# bottom-right corner and is represented in the grid as 1.
# A board that redirects the ball to the left spans the top-right corner to the
# bottom-left corner and is represented in the grid as -1.
#
#
# We drop one ball at the top of each column of the box. Each ball can get
# stuck in the box or fall out of the bottom. A ball gets stuck if it hits a
# "V" shaped pattern between two boards or if a board redirects the ball into
# either wall of the box.
#
# Return an array answer of size n where answer[i] is the column that the ball
# falls out of at the bottom after dropping the ball from the i^th column at
# the top, or -1 if the ball gets stuck in the box.
#
#
# Example 1:
#
#
#
#
# Input: grid =
# [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
# Output: [1,-1,-1,-1,-1]
# Explanation: This example is shown in the photo.
# Ball b0 is dropped at column 0 and falls out of the box at column 1.
# Ball b1 is dropped at column 1 and will get stuck in the box between column 2
# and 3 and row 1.
# Ball b2 is dropped at column 2 and will get stuck on the box between column 2
# and 3 and row 0.
# Ball b3 is dropped at column 3 and will get stuck on the box between column 2
# and 3 and row 0.
# Ball b4 is dropped at column 4 and will get stuck on the box between column 2
# and 3 and row 1.
#
#
# Example 2:
#
#
# Input: grid = [[-1]]
# Output: [-1]
# Explanation: The ball gets stuck against the left wall.
#
#
# Example 3:
#
#
# Input: grid =
# [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
# Output: [0,1,2,3,4,-1]
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is 1 or -1.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # Iterative
    # O(M * N) time complexity
    # O(1) space complexity

    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = list(range(n))
        for y in range(m):
            for x in range(n):
                if res[x] < 0:
                    continue
                c_x = res[x]
                res[x] += grid[y][c_x]
                if (c_x > 0 and grid[y][c_x - 1] - grid[y][c_x]
                        == 2) or (c_x < n - 1 and grid[y][c_x] -
                                  grid[y][c_x + 1] == 2) or res[x] == n:
                    res[x] = -1
        return res

    # DFS
    # O(M * N) time complexity
    # O(M) space complexity
    # def findBall(self, grid: List[List[int]]) -> List[int]:
    #     m, n = len(grid), len(grid[0])

    #     def dfs(c_x, y):
    #         if y >= m:
    #             return c_x
    #         n_x = c_x + grid[y][c_x]
    #         if ((c_x > 0 and grid[y][c_x - 1] - grid[y][c_x] == 2)
    #                 or (c_x < n - 1 and grid[y][c_x] - grid[y][c_x + 1] == 2)
    #                 or not -1 < n_x < n):
    #             return -1
    #         return dfs(n_x, y + 1)

    #     return [dfs(x, 0) for x in range(n)]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findBall, Solution()),
        [
            ([[[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1],
               [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]], [1, -1, -1, -1, -1]),
            ([[[-1]]], [-1]),
            ([[[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1], [
                1, 1, 1, 1, 1, 1
            ], [-1, -1, -1, -1, -1, -1]]], [0, 1, 2, 3, 4, -1]),
            ([[[-1, 1, -1, -1, -1, -1]]], [-1, -1, -1, 2, 3, 4]),
            ([[[
                -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1,
                -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, -1,
                -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, 1,
                -1, 1, -1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1,
                -1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, 1,
                -1, -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, -1
            ]]], [
                -1, -1, -1, 2, 3, 4, 5, 6, -1, -1, 9, 10, 11, 14, -1, -1, 15,
                16, 19, 20, -1, -1, 21, 24, -1, -1, 25, -1, -1, 28, 29, 30, 31,
                32, 33, 34, 35, -1, -1, -1, -1, 40, 41, 42, 43, 44, 45, -1, -1,
                48, -1, -1, -1, -1, 53, 56, -1, -1, -1, -1, 59, 60, 61, 64, 65,
                66, 67, 68, -1, -1, 71, 72, -1, -1, 75, 76, -1, -1, 77, 78, -1,
                -1, -1, -1, 83, 86, -1, -1, 87, -1, -1, -1, -1, 94, 95, -1, -1,
                96, 97, 98
            ]),
        ],
    )
