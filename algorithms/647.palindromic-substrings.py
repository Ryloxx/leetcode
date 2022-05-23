#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (64.72%)
# Likes:    6293
# Dislikes: 155
# Total Accepted:    408.3K
# Total Submissions: 630.7K
# Testcase Example:  '"abc"'
#
# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.
#
#
# Example 1:
#
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
# Example 2:
#
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
#
#
#

from string import ascii_letters
from types import MethodType

from algo_input import run

# @lc code=start


class Solution:

    def countSubstrings(self, s: str) -> int:

        def palin(i, j):
            res = 0
            while i >= 0 and j < len(s) and i <= j:
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
                res += 1
            return res

        i = 0
        res = 0
        while i < len(s):
            l, r = i - 1, i
            while r < len(s) - 1 and s[r] == s[r + 1]:
                r += 1
            res += (r - l) * (r - l + 1) // 2
            res += palin(l, r + 1)
            i = r + 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.countSubstrings, Solution()),
        [
            [["a"], 1],
            [[""], 0],
            [["abc"], 3],
            [["aaa"], 6],
            [[ascii_letters + "".join(reversed(ascii_letters))], 156],
        ],
    )
