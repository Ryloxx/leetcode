#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (48.52%)
# Likes:    8116
# Dislikes: 134
# Total Accepted:    641.8K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]
# ,[10,13,14,17,24],[18,21,23,26,30]]\n' +
# '5'
#
# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
#
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
#
#
# Example 1:
#
#
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true
#
#
# Example 2:
#
#
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9
#
#
#
# from bisect import bisect_left
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(N + M) time complexity
    # O(1) space complexity
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y, x = 0, len(matrix[0]) - 1
        while y < len(matrix) and x >= 0:
            value = matrix[y][x]
            if value == target:
                return True
            elif value < target:
                y += 1
            else:
                x -= 1
        return False

    # O(NlogM) time complexity
    # O(1) space complexity
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     return any(row[idx] == target for row in matrix
    #                for idx in [bisect_left(row, target)] if idx < len(row))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.searchMatrix, Solution()),
        [
            [[[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
               [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5], True],
            [[[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
               [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20], False],
        ],
    )
