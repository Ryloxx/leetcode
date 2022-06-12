#
# @lc app=leetcode id=2042 lang=python3
#
# [2042] Check if Numbers Are Ascending in a Sentence
#
# https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/
#
# algorithms
# Easy (67.49%)
# Likes:    273
# Dislikes: 13
# Total Accepted:    26.3K
# Total Submissions: 39K
# Testcase Example:  '"1 box has 3 blue 4 red 6 green and 12 yellow marbles"'
#
# A sentence is a list of tokens separated by a single space with no leading or
# trailing spaces. Every token is either a positive number consisting of digits
# 0-9 with no leading zeros, or a word consisting of lowercase English
# letters.
#
#
# For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2"
# and "4" are numbers and the other tokens such as "puppy" are words.
#
#
# Given a string s representing a sentence, you need to check if all the
# numbers in s are strictly increasing from left to right (i.e., other than the
# last number, each number is strictly smaller than the number on its right in
# s).
#
# Return true if so, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
# Output: true
# Explanation: The numbers in s are: 1, 3, 4, 6, 12.
# They are strictly increasing from left to right: 1 < 3 < 4 < 6 < 12.
#
#
# Example 2:
#
#
# Input: s = "hello world 5 x 5"
# Output: false
# Explanation: The numbers in s are: 5, 5. They are not strictly increasing.
#
#
# Example 3:
#
#
# Input: s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60
# s"
# Output: false
# Explanation: The numbers in s are: 7, 51, 50, 60. They are not strictly
# increasing.
#
#
#
# Constraints:
#
#
# 3 <= s.length <= 200
# s consists of lowercase English letters, spaces, and digits from 0 to 9,
# inclusive.
# The number of tokens in s is between 2 and 100, inclusive.
# The tokens in s are separated by a single space.
# There are at least two numbers in s.
# Each number in s is a positive number less than 100, with no leading
# zeros.
# s contains no leading or trailing spaces.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def tokenize(self, s: str):
        i = j = 0
        while j < len(s):
            while j < len(s) and s[j] == " ":
                j += 1
            i = j
            while j < len(s) and s[j] != " ":
                j += 1
            yield i, j

    def areNumbersAscending(self, s: str) -> bool:
        last = -float('inf')
        for i, j in self.tokenize(s):
            try:
                num = int(s[i:j])
                if num <= last:
                    return False
                last = num
            except ValueError:
                pass
        return True


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.areNumbersAscending, Solution()),
        [
            [["1 box has 3 blue 4 red 6 green and 12 yellow marbles"], True],
            [["hello world 5 x 5"], False],
            [[
                "sunset is at 7 51 pm overnight lows will "
                "be in the low 50 and 60"
            ], False],
        ],
    )
