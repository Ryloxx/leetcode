#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (43.59%)
# Likes:    8239
# Dislikes: 271
# Total Accepted:    553.2K
# Total Submissions: 1.3M
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of
# s2.
#
#
# Example 1:
#
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
# Example 2:
#
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
#
#
#
from typing import Counter
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def checkInclusion(self, p: str, s: str) -> bool:
        count, window, start, c = Counter(p), Counter(), 0, 0
        for index, i in enumerate(s):
            if i not in count:
                c, start, window = 0, index + 1, Counter()
            else:
                c += 1
                window[i] += 1
                while window[i] > count[i]:
                    window[s[start]] -= 1
                    c -= 1
                    start += 1
                if c == len(p):
                    return True
        return False


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.checkInclusion, Solution()),
        [
            (["ab", "eidbaooo"], True),
            (["ab", "eidboaoo"], False),
        ],
    )
