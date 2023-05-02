#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#
# https://leetcode.com/problems/maximum-ice-cream-bars/description/
#
# algorithms
# Medium (65.69%)
# Likes:    1084
# Dislikes: 451
# Total Accepted:    79K
# Total Submissions: 108.8K
# Testcase Example:  '[1,3,2,4,1]\n7'
#
# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
#
# At the store, there are n ice cream bars. You are given an array costs of
# length n, where costs[i] is the price of the i^th ice cream bar in coins. The
# boy initially has coins coins to spend, and he wants to buy as many ice cream
# bars as possible.
#
# Return the maximum number of ice cream bars the boy can buy with coins
# coins.
#
# Note: The boy can buy the ice cream bars in any order.
#
#
# Example 1:
#
#
# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total
# price of 1 + 3 + 2 + 1 = 7.
#
#
# Example 2:
#
#
# Input: costs = [10,6,8,7,7,8], coins = 5
# Output: 0
# Explanation: The boy cannot afford any of the ice cream bars.
#
#
# Example 3:
#
#
# Input: costs = [1,6,3,1,2,5], coins = 20
# Output: 6
# Explanation: The boy can buy all the ice cream bars for a total price of 1 +
# 6 + 3 + 1 + 2 + 5 = 18.
#
#
#
# Constraints:
#
#
# costs.length == n
# 1 <= n <= 10^5
# 1 <= costs[i] <= 10^5
# 1 <= coins <= 10^8
#
#
# from itertools import accumulate
from typing import Counter, List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # O(N) time complexity
    # O(N) space complexity
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freqs = Counter(costs)
        bought = 0
        for i in filter(lambda x: x in freqs, range(10**5 + 1)):
            count = min(coins // i if i else float("inf"), freqs[i])
            coins -= i * count  # type: ignore
            bought += count
            freqs.pop(i)
            if not freqs or not count:
                break
        return bought  # type: ignore

    # O(NlogN) time complexity
    # O(1) space complexity
    # def maxIceCream(self, costs: List[int], coins: int) -> int:
    #     costs.sort()
    #     for i, s in enumerate(accumulate(costs)):
    #         if s > coins:
    #             return i
    #     return len(costs)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxIceCream, Solution()),
        [
            ([[1, 3, 2, 4, 1], 7], 4),
            ([[10, 6, 8, 7, 7, 8], 5], 0),
            ([[1, 6, 3, 1, 2, 5], 20], 6),
            ([[1, 1, 1, 1, 1, 1], 100], 6),
            ([[1, 1, 1, 1, 1, 1, 1, 1], 6], 6),
            ([[1, 1, 1, 1, 1, 1, 100], 100], 6),
            ([[0, 0, 0, 0], 100], 4),
            ([[0, 0, 0, 0, 101], 100], 4),
            ([[101, 0, 0, 0, 101], 100], 3),
        ],
    )
