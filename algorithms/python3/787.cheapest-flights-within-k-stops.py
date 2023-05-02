#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
#
# algorithms
# Medium (35.90%)
# Likes:    7323
# Dislikes: 320
# Total Accepted:    336.8K
# Total Submissions: 916.2K
# Testcase Example:  '4\n[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# \n0\n3\n1'
#
# There are n cities connected by some number of flights. You are given an
# array flights where flights[i] = [fromi, toi, pricei] indicates that there is
# a flight from city fromi to city toi with cost pricei.
#
# You are also given three integers src, dst, and k, return the cheapest price
# from src to dst with at most k stops. If there is no such route, return
# -1.
#
#
# Example 1:
#
#
# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
# src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and
# has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because
# it uses 2 stops.
#
#
# Example 2:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k
# = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and
# has cost 100 + 100 = 200.
#
#
# Example 3:
#
#
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k
# = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost
# 500.
#
#
#
# Constraints:
#
#
# 1 <= n <= 100
# 0 <= flights.length <= (n * (n - 1) / 2)
# flights[i].length == 3
# 0 <= fromi, toi < n
# fromi != toi
# 1 <= pricei <= 10^4
# There will not be any multiple flights between two cities.
# 0 <= src, dst, k < n
# src != dst
#
#
#
from collections import defaultdict
from heapq import heappop, heappush
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, K: int) -> int:
        city_map = defaultdict(dict)
        for sr, ds, pr in flights:
            city_map[sr][ds] = pr
        h = [(0, src, K + 1)]
        seen = defaultdict(lambda: -float('inf'))
        while h:
            curr_price, curr_stop, size = heappop(h)
            if curr_stop == dst:
                return curr_price
            if seen[curr_stop] >= size:
                continue
            seen[curr_stop] = size
            if size > 0:
                for next_stop in city_map[curr_stop]:
                    heappush(h, (curr_price + city_map[curr_stop][next_stop],
                                 next_stop, size - 1))
        return -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findCheapestPrice, Solution()),
        [
            ([
                4,
                [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600],
                 [2, 3, 200]], 0, 3, 1
            ], 700),
            ([3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1], 200),
            ([3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0], 500),
            ([4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1], 6),
            ([
                13,
                [[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8],
                 [0, 12, 54], [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64],
                 [6, 3, 88], [8, 5, 80], [11, 10, 91], [10, 0, 60], [8, 7, 92],
                 [12, 6, 78], [6, 2, 8], [4, 3, 54], [3, 11, 76], [3, 12, 23],
                 [11, 6, 79], [6, 12, 36],
                 [2, 11, 100], [2, 5, 49], [7, 0, 17], [5, 8, 95], [3, 9, 98],
                 [8, 10, 61], [2, 12, 38], [5, 7, 58], [9, 4, 37], [8, 6, 79],
                 [9, 0, 1], [2, 3, 12], [7, 10, 7], [12, 10, 52], [7, 2, 68],
                 [12, 2, 100], [6, 9, 53], [7, 4, 90], [0, 5, 43], [11, 2, 52],
                 [11, 8, 50], [12, 4, 38], [7, 9, 94], [2, 7, 38], [3, 7, 88],
                 [9, 12, 20], [12, 0, 26], [10, 5, 38], [12, 8, 50],
                 [0, 2, 77], [11, 0, 13], [9, 10, 76], [2, 6, 67], [5, 6, 34],
                 [9, 7, 62], [5, 3, 67]], 10, 1, 10
            ], -1),
        ],
    )
