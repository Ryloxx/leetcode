#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#
# https://leetcode.com/problems/concatenated-words/description/
#
# algorithms
# Hard (45.87%)
# Likes:    3261
# Dislikes: 257
# Total Accepted:    191.3K
# Total Submissions: 387.5K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog",
# "hippopotamuses","rat","ratcatdogcat"]'
#
# Given an array of strings words (without duplicates), return all the
# concatenated words in the given list of words.
#
# A concatenated word is defined as a string that is comprised entirely of at
# least two shorter words in the given array.
#
#
# Example 1:
#
#
# Input: words =
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
#
# Example 2:
#
#
# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 10^4
# 1 <= words[i].length <= 30
# words[i] consists of only lowercase English letters.
# All the strings of words are unique.
# 1 <= sum(words[i].length) <= 10^5
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)

        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True

            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findAllConcatenatedWordsInADict, Solution()),
        [
            ([[
                "cat", "cats", "catsdogcats", "dog", "dogcatsdog",
                "hippopotamuses", "rat", "ratcatdogcat"
            ]], ["catsdogcats", "dogcatsdog", "ratcatdogcat"]),
            ([["cat", "dog", "catdog"]], ["catdog"]),
        ],
    )
