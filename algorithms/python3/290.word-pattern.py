#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (40.43%)
# Likes:    4612
# Dislikes: 534
# Total Accepted:    426.3K
# Total Submissions: 1M
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
#
#
# Example 1:
#
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
#
# Example 2:
#
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
#
# Example 3:
#
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:
        splitted = s.split()
        if len(pattern) != len(splitted):
            return False
        a_to_b = {}
        b_to_a = {}
        for a, b in zip(pattern, splitted):
            if (b in b_to_a and b_to_a[b] != a
                    or a in a_to_b and a_to_b[a] != b):
                return False
            b_to_a[b] = a
            a_to_b[a] = b
        return True


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.wordPattern, Solution()),
        [
            (["abba", "dog cat cat dog"], True),
            (["abba", "dog cat cat fish"], False),
            (["aaaa", "dog cat cat dog"], False),
            (["aaaa", "a a a a"], True),
            (["aaba", "a a a a"], False),
            (["aaba", "a a b a"], True),
            (["aaba", "a a c a"], True),
            (["aaba", "b a c a"], False),
            (["abc", "b c a"], True),
        ],
    )
