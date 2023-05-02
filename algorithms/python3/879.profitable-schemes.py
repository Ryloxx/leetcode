#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#
# https://leetcode.com/problems/profitable-schemes/description/
#
# algorithms
# Hard (40.37%)
# Likes:    699
# Dislikes: 64
# Total Accepted:    21.3K
# Total Submissions: 49.9K
# Testcase Example:  '5\n3\n[2,2]\n[2,3]'
#
# There is a group of n members, and a list of various crimes they could
# commit. The i^th crime generates a profit[i] and requires group[i] members to
# participate in it. If a member participates in one crime, that member can't
# participate in another crime.
#
# Let's call a profitable scheme any subset of these crimes that generates at
# least minProfit profit, and the total number of members participating in that
# subset of crimes is at most n.
#
# Return the number of schemes that can be chosen. Since the answer may be very
# large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# Output: 2
# Explanation: To make a profit of at least 3, the group could either commit
# crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.
#
# Example 2:
#
#
# Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# Output: 7
# Explanation: To make a profit of at least 5, the group could commit any
# crimes, as long as they commit one.
# There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and
# (0,1,2).
#
#
# Constraints:
#
#
# 1 <= n <= 100
# 0 <= minProfit <= 100
# 1 <= group.length <= 100
# 1 <= group[i] <= 100
# profit.length == group.length
# 0 <= profit[i] <= 100
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def profitableSchemes(self, n: int, minProfit: int, group: List[int],
                          profit: List[int]) -> int:
        if not group:
            return 0
        MOD = 10**9 + 7

        dp = [[[0 for _ in range(minProfit + 1)] for _ in range(n + 1)]
              for _ in range(len(group) + 1)]
        for i in range(n + 1):
            dp[len(group)][i][minProfit] = 1

        for idx in range(len(group) - 1, -1, -1):
            for group_length in range(n + 1):
                for curr_profit in range(minProfit + 1):
                    dp[idx][group_length][curr_profit] = (
                        dp[idx + 1][group_length][curr_profit] +
                        (dp[idx + 1][group_length + group[idx]][min(
                            minProfit, curr_profit + profit[idx])]
                         if group_length + group[idx] <= n else 0)) % MOD

        return dp[0][0][0]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.profitableSchemes, Solution()),
        [
            ([5, 3, [2, 2], [2, 3]], 2),
            ([10, 5, [2, 3, 5], [6, 7, 8]], 7),
            ([10, 5, [], []], 0),
            ([
                100, 100,
                [
                    18, 58, 88, 52, 54, 13, 50, 66, 83, 61, 100, 54, 60, 80, 1,
                    19, 78, 54, 67, 20, 57, 46, 12, 6, 14, 43, 64, 81, 30, 60,
                    48, 53, 86, 71, 51, 23, 71, 87, 95, 69, 11, 12, 41, 36, 69,
                    89, 91, 10, 98, 31, 67, 85, 16, 83, 83, 14, 14, 71, 33, 5,
                    40, 61, 22, 19, 34, 70, 50, 21, 91, 77, 4, 36, 16, 38, 56,
                    23, 68, 51, 71, 38, 63, 52, 14, 47, 25, 57, 95, 35, 58, 32,
                    1, 39, 48, 33, 89, 9, 1, 95, 90, 78
                ],
                [
                    96, 77, 37, 98, 66, 44, 18, 37, 47, 9, 38, 82, 74, 12, 71,
                    31, 80, 64, 15, 45, 85, 52, 70, 53, 94, 90, 90, 14, 98, 22,
                    33, 39, 18, 22, 10, 46, 6, 19, 25, 50, 33, 15, 63, 93, 35,
                    0, 76, 44, 37, 68, 35, 80, 70, 66, 4, 88, 66, 93, 49, 19,
                    25, 90, 21, 59, 17, 40, 46, 79, 5, 41, 2, 37, 27, 92, 0,
                    53, 57, 91, 75, 0, 42, 100, 16, 97, 83, 75, 57, 61, 73, 21,
                    63, 97, 75, 95, 84, 14, 98, 47, 0, 13
                ]
            ], 5570822),
        ],
    )
