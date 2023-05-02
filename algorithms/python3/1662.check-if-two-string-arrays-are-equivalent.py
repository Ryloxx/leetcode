#
# @lc app=leetcode id=1662 lang=python3
#
# [1662] Check If Two String Arrays are Equivalent
#
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
#
# algorithms
# Easy (81.95%)
# Likes:    1685
# Dislikes: 160
# Total Accepted:    223.2K
# Total Submissions: 268.4K
# Testcase Example:  '["ab", "c"]\n["a", "bc"]'
#
# Given two string arrays word1 and word2, return true if the two arrays
# represent the same string, and false otherwise.
#
# A string is represented by an array if the array elements concatenated in
# order forms the string.
#
#
# Example 1:
#
#
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.
#
# Example 2:
#
#
# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false
#
#
# Example 3:
#
#
# Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= word1.length, word2.length <= 10^3
# 1 <= word1[i].length, word2[i].length <= 10^3
# 1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3
# word1[i] and word2[i] consist of lowercase letters.
#
#
#
from itertools import chain, zip_longest
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # O(min(N, K)) time complexity
    # O(1) space complexity
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return all(x == y for x, y in zip_longest(chain.from_iterable(word1),
                                                  chain.from_iterable(word2)))

    # O(N + K) time complexity
    # O(N + K) space complexity
    # def arrayStringsAreEqual(self, word1: List[str], word2: List[str])->bool:
    #     return "".join(word1) == "".join(word2)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.arrayStringsAreEqual, Solution()),
        [
            ([["ab", "c"], ["a", "bc"]], True),
            ([["a", "cb"], ["ab", "c"]], False),
            ([["abc", "d", "defg"], ["abcddefg"]], True),
        ],
    )
