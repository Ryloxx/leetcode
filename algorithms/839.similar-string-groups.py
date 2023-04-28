#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#
# https://leetcode.com/problems/similar-string-groups/description/
#
# algorithms
# Hard (47.81%)
# Likes:    1390
# Dislikes: 186
# Total Accepted:    75.9K
# Total Submissions: 151.3K
# Testcase Example:  '["tars","rats","arts","star"]'
#
# Two strings X and Y are similar if we can swap two letters (in different
# positions) of X, so that it equals Y. Also two strings X and Y are similar if
# they are equal.
#
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2),
# and "rats" and "arts" are similar, but "star" is not similar to "tars",
# "rats", or "arts".
#
# Together, these form two connected groups by similarity: {"tars", "rats",
# "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group
# even though they are not similar.  Formally, each group is such that a word
# is in the group if and only if it is similar to at least one other word in
# the group.
#
# We are given a list strs of strings where every string in strs is an anagram
# of every other string in strs. How many groups are there?
#
#
# Example 1:
#
#
# Input: strs = ["tars","rats","arts","star"]
# Output: 2
#
#
# Example 2:
#
#
# Input: strs = ["omv","ovm"]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 300
# 1 <= strs[i].length <= 300
# strs[i] consists of lowercase letters only.
# All words in strs have the same length and are anagrams of each other.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def numSimilarGroups(self, strs: List[str]) -> int:
        m, n = len(strs[0]), len(strs)
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

        for i in range(n):
            for j in range(i + 1, n):
                w_1 = strs[i]
                w_2 = strs[j]
                diff_char_count = 0
                for k in range(m):
                    diff_char_count += w_1[k] != w_2[k]
                    if diff_char_count > 2:
                        break
                (not diff_char_count or diff_char_count == 2) and union(i, j)

        return len(set(find(x) for x in range(n)))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numSimilarGroups, Solution()),
        [
            ([["arts", "rast"]], 2),
            ([["tars", "rats", "arts", "star"]], 2),
            ([["omv", "ovm"]], 1),
            ([["omv"]], 1),
            ([["o"]], 1),
            ([["o", "b"]], 2),
            ([["ob", "ob"]], 1),
            ([["bo", "ob"]], 1),
        ],
    )
