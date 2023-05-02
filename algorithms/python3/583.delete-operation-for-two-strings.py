#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (55.96%)
# Likes:    3677
# Dislikes: 58
# Total Accepted:    147K
# Total Submissions: 255K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings word1 and word2, return the minimum number of steps
# required to make word1 and word2 the same.
#
# In one step, you can delete exactly one character in either string.
#
#
# Example 1:
#
#
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".
#
#
# Example 2:
#
#
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # O(n * m) time complextity
    # O(minlen(n, m)) space complexity
    def minDistance(self, word1: str, word2: str) -> int:
        word2, word1 = sorted([word1, word2], key=len)
        lw1, lw2 = len(word1) + 1, len(word2) + 1
        dp = [0] * lw2
        for i in range(1, lw1):
            left = temp = top_left = 0
            for j in range(1, lw2):
                if word1[i - 1] == word2[j - 1]:
                    temp = 1 + top_left
                else:
                    temp = max(dp[j], left)
                top_left = dp[j]
                dp[j] = temp
                left = temp
        return lw1 + lw2 - 2 * dp[-1] - 2


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minDistance, Solution()),
        [[["sea", "eat"], 2], [["etco", "leetcode"], 4], [["a", "ab"], 1],
         [["benzalphenylhydrazone", "dinitrophenylhydrazine"], 13]],
    )
