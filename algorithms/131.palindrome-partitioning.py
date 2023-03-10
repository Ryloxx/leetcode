#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (62.74%)
# Likes:    9876
# Dislikes: 320
# Total Accepted:    599.2K
# Total Submissions: 933.1K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
#
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= s.length <= 16
# s contains only lowercase English letters.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
def expand(s, i, j):
    n = len(s)
    while i >= 0 and j < n:
        if s[i] != s[j]:
            break
        i -= 1
        j += 1
    return j - i - 1, s[i + 1:j], j


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def solve(palindromes, rest, n):
            if not rest:
                res.append(list(palindromes))
                return
            for i in range(len(rest)):
                la, a, enda = expand(rest, i, i)
                lb, b, endb = expand(rest, i, i + 1)
                if la >= (i * 2 + 1):
                    solve(palindromes + [a], rest[enda:], n - enda)
                if i < n - 1 and b and lb // 2 == i + 1:
                    solve(palindromes + [b], rest[endb:], n - endb)

        solve([], s, len(s))
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.partition, Solution()),
        [
            (["aab"], [["a", "a", "b"], ["aa", "b"]]),
            (["a"], [["a"]]),
        ],
    )
