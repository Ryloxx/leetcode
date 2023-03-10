#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (28.65%)
# Likes:    4982
# Dislikes: 4404
# Total Accepted:    850.5K
# Total Submissions: 2.7M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will
# be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single
# space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between
# two words. The returned string should only have a single space separating the
# words. Do not include any extra spaces.
#
#
# Example 1:
#
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
#
# Example 2:
#
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
#
#
# Example 3:
#
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces '
# '.
# There is at least one word in s.
#
#
#
# Follow-up: If the string data type is mutable in your language, can you solve
# it in-place with O(1) extra space?
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
        # @lc code=end


if __name__ == "__main__":
    run(
        MethodType(Solution.reverseWords, Solution()),
        [
            (["the sky is blue"], "blue is sky the"),
            (["  hello world  "], "world hello"),
            (["a good   example"], "example good a"),
        ],
    )
