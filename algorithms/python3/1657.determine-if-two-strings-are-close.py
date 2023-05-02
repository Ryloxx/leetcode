#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#
# https://leetcode.com/problems/determine-if-two-strings-are-close/description/
#
# algorithms
# Medium (54.49%)
# Likes:    1595
# Dislikes: 75
# Total Accepted:    77.2K
# Total Submissions: 138.8K
# Testcase Example:  '"abc"\n"bca"'
#
# Two strings are considered close if you can attain one from the other using
# the following operations:
#
#
# Operation 1: Swap any two existing characters.
#
#
# For example, abcde -> aecdb
#
#
# Operation 2: Transform every occurrence of one existing character into
# another existing character, and do the same with the other
# character.
#
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into
# a's)
#
#
#
#
# You can use the operations on either string as many times as necessary.
#
# Given two strings, word1 and word2, return true if word1 and word2 are close,
# and false otherwise.
#
#
# Example 1:
#
#
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
#
#
# Example 2:
#
#
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in
# any number of operations.
#
#
# Example 3:
#
#
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
#
#
#
# Constraints:
#
#
# 1 <= word1.length, word2.length <= 10^5
# word1 and word2 contain only lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType
from collections import Counter


# @lc code=start
class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        return len(word1) == len(word2) and set(word1) == set(
            word2) and Counter(Counter(word1).values()) == Counter(
                Counter(word2).values())


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.closeStrings, Solution()),
        [
            (["abc", "bca"], True),
            (["a", "aa"], False),
            (["cabbba", "abbccc"], True),
            (["a" * 10**5, "b" * 10**5], False),
            (["a" * 3**5 + "b" * 3**5, "b" * 3**5 + "a" * 3**5], True),
        ],
    )
