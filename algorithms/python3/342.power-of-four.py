#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (44.07%)
# Likes:    2284
# Dislikes: 313
# Total Accepted:    368.1K
# Total Submissions: 814.8K
# Testcase Example:  '16'
#
# Given an integer n, return true if it is a power of four. Otherwise, return
# false.
#
# An integer n is a power of four, if there exists an integer x such that n ==
# 4^x.
#
#
# Example 1:
# Input: n = 16
# Output: true
# Example 2:
# Input: n = 5
# Output: false
# Example 3:
# Input: n = 1
# Output: true
#
#
# Constraints:
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without loops/recursion?
#
from types import MethodType
from algo_input import run


# @lc code=start
class Solution:

    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1)) and n & 1431655765 == n


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isPowerOfFour, Solution()),
        [
            [[16], True],
            [[5], False],
            [[1], True],
        ],
    )
