#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (65.35%)
# Likes:    4451
# Dislikes: 149
# Total Accepted:    139.9K
# Total Submissions: 214.2K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string s, return the score of the string.
#
# The score of a balanced parentheses string is based on the following
# rule:
#
#
# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: 1
#
#
# Example 2:
#
#
# Input: s = "(())"
# Output: 2
#
#
# Example 3:
#
#
# Input: s = "()()"
# Output: 2
#
#
#
# Constraints:
#
#
# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                p = stack.pop()
                stack[-1] += max(p * 2, 1)

        return stack[0]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.scoreOfParentheses, Solution()),
        [[["()"], 1], [["(())"], 2], [["()()"], 2], [["(()())((()))"], 8],
         [["((()(())))((()))"], 16]],
    )
