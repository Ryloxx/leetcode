#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (49.02%)
# Likes:    9700
# Dislikes: 295
# Total Accepted:    671.8K
# Total Submissions: 1.4M
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
#
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
# Example 2:
#
#
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
#
# Constraints:
#
#
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
#
#
#
from typing import Counter, List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        count, window, start, c, ans = Counter(p), Counter(), 0, 0, []
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
                    ans.append(start)
        return ans


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findAnagrams, Solution()),
        [
            (["cbaebabacd", "abc"], [0, 6]),
            (["abab", "ab"], [0, 1, 2]),
        ],
    )
