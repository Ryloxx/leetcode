#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
#
# algorithms
# Medium (50.52%)
# Likes:    2086
# Dislikes: 164
# Total Accepted:    118.2K
# Total Submissions: 233.6K
# Testcase Example:  '["un","iq","ue"]'
#
# You are given an array of strings arr. A string s is formed by the
# concatenation of a subsequence of arr that has unique characters.
#
# Return the maximum possible length of s.
#
# A subsequence is an array that can be derived from another array by deleting
# some or no elements without changing the order of the remaining elements.
#
#
# Example 1:
#
#
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.
#
#
# Example 2:
#
#
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" +
# "ers") and "acters" ("act" + "ers").
#
#
# Example 3:
#
#
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lowercase English letters.
#
#
#
# from functools import cache
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # Iterative
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for i in arr:
            s = set(i)
            if len(s) != len(i):
                continue
            for n in range(len(dp)):
                if dp[n] & s:
                    continue
                dp.append(s | dp[n])
        return max(map(len, dp))

    # Recursive
    # def maxLength(self, arr: List[str]) -> int:
    # c_arr = list([ord(i) - ord('a') for i in x]
    #              for x in filter(lambda x: not len(set(x)) - len(x), arr))

    # @cache
    # def dp(mask: int, i: int):
    #     if i >= len(c_arr):
    #         return 0
    #     res = dfs(mask, i + 1)
    #     for c in c_arr[i]:
    #         if mask & (t := 1 << c):
    #             return res
    #         mask |= t
    #     return max(res, dfs(mask, i + 1) + len(c_arr[i]))

    # return dp(0, 0)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxLength, Solution()),
        [
            ([["un", "iq", "ue"]], 4),
            ([["cha", "r", "act", "ers"]], 6),
            ([["aa", "bb"]], 0),
            ([["abcdefghijklmnopqrstuvwxyz"]], 26),
            ([["abcdefghijklmnopqrstuvwxyz" for _ in range(16)]], 26),
            ([list("abcdefghijklmnopqrstuvwxyz"[:16])], 16),
        ],
    )
