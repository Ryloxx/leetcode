#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (55.88%)
# Likes:    2929
# Dislikes: 358
# Total Accepted:    548.5K
# Total Submissions: 950.8K
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#
# Constraints:
#
#
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def canConstruct(self, ransomNote, magazine):
        return not any(
            magazine.count(i) < ransomNote.count(i) for i in set(ransomNote))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.canConstruct, Solution()),
        [
            [["a", "b"], False],
            [["aa", "ab"], False],
            [["aa", "aab"], True],
            [["aa", "aa"], True],
            [["aa", "aaaaaaa"], True],
            [["aab", "aaaaaaa"], False],
            [["", ""], True],
            [["", "a"], True],
            [["a", ""], False],
        ],
    )
