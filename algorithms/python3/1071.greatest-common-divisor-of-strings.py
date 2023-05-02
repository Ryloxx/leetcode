#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (51.02%)
# Likes:    1795
# Dislikes: 339
# Total Accepted:    96.7K
# Total Submissions: 184.4K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t
# (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x
# divides both str1 and str2.
#
#
# Example 1:
#
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#
#
# Example 2:
#
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
#
# Example 3:
#
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
#
#
# Constraints:
#
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def gcdOfStrings(self, s1: str, s2: str) -> str:
        if s1 == s2:
            return s1
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        if s2[:len(s1)] == s1:
            return self.gcdOfStrings(s1, s2[len(s1):])
        else:
            return ""


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.gcdOfStrings, Solution()),
        [
            (["ABCABC", "ABC"], "ABC"),
            (["ABABAB", "ABAB"], "AB"),
            (["LEET", "CODE"], ""),
        ],
    )
