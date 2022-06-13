#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#
# https://leetcode.com/problems/critical-connections-in-a-network/description/
#
# algorithms
# Hard (54.12%)
# Likes:    4548
# Dislikes: 163
# Total Accepted:    175.7K
# Total Submissions: 323.7K
# Testcase Example:  '4\n[[0,1],[1,2],[2,0],[1,3]]'
#
# There are n servers numbered from 0 to n - 1 connected by undirected
# server-to-server connections forming a network where connections[i] = [ai,
# bi] represents a connection between servers ai and bi. Any server can reach
# other servers directly or indirectly through the network.
#
# A critical connection is a connection that, if removed, will make some
# servers unable to reach some other server.
#
# Return all critical connections in the network in any order.
#
#
# Example 1:
#
#
# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
#
#
# Example 2:
#
#
# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]
#
#
#
# Constraints:
#
#
# 2 <= n <= 10^5
# n - 1 <= connections.length <= 10^5
# 0 <= ai, bi <= n - 1
# ai != bi
# There are no repeated connections.
#
#
#
from itertools import zip_longest
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def criticalConnections(self, n: int,
                            connections: List[List[int]]) -> List[List[int]]:
        graph = list(list() for x in range(n))
        ids = [None] * n
        onStack = [False] * n
        low_link = [-1] * n
        stack = []
        res = []
        idx = 0

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u, src):
            nonlocal graph, ids, onStack, low_link, stack, res, idx
            ids[u] = low_link[idx] = idx
            stack.append(u)
            onStack[idx] = True
            idx += 1
            for v in graph[u]:
                if v == src:
                    continue
                if ids[v] is None:
                    dfs(v, u)
                    low_link[ids[u]] = min(low_link[ids[v]], low_link[ids[u]])
                elif onStack[ids[v]]:
                    low_link[ids[u]] = min(ids[v], low_link[ids[u]])
            if low_link[ids[u]] == ids[u]:
                # At this point u is the root of a scc
                while True:
                    v = stack.pop()
                    onStack[ids[v]] = False
                    if v == u:
                        # Since src has been visited before u
                        # and u is a root of a scc then it's not possible
                        # for src to be part of u scc.
                        # Src has to be part of another scc
                        # therefore the link [src u] is a critical connection
                        if src is not None:
                            res.append((src, u))
                        break

        for u in range(n):
            if ids[u] is None:
                dfs(u, None)

        return res


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.criticalConnections, Solution()), [
        [[4, [[0, 1], [1, 2], [2, 0], [1, 3]]], [[1, 3]]],
        [[2, [[0, 1]]], [[0, 1]]],
    ],
        comparator=lambda x, y: all(a == b for a, b in zip_longest(
            map(list, sorted(x)), map(list, sorted(y)))))
