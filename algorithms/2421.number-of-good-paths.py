#
# @lc app=leetcode id=2421 lang=python3
#
# [2421] Number of Good Paths
#
# https://leetcode.com/problems/number-of-good-paths/description/
#
# algorithms
# Hard (40.29%)
# Likes:    1204
# Dislikes: 57
# Total Accepted:    23.9K
# Total Submissions: 45.7K
# Testcase Example:  '[1,3,2,1,3]\n[[0,1],[0,2],[2,3],[2,4]]'
#
# There is a tree (i.e. a connected, undirected graph with no cycles)
# consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.
#
# You are given a 0-indexed integer array vals of length n where vals[i]
# denotes the value of the i^th node. You are also given a 2D integer array
# edges where edges[i] = [ai, bi] denotes that there exists an undirected edge
# connecting nodes ai and bi.
#
# A good path is a simple path that satisfies the following conditions:
#
#
# The starting node and the ending node have the same value.
# All nodes between the starting node and the ending node have values less than
# or equal to the starting node (i.e. the starting node's value should be the
# maximum value along the path).
#
#
# Return the number of distinct good paths.
#
# Note that a path and its reverse are counted as the same path. For example, 0
# -> 1 is considered to be the same as 1 -> 0. A single node is also considered
# as a valid path.
#
#
# Example 1:
#
#
# Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
# Output: 6
# Explanation: There are 5 good paths consisting of a single node.
# There is 1 additional good path: 1 -> 0 -> 2 -> 4.
# (The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 ->
# 4.)
# Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
#
#
# Example 2:
#
#
# Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
# Output: 7
# Explanation: There are 5 good paths consisting of a single node.
# There are 2 additional good paths: 0 -> 1 and 2 -> 3.
#
#
# Example 3:
#
#
# Input: vals = [1], edges = []
# Output: 1
# Explanation: The tree consists of only one node, so there is one good
# path.
#
#
#
# Constraints:
#
#
# n == vals.length
# 1 <= n <= 3 * 10^4
# 0 <= vals[i] <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges represents a valid tree.
#
#
#
from collections import defaultdict
from typing import Counter, List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def numberOfGoodPaths(self, vals: List[int],
                          edges: List[List[int]]) -> int:
        n = len(vals)
        graph = [[] for _ in range(n)]
        parents = list(range(n))
        buckets = defaultdict(list)
        rank = [0] * n
        res = 0

        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x

        def union(x, y):
            p_x, p_y = sorted([find(x), find(y)], key=lambda x: rank[x])
            if p_x == p_y:
                return
            parents[p_x] = p_y
            rank[p_y] = max(rank[p_y], rank[p_x] + 1)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i, j in enumerate(vals):
            buckets[j].append(i)
        for i in sorted(buckets):
            components = Counter()
            for j in buckets[i]:
                for neigh in graph[j]:
                    if vals[neigh] <= i:
                        union(j, neigh)
            for j in buckets[i]:
                components[find(j)] += 1
            res += sum((x * (x + 1)) // 2 for x in components.values())
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numberOfGoodPaths, Solution()),
        [
            ([[1, 3, 2, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]]], 6),
            ([[2, 5, 5, 1, 5, 2, 3, 5, 1, 5],
              [[0, 1], [2, 1], [3, 2], [3, 4], [3, 5], [5, 6], [1, 7], [8, 4],
               [9, 7]]], 20),
            ([[1, 1, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]], 7),
            ([[1], []], 1),
            ([[2, 2, 2, 2, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]], 11),
            ([[1, 2, 3, 4, 3], [[0, 1], [1, 2], [2, 3], [2, 4]]], 6),
            ([[1, 3, 0, 1, 3], [[0, 1], [0, 2], [2, 3], [2, 4]]], 7),
        ],
    )
