#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (47.87%)
# Likes:    2836
# Dislikes: 259
# Total Accepted:    238.5K
# Total Submissions: 489.5K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
#  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, handle multiple queries of the following
# type:
#
#
# Calculate the sum of the elements of matrix inside the rectangle defined by
# its upper left corner (row1, col1) and lower right corner (row2, col2).
#
#
# Implement the NumMatrix class:
#
#
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix
# matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the
# elements of matrix inside the rectangle defined by its upper left corner
# (row1, col1) and lower right corner (row2, col2).
#
#
#
# Example 1:
#
#
# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0,
# 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]
#
# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2,
# 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green
# rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue
# rectangle)
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -10^5 <= matrix[i][j] <= 10^5
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 10^4 calls will be made to sumRegion.
#
#
#

from types import MethodType
from typing import List
from algo_input import run


# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                a = matrix[y][x - 1] if x > 0 else 0
                b = matrix[y - 1][x] if y > 0 else 0
                c = matrix[y - 1][x - 1] if y > 0 and x > 0 else 0
                matrix[y][x] += a + b - c
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2][col2] - (
            self.matrix[row2][col1 - 1] if col1 > 0 else 0
        ) - (self.matrix[row1 - 1][col2] if row1 > 0 else 0) + (
            self.matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

if __name__ == "__main__":
    run(
        MethodType(
            NumMatrix.sumRegion,
            NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5],
                       [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])),
        [[[2, 1, 4, 3], 8], [[1, 1, 2, 2], 11], [[1, 2, 2, 4], 12]])
    run(MethodType(NumMatrix.sumRegion, NumMatrix([[-1]])),
        [[[0, 0, 0, 0], -1]])
