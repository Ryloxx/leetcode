#
# @lc app=leetcode id=2316 lang=python3
#
# [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
#
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/
#
# algorithms
# Medium (38.60%)
# Likes:    1154
# Dislikes: 26
# Total Accepted:    42.4K
# Total Submissions: 91.5K
# Testcase Example:  '3\n[[0,1],[0,2],[1,2]]'
#
# You are given an integer n. There is an undirected graph with n nodes,
# numbered from 0 to n - 1. You are given a 2D integer array edges where
# edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
# nodes ai and bi.
#
# Return the number of pairs of different nodes that are unreachable from each
# other.
#
#
# Example 1:
#
#
# Input: n = 3, edges = [[0,1],[0,2],[1,2]]
# Output: 0
# Explanation: There are no pairs of nodes that are unreachable from each
# other. Therefore, we return 0.
#
#
# Example 2:
#
#
# Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# Output: 14
# Explanation: There are 14 pairs of nodes that are unreachable from each
# other:
#
# [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
# Therefore, we return 14.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
# 0 <= edges.length <= 2 * 10^5
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no repeated edges.
#
#
#
from collections import Counter
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        rank = [0] * n

        def find(x: int):
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
            union(u, v)

        buckets = Counter()
        for i in range(n):
            buckets[find(i)] += 1
        res = 0
        for cmp_size in buckets.values():
            n -= cmp_size
            res += cmp_size * n
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.countPairs, Solution()),
        [
            ([3, [[0, 1], [0, 2], [1, 2]]], 0),
            ([7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]], 14),
            ([9, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4], [1, 7], [3, 8]]
              ], 26),
        ],
    )
