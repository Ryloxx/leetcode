#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (51.90%)
# Likes:    8390
# Dislikes: 362
# Total Accepted:    607K
# Total Submissions: 1.2M
# Testcase Example:  '12'
#
# Given an integer n, return the least number of perfect square numbers that
# sum to n.
#
# A perfect square is an integer that is the square of an integer; in other
# words, it is the product of some integer with itself. For example, 1, 4, 9,
# and 16 are perfect squares while 3 and 11 are not.
#
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#
from algo_input import run
from types import MethodType
from math import sqrt


# @lc code=start
class Solution:

    def numSquares(self, n: int) -> int:
        limit = int(sqrt(n)) + 1
        for i in range(limit):
            for j in range(i, limit):
                k = int(sqrt((abs(n - i**2 - j**2))))
                if i**2 + j**2 + k**2 == n:
                    return sum(map(bool, [i, j, k]))
        return 4


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numSquares, Solution()),
        [
            ([12], 3),
            ([13], 2),
            ([2], 2),
        ],
    )
