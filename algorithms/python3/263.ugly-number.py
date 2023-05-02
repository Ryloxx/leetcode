#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (41.82%)
# Likes:    1949
# Dislikes: 1229
# Total Accepted:    343.4K
# Total Submissions: 820.8K
# Testcase Example:  '6'
#
# An ugly number is a positive integer whose prime factors are limited to 2, 3,
# and 5.
#
# Given an integer n, return true if n is an ugly number.
#
#
# Example 1:
#
#
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
#
#
# Example 2:
#
#
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are
# limited to 2, 3, and 5.
#
#
# Example 3:
#
#
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
#
#
#
# Constraints:
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    upper = pow(30, 32)

    def isUgly(self, n: int) -> bool:
        return n > 0 and not Solution.upper % n


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isUgly, Solution()),
        [
            ([6], True),
            ([1], True),
            ([14], False),
            ([0], False),
            ([-6], False),
            ([-1], False),
            ([-14], False),
            ([-0], False),
        ],
    )
