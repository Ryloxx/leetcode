#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
#
# algorithms
# Hard (40.64%)
# Likes:    1058
# Dislikes: 35
# Total Accepted:    25.7K
# Total Submissions: 56K
# Testcase Example:  '"abaca"\n[[0,1],[0,2],[2,3],[3,4]]'
#
# There is a directed graph of n colored nodes and m edges. The nodes are
# numbered from 0 to n - 1.
#
# You are given a string colors where colors[i] is a lowercase English letter
# representing the color of the i^th node in this graph (0-indexed). You are
# also given a 2D array edges where edges[j] = [aj, bj] indicates that there is
# a directed edge from node aj to node bj.
#
# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk
# such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The
# color value of the path is the number of nodes that are colored the most
# frequently occurring color along that path.
#
# Return the largest color value of any valid path in the given graph, or -1 if
# the graph contains a cycle.
#
#
# Example 1:
#
#
#
#
# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a"
# (red in the above image).
#
#
# Example 2:
#
#
#
#
# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.
#
#
#
# Constraints:
#
#
# n == colors.length
# m == edges.length
# 1 <= n <= 10^5
# 0 <= m <= 10^5
# colors consists of lowercase English letters.
# 0 <= aj, bj < n
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = {}
        memo = {}
        has_cycle = False
        for u, v in edges:
            graph.setdefault(u, []).append(v)

        def dfs(u, seen):
            nonlocal has_cycle
            p = [0] * 26
            if u in seen:
                has_cycle = True
                return p
            if u in memo:
                return memo[u]
            if u in graph:
                seen.add(u)
                for v in graph[u]:
                    for idx, q in enumerate(dfs(v, seen)):
                        p[idx] = max(p[idx], q)
                seen.remove(u)
            p[ord(colors[u]) - ord('a')] += 1
            memo[u] = p
            return p

        res = max(map(max, (dfs(x, set()) for x in graph if not has_cycle)),
                  default=int(bool(colors)))
        return -1 if has_cycle else res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.largestPathValue, Solution()),
        [
            (["abaca", [[0, 1], [0, 2], [2, 3], [3, 4]]], 3),
            (["a", [[0, 0]]], -1),
            (["g", []], 1),
            ([
                "hhqhuqhqff",
                [[0, 1], [0, 2], [2, 3], [3, 4], [3, 5], [5, 6], [2, 7],
                 [6, 7], [7, 8], [3, 8], [5, 8], [8, 9], [3, 9], [6, 9]]
            ], 3),
        ],
    )
