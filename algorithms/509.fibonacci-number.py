#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
# https://leetcode.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (68.22%)
# Likes:    4042
# Dislikes: 274
# Total Accepted:    861.8K
# Total Submissions: 1.3M
# Testcase Example:  '2'
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
#
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
#
#
# Given n, calculate F(n).
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#
#
# Example 3:
#
#
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
#
# Constraints:
#
#
# 0 <= n <= 30
#
#
#
from functools import cache
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(N) time complexity
    # O(1) space complxity (without cache)
    @cache
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

    # O(1) time complexity
    # O(N) space complexity
    # LOOKUP = [
    #     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
    #     1597,
    #     2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
    #     317811, 514229, 832040
    # ]

    # def fib(self, n: int) -> int:
    #     return Solution.LOOKUP[n]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.fib, Solution()),
        [
            [[0], 0],
            [[1], 1],
            [[2], 1],
            [[10], 55],
            [[30], 832040],
        ],
    )
