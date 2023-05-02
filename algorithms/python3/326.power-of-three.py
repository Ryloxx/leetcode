#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (43.52%)
# Likes:    1877
# Dislikes: 178
# Total Accepted:    564.5K
# Total Submissions: 1.3M
# Testcase Example:  '27'
#
# Given an integer n, return true if it is a power of three. Otherwise, return
# false.
#
# An integer n is a power of three, if there exists an integer x such that n ==
# 3^x.
#
#
# Example 1:
#
#
# Input: n = 27
# Output: true
#
#
# Example 2:
#
#
# Input: n = 0
# Output: false
#
#
# Example 3:
#
#
# Input: n = 9
# Output: true
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
# Follow up: Could you solve it without loops/recursion?
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and not 3486784401 % n


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isPowerOfThree, Solution()),
        [
            [[27], True],
            [[0], False],
            [[42], False],
            [[100], False],
            [[-100], False],
            [[-9], False],
            [[-27], False],
            [[9], True],
            [[1], True],
        ],
    )
