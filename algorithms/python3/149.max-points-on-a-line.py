#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (21.90%)
# Likes:    2287
# Dislikes: 310
# Total Accepted:    279.8K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane, return the maximum number of points that lie on the same straight
# line.
#
#
# Example 1:
#
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
#
#
# Example 2:
#
#
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# All the points are unique.
#
#
#
from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType

# @lc code=start


class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        def slope(p_1, p_2):
            den = (p_2[1] - p_1[1])
            num = (p_2[0] - p_1[0])
            if not den:
                return None, None
            m = num / den
            p = p_1[1] - m * p_1[0]
            y_intersection = -p / m if m else p_1[1]
            return m, y_intersection

        i = res = 0
        while i < len(points) - res:
            slopes = defaultdict(int)
            for j in range(i + 1, len(points)):
                _slope = slope(points[i], points[j])
                slopes[_slope] += 1
                res = max(res, 1 + slopes[_slope])
            i += 1

        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxPoints, Solution()),
        [
            ([[[1, 1], [2, 2], [3, 3]]], 3),
            ([[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]], 4),
            ([[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4], [5, 2], [6, 3],
               [7, 4]]], 4),
            ([[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4], [5, 2], [6, 3],
               [7, 4], [8, 5]]], 5),
            ([[]], 0),
            ([[[0, 0]]], 1),
            ([[[2, 3], [3, 3], [-5, 3]]], 3),
            ([[[7, 3], [19, 19], [-16, 3], [13, 17], [-18, 1], [-18, -17],
               [13, -3], [3, 7], [-11, 12], [7, 19], [19, -12], [20, -18],
               [-16, -15], [-10, -15], [-16, -18], [-14, -1], [18, 10],
               [-13, 8], [7, -5], [-4, -9], [-11, 2], [-9, -9], [-5, -16],
               [10, 14], [-3, 4], [1, -20], [2, 16], [0, 14], [-14, 5],
               [15, -11], [3, 11], [11, -10], [-1, -7], [16, 7], [1, -11],
               [-8, -3], [1, -6], [19, 7], [3, 6], [-1, -2], [7, -3], [-6, -8],
               [7, 1], [-15, 12], [-17, 9], [19, -9], [1, 0], [9, -10],
               [6, 20], [-12, -4], [-16, -17], [14, 3], [0, -1], [-18, 9],
               [-15, 15], [-3, -15], [-5, 20], [15, -14], [9, -17], [10, -14],
               [-7, -11], [14, 9], [1, -1], [15, 12], [-5, -1], [-17, -5],
               [15, -2], [-12, 11], [19, -18], [8, 7], [-5, -3], [-17, -1],
               [-18, 13], [15, -3], [4, 18], [-14, -15], [15, 8], [-18, -12],
               [-15, 19], [-9, 16], [-9, 14], [-12, -14], [-2, -20], [-3, -13],
               [10, -7], [-2, -10], [9, 10], [-1, 7], [-17, -6], [-15, 20],
               [5, -17], [6, -6], [-11, -8]]], 6),
        ],
    )
