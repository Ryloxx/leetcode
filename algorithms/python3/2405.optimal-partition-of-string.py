#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#
# https://leetcode.com/problems/optimal-partition-of-string/description/
#
# algorithms
# Medium (74.58%)
# Likes:    575
# Dislikes: 28
# Total Accepted:    37.1K
# Total Submissions: 48.9K
# Testcase Example:  '"abacaba"'
#
# Given a string s, partition the string into one or more substrings such that
# the characters in each substring are unique. That is, no letter appears in a
# single substring more than once.
#
# Return the minimum number of substrings in such a partition.
#
# Note that each character should belong to exactly one substring in a
# partition.
#
#
# Example 1:
#
#
# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.
#
#
# Example 2:
#
#
# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only English lowercase letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def partitionString(self, s: str) -> int:
        res = 0
        seen = set()
        for c in s:
            if c in seen:
                seen = set()
                res += 1
            seen.add(c)
        return res + bool(seen)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.partitionString, Solution()),
        [
            (["abacaba"], 4),
            (["ssssss"], 6),
            (["shkqbyutdvknyrpjof"], 2),
            ([""], 0),
            (["s"], 1),
        ],
    )
