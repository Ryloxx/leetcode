#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
#
# algorithms
# Easy (81.39%)
# Likes:    1361
# Dislikes: 35
# Total Accepted:    135.5K
# Total Submissions: 163.9K
# Testcase Example:  '"thequickbrownfoxjumpsoverthelazydog"'
#
# A pangram is a sentence where every letter of the English alphabet appears at
# least once.
#
# Given a string sentence containing only lowercase English letters, return
# true if sentence is a pangram, or false otherwise.
#
#
# Example 1:
#
#
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English
# alphabet.
#
#
# Example 2:
#
#
# Input: sentence = "leetcode"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def checkIfPangram(self, sentence: str) -> bool:
        res = set()
        for i in sentence:
            res.add(i)
            if len(res) == 26:
                return True
        return False


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.checkIfPangram, Solution()),
        [
            (["thequickbrownfoxjumpsoverthelazydog"], True),
            (["leetcode"], False),
        ],
    )
