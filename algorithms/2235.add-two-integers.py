#
# @lc app=leetcode id=2235 lang=python3
#
# [2235] Add Two Integers
#
# https://leetcode.com/problems/add-two-integers/description/
#
# algorithms
# Easy (93.12%)
# Likes:    149
# Dislikes: 628
# Total Accepted:    26.6K
# Total Submissions: 28.5K
# Testcase Example:  '12\n5'
#
# Given two integers num1 and num2, return the sum of the two integers.
#
# Example 1:
#
#
# Input: num1 = 12, num2 = 5
# Output: 17
# Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is
# returned.
#
#
# Example 2:
#
#
# Input: num1 = -10, num2 = 4
# Output: -6
# Explanation: num1 + num2 = -6, so -6 is returned.
#
#
#
# Constraints:
#
#
# -100 <= num1, num2 <= 100
#
#
#

from types import MethodType
from algo_input import run

# @lc code=start


class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


# @lc code=end

run(
    MethodType(Solution.sum, Solution()),
    [
        [[-10, 4], -6],
        [[0, 4], 4],
        [[10, 4], 14],
        [[12, 5], 17],
    ],
)
