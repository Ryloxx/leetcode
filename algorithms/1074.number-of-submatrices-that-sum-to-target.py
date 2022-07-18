#
# @lc app=leetcode id=1074 lang=python3
#
# [1074] Number of Submatrices That Sum to Target
#
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/
#
# algorithms
# Hard (66.33%)
# Likes:    1683
# Dislikes: 40
# Total Accepted:    52K
# Total Submissions: 77.8K
# Testcase Example:  '[[0,1,0],[1,1,1],[0,1,0]]\n0'
#
# Given a matrix and a target, return the number of non-empty submatrices that
# sum to target.
#
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x
# <= x2 and y1 <= y <= y2.
#
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if
# they have some coordinate that is different: for example, if x1 != x1'.
#
#
# Example 1:
#
#
# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
#
#
# Example 2:
#
#
# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the
# 2x2 submatrix.
#
#
# Example 3:
#
#
# Input: matrix = [[904]], target = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8
#
#
#
from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # O(M**2 * N) time complexity
    # O(N) space complexity
    def numSubmatrixSumTarget(self, matrix: List[List[int]],
                              target: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            row.append(0)
        matrix.append([0] * (n + 1))

        for y in range(m):
            for x in range(n):
                matrix[y][x] += matrix[y - 1][x] + matrix[y][x - 1] - matrix[
                    y - 1][x - 1]

        res = 0
        for y2 in range(m):
            for y1 in range(y2 + 1):
                memo = defaultdict(int, {0: 1})
                for x in range(n):
                    s = matrix[y2][x] - matrix[y2][-1] - matrix[
                        y1 - 1][x] + matrix[y1 - 1][-1]
                    res += memo[s - target]
                    memo[s] += 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numSubmatrixSumTarget, Solution()),
        [
            [[[[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0], 4],
            [[[[0, -1, 0], [1, -1, 1], [2, 1, -4]], -1], 10],
            [[[[0] * 50 for _ in range(50)], 0], 1625625],
            [[[[1] * 100 for _ in range(100)], 0], 0],
        ],
    )
