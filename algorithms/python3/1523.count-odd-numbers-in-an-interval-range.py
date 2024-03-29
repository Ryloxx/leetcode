#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
#
# algorithms
# Easy (46.13%)
# Likes:    2241
# Dislikes: 136
# Total Accepted:    255.1K
# Total Submissions: 513.9K
# Testcase Example:  '3\n7'
#
# Given two non-negative integers low and high. Return the count of odd numbers
# between low and high (inclusive).
#
#
# Example 1:
#
#
# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
#
# Example 2:
#
#
# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].
#
#
# Constraints:
#
#
# 0 <= low <= high <= 10^9
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1 + low % 2 + high % 2) // 2


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.countOdds, Solution()),
        [
            ([3, 7], 3),
            ([8, 10], 1),
            ([5, 5], 1),
        ],
    )
