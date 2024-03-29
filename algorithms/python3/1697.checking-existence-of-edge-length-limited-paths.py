#
# @lc app=leetcode id=1697 lang=python3
#
# [1697] Checking Existence of Edge Length Limited Paths
#
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/
#
# algorithms
# Hard (50.42%)
# Likes:    1137
# Dislikes: 29
# Total Accepted:    22.8K
# Total Submissions: 39.6K
# Testcase Example:  '3\n[[0,1,2],[1,2,4],[2,0,8],[1,0,16]]\n[[0,1,2],[0,2,5]]'
#
# An undirected graph of n nodes is defined by edgeList, where edgeList[i] =
# [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi.
# Note that there may be multiple edges between two nodes.
#
# Given an array queries, where queries[j] = [pj, qj, limitj], your task is to
# determine for each queries[j] whether there is a path between pj and qj such
# that each edge on the path has a distance strictly less than limitj .
#
# Return a boolean array answer, where answer.length == queries.length and the
# j^th value of answer is true if there is a path for queries[j] is true, and
# false otherwise.
#
#
# Example 1:
#
#
# Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries =
# [[0,1,2],[0,2,5]]
# Output: [false,true]
# Explanation: The above figure shows the given graph. Note that there are two
# overlapping edges between 0 and 1 with distances 2 and 16.
# For the first query, between 0 and 1 there is no path where each distance is
# less than 2, thus we return false for this query.
# For the second query, there is a path (0 -> 1 -> 2) of two edges with
# distances less than 5, thus we return true for this query.
#
#
# Example 2:
#
#
# Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries =
# [[0,4,14],[1,4,13]]
# Output: [true,false]
# Exaplanation: The above figure shows the given graph.
#
#
#
# Constraints:
#
#
# 2 <= n <= 10^5
# 1 <= edgeList.length, queries.length <= 10^5
# edgeList[i].length == 3
# queries[j].length == 3
# 0 <= ui, vi, pj, qj <= n - 1
# ui != vi
# pj != qj
# 1 <= disi, limitj <= 10^9
# There may be multiple edges between two nodes.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]],
                                  queries: List[List[int]]) -> List[bool]:
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

        edgeList.sort(key=lambda x: x[2])
        sorted_idx = sorted(range(len(queries)), key=lambda x: queries[x][2])
        edge_idx = 0
        res = [False] * len(queries)
        for idx, (u, v, limit) in ((idx, queries[idx]) for idx in sorted_idx):
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                union(edgeList[edge_idx][0], edgeList[edge_idx][1])
                edge_idx += 1
            res[idx] = (find(u) == find(v))
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.distanceLimitedPathsExist, Solution()),
        [
            ([
                3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
                [[0, 1, 2], [0, 2, 5]]
            ], [False, True]),
            ([
                5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
                [[0, 4, 14], [1, 4, 13]]
            ], [True, False]),
        ],
    )
