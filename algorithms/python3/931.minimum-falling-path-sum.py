#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
# https://leetcode.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (67.44%)
# Likes:    3469
# Dislikes: 104
# Total Accepted:    180.2K
# Total Submissions: 261.8K
# Testcase Example:  '[[2,1,3],[6,5,4],[7,8,9]]'
#
# Given an n x n array of integers matrix, return the minimum sum of any
# falling path through matrix.
#
# A falling path starts at any element in the first row and chooses the element
# in the next row that is either directly below or diagonally left/right.
# Specifically, the next element from position (row, col) will be (row + 1, col
# - 1), (row + 1, col), or (row + 1, col + 1).
#
#
# Example 1:
#
#
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
#
#
# Example 2:
#
#
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
#
#
#
# Constraints:
#
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
#
#
#
from algo_input import run
from types import MethodType
from typing import List
from sys import maxsize

# from functools import cache


# @lc code=start
class Solution:
    # O(M * N) time complexity
    # O(N) space complexity
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = matrix[0]
        for i in range(1, m):
            ndp = [maxsize] * n
            for j in range(n):
                for offset in range(-1, 2):
                    idx = j + offset
                    if not (0 <= idx < m):
                        continue
                    ndp[idx] = min(ndp[idx], dp[j] + matrix[i][idx])
            dp, ndp = ndp, dp
        return min(dp, default=0)

    # O(M * N) time complexity
    # O(M * N) space complexity
    # def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    #     if not matrix:
    #         return 0
    #     m, n = len(matrix), len(matrix[0])

    #     @cache
    #     def dp(y, x) -> int:
    #         if not 0 <= y < m:
    #             return 0
    #         if not 0 <= x < n:
    #             return maxsize
    #         return matrix[y][x] + min(dp(y + 1, x - 1), dp(y + 1, x),
    #                                   dp(y + 1, x + 1))

    #     return min((dp(0, x) for x in range(n)), default=0)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minFallingPathSum, Solution()),
        [
            ([[[2, 1, 3], [6, 5, 4], [7, 8, 9]]], 13),
            ([[[-19, 57], [-40, -5]]], -59),
            ([[[], []]], 0),
            ([[[]]], 0),
            ([[]], 0),
        ],
    )
