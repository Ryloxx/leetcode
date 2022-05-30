#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (17.00%)
# Likes:    2848
# Dislikes: 9924
# Total Accepted:    480.8K
# Total Submissions: 2.8M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.
#
# The integer division should truncate toward zero, which means losing its
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335
# would be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.
#
# Note: Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this
# problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31
# - 1, and if the quotient is strictly less than -2^31, then return -2^31.
#
#
# Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
#
#
# Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
#
#
#
# Constraints:
#
#
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0
#
#
#

from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    BOUND = 0x7FFFFFFF

    def in_bound(self, a: int, b: int) -> int:
        if a < 0:
            return a + b if b >= ~Solution.BOUND - a else ~Solution.BOUND
        else:
            return a + b if b <= Solution.BOUND - a else Solution.BOUND

    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise ValueError
        if (dividend == ~Solution.BOUND):
            if (divisor < 0):
                return self.in_bound(self.divide(dividend - divisor, divisor),
                                     1)
            return self.in_bound(self.divide(dividend + divisor, divisor), -1)
        if (divisor == ~Solution.BOUND):
            return 0
        if dividend < 0:
            return ~self.in_bound(self.divide(~dividend + 1, divisor), -1)
        if divisor < 0:
            return ~self.in_bound(self.divide(dividend, ~divisor + 1), -1)
        if dividend < divisor:
            return 0
        quotient, p, limit = 0, divisor, dividend >> 1
        while p <= limit:
            p <<= 1
            quotient += 1
        return self.in_bound(1 << quotient, self.divide(dividend - p, divisor))


# @lc code=end

if __name__ == "__main__":
    run(
        MethodType(Solution.divide, Solution()),
        [
            [[-2**31, 2], -1073741824],
            [[10, 3], 3],
            [[7, -3], -2],
            [[-3, -3], 1],
            [[2**31 - 1, 2], 1073741823],
            [[2**31 - 1, -2**31], 0],
            [[-2**31, 2**31 - 1], -1],
            [[-2**31, -2**31], 1],
            [[2**31 - 1, 2**31 - 1], 1],
            [[-2**31, 1], -2**31],
            [[2**31 - 1, 1], 2**31 - 1],
            [[-2**31, -1], 2**31 - 1],
            [[2**31 - 1, -1], -(2**31 - 1)],
            [[-2**31, (-2**31) // 2], 2],
            [[-2**31, ((-2**31) // 2) - 1], 1],
            [[-2**31, ((-2**31) // 2) + 1], 2],
            [[2**31 - 1, (2**31 - 1) // 2], 2],
            [[2**31 - 1, ((2**31 - 1) // 2) + 1], 1],
            [[2**31 - 1, ((2**31 - 1) // 2) - 1], 2],
            [[-2**31, 122481290], -17],
        ],
    )
