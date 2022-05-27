#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
#
# algorithms
# Easy (85.53%)
# Likes:    1976
# Dislikes: 117
# Total Accepted:    290.4K
# Total Submissions: 338.3K
# Testcase Example:  '14'
#
# Given an integer num, return the number of steps to reduce it to zero.
#
# In one step, if the current number is even, you have to divide it by 2,
# otherwise, you have to subtract 1 from it.
#
#
# Example 1:
#
#
# Input: num = 14
# Output: 6
# Explanation:
# Step 1) 14 is even; divide by 2 and obtain 7.
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3.
# Step 4) 3 is odd; subtract 1 and obtain 2.
# Step 5) 2 is even; divide by 2 and obtain 1.
# Step 6) 1 is odd; subtract 1 and obtain 0.
#
#
# Example 2:
#
#
# Input: num = 8
# Output: 4
# Explanation:
# Step 1) 8 is even; divide by 2 and obtain 4.
# Step 2) 4 is even; divide by 2 and obtain 2.
# Step 3) 2 is even; divide by 2 and obtain 1.
# Step 4) 1 is odd; subtract 1 and obtain 0.
#
#
# Example 3:
#
#
# Input: num = 123
# Output: 12
#
#
#
# Constraints:
#
#
# 0 <= num <= 10^6
#
#
#

from types import MethodType
from algo_input import run


# @lc code=start
class Solution:

    def numberOfSteps(self, num: int) -> int:
        t = bin(num)
        return len(t) + t.count("1") - 3


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numberOfSteps, Solution()),
        [
            [[14], 6],
            [[8], 4],
            [[123], 12],
            [[0], 0],
            [[1], 1],
            [[2], 2],
            [[3], 3],
        ],
    )
