#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (51.10%)
# Likes:    16080
# Dislikes: 481
# Total Accepted:    2.1M
# Total Submissions: 4M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
# Constraints:
#
#
# 1 <= n <= 45
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        while n > 2:
            b, a = a + b, b
            n -= 1
        return 1 if n <= 1 else b


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.climbStairs, Solution()),
        [
            ([2], 2),
            ([3], 3),
        ],
    )
