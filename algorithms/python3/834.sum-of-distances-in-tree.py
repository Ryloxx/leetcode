#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#
# https://leetcode.com/problems/sum-of-distances-in-tree/description/
#
# algorithms
# Hard (54.24%)
# Likes:    3228
# Dislikes: 69
# Total Accepted:    50.2K
# Total Submissions: 91.6K
# Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
#
# There is an undirected connected tree with n nodes labeled from 0 to n - 1
# and n - 1 edges.
#
# You are given the integer n and the array edges where edges[i] = [ai, bi]
# indicates that there is an edge between nodes ai and bi in the tree.
#
# Return an array answer of length n where answer[i] is the sum of the
# distances between the i^th node in the tree and all other nodes.
#
#
# Example 1:
#
#
# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.
#
#
# Example 2:
#
#
# Input: n = 1, edges = []
# Output: [0]
#
#
# Example 3:
#
#
# Input: n = 2, edges = [[1,0]]
# Output: [1,1]
#
#
#
# Constraints:
#
#
# 1 <= n <= 3 * 10^4
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# The given input represents a valid tree.
#
#
#
from collections import defaultdict
from types import MethodType
from typing import List

from algo_input import run


# @lc code=start
class Solution:

    def sumOfDistancesInTree(self, n: int,
                             edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * n
        res = [0] * n

        def dfs(node=0, parent=None):
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(child, node)
                count[node] += count[child]
                res[node] += res[child] + count[child]

        def dfs2(node=0, parent=None):
            for child in graph[node]:
                if child == parent:
                    continue
                res[child] = res[node] + n - 2 * count[child]
                dfs2(child, node)

        dfs()
        dfs2()
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.sumOfDistancesInTree, Solution()),
        [
            ([6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
              ], [8, 12, 6, 10, 10, 10]),
            ([1, []], [0]),
            ([2, [[1, 0]]], [1, 1]),
            ([3 * 10**4, list([0, x] for x in range(1, 3 * 10**4))
              ], [29999] + [59997] * (3 * 10**4 - 1)),
        ],
    )
