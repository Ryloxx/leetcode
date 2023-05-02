#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (50.94%)
# Likes:    5190
# Dislikes: 387
# Total Accepted:    433.3K
# Total Submissions: 842.3K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below. More
# formally, if you are on index i on the current row, you may move to either
# index i or index i + 1 on the next row.
#
#
# Example 1:
#
#
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
# ⁠  2
# ⁠ 3 4
# ⁠6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined
# above).
#
#
# Example 2:
#
#
# Input: triangle = [[-10]]
# Output: -10
#
#
#
# Constraints:
#
#
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4 <= triangle[i][j] <= 10^4
#
#
#
# Follow up: Could you do this using only O(n) extra space, where n is the
# total number of rows in the triangle?
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(
                    triangle[row - 1][col]
                    if col < len(triangle[row]) - 1 else float('inf'),
                    triangle[row - 1][col -
                                      1] if col - 1 >= 0 else float('inf'))
        return min(triangle[-1], default=0)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minimumTotal, Solution()),
        [
            [[[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]], 11],
            [[[[-10]]], -10],
            [[[[]]], 0],
        ],
    )
