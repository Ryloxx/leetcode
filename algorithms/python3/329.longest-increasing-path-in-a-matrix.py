#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (49.99%)
# Likes:    5354
# Dislikes: 92
# Total Accepted:    328.4K
# Total Submissions: 657.3K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an m x n integers matrix, return the length of the longest increasing
# path in matrix.
#
# From each cell, you can either move in four directions: left, right, up, or
# down. You may not move diagonally or move outside the boundary (i.e.,
# wrap-around is not allowed).
#
#
# Example 1:
#
#
# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
#
#
# Example 2:
#
#
# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
#
#
# Example 3:
#
#
# Input: matrix = [[1]]
# Output: 1
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 2^31 - 1
#
#
#

from itertools import product
from types import MethodType
from typing import List

from algo_input import run

# @lc code=start


class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}

        def dfs(start, cell, current_dist, seen):
            if cell in dp:
                return dp[cell]
            dist_to_end = 0
            for neigh in [(cell[0] + dy, cell[1] + dx)
                          for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]:
                if (not (0 <= neigh[0] < len(matrix)
                         and 0 <= neigh[1] < len(matrix[0])) or neigh in seen
                        or matrix[cell[0]][cell[1]] -
                        matrix[neigh[0]][neigh[1]] >= 0):
                    continue
                seen.add(neigh)
                dist_to_end = max(dfs(start, neigh, current_dist + 1, seen),
                                  dist_to_end)
                seen.discard(neigh)
            dist_to_end += 1
            dp[cell] = dist_to_end
            return dist_to_end

        return max(
            dfs(start, start, 1, {start})
            for start in product(range(len(matrix)), range(len(matrix[0]))))


# @lc code=end

testCases = [
    [
        [
            [4],
            [5],
            [6],
            [7],
            [8],
            [7],
            [6],
            [5],
            [4],
            [3],
            [2],
            [1],
            [0],
            [5],
            [4],
            [3],
            [2],
            [1],
            [0],
        ],
        9,
    ],
    [[[7, 7, 5], [2, 4, 6], [8, 2, 0]], 4],
    [[[1]], 1],
    [[[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4],
    [[[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4],
]
if __name__ == "__main__":
    run(
        MethodType(Solution.longestIncreasingPath, Solution()),
        [
            [
                [[
                    [4],
                    [5],
                    [6],
                    [7],
                    [8],
                    [7],
                    [6],
                    [5],
                    [4],
                    [3],
                    [2],
                    [1],
                    [0],
                    [5],
                    [4],
                    [3],
                    [2],
                    [1],
                    [0],
                ]],
                9,
            ],
            [[[[7, 7, 5], [2, 4, 6], [8, 2, 0]]], 4],
            [[[[1]]], 1],
            [[[[9, 9, 4], [6, 6, 8], [2, 1, 1]]], 4],
            [[[[3, 4, 5], [3, 2, 6], [2, 2, 1]]], 4],
        ],
    )
