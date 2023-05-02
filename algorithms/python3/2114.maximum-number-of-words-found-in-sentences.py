#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/
#
# algorithms
# Easy (88.73%)
# Likes:    541
# Dislikes: 21
# Total Accepted:    70.5K
# Total Submissions: 79.5K
# Testcase Example:  '[
#   "alice and bob love leetcode",
#   "i think so too",
#   "this is great thanks very much"
# ]'
#
# A sentence is a list of words that are separated by a single space with no
# leading or trailing spaces.
#
# You are given an array of strings sentences, where each sentences[i]
# represents a single sentence.
#
# Return the maximum number of words that appear in a single sentence.
#
#
# Example 1:
#
#
# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is
# great thanks very much"]
# Output: 6
# Explanation:
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.
# Thus, the maximum number of words in a single sentence comes from the third
# sentence, which has 6 words.
#
#
# Example 2:
#
#
# Input: sentences = ["please wait", "continue to fight", "continue to win"]
# Output: 3
# Explanation: It is possible that multiple sentences contain the same number
# of words.
# In this example, the second and third sentences (underlined) have the same
# number of words.
#
#
#
# Constraints:
#
#
# 1 <= sentences.length <= 100
# 1 <= sentences[i].length <= 100
# sentences[i] consists only of lowercase English letters and ' ' only.
# sentences[i] does not have leading or trailing spaces.
# All the words in sentences[i] are separated by a single space.
#
#
#

# @lc code=start
from types import MethodType
from typing import List

from algo_input import run


class Solution:

    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(map(len, map(str.split, sentences)))


# @lc code=end

if __name__ == "__main__":
    run(
        MethodType(Solution.mostWordsFound, Solution()),
        [
            [[["please wait", "continue to fight", "continue to win"]], 3],
            [
                [[
                    "alice and bob love leetcode",
                    "i think so too",
                    "this is great thanks very much",
                ]],
                6,
            ],
        ],
    )
