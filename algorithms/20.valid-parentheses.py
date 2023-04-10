#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.55%)
# Likes:    18885
# Dislikes: 1100
# Total Accepted:    3.2M
# Total Submissions: 7.9M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def isValid(self, s: str) -> bool:
        d_map = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            elif c in "([{":
                stack.append(d_map[c])
            else:
                return False
        return not stack


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isValid, Solution()),
        [
            (["()"], True),
            (["()[]{}"], True),
            (["(]"], False),
            (["([)]"], False),
            ([""], True),
            (["{[]}"], True),
        ],
    )
