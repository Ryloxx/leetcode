#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#
# https://leetcode.com/problems/find-and-replace-pattern/description/
#
# algorithms
# Medium (75.58%)
# Likes:    2014
# Dislikes: 124
# Total Accepted:    104.9K
# Total Submissions: 138.2K
# Testcase Example:  '["abc","deq","mee","aqq","dkd","ccc"]\n"abb"'
#
# Given a list of strings words and a string pattern, return a list of words[i]
# that match pattern. You may return the answer in any order.
#
# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired
# word.
#
# Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same
# letter.
#
#
# Example 1:
#
#
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a ->
# m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
# permutation, since a and b map to the same letter.
#
#
# Example 2:
#
#
# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def findAndReplacePattern(self, words: List[str],
                              pattern: str) -> List[str]:

        def compare(word):
            memo_a, memo_b = {}, {}
            return all(
                memo_a.setdefault(c_1, code) == memo_b.setdefault(c_2, code)
                for code, (c_1, c_2) in enumerate(zip(word, pattern)))

        return filter(compare, words)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findAndReplacePattern, Solution()),
        [
            [[["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"],
             ["mee", "aqq"]],
            [[["a", "b", "c"], "a"], ["a", "b", "c"]],
            [[["ab", "bc", "cd"], "aa"], []],
        ],
    )
