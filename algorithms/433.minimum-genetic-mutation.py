#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#
# https://leetcode.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (46.88%)
# Likes:    2119
# Dislikes: 219
# Total Accepted:    100.2K
# Total Submissions: 193.1K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# A gene string can be represented by an 8-character long string, with choices
# from 'A', 'C', 'G', and 'T'.
#
# Suppose we need to investigate a mutation from a gene string start to a gene
# string end where one mutation is defined as one single character changed in
# the gene string.
#
#
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
#
#
# There is also a gene bank bank that records all the valid gene mutations. A
# gene must be in bank to make it a valid gene string.
#
# Given the two gene strings start and end and the gene bank bank, return the
# minimum number of mutations needed to mutate from start to end. If there is
# no such a mutation, return -1.
#
# Note that the starting point is assumed to be valid, so it might not be
# included in the bank.
#
#
# Example 1:
#
#
# Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
#
#
# Example 2:
#
#
# Input: start = "AACCGGTT", end = "AAACGGTA", bank =
# ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
#
#
# Example 3:
#
#
# Input: start = "AAAAACCC", end = "AACCCCCC", bank =
# ["AAAACCCC","AAACCCCC","AACCCCCC"]
# Output: 3
#
#
#
# Constraints:
#
#
# start.length == 8
# end.length == 8
# 0 <= bank.length <= 10
# bank[i].length == 8
# start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
#
#
#
from collections import deque
from typing import List, Tuple
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank.append(start)

        def neigh(a):
            return filter(lambda x: sum(i != j for i, j in zip(a, x)) == 1,
                          bank)

        q: deque[Tuple[str, int]] = deque([(start, 0)])
        visited = set()
        while q:
            curr, d = q.popleft()
            if curr in visited:
                continue
            if curr == end:
                return d
            visited.add(curr)
            for n in neigh(curr):
                q.append((n, d + 1))
        return -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minMutation, Solution()),
        [
            (["AACCGGTT", "AACCGGTA", ["AACCGGTA"]], 1),
            (["AA", "CT", ["CA", "TA", "AG", "GC", "CT"]], 2),
            (["AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
              ], 2),
            (["AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
              ], 3),
            (["A", "T", ["T"]], 1),
            (["A", "A", ["A"]], 0),
            (["A", "A", ["G"]], 0),
            (["A", "G", ["T"]], -1),
        ],
    )
