#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#
# https://leetcode.com/problems/break-a-palindrome/description/
#
# algorithms
# Medium (52.30%)
# Likes:    1666
# Dislikes: 627
# Total Accepted:    116.8K
# Total Submissions: 219.5K
# Testcase Example:  '"abccba"'
#
# Given a palindromic string of lowercase English letters palindrome, replace
# exactly one character with any lowercase English letter so that the resulting
# string is not a palindrome and that it is the lexicographically smallest one
# possible.
#
# Return the resulting string. If there is no way to replace a character to
# make it not a palindrome, return an empty string.
#
# A string a is lexicographically smaller than a string b (of the same length)
# if in the first position where a and b differ, a has a character strictly
# smaller than the corresponding character in b. For example, "abcc" is
# lexicographically smaller than "abcd" because the first position they differ
# is at the fourth character, and 'c' is smaller than 'd'.
#
#
# Example 1:
#
#
# Input: palindrome = "abccba"
# Output: "aaccba"
# Explanation: There are many ways to make "abccba" not a palindrome, such as
# "zbccba", "aaccba", and "abacba".
# Of all the ways, "aaccba" is the lexicographically smallest.
#
#
# Example 2:
#
#
# Input: palindrome = "a"
# Output: ""
# Explanation: There is no way to replace a single character to make "a" not a
# palindrome, so return an empty string.
#
#
#
# Constraints:
#
#
# 1 <= palindrome.length <= 1000
# palindrome consists of only lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]
        return palindrome[:-1] + "b"


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.breakPalindrome, Solution()),
        [
            (["abccba"], "aaccba"),
            (["aabcaa"], "aaacaa"),
            (["aba"], "abb"),
            (["aacaa"], "aacab"),
            (["abba"], "aaba"),
            (["abaaba"], "aaaaba"),
            (["aaaa"], "aaab"),
            (["zzzz"], "azzz"),
            (["a"], ""),
            ([""], ""),
        ],
    )
