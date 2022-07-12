#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (40.32%)
# Likes:    2367
# Dislikes: 179
# Total Accepted:    97.4K
# Total Submissions: 243.6K
# Testcase Example:  '[1,1,2,2,2]'
#
# You are given an integer array matchsticks where matchsticks[i] is the length
# of the i^th matchstick. You want to use all the matchsticks to make one
# square. You should not break any stick, but you can link them up, and each
# matchstick must be used exactly one time.
#
# Return true if you can make this square and false otherwise.
#
#
# Example 1:
#
#
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
#
#
# Example 2:
#
#
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
#
#
#
# Constraints:
#
#
# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 10^8
#
#
#
from functools import cache
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def makesquare(self, matchsticks: List[int]) -> bool:
        side_length = sum(matchsticks)
        if not side_length or side_length % 4:
            return False
        side_length //= 4

        @cache
        def dp(available_matchsticks):
            if not available_matchsticks:
                return 0
            for i in range(len(matchsticks)):
                if available_matchsticks & (1 << i):
                    unfilled_side = dp(available_matchsticks ^ 1 << i)
                    if unfilled_side >= 0 and unfilled_side + matchsticks[
                            i] <= side_length:
                        return (unfilled_side + matchsticks[i]) % side_length
            return -1

        return not dp((1 << len(matchsticks)) - 1)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.makesquare, Solution()),
        [
            [[[12, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60]],
             False],
            [[[5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]], True],
            [[[5, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], True],
            [[[
                7215807, 6967211, 5551998, 6632092, 2802439, 821366, 2465584,
                9415257, 8663937, 3976802, 2850841, 803069, 2294462, 8242205,
                9922998
            ]], False],
            [[[9, 9, 3, 9, 7, 7, 7, 6, 4, 9, 8, 6, 8, 1, 5]], False],
            [[[18, 16, 14, 17, 13, 14, 11, 14, 1, 2, 18, 7, 3, 20, 17]], False
             ],
            [[[5, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], False],
            [[[1, 1, 2, 2, 2]], True],
            [[[1, 1, 1, 1]], True],
            [[[10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], False],
            [[[1, 1, 1, 1, 1]], False],
            [[[15]], False],
            [[[1, 15, 1, 1]], False],
            [[[]], False],
            [[[3, 3, 3, 3, 4]], False],
        ],
    )
