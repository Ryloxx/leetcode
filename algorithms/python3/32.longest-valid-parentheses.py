#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (31.33%)
# Likes:    7788
# Dislikes: 265
# Total Accepted:    487.3K
# Total Submissions: 1.6M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
#
# Example 1:
#
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
#
# Example 2:
#
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
#
# Example 3:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
#
#
#

from types import MethodType
from algo_input import run


# @lc code=start
class Solution:

    def longestValidParentheses(self, s: str) -> int:
        stack, parenthesis, longest_sub = [], [], 0
        for char in s:
            if char == "(":
                stack.append([1, 0])
            else:
                if stack and stack[-1][0]:
                    stack[-1][0] -= 1
                    stack[-1][1] += 1
                    longest_sub = max(longest_sub, stack[-1][1])
                else:
                    parenthesis.append(-float('inf'))
            if stack and not stack[-1][0]:
                _, c = stack.pop()
                if stack:
                    stack[-1][1] += c
                    longest_sub = max(longest_sub, stack[-1][1])
                else:
                    parenthesis.append(c)
        parenthesis += [-float('inf'), longest_sub]
        current_longest = res = 0
        for length in parenthesis:
            current_longest = max(0, current_longest + length)
            res = max(res, current_longest)
        return res * 2


# @lc code=end

if __name__ == "__main__":
    run(MethodType(Solution.longestValidParentheses, Solution()), [
        [["(()"], 2],
        [[")()())"], 4],
        [["(())(())"], 8],
        [["(())(())"], 8],
        [["(()(())"], 6],
        [["()(())"], 6],
        [["(()())((()))"], 12],
        [["(()())((())"], 6],
        [["(((("], 0],
        [["(((()"], 2],
        [["))()))"], 2],
        [[""], 0],
        [["(()(((()"], 2],
        [["(()()(((()"], 4],
    ])
