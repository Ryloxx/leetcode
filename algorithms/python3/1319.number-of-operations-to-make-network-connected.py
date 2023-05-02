#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
#
# algorithms
# Medium (58.55%)
# Likes:    3709
# Dislikes: 47
# Total Accepted:    140.1K
# Total Submissions: 230.9K
# Testcase Example:  '4\n[[0,1],[0,2],[1,2]]'
#
# There are n computers numbered from 0 to n - 1 connected by ethernet cables
# connections forming a network where connections[i] = [ai, bi] represents a
# connection between computers ai and bi. Any computer can reach any other
# computer directly or indirectly through the network.
#
# You are given an initial computer network connections. You can extract
# certain cables between two directly connected computers, and place them
# between any pair of disconnected computers to make them directly connected.
#
# Return the minimum number of times you need to do this in order to make all
# the computers connected. If it is not possible, return -1.
#
#
# Example 1:
#
#
# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1
# Explanation: Remove cable between computer 1 and 2 and place between
# computers 1 and 3.
#
#
# Example 2:
#
#
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
# Output: 2
#
#
# Example 3:
#
#
# Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
# Output: -1
# Explanation: There are not enough cables.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
# 1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
# connections[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no repeated connections.
# No two computers are connected by more than one cable.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
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

        for u, v in connections:
            union(u, v)

        return len(set(find(u) for u in range(n))) - 1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.makeConnected, Solution()),
        [
            ([4, [[0, 1], [0, 2], [1, 2]]], 1),
            ([6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]], 2),
            ([6, [[0, 1], [0, 2], [0, 3], [1, 2]]], -1),
            ([6, []], -1),
        ],
    )
