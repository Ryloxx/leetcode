#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (51.42%)
# Likes:    7512
# Dislikes: 740
# Total Accepted:    1.1M
# Total Submissions: 2.1M
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
#
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
#
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    # def addBinary(self, a: str, b: str) -> str:

    #     def tobin(s):
    #         c = 0
    #         for i in s:
    #             c <<= 1
    #             if i == "1":
    #                 c += 1

    #         return c

    #     def tos(b):
    #         s = []
    #         while b:
    #             if b & 1:
    #                 s.append("1")
    #             else:
    #                 s.append("0")
    #             b >>= 1
    #         return "".join(reversed(s)) or "0"

    #     return tos(tobin(a) + tobin(b))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.addBinary, Solution()),
        [
            (["11", "1"], "100"),
            (["1010", "1011"], "10101"),
        ],
    )
