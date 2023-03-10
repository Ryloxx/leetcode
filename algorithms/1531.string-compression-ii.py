#
# @lc app=leetcode id=1531 lang=python3
#
# [1531] String Compression II
#
# https://leetcode.com/problems/string-compression-ii/description/
#
# algorithms
# Hard (38.08%)
# Likes:    827
# Dislikes: 67
# Total Accepted:    18.2K
# Total Submissions: 42K
# Testcase Example:  '"aaabcccd"\n2'
#
# Run-length encoding is a string compression method that works by replacing
# consecutive identical characters (repeated 2 or more times) with the
# concatenation of the character and the number marking the count of the
# characters (length of the run). For example, to compress the string "aabccc"
# we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string
# becomes "a2bc3".
#
# Notice that in this problem, we are not adding '1' after single characters.
#
# Given a string s and an integer k. You need to delete at most k characters
# from s such that the run-length encoded version of s has minimum length.
#
# Find the minimum length of the run-length encoded version of s after deleting
# at most k characters.
#
#
# Example 1:
#
#
# Input: s = "aaabcccd", k = 2
# Output: 4
# Explanation: Compressing s without deleting anything will give us "a3bc3d" of
# length 6. Deleting any of the characters 'a' or 'c' would at most decrease
# the length of the compressed string to 5, for instance delete 2 'a' then we
# will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way
# is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of
# length 4.
#
# Example 2:
#
#
# Input: s = "aabbaa", k = 2
# Output: 2
# Explanation: If we delete both 'b' characters, the resulting compressed
# string would be "a4" of length 2.
#
#
# Example 3:
#
#
# Input: s = "aaaaaaaaaaa", k = 0
# Output: 3
# Explanation: Since k is zero, we cannot delete anything. The compressed
# string is "a11" of length 3.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 100
# 0 <= k <= s.length
# s contains only lowercase English letters.
#
#
#
from functools import cache
from sys import maxsize
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @cache
        def dp(i: int, j: int, prev_letter: str, prev_count: int):
            if i >= len(s):
                return 0
            if s[i] == prev_letter:
                return dp(i + 1, j, s[i], prev_count + 1) + int(
                    prev_count <= 1 or prev_count == 9 or prev_count == 99)
            else:
                return min(
                    dp(i + 1, j, s[i], 1) + 1,
                    maxsize if j <= 0 else dp(i + 1, j -
                                              1, prev_letter, prev_count))

        return dp(0, k, "", 0)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.getLengthOfOptimalCompression, Solution()),
        [
            (["aabbaa", 2], 2),
            (["aaabcccd", 2], 4),
            (["aaaaaaaaaaa", 0], 3),
            (["", 0], 0),
            (["a" * 100, 0], 4),
            (["a" * 100, 1], 3),
            (["a" * 100, 10], 3),
            (["a" * 100, 90], 3),
            (["a" * 100, 91], 2),
            (["a" * 100, 98], 2),
            (["a" * 100, 99], 1),
            (["a" * 100, 100], 0),
        ],
    )
