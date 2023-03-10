#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (66.44%)
# Likes:    9772
# Dislikes: 224
# Total Accepted:    552.4K
# Total Submissions: 831.4K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
#
#
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
#
# Constraints:
#
#
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = [(T[-1], len(T) - 1)]
        for i in range(len(T) - 2, -1, -1):
            if stack[-1][0] > T[i]:
                stack.append((T[i], i))
                ans[i] = 1
            else:
                while stack and stack[-1][0] <= T[i]:
                    stack.pop()
                if stack:
                    ans[i] = stack[-1][1] - i
                stack.append((T[i], i))
        return ans


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.dailyTemperatures, Solution()),
        [
            ([[73, 74, 75, 71, 69, 72, 76, 73]], [1, 1, 4, 2, 1, 1, 0, 0]),
            ([[30, 40, 50, 60]], [1, 1, 1, 0]),
            ([[30, 60, 90]], [1, 1, 0]),
        ],
    )
