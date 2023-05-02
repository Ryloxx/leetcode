#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#
# https://leetcode.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (50.14%)
# Likes:    3006
# Dislikes: 48
# Total Accepted:    95.8K
# Total Submissions: 188.6K
# Testcase Example:  '["a==b","b!=a"]'
#
# You are given an array of strings equations that represent relationships
# between variables where each string equations[i] is of length 4 and takes one
# of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase
# letters (not necessarily different) that represent one-letter variable
# names.
#
# Return true if it is possible to assign integers to variable names so as to
# satisfy all the given equations, or false otherwise.
#
#
# Example 1:
#
#
# Input: equations = ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is
# satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.
#
#
# Example 2:
#
#
# Input: equations = ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
#
#
#
# Constraints:
#
#
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] is a lowercase letter.
# equations[i][1] is either '=' or '!'.
# equations[i][2] is '='.
# equations[i][3] is a lowercase letter.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def equationsPossible(self, equations: List[str]) -> bool:
        parents = list(range(26))
        rank = [0] * 26

        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x

        def union(x, y):
            p_x, p_y = find(x), find(y)
            if p_x == p_y:
                return
            if rank[p_x] > rank[p_y]:
                parents[p_y] = p_x
                rank[p_x] = max(rank[p_x], rank[p_y] + 1)
            else:
                parents[p_x] = p_y
                rank[p_y] = max(rank[p_y], rank[p_x] + 1)

        for x, e, e2, y in equations:
            x = ord(x) % 26
            y = ord(y) % 26
            if e == "=":
                union(x, y)
        for x, e, e2, y in equations:
            x = ord(x) % 26
            y = ord(y) % 26
            if e == "!" and find(x) == find(y):
                return False
        return True


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.equationsPossible, Solution()),
        [
            [[["a==b", "b!=a"]], False],
            [[["a==b", "b==a"]], True],
            [[["a!=a"]], False],
            [[["a!=b", "b!=c", "c!=a"]], True],
            [[["a!=b", "b!=c", "c!=a"]], True],
            [[["a==b", "b!=c", "c==a"]], False],
            [[["e==e", "d!=e", "c==d", "d!=e"]], True],
            [[[
                "g==c", "f!=e", "e==b", "j==b", "g!=a", "e==c", "b!=f", "d!=a",
                "j==g", "f!=i", "a==e"
            ]], False],
            [[["a==b", "b==c", "d==e", "e==f", "d==a", "f!=a"]], False],
        ],
    )
