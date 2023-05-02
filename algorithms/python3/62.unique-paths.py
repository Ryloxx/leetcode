#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (60.15%)
# Likes:    10318
# Dislikes: 321
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '3\n7'
#
# There is a robot on an m x n grid. The robot is initially located at the
# top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths
# that the robot can take to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to
# 2 * 10^9.
#
#
# Example 1:
#
#
# Input: m = 3, n = 7
# Output: 28
#
#
# Example 2:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach
# the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 100
#
#
#
from math import factorial
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        n, m = sorted([m, n])
        n -= 1
        m += n - 1
        return factorial(m) // (factorial(n) * factorial(m - n))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.uniquePaths, Solution()),
        [
            [[3, 7], 28],
            [[3, 2], 3],
        ],
    )
