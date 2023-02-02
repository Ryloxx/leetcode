#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#
# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
#
# algorithms
# Easy (52.74%)
# Likes:    3311
# Dislikes: 1077
# Total Accepted:    384.2K
# Total Submissions: 727.3K
# Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'
#
# In an alien language, surprisingly, they also use English lowercase letters,
# but possibly in a different order. The order of the alphabet is some
# permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the
# alphabet, return true if and only if the given words are sorted
# lexicographically in this alien language.
#
#
# Example 1:
#
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is
# sorted.
#
#
# Example 2:
#
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] >
# words[1], hence the sequence is unsorted.
#
#
# Example 3:
#
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is
# shorter (in size.) According to lexicographical rules "apple" > "app",
# because 'l' > '∅', where '∅' is defined as the blank character which is less
# than any other character (More info).
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup = {k: v for v, k in enumerate(order)}
        for i in range(1, len(words)):
            for j in range(len(words[i - 1])):
                if j >= len(words[i]):
                    return False
                if words[i - 1][j] != words[i][j]:
                    if lookup[words[i - 1][j]] > lookup[words[i][j]]:
                        return False
                    break
        return True


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isAlienSorted, Solution()),
        [
            ([["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"], True),
            ([["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"], False),
            ([["apple", "app"], "abcdefghijklmnopqrstuvwxyz"], False),
            ([["aaaaaaaa", "apple", "app"], "abcdefghijklmnopqrstuvwxyz"
              ], False),
            ([["a" * 20, "a" * 19], "abcdefghijklmnopqrstuvwxyz"], False),
            ([["a" * 19, "a" * 20], "abcdefghijklmnopqrstuvwxyz"], True),
        ],
    )
