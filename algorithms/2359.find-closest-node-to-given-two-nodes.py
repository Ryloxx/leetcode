#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
#
# algorithms
# Medium (34.29%)
# Likes:    1336
# Dislikes: 306
# Total Accepted:    57K
# Total Submissions: 124.5K
# Testcase Example:  '[2,2,3,-1]\n0\n1'
#
# You are given a directed graph of n nodes numbered from 0 to n - 1, where
# each node has at most one outgoing edge.
#
# The graph is represented with a given 0-indexed array edges of size n,
# indicating that there is a directed edge from node i to node edges[i]. If
# there is no outgoing edge from i, then edges[i] == -1.
#
# You are also given two integers node1 and node2.
#
# Return the index of the node that can be reached from both node1 and node2,
# such that the maximum between the distance from node1 to that node, and from
# node2 to that node is minimized. If there are multiple answers, return the
# node with the smallest index, and if no possible answer exists, return -1.
#
# Note that edges may contain cycles.
#
#
# Example 1:
#
#
# Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
# Output: 2
# Explanation: The distance from node 0 to node 2 is 1, and the distance from
# node 1 to node 2 is 1.
# The maximum of those two distances is 1. It can be proven that we cannot get
# a node with a smaller maximum distance than 1, so we return node 2.
#
#
# Example 2:
#
#
# Input: edges = [1,2,-1], node1 = 0, node2 = 2
# Output: 2
# Explanation: The distance from node 0 to node 2 is 2, and the distance from
# node 2 to itself is 0.
# The maximum of those two distances is 2. It can be proven that we cannot get
# a node with a smaller maximum distance than 2, so we return node 2.
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
# 0 <= node1, node2 < n
#
#
#
from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def closestMeetingNode(self, edges: List[int], node1: int,
                           node2: int) -> int:

        def f(start):
            res, prev, dist = defaultdict(lambda: -float('inf')), start, 0
            while (next_node := edges[prev]) != -1 and next_node not in res:
                res[prev] = max(res[prev], dist)
                prev = next_node
                dist += 1
            res[prev] = max(res[prev], dist)
            return res

        return min(
            (path_node1 := f(node1)).keys() & (path_node2 := f(node2)).keys(),
            key=lambda node: [max(path_node1[node], path_node2[node]), node],
            default=-1)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.closestMeetingNode, Solution()),
        [
            ([[2, 2, 3, -1], 0, 1], 2),
            ([[1, 2, -1], 0, 2], 2),
            ([[1, 2, 3, -1, 5, 6, 7, -1], 0, 4], -1),
            ([[1, 2, 3, 4, 5, 6, 7, -1], 0, 4], 4),
            ([[5, -1, 3, 4, 5, 6, -1, -1, 4, 3], 0, 0], 0),
            ([[2, 0, 0], 2, 0], 0),
            ([[4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6], 1),
            ([[4, 3, 0, 5, 3, -1], 4, 0], 4),
        ],
    )
