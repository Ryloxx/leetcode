#
# @lc app=leetcode id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/
#
# algorithms
# Hard (45.32%)
# Likes:    1360
# Dislikes: 33
# Total Accepted:    33.8K
# Total Submissions: 65.7K
# Testcase Example:  '[-1,0,0,1,1,2]\n"abacbe"'
#
# You are given a tree (i.e. a connected, undirected graph that has no cycles)
# rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is
# represented by a 0-indexed array parent of size n, where parent[i] is the
# parent of node i. Since node 0 is the root, parent[0] == -1.
#
# You are also given a string s of length n, where s[i] is the character
# assigned to node i.
#
# Return the length of the longest path in the tree such that no pair of
# adjacent nodes on the path have the same character assigned to them.
#
#
# Example 1:
#
#
# Input: parent = [-1,0,0,1,1,2], s = "abacbe"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different
# characters in the tree is the path: 0 -> 1 -> 3. The length of this path is
# 3, so 3 is returned.
# It can be proven that there is no longer path that satisfies the
# conditions.
#
#
# Example 2:
#
#
# Input: parent = [-1,0,0,0], s = "aabc"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different
# characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is
# returned.
#
#
#
# Constraints:
#
#
# n == parent.length == s.length
# 1 <= n <= 10^5
# 0 <= parent[i] <= n - 1 for all i >= 1
# parent[0] == -1
# parent represents a valid tree.
# s consists of only lowercase English letters.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def longestPath(self, parent: List[int], s: str) -> int:
        graph = [[] for _ in range(len(s))]
        for u, v in enumerate(parent):
            v >= 0 and graph[v].append(u)
        res = 0

        def dfs(node):
            nonlocal res
            left = right = 0
            for neigh in graph[node]:
                dist = dfs(neigh)
                if s[neigh] != s[node]:
                    if dist > left:
                        right = left
                        left = dist
                    elif dist > right:
                        right = dist
            res = max(res, left + right + 1)
            return max(left, right) + 1

        return len(parent) and dfs(0) and res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestPath, Solution()),
        [
            ([[-1, 0, 0, 1, 1, 2], "abacbe"], 3),
            ([[-1, 0, 0, 0], "aabc"], 3),
            ([[-1], "a"], 1),
            ([[], ""], 0),
            ([[-1, 0, 1, 2, 3, 4, 5], "abcdefg"], 7),
        ],
    )
