#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/
#
# algorithms
# Medium (38.60%)
# Likes:    1514
# Dislikes: 30
# Total Accepted:    64.2K
# Total Submissions: 135.4K
# Testcase Example:  '["lc","cl","gg"]'
#
# You are given an array of strings words. Each element of words consists of
# two lowercase English letters.
#
# Create the longest possible palindrome by selecting some elements from words
# and concatenating them in any order. Each element can be selected at most
# once.
#
# Return the length of the longest palindrome that you can create. If it is
# impossible to create any palindrome, return 0.
#
# A palindrome is a string that reads the same forward and backward.
#
#
# Example 1:
#
#
# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of
# length 6.
# Note that "clgglc" is another longest palindrome that can be created.
#
#
# Example 2:
#
#
# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" =
# "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.
#
#
# Example 3:
#
#
# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is
# "xx".
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 10^5
# words[i].length == 2
# words[i] consists of lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType
from typing import List
from collections import defaultdict


# @lc code=start
class Solution:

    def longestPalindrome(self, words: List[str]) -> int:
        count, res = defaultdict(int), 0
        for w in words:
            if (c := count[(r_w := w[::-1])]) > 0:
                count[r_w] = c = c - 1
                if not c:
                    del count[r_w]
                res += 4
                continue
            count[w] += 1
        return (res + any(count[x] > 0
                          for x in filter(lambda x: x[0] == x[1], count)) * 2)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestPalindrome, Solution()),
        [([["nn", "nn", "hg", "gn", "nn", "hh", "gh", "nn", "nh", "nh"]], 14),
         ([["lc", "cl", "gg"]], 6),
         ([["ab", "ty", "yt", "lc", "cl", "ab"]], 8),
         ([["cc", "ll", "xx"]], 2), ([["ll"]], 2), ([["ll", "ll", "ll"]], 6),
         ([["ll", "ll", "aa", "aa", "aa", "aa", "ll"]], 14),
         ([["ll", "ll", "ab", "ba", "aa", "aa", "aa", "aa", "ab", "ba", "ll"]
           ], 22)],
    )
