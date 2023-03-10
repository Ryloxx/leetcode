#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#
# https://leetcode.com/problems/rectangle-area/description/
#
# algorithms
# Medium (40.16%)
# Likes:    884
# Dislikes: 1097
# Total Accepted:    145.4K
# Total Submissions: 355.2K
# Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
#
# Given the coordinates of two rectilinear rectangles in a 2D plane, return the
# total area covered by the two rectangles.
#
# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its
# top-right corner (ax2, ay2).
#
# The second rectangle is defined by its bottom-left corner (bx1, by1) and its
# top-right corner (bx2, by2).
#
#
# Example 1:
#
#
# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 =
# 2
# Output: 45
#
#
# Example 2:
#
#
# Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2
# = 2
# Output: 16
#
#
#
# Constraints:
#
#
# -10^4 <= ax1 <= ax2 <= 10^4
# -10^4 <= ay1 <= ay2 <= 10^4
# -10^4 <= bx1 <= bx2 <= 10^4
# -10^4 <= by1 <= by2 <= 10^4
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int,
                    by1: int, bx2: int, by2: int) -> int:

        h = min(0, max(ay1, by1) - min(ay2, by2))
        w = min(0, max(ax1, bx1) - min(ax2, bx2))

        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - h * w


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.computeArea, Solution()),
        [
            ([-2, -2, 2, 2, 3, 3, 4, 4], 17),
            ([-3, 0, 3, 4, 0, -1, 9, 2], 45),
            ([-2, -2, 2, 2, -2, -2, 2, 2], 16),
            ([-3, 0, 3, 4, -3, -1, 9, 2], 48),
            ([-3, 0, 3, 4, -3, 0, 9, 2], 36),
            ([0, 0, 0, 0, -1, -1, 1, 1], 4),
            ([-3, -3, 3, 3, -2, -2, 1, 1], 36),
        ],
    )
