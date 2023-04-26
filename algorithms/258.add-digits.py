#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (63.60%)
# Likes:    3525
# Dislikes: 1801
# Total Accepted:    582.2K
# Total Submissions: 902.1K
# Testcase Example:  '38'
#
# Given an integer num, repeatedly add all its digits until the result has only
# one digit, and return it.
#
#
# Example 1:
#
#
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
#
#
# Example 2:
#
#
# Input: num = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= num <= 2^31 - 1
#
#
#
# Follow up: Could you do it without any loop/recursion in O(1) runtime?
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def addDigits(self, num: int) -> int:
        return 0 if not num else 1 + (num - 1) % 9


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.addDigits, Solution()),
        [
            ([38], 2),
            ([0], 0),
        ],
    )
