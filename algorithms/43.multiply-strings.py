#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (37.81%)
# Likes:    4491
# Dislikes: 1806
# Total Accepted:    523.6K
# Total Submissions: 1.4M
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
#
# Note: You must not use any built-in BigInteger library or convert the inputs
# to integer directly.
#
#
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Constraints:
#
#
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
#
#
#
from itertools import chain, repeat, zip_longest
from typing import Iterable
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def add(self, numa: Iterable[int], numb: Iterable[int]):
        res = []
        carry = 0
        for a, b in zip_longest(numa, numb, fillvalue=0):
            n = a + b + carry
            res.append(n % 10)
            carry = n // 10
        res.append(carry)
        while len(res) > 1 and not res[-1]:
            res.pop()
        return res

    def multiply(self, num1: str, num2: str) -> str:
        lookup = {0: [0]}
        for i in range(1, 10):
            lookup[i] = self.add(lookup[i - 1], map(int, reversed(num1)))
        res = [0]
        for exp, x in enumerate(reversed(num2)):
            res = self.add(res, chain(repeat(0, exp), lookup[int(x)]))
        return "".join(map(str, reversed(res)))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.multiply, Solution()),
        [[["123", "456"], "56088"], [["2", "3"], "6"], [["50", "50"], "2500"],
         [["0", "52"], "0"],
         [[
             "736235884905755550581892956148765407"
             "784815709486433284072503587141716591"
             "181175114605415568267938975098364821"
             "846829468304249417020283003891443936"
             "589153244853037011765175448815262096",
             "893612294838593011685462651041010201"
             "750234231759027442647317537612971699"
         ], "657909438653154459392747599257995344"
          "530494974780206502515722324451598536716"
          "171190590610462168637026814948272534"
          "392739763368391730453087446820494802663"
          "124896253303098162424609627928875328"
          "635438566049225777171566211716146060991"
          "597986043885556296115421104"]],
    )
