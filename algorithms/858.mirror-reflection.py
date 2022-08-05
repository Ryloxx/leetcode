#
# @lc app=leetcode id=858 lang=python3
#
# [858] Mirror Reflection
#
# https://leetcode.com/problems/mirror-reflection/description/
#
# algorithms
# Medium (59.61%)
# Likes:    933
# Dislikes: 2204
# Total Accepted:    64.6K
# Total Submissions: 102.7K
# Testcase Example:  '2\n1'
#
# There is a special square room with mirrors on each of the four walls. Except
# for the southwest corner, there are receptors on each of the remaining
# corners, numbered 0, 1, and 2.
#
# The square room has walls of length p and a laser ray from the southwest
# corner first meets the east wall at a distance q from the 0^th receptor.
#
# Given the two integers p and q, return the number of the receptor that the
# ray meets first.
#
# The test cases are guaranteed so that the ray will meet a receptor
# eventually.
#
#
# Example 1:
#
#
# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back
# to the left wall.
#
#
# Example 2:
#
#
# Input: p = 3, q = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= q <= p <= 1000
#
#
#
from math import gcd
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # O(logN) time complexity
    # O(1) space complexity
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        p, q = p // g % 2, q // g % 2
        return 1 - p + q


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.mirrorReflection, Solution()),
        [
            [[5, 2], 0],
            [[2, 1], 2],
            [[15, 14], 0],
            [[1000, 1], 2],
            [[3, 1], 1],
            [[5, 1], 1],
            [[5, 1], 1],
            [[10, 7], 2],
            [[4, 2], 2],
            [[6, 4], 0],
            [[12, 3], 2],
            [[12, 4], 1],
            [[12, 6], 2],
            [[14, 10], 1],
        ],
    )
