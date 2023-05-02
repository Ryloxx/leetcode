#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/
#
# algorithms
# Medium (40.92%)
# Likes:    1006
# Dislikes: 44
# Total Accepted:    42.2K
# Total Submissions: 90.8K
# Testcase Example:  '[["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
# \n[1,2]'
#
# You are given an m x n matrix maze (0-indexed) with empty cells (represented
# as '.') and walls (represented as '+'). You are also given the entrance of
# the maze, where entrance = [entrancerow, entrancecol] denotes the row and
# column of the cell you are initially standing at.
#
# In one step, you can move one cell up, down, left, or right. You cannot step
# into a cell with a wall, and you cannot step outside the maze. Your goal is
# to find the nearest exit from the entrance. An exit is defined as an empty
# cell that is at the border of the maze. The entrance does not count as an
# exit.
#
# Return the number of steps in the shortest path from the entrance to the
# nearest exit, or -1 if no such path exists.
#
#
# Example 1:
#
#
# Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]],
# entrance = [1,2]
# Output: 1
# Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
# Initially, you are at the entrance cell [1,2].
# - You can reach [1,0] by moving 2 steps left.
# - You can reach [0,2] by moving 1 step up.
# It is impossible to reach [2,3] from the entrance.
# Thus, the nearest exit is [0,2], which is 1 step away.
#
#
# Example 2:
#
#
# Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
# Output: 2
# Explanation: There is 1 exit in this maze at [1,2].
# [1,0] does not count as an exit since it is the entrance cell.
# Initially, you are at the entrance cell [1,0].
# - You can reach [1,2] by moving 2 steps right.
# Thus, the nearest exit is [1,2], which is 2 steps away.
#
#
# Example 3:
#
#
# Input: maze = [[".","+"]], entrance = [0,0]
# Output: -1
# Explanation: There are no exits in this maze.
#
#
#
# Constraints:
#
#
# maze.length == m
# maze[i].length == n
# 1 <= m, n <= 100
# maze[i][j] is either '.' or '+'.
# entrance.length == 2
# 0 <= entrancerow < m
# 0 <= entrancecol < n
# entrance will always be an empty cell.
#
#
#
from algo_input import run
from types import MethodType
from typing import List
from collections import deque


# @lc code=start
class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque([(0, *entrance)])
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        while q:
            d, *cell = q.popleft()
            if (not cell[0] or not cell[1] or cell[0] == m - 1
                    or cell[1] == n - 1) and cell != entrance:
                return d
            for d_y, d_x in directions:
                n_y, n_x = cell[0] + d_y, cell[1] + d_x
                if 0 <= n_y < m and 0 <= n_x < n and maze[n_y][n_x] == ".":
                    maze[n_y][n_x] = "+"
                    q.append((d + 1, n_y, n_x))  # type: ignore

        return -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.nearestExit, Solution()),
        [
            ([[["+", "+", ".", "+"], [".", ".", ".", "+"],
               ["+", "+", "+", "."]], [1, 2]], 1),
            ([[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]], 2),
            ([[[".", "+"]], [0, 0]], -1),
            ([[["."]], [0, 0]], -1),
            ([[[".", "."]], [0, 0]], 1),
        ],
    )
