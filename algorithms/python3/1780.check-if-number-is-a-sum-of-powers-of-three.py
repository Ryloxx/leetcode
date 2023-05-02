#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description/
#
# algorithms
# Medium (64.87%)
# Likes:    548
# Dislikes: 20
# Total Accepted:    22.9K
# Total Submissions: 35.2K
# Testcase Example:  '12'
#
# Given an integer n, return true if it is possible to represent n as the sum
# of distinct powers of three. Otherwise, return false.
#
# An integer y is a power of three if there exists an integer x such that y ==
# 3^x.
#
#
# Example 1:
#
#
# Input: n = 12
# Output: true
# Explanation: 12 = 3^1 + 3^2
#
#
# Example 2:
#
#
# Input: n = 91
# Output: true
# Explanation: 91 = 3^0 + 3^2 + 3^4
#
#
# Example 3:
#
#
# Input: n = 21
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^7
#
#
#
from operator import itemgetter
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    POWER_OF_THREE_LOOKUP = [3**x for x in range(15)]

    def checkPowersOfThree(self, n: int) -> bool:
        if not n:
            return False
        i = 0
        while i < len(Solution.POWER_OF_THREE_LOOKUP) and (
                p := Solution.POWER_OF_THREE_LOOKUP[i]) <= n:
            i += 1
            if not n % p:
                temp = (n // p) - 1
                if not temp % 3:
                    n = temp
                    i = 0
        return n == 0


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.checkPowersOfThree, Solution()),
        [
            [[1], True],
            [[33], False],
            [[5], False],
            [[0], False],
            [[12], True],
            [[91], True],
            [[4], True],
            [[6], False],
            [[7], False],
            [[8], False],
            [[9], True],
            [[21], False],
            [[sum(itemgetter(4, 5, 6)(Solution.POWER_OF_THREE_LOOKUP))], True],
            [[sum(itemgetter(4, 5, 5)(Solution.POWER_OF_THREE_LOOKUP))], False
             ],
            [[sum(Solution.POWER_OF_THREE_LOOKUP)], True],
        ],
    )
