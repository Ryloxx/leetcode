#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#
# https://leetcode.com/problems/unique-morse-code-words/description/
#
# algorithms
# Easy (80.04%)
# Likes:    1991
# Dislikes: 1348
# Total Accepted:    284.1K
# Total Submissions: 344.5K
# Testcase Example:  '["gin","zen","gig","msg"]'
#
# International Morse Code defines a standard encoding where each letter is
# mapped to a series of dots and dashes, as follows:
#
#
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
#
#
# For convenience, the full table for the 26 letters of the English alphabet is
# given below:
#
#
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#
# Given an array of strings words where each word can be written as a
# concatenation of the Morse code of each letter.
#
#
# For example, "cab" can be written as "-.-..--...", which is the concatenation
# of "-.-.", ".-", and "-...". We will call such a concatenation the
# transformation of a word.
#
#
# Return the number of different transformations among all words we have.
#
#
# Example 1:
#
#
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".
#
#
# Example 2:
#
#
# Input: words = ["a"]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 12
# words[i] consists of lowercase English letters.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lookup = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        return len(
            set("".join(map(lambda c: lookup[ord(c) - ord('a')], w))
                for w in words))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.uniqueMorseRepresentations, Solution()),
        [
            [[["gin", "zen", "gig", "msg"]], 2],
            [[["a"]], 1],
        ],
    )
