#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
# https://leetcode.com/problems/all-paths-from-source-to-target/description/
#
# algorithms
# Medium (81.54%)
# Likes:    5461
# Dislikes: 127
# Total Accepted:    368.5K
# Total Submissions: 451.2K
# Testcase Example:  '[[1,2],[3],[3],[]]'
#
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find
# all possible paths from node 0 to node n - 1 and return them in any order.
#
# The graph is given as follows: graph[i] is a list of all nodes you can visit
# from node i (i.e., there is a directed edge from node i to node
# graph[i][j]).
#
#
# Example 1:
#
#
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
#
#
# Example 2:
#
#
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#
#
#
# Constraints:
#
#
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# All the elements of graph[i] are unique.
# The input graph is guaranteed to be a DAG.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph, ans = graph, []

        def dfs(current_node, path):
            if current_node == len(graph) - 1:
                ans.append(path + [current_node])
                return
            path.append(current_node)
            for node in graph[current_node]:
                dfs(node, path)
            path.pop()

        dfs(0, [])
        return ans


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.allPathsSourceTarget, Solution()),
        [
            ([[[1, 2], [3], [3], []]], [[0, 1, 3], [0, 2, 3]]),
            ([[[4, 3, 1], [3, 2, 4], [3], [4], []]],
             [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]),
        ],
    )
