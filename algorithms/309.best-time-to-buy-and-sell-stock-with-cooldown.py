#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (54.70%)
# Likes:    7299
# Dislikes: 244
# Total Accepted:    350.9K
# Total Submissions: 636.8K
# Testcase Example:  '[1,2,3,0,2]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
#
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times) with the following restrictions:
#
#
# After you sell your stock, you cannot buy stock on the next day (i.e.,
# cooldown one day).
#
#
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
#
#
# Example 1:
#
#
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#
#
# Example 2:
#
#
# Input: prices = [1]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        b, s1, s2 = -prices[0], 0, 0
        for price in prices:
            b = max(b, s2 - price)
            s1, s2 = max(s1, b + price), s1
        return max(b, s1)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxProfit, Solution()),
        [
            ([[1, 2, 3, 0, 2]], 3),
            ([[1]], 0),
            ([[1, 2, 3, 0, 2, 4, 3, 4]], 5),
            ([[6, 1, 3, 2, 4, 7]], 6),
        ],
    )
