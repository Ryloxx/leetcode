#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# algorithms
# Easy (71.05%)
# Likes:    5053
# Dislikes: 198
# Total Accepted:    398.4K
# Total Submissions: 564.7K
# Testcase Example:  '"abbaca"'
#
# You are given a string s consisting of lowercase English letters. A duplicate
# removal consists of choosing two adjacent and equal letters and removing
# them.
#
# We repeatedly make duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It
# can be proven that the answer is unique.
#
#
# Example 1:
#
#
# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent
# and equal, and this is the only possible move.  The result of this move is
# that the string is "aaca", of which only "aa" is possible, so the final
# string is "ca".
#
#
# Example 2:
#
#
# Input: s = "azxxzy"
# Output: "ay"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
                continue
            stack.append(c)

        return "".join(stack)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.removeDuplicates, Solution()),
        [
            (["abbaca"], "ca"),
            (["azxxzy"], "ay"),
        ],
    )
