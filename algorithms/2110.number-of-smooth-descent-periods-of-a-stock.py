#
# @lc app=leetcode id=2110 lang=python3
#
# [2110] Number of Smooth Descent Periods of a Stock
#
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/
#
# algorithms
# Medium (55.67%)
# Likes:    363
# Dislikes: 13
# Total Accepted:    19.7K
# Total Submissions: 35.3K
# Testcase Example:  '[3,2,1,4]'
#
# You are given an integer array prices representing the daily price history of
# a stock, where prices[i] is the stock price on the i^th day.
#
# A smooth descent period of a stock consists of one or more contiguous days
# such that the price on each day is lower than the price on the preceding day
# by exactly 1. The first day of the period is exempted from this rule.
#
# Return the number of smooth descent periods.
#
#
# Example 1:
#
#
# Input: prices = [3,2,1,4]
# Output: 7
# Explanation: There are 7 smooth descent periods:
# [3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
# Note that a period with one day is a smooth descent period by the
# definition.
#
#
# Example 2:
#
#
# Input: prices = [8,6,7,7]
# Output: 4
# Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
# Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.
#
#
# Example 3:
#
#
# Input: prices = [1]
# Output: 1
# Explanation: There is 1 smooth descent period: [1]
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 10^5
# 1 <= prices[i] <= 10^5
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def getDescentPeriods(self, prices: List[int]) -> int:
        res, streak = 0, 1
        for idx in range(1, len(prices)):
            res += streak
            streak += 1
            if prices[idx] - prices[idx - 1] != -1:
                streak = 1
        return res + streak


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.getDescentPeriods, Solution()),
        [
            [[[3, 2, 1, 4]], 7],
            [[[8, 6, 7, 7]], 4],
            [[[1]], 1],
        ],
    )
