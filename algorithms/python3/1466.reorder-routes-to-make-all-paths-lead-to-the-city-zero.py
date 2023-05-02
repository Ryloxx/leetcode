#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
#
# algorithms
# Medium (61.73%)
# Likes:    2697
# Dislikes: 71
# Total Accepted:    95.6K
# Total Submissions: 148.6K
# Testcase Example:  '6\n[[0,1],[1,3],[2,3],[4,0],[4,5]]'
#
# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there
# is only one way to travel between two different cities (this network form a
# tree). Last year, The ministry of transport decided to orient the roads in
# one direction because they are too narrow.
#
# Roads are represented by connections where connections[i] = [ai, bi]
# represents a road from city ai to city bi.
#
# This year, there will be a big event in the capital (city 0), and many people
# want to travel to this city.
#
# Your task consists of reorienting some roads such that each city can visit
# the city 0. Return the minimum number of edges changed.
#
# It's guaranteed that each city can reach city 0 after reorder.
#
#
# Example 1:
#
#
# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node
# can reach the node 0 (capital).
#
#
# Example 2:
#
#
# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2
# Explanation: Change the direction of edges show in red such that each node
# can reach the node 0 (capital).
#
#
# Example 3:
#
#
# Input: n = 3, connections = [[1,0],[2,0]]
# Output: 0
#
#
#
# Constraints:
#
#
# 2 <= n <= 5 * 10^4
# connections.length == n - 1
# connections[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi
#
#
#
from collections import defaultdict, deque
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(set)
        s = set()
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
            s.add((a, b))
        q = deque([0])
        ans = 0
        seen = set()
        while q:
            curr = q.popleft()
            if curr in seen:
                continue
            seen.add(curr)
            for i in graph[curr]:
                if (i, curr) not in s and i not in seen:
                    ans += 1
                q.append(i)
        return ans


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minReorder, Solution()),
        [
            ([6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]], 3),
            ([5, [[1, 0], [1, 2], [3, 2], [3, 4]]], 2),
            ([3, [[1, 0], [2, 0]]], 0),
        ],
    )
