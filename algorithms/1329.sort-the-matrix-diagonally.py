#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#
# https://leetcode.com/problems/sort-the-matrix-diagonally/description/
#
# algorithms
# Medium (81.36%)
# Likes:    2115
# Dislikes: 191
# Total Accepted:    101.6K
# Total Submissions: 123.4K
# Testcase Example:  '[[3,3,1,1],[2,2,1,2],[1,1,1,2]]'
#
# A matrix diagonal is a diagonal line of cells starting from some cell in
# either the topmost row or leftmost column and going in the bottom-right
# direction until reaching the matrix's end. For example, the matrix diagonal
# starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells
# mat[2][0], mat[3][1], and mat[4][2].
#
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending
# order and return the resulting matrix.
#
#
# Example 1:
#
#
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
#
#
# Example 2:
#
#
# Input: mat =
# [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
# Output:
# [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
#
#
#
# Constraints:
#
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100
#
#
#
from itertools import chain, product
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O((M + N) * min(M, N) * log(min(M, N))) time complexity
    # O(min(M, N)) space complexity
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        for start_y, start_x in chain(product([0], range(len(mat[0]))),
                                      product(range(1, len(mat)), [0])):
            diagonal_idxes = list(
                (start_y + i, start_x + i)
                for i in range(min(len(mat) - start_y,
                                   len(mat[0]) - start_x)))
            for ((y, x),
                 value) in zip(diagonal_idxes,
                               sorted(mat[y][x] for y, x in diagonal_idxes)):
                mat[y][x] = value

        return mat


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.diagonalSort, Solution()),
        [
            [[[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]],
             [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]],
            [[[[11, 25, 66, 1, 69, 7], [23, 55, 17, 45, 15, 52],
               [75, 31, 36, 44, 58, 8], [22, 27, 33, 25, 68, 4],
               [84, 28, 14, 11, 5, 50]]],
             [[5, 17, 4, 1, 52, 7], [11, 11, 25, 45, 8, 69],
              [14, 23, 25, 44, 58, 15], [22, 27, 31, 36, 50, 66],
              [84, 28, 75, 33, 55, 68]]],
            [
                [[[]]],
                [[]],
            ],
            [
                [[[1]]],
                [[1]],
            ],
            [
                [[[1, 2, 3]]],
                [[1, 2, 3]],
            ],
            [
                [[[1], [2], [3]]],
                [[1], [2], [3]],
            ],
            [
                [[[1, 2], [2, 3], [3, 4]]],
                [[1, 2], [2, 3], [3, 4]],
            ],
        ],
    )
