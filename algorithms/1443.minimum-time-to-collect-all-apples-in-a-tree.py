#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
#
# algorithms
# Medium (56.07%)
# Likes:    2100
# Dislikes: 177
# Total Accepted:    55.3K
# Total Submissions: 92.8K
# Testcase Example:  '7\n' +
# '[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]\n' +
# '[false,false,true,false,true,true,false]'
#
# Given an undirected tree consisting of n vertices numbered from 0 to n-1,
# which has some apples in their vertices. You spend 1 second to walk over one
# edge of the tree. Return the minimum time in seconds you have to spend to
# collect all apples in the tree, starting at vertex 0 and coming back to this
# vertex.
#
# The edges of the undirected tree are given in the array edges, where edges[i]
# = [ai, bi] means that exists an edge connecting the vertices ai and bi.
# Additionally, there is a boolean array hasApple, where hasApple[i] = true
# means that vertex i has an apple; otherwise, it does not have any apple.
#
#
# Example 1:
#
#
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,true,true,false]
# Output: 8
# Explanation: The figure above represents the given tree where red vertices
# have an apple. One optimal path to collect all apples is shown by the green
# arrows.
#
#
# Example 2:
#
#
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,false,true,false]
# Output: 6
# Explanation: The figure above represents the given tree where red vertices
# have an apple. One optimal path to collect all apples is shown by the green
# arrows.
#
#
# Example 3:
#
#
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,false,false,false,false,false]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai < bi <= n - 1
# fromi < toi
# hasApple.length == n
#
#
#
from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minTime(self, n: int, edges: List[List[int]],
                hasApple: List[bool]) -> int:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(curr, parent):
            return (res := sum(
                dfs(node, curr)
                for node in graph[curr] if node != parent)) + 2 * bool(
                    (hasApple[curr] or res))

        return max(0, dfs(0, -1) - 2)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minTime, Solution()),
        [
            ([
                7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                [False, False, True, False, True, True, False]
            ], 8),
            ([
                7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                [False, False, True, False, False, True, False]
            ], 6),
            ([
                7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                [False, False, False, False, False, False, False]
            ], 0),
        ],
    )
