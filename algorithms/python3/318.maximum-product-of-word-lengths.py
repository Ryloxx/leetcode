#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (56.69%)
# Likes:    2051
# Dislikes: 99
# Total Accepted:    154.4K
# Total Submissions: 267.4K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, return the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. If no such
# two words exist, return 0.
#
#
# Example 1:
#
#
# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".
#
#
# Example 2:
#
#
# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".
#
#
# Example 3:
#
#
# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.
#
#
#
# Constraints:
#
#
# 2 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# words[i] consists only of lowercase English letters.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution():

    def maxProduct(self, words: List[str]):
        sw = list(map(set, words))  # O(M * N)
        return max((len(words[i]) * len(words[j]) for i in range(len(words))
                    for j in range(i + 1, len(words)) if not (sw[i] & sw[j])),
                   default=0)  # O(M^2) because set comparison is O(26)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxProduct, Solution()),
        [
            [[["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]], 16],
            [[["a", "ab", "abc", "d", "cd", "bcd", "abcd"]], 4],
            [[["a", "aa", "aaa", "aaaa"]], 0],
        ],
    )
