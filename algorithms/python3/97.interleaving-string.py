#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Medium (34.83%)
# Likes:    4572
# Dislikes: 251
# Total Accepted:    290.5K
# Total Submissions: 815.8K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
# s1 and s2.
#
# An interleaving of two strings s and t is a configuration where they are
# divided into non-empty substrings such that:
#
#
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 +
# t3 + s3 + ...
#
#
# Note: a + b is the concatenation of strings a and b.
#
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
# Example 3:
#
#
# Input: s1 = "", s2 = "", s3 = ""
# Output: true
#
#
#
# Constraints:
#
#
# 0 <= s1.length, s2.length <= 100
# 0 <= s3.length <= 200
# s1, s2, and s3 consist of lowercase English letters.
#
#
#
# Follow up: Could you solve it using only O(s2.length) additional memory
# space?
#
#
from collections import deque
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(N * M) time complexity
    # O(N * M) space complexity
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False
        q = deque()
        q.append((0, 0))
        seen = set()
        while q:
            i, j = q.popleft()
            if i + j == n + m:
                return True
            if (i, j) in seen or i + j > n + m:
                continue
            seen.add((i, j))
            if i < n and s1[i] == s3[i + j]:
                q.append((i + 1, j))
            if j < m and s2[j] == s3[i + j]:
                q.append((i, j + 1))
        return False

    # O(N * M) time complexity
    # O(min(N, M)) space complexity
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     s1, s2 = sorted([s1, s2], key=len)
    #     n, m = len(s1), len(s2)
    #     if n + m != len(s3):
    #         return False
    #     dp = [True] * (m + 1)

    #     for j in range(1, m + 1):
    #         dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

    #     for i in range(1, n + 1):
    #         dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
    #         for j in range(1, m + 1):
    #             dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
    #                 dp[j - 1] and s2[j - 1] == s3[i + j - 1])
    #     return dp[-1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isInterleave, Solution()),
        [
            [["aabcc", "dbbca", "aadbbcbcac"], True],
            [[
                "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbb"
                "ababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
                "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaab"
                "aaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
                "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabb"
                "baaaaabbbbaabbaaabababbaaaaaabababbababaababbababb"
                "bababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababa"
                "ababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
            ], False],
            [["a", "b", "c"], False],
            [["a", "b", "abc"], False],
            [["a", "b", "aabb"], False],
            [["ab", "bc", "abbc"], True],
            [["abbc", "bccb", "ac"], False],
            [["aabcc", "dbbca", "aadbbbaccc"], False],
            [["", "", ""], True],
            [[
                "sfjgeahvgntskkktuyotbdkdsuqeiddzddxqibioujdtpzqsdfndwdwduu",
                "vuejimuamdkipzppcwogffbwwrihhjgihkxhdtltqvydeibtrfzgequuot"
                "ujkspqbdfhjsfdumbygghuopyutrnshroqzutgktoszbanznayqlewymtz"
                "coczyelfelenfischefdkvdyxv",
                "sfvuejimuajgeahvgmdkipzppcwogfnfbwwrihhjgihkxhdtlttskkktqv"
                "yduyoeibtrfztbgequuotudkdsuqjkspqbdfhjsfdueidmbygghudzddxo"
                "pyutqibrnshroqioujdzutgktpzqsdtoszbanznayqlefnwymtzcocdzye"
                "lfelenwdwdufischuefdkvdyxv"
            ], True],
        ],
    )
