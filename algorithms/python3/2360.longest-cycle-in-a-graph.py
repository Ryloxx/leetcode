#
# @lc app=leetcode id=2360 lang=python3
#
# [2360] Longest Cycle in a Graph
#
# https://leetcode.com/problems/longest-cycle-in-a-graph/description/
#
# algorithms
# Hard (38.60%)
# Likes:    1367
# Dislikes: 27
# Total Accepted:    37.5K
# Total Submissions: 80.4K
# Testcase Example:  '[3,3,4,2,3]'
#
# You are given a directed graph of n nodes numbered from 0 to n - 1, where
# each node has at most one outgoing edge.
#
# The graph is represented with a given 0-indexed array edges of size n,
# indicating that there is a directed edge from node i to node edges[i]. If
# there is no outgoing edge from node i, then edges[i] == -1.
#
# Return the length of the longest cycle in the graph. If no cycle exists,
# return -1.
#
# A cycle is a path that starts and ends at the same node.
#
#
# Example 1:
#
#
# Input: edges = [3,3,4,2,3]
# Output: 3
# Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
# The length of this cycle is 3, so 3 is returned.
#
#
# Example 2:
#
#
# Input: edges = [2,-1,3,1]
# Output: -1
# Explanation: There are no cycles in this graph.
#
#
#
# Constraints:
#
#
# n == edges.length
# 2 <= n <= 10^5
# -1 <= edges[i] < n
# edges[i] != i
#
#
#
from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(int)
        for u, v in enumerate(edges):
            graph[u] = v
        visited = set()
        res = -1
        for u in graph:
            dist = 0
            dists = {}
            while u in graph:
                u = graph[u]
                dist += 1
                if u in dists:
                    res = max(res, dist - dists[u])
                if u in visited:
                    break
                dists[u] = dist
                visited.add(u)
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestCycle, Solution()),
        [
            ([[3, 3, 4, 2, 3]], 3),
            ([[2, -1, 3, 1]], -1),
            ([[]], -1),
            ([[3, 4, 0, 2, -1, 2]], 3),
        ],
    )
