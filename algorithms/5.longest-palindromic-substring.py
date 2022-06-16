#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.80%)
# Likes:    18306
# Dislikes: 1084
# Total Accepted:    1.9M
# Total Submissions: 5.9M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(set(s)) == 1:
            return s

        def substrPalindrome(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j

        start, end = max((substrPalindrome(x, x + y) for y in range(2)
                          for x in range(len(s))),
                         key=lambda x: x[1] - x[0], default=(0, 0))
        return s[start:end]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestPalindrome, Solution()),
        [
            [["babad"], "bab"],
            [[""], ""],
            [["cbbd"], "bb"],
            [["aaaa"], "aaaa"],
            [["a" * 1000], "a" * 1000],
            [["a" * 1000 + "b"], "a" * 1000],
        ],
    )
