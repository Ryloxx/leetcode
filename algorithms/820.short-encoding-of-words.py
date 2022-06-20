#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#
# https://leetcode.com/problems/short-encoding-of-words/description/
#
# algorithms
# Medium (55.28%)
# Likes:    708
# Dislikes: 266
# Total Accepted:    45.7K
# Total Submissions: 82.6K
# Testcase Example:  '["time","me","bell"]'
#
# A valid encoding of an array of words is any reference string s and array of
# indices indices such that:
#
#
# words.length == indices.length
# The reference string s ends with the '#' character.
# For each index indices[i], the substring of s starting from indices[i] and up
# to (but not including) the next '#' character is equal to words[i].
#
#
# Given an array of words, return the length of the shortest reference string s
# possible of any valid encoding of words.
#
#
# Example 1:
#
#
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2,
# 5].
# words[0] = "time", the substring of s starting from indices[0] = 0 to the
# next '#' is underlined in "time#bell#"
# words[1] = "me", the substring of s starting from indices[1] = 2 to the next
# '#' is underlined in "time#bell#"
# words[2] = "bell", the substring of s starting from indices[2] = 5 to the
# next '#' is underlined in "time#bell#"
#
#
# Example 2:
#
#
# Input: words = ["t"]
# Output: 2
# Explanation: A valid encoding would be s = "t#" and indices = [0].
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 7
# words[i] consists of only lowercase letters.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    MAX_WORD_LENGTH_KEY = "word_max_length"

    # O(N) time complexity
    # O(N) space complexity
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = {}
        for w in words:
            temp = trie
            for c in reversed(w):
                temp = temp.setdefault(c, {})
            temp[Solution.MAX_WORD_LENGTH_KEY] = len(w) + 1

        def dfs(current):
            if len(current) == 1 and Solution.MAX_WORD_LENGTH_KEY in current:
                return current[Solution.MAX_WORD_LENGTH_KEY]
            return sum(
                dfs(value) for key, value in current.items()
                if key != Solution.MAX_WORD_LENGTH_KEY)

        return dfs(trie)

    # O(NlogN) time complexity
    # O(N) space complexity
    # def minimumLengthEncoding(self, words: List[str]) -> int:
    #     words.sort(key=len, reverse=True)
    #     trie = set()
    #     res = 0
    #     for w in words:
    #         if w in trie:
    #             continue
    #         res += len(w) + 1
    #         trie.update(w[x:] for x in range(len(w)))
    #     return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minimumLengthEncoding, Solution()),
        [
            [[["time", "me", "bell"]], 10],
            [[["time", "me", "ti"]], 8],
            [[["me", "time"]], 5],
            [[["t"]], 2],
        ],
    )
