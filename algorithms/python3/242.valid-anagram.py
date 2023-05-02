#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (61.51%)
# Likes:    5781
# Dislikes: 232
# Total Accepted:    1.5M
# Total Submissions: 2.4M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#
from collections import Counter
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isAnagram, Solution()),
        [
            [["anagram", "nagaram"], True],
            [["rat", "car"], False],
            [["", ""], True],
        ],
    )
