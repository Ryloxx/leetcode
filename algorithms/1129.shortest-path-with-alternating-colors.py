#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#
# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
#
# algorithms
# Medium (42.98%)
# Likes:    2293
# Dislikes: 108
# Total Accepted:    63.5K
# Total Submissions: 140.4K
# Testcase Example:  '3\n[[0,1],[1,2]]\n[]'
#
# You are given an integer n, the number of nodes in a directed graph where the
# nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph,
# and there could be self-edges and parallel edges.
#
# You are given two arrays redEdges and blueEdges where:
#
#
# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node
# ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from
# node uj to node vj in the graph.
#
#
# Return an array answer of length n, where each answer[x] is the length of the
# shortest path from node 0 to node x such that the edge colors alternate along
# the path, or -1 if such a path does not exist.
#
#
# Example 1:
#
#
# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
#
#
# Example 2:
#
#
# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]
#
#
#
# Constraints:
#
#
# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n
#
#
#
from collections import deque
from typing import Deque, List, Tuple
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]],
                                 blueEdges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        res = [-1] * n

        for u, v in redEdges:
            graph[u].append((v, 0))
        for u, v in blueEdges:
            graph[u].append((v, 1))

        q: Deque[Tuple[int, int, int]] = deque([(0, 1, 0), (0, 0, 0)])
        seen = set()
        while q:
            node, color, dist = q.popleft()
            if (node, color) in seen:
                continue
            seen.add((node, color))
            res[node] = dist if res[node] < 0 else min(res[node], dist)
            for neigh, next_color in graph[node]:
                if color == next_color:
                    continue
                q.append((neigh, next_color, dist + 1))
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.shortestAlternatingPaths, Solution()),
        [
            ([3, [[0, 1], [1, 2]], []], [0, 1, -1]),
            ([3, [[0, 1]], [[2, 1]]], [0, 1, -1]),
            ([3, [[0, 1], [0, 2]], [[1, 0]]], [0, 1, 1]),
        ],
    )
