#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#
# https://leetcode.com/problems/utf-8-validation/description/
#
# algorithms
# Medium (39.21%)
# Likes:    796
# Dislikes: 2642
# Total Accepted:    108.1K
# Total Submissions: 241.2K
# Testcase Example:  '[197,130,1]'
#
# Given an integer array data representing the data, return whether it is a
# valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded
# characters).
#
# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following
# rules:
#
#
# For a 1-byte character, the first bit is a 0, followed by its Unicode
# code.
# For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0,
# followed by n - 1 bytes with the most significant 2 bits being 10.
#
#
# This is how the UTF-8 encoding would work:
#
#
# ⁠    Number of Bytes   |        UTF-8 Octet Sequence
# ⁠                      |              (binary)
# ⁠  --------------------+-----------------------------------------
# ⁠           1          |   0xxxxxxx
# ⁠           2          |   110xxxxx 10xxxxxx
# ⁠           3          |   1110xxxx 10xxxxxx 10xxxxxx
# ⁠           4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#
#
# x denotes a bit in the binary form of a byte that may be either 0 or 1.
#
# Note: The input is an array of integers. Only the least significant 8 bits of
# each integer is used to store the data. This means each integer represents
# only 1 byte of data.
#
#
# Example 1:
#
#
# Input: data = [197,130,1]
# Output: true
# Explanation: data represents the octet sequence: 11000101 10000010 00000001.
# It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte
# character.
#
#
# Example 2:
#
#
# Input: data = [235,140,4]
# Output: false
# Explanation: data represented the octet sequence: 11101011 10001100 00000100.
# The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes
# character.
# The next byte is a continuation byte which starts with 10 and that's correct.
# But the second continuation byte does not start with 10, so it is
# invalid.
#
#
#
# Constraints:
#
#
# 1 <= data.length <= 2 * 10^4
# 0 <= data[i] <= 255
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def validUtf8(self, data: List[int]) -> bool:
        left = 0
        while left < len(data):
            code_length = -1
            if (data[left] >> 7) ^ 1 == 1:
                code_length = 0
            if (data[left] >> 5) ^ ((1 << 3) - 1) == 1:
                code_length = 1
            if (data[left] >> 4) ^ ((1 << 4) - 1) == 1:
                code_length = 2
            if (data[left] >> 3) ^ ((1 << 5) - 1) == 1:
                code_length = 3
            if code_length < 0:
                return False
            left += 1
            for _ in range(code_length):
                if (left >= len(data)
                        or (data[left] >> 6) ^ ((1 << 2) - 1) != 1):
                    return False
                left += 1

        return True


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.validUtf8, Solution()),
        [
            [[[
                194, 155, 231, 184, 185, 246, 176, 131, 161, 222, 174, 227,
                162, 134, 241, 154, 168, 185, 218, 178, 229, 187, 139, 246,
                178, 187, 139, 204, 146, 225, 148, 179, 245, 139, 172, 134,
                193, 156, 233, 131, 154, 240, 166, 188, 190, 216, 150, 230,
                145, 144, 240, 167, 140, 163, 221, 190, 238, 168, 139, 241,
                154, 159, 164, 199, 170, 224, 173, 140, 244, 182, 143, 134,
                206, 181, 227, 172, 141, 241, 146, 159, 170, 202, 134, 230,
                142, 163, 244, 172, 140, 191
            ]], True],
            [[[197, 130, 1]], True],
            [[[248, 130, 130, 130]], False],
            [[[235, 140, 4]], False],
        ],
    )
