#
# @lc app=leetcode id=1563 lang=python3
#
# [1563] Stone Game V
#
# https://leetcode.com/problems/stone-game-v/description/
#
# algorithms
# Hard (40.84%)
# Likes:    386
# Dislikes: 60
# Total Accepted:    13.2K
# Total Submissions: 32.5K
# Testcase Example:  '[6,2,3,4,5,5]'
#
# There are several stones arranged in a row, and each stone has an associated
# value which is an integer given in the array stoneValue.
#
# In each round of the game, Alice divides the row into two non-empty rows
# (i.e. left row and right row), then Bob calculates the value of each row
# which is the sum of the values of all the stones in this row. Bob throws away
# the row which has the maximum value, and Alice's score increases by the value
# of the remaining row. If the value of the two rows are equal, Bob lets Alice
# decide which row will be thrown away. The next round starts with the
# remaining row.
#
# The game ends when there is only one stone remaining. Alice's is initially
# zero.
#
# Return the maximum score that Alice can obtain.
#
#
# Example 1:
#
#
# Input: stoneValue = [6,2,3,4,5,5]
# Output: 18
# Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5].
# The left row has the value 11 and the right row has value 14. Bob throws away
# the right row and Alice's score is now 11.
# In the second round Alice divides the row to [6], [2,3]. This time Bob throws
# away the left row and Alice's score becomes 16 (11 + 5).
# The last round Alice has only one choice to divide the row which is [2], [3].
# Bob throws away the right row and Alice's score is now 18 (16 + 2). The game
# ends because only one stone is remaining in the row.
#
#
# Example 2:
#
#
# Input: stoneValue = [7,7,7,7,7,7,7]
# Output: 28
#
#
# Example 3:
#
#
# Input: stoneValue = [4]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= stoneValue.length <= 500
# 1 <= stoneValue[i] <= 10^6
#
#
#
from functools import cache
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def stoneGameV(self, stoneValue: List[int]) -> int:

        @cache
        def cSum(i):
            if i < 0:
                return 0
            return cSum(i - 1) + stoneValue[i]

        @cache
        def prefix(i, j):
            return cSum(j) - cSum(i - 1)

        @cache
        def findK(i, j):
            if i == j:
                return i
            k = findK(i, j - 1)
            while prefix(i, k) * 2 < prefix(i, j):
                k += 1
            return k

        dp, left, right = [[[0] * len(stoneValue)
                            for _ in range(len(stoneValue))] for _ in range(3)]
        for i in range(len(stoneValue)):
            left[i][i] = right[i][i] = stoneValue[i]
        for step in range(1, len(stoneValue)):
            for i in range(len(stoneValue) - step):
                j = i + step
                k = findK(i, j)
                if prefix(i, k) * 2 == prefix(i, j):
                    dp[i][j] = max(left[i][k], right[k + 1][j])
                else:
                    dp[i][j] = max(left[i][k - 1] if k != i else 0,
                                   right[k + 1][j] if k != j else 0)
                left[i][j] = max(left[i][j - 1], prefix(i, j) + dp[i][j])
                right[i][j] = max(right[i + 1][j], prefix(i, j) + dp[i][j])
        return dp[0][-1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.stoneGameV, Solution()),
        [
            [[[
                39994, 3, 4, 10000, 10000, 10000, 10000, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1000000
            ]], 150003],
            [[[6, 2, 3, 4, 5, 5]], 18],
            [[[6, 2, 3]], 7],
            [[[7, 7, 7, 7, 7, 7, 7]], 28],
            [[[4]], 0],
            [[[
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661, 809661,
                809661, 809661, 809661, 809661, 809661, 809661, 809661
            ]], 240469317],
            [[[
                73, 19, 19, 43, 17, 58, 82, 12, 41, 16, 79, 52, 94, 36, 98, 36,
                31, 4, 88, 8, 38, 50, 62, 62, 21, 34, 86, 61, 93, 63, 24, 44,
                55, 86, 74, 82, 76, 87, 13, 13, 67, 26, 71, 93, 62, 15, 68, 92,
                63, 91, 53, 79, 74, 95, 34, 72, 9, 55, 11, 98, 29, 81, 90, 78,
                92, 36, 37, 19, 76, 93, 65, 16, 16, 77, 92, 65, 39, 12, 63, 70,
                88, 18, 60, 4, 36, 33, 81, 30, 15, 34, 56, 86, 50, 45, 44, 60,
                87, 78, 4, 38, 96, 94, 57, 17, 57, 59, 13, 77, 99, 89, 23, 78,
                33, 80, 75, 93, 88, 29, 2, 8, 25, 41, 14, 80, 57, 65, 25, 55,
                41, 35, 46, 84, 98, 8, 7, 2, 81, 45, 98, 97, 64, 99, 31, 81,
                86, 43, 58, 9, 77, 61, 92, 31, 12, 75, 45, 87, 31, 78, 28, 62,
                6, 40, 63, 67, 57, 68, 68, 56, 82, 81, 18, 55, 49, 11, 58, 57,
                12, 80, 14, 99, 63, 48, 46, 10, 17, 32, 99, 64, 47, 63, 24, 13,
                91, 92, 15, 80, 14, 45, 50, 91, 74, 57, 69, 19, 9, 12, 22, 51,
                84, 76, 58, 77, 32, 18, 90, 5, 32, 92, 35, 77, 11, 67, 75, 54,
                70, 44, 51, 60, 26, 73, 71, 41, 77, 1, 73, 67, 54, 47, 83, 14,
                65, 73, 67, 56, 48, 17, 1, 8, 2, 22, 36, 85, 91, 60, 48, 13,
                37, 90, 49, 36, 23, 10, 95, 51, 82, 12, 34, 95, 16, 82, 71, 28,
                35, 74, 28, 28, 51, 65, 44, 54, 54, 87, 20, 32, 62, 19, 84, 22,
                1, 77, 63, 71, 68, 29, 99, 47, 62, 27, 32, 35, 29, 5, 93, 54,
                4, 81, 84, 52, 84, 46, 72, 69, 40, 19, 26, 17, 41, 70, 61, 70,
                92, 97, 56, 53, 90, 66, 2, 20, 59, 62, 82, 86, 19, 28, 10, 99,
                18, 87, 42, 3, 2, 25, 31, 27, 66, 99, 1, 88, 34, 24, 89, 41,
                90, 30, 37, 77, 28, 63, 80, 16, 91, 42, 75, 47, 96, 89, 28, 41,
                93, 78, 14, 57, 100, 97, 5, 19, 13, 84, 29, 17, 5, 63, 40, 79,
                57, 94, 98, 65, 51, 57, 19, 7, 95, 50, 32, 84, 53, 75, 71, 95,
                13, 57, 19, 83, 45, 7, 6, 65, 90, 90, 19, 17, 100, 40, 54, 80,
                26, 98, 72, 26, 58, 38, 23, 23, 69, 83, 51, 57, 60, 100, 73,
                20, 73, 22, 79, 83, 51, 21, 38, 100, 4, 76, 63, 71, 72, 91, 38,
                47, 29, 18, 59, 89, 67, 88, 97, 97, 59, 81, 53, 87, 82, 68, 4,
                12, 61, 68, 77, 70, 85, 61, 99, 64, 28, 35, 3, 12, 45, 53, 43,
                30, 28, 93, 34, 47, 39, 37, 63, 1, 42, 37, 17, 62, 91, 56, 47,
                90, 21, 45, 22, 85
            ]], 26056],
        ],
    )
