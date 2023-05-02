#
# @lc app=leetcode id=1680 lang=python3
#
# [1680] Concatenation of Consecutive Binary Numbers
#
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/
#
# algorithms
# Medium (52.61%)
# Likes:    433
# Dislikes: 247
# Total Accepted:    39.4K
# Total Submissions: 73.7K
# Testcase Example:  '1'
#
# Given an integer n, return the decimal value of the binary string formed by
# concatenating the binary representations of 1 to n in order, modulo 10^9 +
# 7.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: 1
# Explanation: "1" in binary corresponds to the decimal value 1.
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 27
# Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
# After concatenating them, we have "11011", which corresponds to the decimal
# value 27.
#
#
# Example 3:
#
#
# Input: n = 12
# Output: 505379714
# Explanation: The concatenation results in
# "1101110010111011110001001101010111100".
# The decimal value of that is 118505380540.
# After modulo 10^9 + 7, the result is 505379714.
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def concatenatedBinary(self, n: int) -> int:
        MOD = 7 + 10**9
        res = 0
        for i in range(1, n + 1):
            res <<= i.bit_length()
            res += i
            res %= MOD
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.concatenatedBinary, Solution()),
        [
            [[0], 0],
            [[3], 27],
            [[1], 1],
            [[12], 505379714],
            [[10**5], 757631812],
        ],
    )
