#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#
# https://leetcode.com/problems/removing-stars-from-a-string/description/
#
# algorithms
# Medium (64.23%)
# Likes:    1777
# Dislikes: 125
# Total Accepted:    101.6K
# Total Submissions: 140.9K
# Testcase Example:  '"leet**cod*e"'
#
# You are given a string s, which contains stars *.
#
# In one operation, you can:
#
#
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star
# itself.
#
#
# Return the string after all stars have been removed.
#
# Note:
#
#
# The input will be generated such that the operation is always possible.
# It can be shown that the resulting string will always be unique.
#
#
#
# Example 1:
#
#
# Input: s = "leet**cod*e"
# Output: "lecoe"
# Explanation: Performing the removals from left to right:
# - The closest character to the 1^st star is 't' in "leet**cod*e". s becomes
# "lee*cod*e".
# - The closest character to the 2^nd star is 'e' in "lee*cod*e". s becomes
# "lecod*e".
# - The closest character to the 3^rd star is 'd' in "lecod*e". s becomes
# "lecoe".
# There are no more stars, so we return "lecoe".
#
# Example 2:
#
#
# Input: s = "erase*****"
# Output: ""
# Explanation: The entire string is removed, so we return an empty string.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters and stars *.
# The operation above can be performed on s.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def removeStars(self, s: str) -> str:
        res = []
        for c in s:
            if c == "*":
                res and res.pop()
            else:
                res.append(c)
        return "".join(res)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.removeStars, Solution()),
        [
            (["leet**cod*e"], "lecoe"),
            (["erase*****"], ""),
        ],
    )
