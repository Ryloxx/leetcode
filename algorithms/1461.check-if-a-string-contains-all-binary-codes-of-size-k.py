#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/
#
# algorithms
# Medium (54.44%)
# Likes:    1412
# Dislikes: 76
# Total Accepted:    75.8K
# Total Submissions: 134.1K
# Testcase Example:  '"00110110"\n2'
#
# Given a binary string s and an integer k, return true if every binary code of
# length k is a substring of s. Otherwise, return false.
#
#
# Example 1:
#
#
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They
# can be all found as substrings at indices 0, 1, 3 and 2 respectively.
#
#
# Example 2:
#
#
# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that
# both exist as a substring.
#
#
# Example 3:
#
#
# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the
# array.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^5
# s[i] is either '0' or '1'.
# 1 <= k <= 20
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        if k <= 0:
            return 0
        hash, limit = 0, 1 << k
        t = [False] * limit
        ones = limit - 1
        for i in range(len(s)):
            hash = ((hash << 1) & ones) | int(s[i])
            if i >= k - 1 and not t[hash]:
                t[hash] = True
                limit -= 1
                if not limit:
                    return True
        return False


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.hasAllCodes, Solution()),
        [
            [["0110", 1], True],
            [["0110", 2], False],
            [["00110110", 2], True],
            [["00110", 2], True],
            [["01100", 2], True],
            [[('1000000100011111100110110001110011011100010001101001'
               '10000000001111000000111011111011110001000110001110111'
               '00110111110101010110000111111100100010110100011010011'
               '00110001100001000111110100110101001110111010110111110'
               '10111001101001001001111111000110100000110001111001101'
               '10010101010100101011000001110000010011011100000010001'
               '11110101011010011100011000010110101110100011010101110'
               '01111111010011101001010010010100011001110111000110101'
               '10111111101101101110110111001001111010000000111100111'
               '11111001101100000010111001101101011011000111111001011'
               '1111010011011011'), 4], True],
        ],
    )
