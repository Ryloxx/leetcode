#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#
# https://leetcode.com/problems/valid-square/description/
#
# algorithms
# Medium (43.87%)
# Likes:    724
# Dislikes: 769
# Total Accepted:    85.3K
# Total Submissions: 194.1K
# Testcase Example:  '[0,0]\n[1,1]\n[1,0]\n[0,1]'
#
# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return
# true if the four points construct a square.
#
# The coordinate of a point pi is represented as [xi, yi]. The input is not
# given in any order.
#
# A valid square has four equal sides with positive length and four equal
# angles (90-degree angles).
#
#
# Example 1:
#
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true
#
#
# Example 2:
#
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false
#
#
# Example 3:
#
#
# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true
#
#
#
# Constraints:
#
#
# p1.length == p2.length == p3.length == p4.length == 2
# -10^4 <= xi, yi <= 10^4
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int],
                    p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        return len(set(map(tuple, points))) == 4 and len(
            {((x1 - x2)**2 + (y1 - y2)**2)**(1 / 2)
             for i in range(4) for j in range(i + 1, 4)
             for (x1, y1), (x2, y2) in [[points[i], points[j]]]}) == 2


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.validSquare, Solution()),
        [
            [[[0, 1], [0, 2], [0, 1], [0, 0]], False],
            [[[0, 1], [0, 2], [0, 3], [0, 4]], False],
            [[[0, 1], [0, 0], [0, 0], [0, 0]], False],
            [[[0, 0], [0, 0], [0, 0], [0, 0]], False],
            [[[1, 0], [-1, 0], [0, 1], [0, -1]], True],
            [[[0, 0], [1, 1], [1, 0], [0, 1]], True],
            [[[0, 0], [1, 1], [1, 0], [0, 12]], False],
            [[[1, 1], [5, 3], [3, 5], [7, 7]], False],
        ],
    )
