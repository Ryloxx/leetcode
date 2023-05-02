#
# @lc app=leetcode id=390 lang=python3
#
# [390] Elimination Game
#
# https://leetcode.com/problems/elimination-game/description/
#
# algorithms
# Medium (46.38%)
# Likes:    786
# Dislikes: 511
# Total Accepted:    46K
# Total Submissions: 99.2K
# Testcase Example:  '9'
#
# You have a list arr of all integers in the range [1, n] sorted in a strictly
# increasing order. Apply the following algorithm on arr:
#
#
# Starting from left to right, remove the first number and every other number
# afterward until you reach the end of the list.
# Repeat the previous step again, but this time from right to left, remove the
# rightmost number and every other number from the remaining numbers.
# Keep repeating the steps again, alternating left to right and right to left,
# until a single number remains.
#
#
# Given the integer n, return the last number that remains in arr.
#
#
# Example 1:
#
#
# Input: n = 9
# Output: 6
# Explanation:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [2, 4, 6, 8]
# arr = [2, 6]
# arr = [6]
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
#
#
#

from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def lastRemaining(self, n: int) -> int:
        if not n:
            return 0
        jump = res = switch = 1
        while n != 1:
            res += jump if switch or n & 1 else 0
            switch = not switch
            jump <<= 1
            n >>= 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.lastRemaining, Solution()),
        [
            [[24], 14],
            [[22], 8],
            [[9], 6],
            [[1], 1],
            [[100], 54],
            [[200], 94],
            [[300], 126],
            [[400], 214],
            [[10**9], 534765398],
        ],
    )
