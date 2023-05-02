#
# @lc app=leetcode id=576 lang=python3
#
# [576] Out of Boundary Paths
#
# https://leetcode.com/problems/out-of-boundary-paths/description/
#
# algorithms
# Medium (40.16%)
# Likes:    1656
# Dislikes: 185
# Total Accepted:    68.6K
# Total Submissions: 168.6K
# Testcase Example:  '2\n2\n2\n0\n0'
#
# There is an m x n grid with a ball. The ball is initially at the position
# [startRow, startColumn]. You are allowed to move the ball to one of the four
# adjacent cells in the grid (possibly out of the grid crossing the grid
# boundary). You can apply at most maxMove moves to the ball.
#
# Given the five integers m, n, maxMove, startRow, startColumn, return the
# number of paths to move the ball out of the grid boundary. Since the answer
# can be very large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
# Output: 6
#
#
# Example 2:
#
#
# Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
# Output: 12
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 50
# 0 <= maxMove <= 50
# 0 <= startRow < m
# 0 <= startColumn < n
#
#
#
from functools import cache
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int,
                  startColumn: int) -> int:
        MOD = 10**9 + 7
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        @cache
        def dp(y, x, remaining_moves):
            if y < 0 or x < 0 or y == m or x == n:
                return 1
            if remaining_moves == 0:
                return 0

            return sum(
                dp(y + dy, x + dx, remaining_moves - 1) % MOD
                for dy, dx in directions) % MOD

        return dp(startRow, startColumn, maxMove)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findPaths, Solution()),
        [
            [[1, 3, 3, 0, 1], 12],
            [[2, 2, 2, 0, 0], 6],
            [[2, 5, 11, 0, 0], 28832],
            [[7, 6, 13, 0, 2], 1659429],
        ],
    )
