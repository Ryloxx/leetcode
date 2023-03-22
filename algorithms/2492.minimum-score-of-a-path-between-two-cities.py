#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
#
# algorithms
# Medium (45.90%)
# Likes:    360
# Dislikes: 57
# Total Accepted:    16.4K
# Total Submissions: 34.8K
# Testcase Example:  '4\n[[1,2,9],[2,3,6],[2,4,5],[1,4,7]]'
#
# You are given a positive integer n representing n cities numbered from 1 to
# n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei]
# indicates that there is a bidirectional road between cities ai and bi with a
# distance equal to distancei. The cities graph is not necessarily connected.
#
# The score of a path between two cities is defined as the minimum distance of
# a road in this path.
#
# Return the minimum possible score of a path between cities 1 and n.
#
# Note:
#
#
# A path is a sequence of roads between two cities.
# It is allowed for a path to contain the same road multiple times, and you can
# visit cities 1 and n multiple times along the path.
# The test cases are generated such that there is at least one path between 1
# and n.
#
#
#
# Example 1:
#
#
# Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
# Output: 5
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 ->
# 4. The score of this path is min(9,5) = 5.
# It can be shown that no other path has less score.
#
#
# Example 2:
#
#
# Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
# Output: 2
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1
# -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
#
#
#
# Constraints:
#
#
# 2 <= n <= 10^5
# 1 <= roads.length <= 10^5
# roads[i].length == 3
# 1 <= ai, bi <= n
# ai != bi
# 1 <= distancei <= 10^4
# There are no repeated edges.
# There is at least one path between 1 and n.
#
#
#
from collections import defaultdict, deque
from sys import maxsize
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        q = deque([1])
        seen = set()
        res = min_target = maxsize

        for u, v, d in roads:
            graph[u][v] = d
            graph[v][u] = d
            min_target = min(d, min_target)

        while q:
            u = q.popleft()
            if u in seen:
                continue
            seen.add(u)
            for v in graph[u]:
                res = min(res, graph[u][v])
                q.append(v)
            if res == min_target:
                break
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minScore, Solution()),
        [
            ([4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]], 5),
            ([4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]], 2),
        ],
    )
