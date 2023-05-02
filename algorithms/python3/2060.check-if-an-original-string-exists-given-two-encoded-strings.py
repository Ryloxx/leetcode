#
# @lc app=leetcode id=2060 lang=python3
#
# [2060] Check if an Original String Exists Given Two Encoded Strings
#
# https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/description/
#
# algorithms
# Hard (40.73%)
# Likes:    179
# Dislikes: 96
# Total Accepted:    6.8K
# Total Submissions: 16.7K
# Testcase Example:  '"internationalization"\n"i18n"'
#
# An original string, consisting of lowercase English letters, can be encoded
# by the following steps:
#
#
# Arbitrarily split it into a sequence of some number of non-empty
# substrings.
# Arbitrarily choose some elements (possibly none) of the sequence, and replace
# each with its length (as a numeric string).
# Concatenate the sequence as the encoded string.
#
#
# For example, one way to encode an original string "abcdefghijklmnop" might
# be:
#
#
# Split it as a sequence: ["ab", "cdefghijklmn", "o", "p"].
# Choose the second and third elements to be replaced by their lengths,
# respectively. The sequence becomes ["ab", "12", "1", "p"].
# Concatenate the elements of the sequence to get the encoded string:
# "ab121p".
#
#
# Given two encoded strings s1 and s2, consisting of lowercase English letters
# and digits 1-9 (inclusive), return true if there exists an original string
# that could be encoded as both s1 and s2. Otherwise, return false.
#
# Note: The test cases are generated such that the number of consecutive digits
# in s1 and s2 does not exceed 3.
#
#
# Example 1:
#
#
# Input: s1 = "internationalization", s2 = "i18n"
# Output: true
# Explanation: It is possible that "internationalization" was the original
# string.
# - "internationalization"
# ⁠ -> Split:       ["internationalization"]
# ⁠ -> Do not replace any element
# ⁠ -> Concatenate:  "internationalization", which is s1.
# - "internationalization"
# ⁠ -> Split:       ["i", "nternationalizatio", "n"]
# ⁠ -> Replace:     ["i", "18",                 "n"]
# ⁠ -> Concatenate:  "i18n", which is s2
#
#
# Example 2:
#
#
# Input: s1 = "l123e", s2 = "44"
# Output: true
# Explanation: It is possible that "leetcode" was the original string.
# - "leetcode"
# ⁠ -> Split:      ["l", "e", "et", "cod", "e"]
# ⁠ -> Replace:    ["l", "1", "2",  "3",   "e"]
# ⁠ -> Concatenate: "l123e", which is s1.
# - "leetcode"
# ⁠ -> Split:      ["leet", "code"]
# ⁠ -> Replace:    ["4",    "4"]
# ⁠ -> Concatenate: "44", which is s2.
#
#
# Example 3:
#
#
# Input: s1 = "a5b", s2 = "c5b"
# Output: false
# Explanation: It is impossible.
# - The original string encoded as s1 must start with the letter 'a'.
# - The original string encoded as s2 must start with the letter 'c'.
#
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 40
# s1 and s2 consist of digits 1-9 (inclusive), and lowercase English letters
# only.
# The number of consecutive digits in s1 and s2 does not exceed 3.
#
#
#
from functools import cache
from itertools import accumulate, takewhile
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def possiblyEquals(self, s1: str, s2: str) -> bool:
        s1, s2 = [
            list(map(lambda x: ord(x) - ord("0"), s + "a" + chr(255)))
            for s in [s1, s2]
        ]

        @cache
        def dfs(i=0, j=0, diff=0):
            c_1 = s1[i]
            c_2 = s2[j]
            if 10 <= c_1 < 123 and 10 <= c_2 < 123:
                if not diff:
                    return c_1 == c_2 and dfs(i + 1, j + 1, 0)
                elif diff < 0:
                    return dfs(i + 1, j, diff + 1)
                else:
                    return dfs(i, j + 1, diff - 1)
            return (any(
                dfs(i + offset * c_oi, j + offset * c_oj, diff + p * c_dd)
                for c_s, c_i, c_oi, c_oj, c_dd in [[s1, i, 1, 0, 1],
                                                   [s2, j, 0, 1, -1]]
                for offset, p in enumerate(
                    accumulate(takewhile(lambda x: c_s[x] < 10,
                                         range(c_i, len(c_s))),
                               lambda a, b: a * 10 + c_s[b],
                               initial=0)) if offset > 0)
                    or (not diff and (c_1 == c_2) and c_1 >= 123))

        return dfs()


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.possiblyEquals, Solution()),
        [
            [["l123e", "44"], True],
            [["123baby", "51baby"], True],
            [["123baby", "52aby"], True],
            [["456", "124"], False],
            [["a5b", "c5b"], False],
            [["456", "501"], True],
            [["123a456a789a" * 3, "123a456a789a" * 3], True],
            [["49u74v37v687u179v588u958u2", "2v191u7u275u937u5v883v2u61v"],
             False],
        ],
    )
