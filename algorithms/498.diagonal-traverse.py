#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (56.90%)
# Likes:    2319
# Dislikes: 547
# Total Accepted:    209.2K
# Total Submissions: 365.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix mat, return an array of all the elements of the array
# in a diagonal order.
#
#
# Example 1:
#
#
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
#
#
# Example 2:
#
#
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]
#
#
#
# Constraints:
#
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 10^4
# 1 <= m * n <= 10^4
# -10^5 <= mat[i][j] <= 10^5
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        return list(mat[i][no_d - i] for no_d in range(n + m) for seq in [
            range(max(0, no_d - max(m, n) + 1, no_d - m + 1), min(n, no_d + 1))
        ] for i in (seq if no_d % 2 else reversed(seq)))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findDiagonalOrder, Solution()),
        [
            [[[[6, 9, 7]]], [6, 9, 7]],
            [[[[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12]]],
             [1, 2, 4, 7, 5, 3, 10, 6, 8, 9, 11, 12]],
            [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [1, 2, 4, 7, 5, 3, 6, 8, 9]],
            [[[[3], [2]]], [3, 2]],
            [[[[1, 2], [3, 4]]], [1, 2, 3, 4]],
        ],
    )
