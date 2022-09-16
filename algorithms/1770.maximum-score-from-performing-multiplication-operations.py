#
# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/description/
#
# algorithms
# Medium (35.64%)
# Likes:    1971
# Dislikes: 461
# Total Accepted:    74.6K
# Total Submissions: 209.3K
# Testcase Example:  '[1,2,3]\n[3,2,1]'
#
# You are given two integer arrays nums and multipliers of size n and m
# respectively, where n >= m. The arrays are 1-indexed.
#
# You begin with a score of 0. You want to perform exactly m operations. On the
# i^th operation (1-indexed), you will:
#
#
# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Remove x from the array nums.
#
#
# Return the maximum score after performing m operations.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14.
#
# Example 2:
#
#
# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the
# score.
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score.
# The total score is 50 + 15 - 9 + 4 + 42 = 102.
#
#
#
# Constraints:
#
#
# n == nums.length
# m == multipliers.length
# 1 <= m <= 10^3
# m <= n <= 10^5
# -1000 <= nums[i], multipliers[i] <= 1000
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(multipliers)
        dp = [0] * (n + 1)
        current = [0] * (n + 1)
        for k in range(n - 1, -1, -1):
            for i in range(k, -1, -1):
                j = len(nums) + i - 1 - k
                current[i] = max(multipliers[k] * nums[i] + dp[i + 1],
                                 multipliers[k] * nums[j] + dp[i])
            dp, current = current, dp
        return dp[0]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maximumScore, Solution()),
        [
            [[[-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]], 102],
            [[[1, 2, 3], [3, 2, 1]], 14],
        ],
    )
