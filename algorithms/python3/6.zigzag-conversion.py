#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (43.32%)
# Likes:    5024
# Dislikes: 10688
# Total Accepted:    921.2K
# Total Submissions: 2.1M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
#
# string convert(string s, int numRows);
#
#
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
# Example 3:
#
#
# Input: s = "A", numRows = 1
# Output: "A"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def convert(self, s: str, numRows: int) -> str:
        x = [2 * x * (numRows - 1) for x in range(1 + len(s) // numRows)]
        res = []
        seen = set()
        for i in x:
            if i in seen:
                continue
            if 0 <= i < len(s):
                res.append(s[i])
            seen.add(i)
            if i > 0:
                x.append(i - 1)
            if i < len(s) + numRows:
                x.append(i + 1)
        return "".join(res)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.convert, Solution()),
        [
            (["PAYPALISHIRING", 3], "PAHNAPLSIIGYIR"),
            (["PAYPALISHIRING", 4], "PINALSIGYAHRPI"),
            (["A", 1], "A"),
        ],
    )
