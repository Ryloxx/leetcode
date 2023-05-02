#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#
# https://leetcode.com/problems/validate-stack-sequences/description/
#
# algorithms
# Medium (67.63%)
# Likes:    4215
# Dislikes: 73
# Total Accepted:    206.5K
# Total Submissions: 303.6K
# Testcase Example:  '[1,2,3,4,5]\n[4,5,3,2,1]'
#
# Given two integer arrays pushed and popped each with distinct values, return
# true if this could have been the result of a sequence of push and pop
# operations on an initially empty stack, or false otherwise.
#
#
# Example 1:
#
#
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#
#
# Example 2:
#
#
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
#
#
#
# Constraints:
#
#
# 1 <= pushed.length <= 1000
# 0 <= pushed[i] <= 1000
# All the elements of pushed are unique.
# popped.length == pushed.length
# popped is a permutation of pushed.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def validateStackSequences(self, pushed: List[int],
                               popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            while j < len(popped) and stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.validateStackSequences, Solution()),
        [
            ([[1, 2, 3, 4, 5], [4, 5, 3, 2, 1]], True),
            ([[1, 2, 3, 4, 5], [4, 3, 5, 1, 2]], False),
        ],
    )
