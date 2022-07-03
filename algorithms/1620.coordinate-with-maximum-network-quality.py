#
# @lc app=leetcode id=1620 lang=python3
#
# [1620] Coordinate With Maximum Network Quality
#
# https://leetcode.com/problems/coordinate-with-maximum-network-quality/description/
#
# algorithms
# Medium (37.12%)
# Likes:    62
# Dislikes: 211
# Total Accepted:    6.6K
# Total Submissions: 17.6K
# Testcase Example:  '[[1,2,5],[2,1,7],[3,1,9]]\n2'
#
# You are given an array of network towers towers, where towers[i] = [xi, yi,
# qi] denotes the i^th network tower with location (xi, yi) and quality factor
# qi. All the coordinates are integral coordinates on the X-Y plane, and the
# distance between the two coordinates is the Euclidean distance.
#
# You are also given an integer radius where a tower is reachable if the
# distance is less than or equal to radius. Outside that distance, the signal
# becomes garbled, and the tower is not reachable.
#
# The signal quality of the i^th tower at a coordinate (x, y) is calculated
# with the formula ⌊qi / (1 + d)⌋, where d is the distance between the tower
# and the coordinate. The network quality at a coordinate is the sum of the
# signal qualities from all the reachable towers.
#
# Return the array [cx, cy] representing the integral coordinate (cx, cy) where
# the network quality is maximum. If there are multiple coordinates with the
# same network quality, return the lexicographically minimum non-negative
# coordinate.
#
# Note:
#
#
# A coordinate (x1, y1) is lexicographically smaller than (x2, y2) if
# either:
#
#
# x1 < x2, or
# x1 == x2 and y1 < y2.
#
#
# ⌊val⌋ is the greatest integer less than or equal to val (the floor
# function).
#
#
#
# Example 1:
#
#
# Input: towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
# Output: [2,1]
# Explanation: At coordinate (2, 1) the total quality is 13.
# - Quality of 7 from (2, 1) results in ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
# - Quality of 5 from (1, 2) results in ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
# - Quality of 9 from (3, 1) results in ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
# No other coordinate has a higher network quality.
#
# Example 2:
#
#
# Input: towers = [[23,11,21]], radius = 9
# Output: [23,11]
# Explanation: Since there is only one tower, the network quality is highest
# right at the tower's location.
#
#
# Example 3:
#
#
# Input: towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
# Output: [1,2]
# Explanation: Coordinate (1, 2) has the highest network quality.
#
#
#
# Constraints:
#
#
# 1 <= towers.length <= 50
# towers[i].length == 3
# 0 <= xi, yi, qi <= 50
# 1 <= radius <= 50
#
#
#
from typing import List

from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def bestCoordinate(self, towers: List[List[int]],
                       radius: int) -> List[int]:
        seen = set()
        towers.append([0, 0, 0])
        buckets = [[] for _ in range(51)]
        for x, y, q in towers:
            buckets[x].append([x, y, q])

        def lexicographicalyOrder(x):
            return [x[0], -x[1][0], -x[1][1]]

        def bfs(x, y, d):
            if (x, y) in seen or d < 0\
                 or not (0 <= x <= 50)\
                    or not (0 <= y <= 50):
                return [-1, [0, 0]]
            seen.add((x, y))
            return max([
                sum(q // (1 + dist)
                    for j in range(max(0, x - radius), min(x + radius + 1, 51))
                    for x2, y2, q in buckets[j]
                    for dist in [((x - x2)**2 + (y - y2)**2)**(1 / 2)]
                    if dist <= radius), [x, y]
            ],
                       bfs(x + 1, y + 1, d - 1),
                       bfs(x - 1, y - 1, d - 1),
                       bfs(x - 1, y + 1, d - 1),
                       bfs(x + 1, y - 1, d - 1),
                       bfs(x + 1, y, d - 1),
                       bfs(x - 1, y, d - 1),
                       bfs(x, y + 1, d - 1),
                       bfs(x, y - 1, d - 1),
                       key=lexicographicalyOrder)

        return max((bfs(x, y, radius) for x, y, _ in towers),
                   key=lexicographicalyOrder)[1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.bestCoordinate, Solution()),
        [
            [[[[23, 11, 21]], 9], [23, 11]],
            [[[[0, 1, 2], [2, 1, 2], [1, 0, 2], [1, 2, 2]], 1], [1, 1]],
            [[[[2, 1, 9], [0, 1, 9]], 2], [0, 1]],
            [[[[42, 0, 0]], 7], [0, 0]],
            [[[[1, 2, 5], [2, 1, 7], [3, 1, 9]], 2], [2, 1]],
            [[[[1, 2, 13], [2, 1, 7], [0, 1, 9]], 2], [1, 2]],
        ],
    )
