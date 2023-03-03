#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Medium (37.77%)
# Likes:    2692
# Dislikes: 134
# Total Accepted:    1.6M
# Total Submissions: 4.2M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#
# Example 1:
#
#
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
#
# Example 2:
#
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
#
#
#
# Constraints:
#
#
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        i = 1
        j = 0
        kmp = [0] * len(needle)
        while i < len(needle):
            if needle[i] == needle[j]:
                kmp[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = kmp[j - 1]
            else:
                i += 1
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = kmp[j - 1]
            else:
                i += 1
        return i - len(needle) if j == len(needle) else -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.strStr, Solution()),
        [
            (["sadbutsad", "sad"], 0),
            (["leetcode", "leeto"], -1),
        ],
    )
