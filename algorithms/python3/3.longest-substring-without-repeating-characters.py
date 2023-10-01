#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.10%)
# Likes:    24471
# Dislikes: 1079
# Total Accepted:    3.4M
# Total Submissions: 10.2M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#
from collections import defaultdict
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        memo, left, res = defaultdict(lambda: -1), -1, 0
        for right, c in enumerate(s):
            left = max(left, memo[c])
            memo[c] = right
            res = max(res, right - left)
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.lengthOfLongestSubstring, Solution()),
        [
            [["abcabcbb"], 3],
            [["abc"], 3],
            [["abca"], 3],
            [["bbbbb"], 1],
            [["pwwkew"], 3],
            [[" "], 1],
            [["anviaj"], 5],
            [["abba"], 2],
            [["vqblqcb"], 4],
            [["tmmzuxt"], 5],
            [["dvdf"], 3],
            [[
                "ysbghjjrfumqjpyktddsnxftvdqgxzlvrneaynufhgy"
                "qxwaqzelmbsiyxaeubrqvguvehpmrykhvikokqzwttg"
            ], 12],
        ],
    )
