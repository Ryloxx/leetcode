#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#
# https://leetcode.com/problems/maximum-69-number/description/
#
# algorithms
# Easy (78.88%)
# Likes:    2156
# Dislikes: 185
# Total Accepted:    189.3K
# Total Submissions: 230.8K
# Testcase Example:  '9669'
#
# You are given a positive integer num consisting only of digits 6 and 9.
#
# Return the maximum number you can get by changing at most one digit (6
# becomes 9, and 9 becomes 6).
#
#
# Example 1:
#
#
# Input: num = 9669
# Output: 9969
# Explanation:
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
#
#
# Example 2:
#
#
# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
#
#
# Example 3:
#
#
# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
#
#
#
# Constraints:
#
#
# 1 <= num <= 10^4
# num consists of only 6 and 9 digits.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def maximum69Number(self, num: int) -> int:
        a, b, c = num, 0, -1
        while a > 0:
            if (a % 10 == 6):
                c = b
            b += 1
            a //= 10
        return num if c < 0 else num + 3 * 10**(c)

    # Using string
    # def maximum69Number(self, num: int) -> int:
    #     return int(str(num).replace('6', '9', 1))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maximum69Number, Solution()),
        [
            ([9669], 9969),
            ([9996], 9999),
            ([9999], 9999),
        ],
    )
