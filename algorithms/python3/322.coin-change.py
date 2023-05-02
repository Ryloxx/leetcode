#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (40.17%)
# Likes:    11505
# Dislikes: 272
# Total Accepted:    997.7K
# Total Submissions: 2.5M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
#
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Example 3:
#
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#

from functools import cache
from types import MethodType
from typing import List

from algo_input import run

# @lc code=start


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(filter(None, coins))

        @cache
        def dfs(current=0):
            if current > amount:
                return float("inf")
            if current == amount:
                return 0
            return 1 + min((dfs(current + i) for i in coins), default=-1)

        res = dfs()
        return -1 if res == float("inf") else res


# @lc code=end

if __name__ == "__main__":
    run(MethodType(Solution.coinChange, Solution()),
        [[[[1, 2, 0, 3, 4], 10], 3]])
