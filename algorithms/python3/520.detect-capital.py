#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (55.56%)
# Likes:    2276
# Dislikes: 405
# Total Accepted:    311.6K
# Total Submissions: 553.9K
# Testcase Example:  '"USA"'
#
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
#
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
#
#
# Given a string word, return true if the usage of capitals in it is right.
#
#
# Example 1:
# Input: word = "USA"
# Output: true
# Example 2:
# Input: word = "FlaG"
# Output: false
#
#
# Constraints:
#
#
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.
#
#
#
from collections import defaultdict
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    state_lookup = defaultdict(
        lambda: lambda w: False, {
            0: lambda w: all(map(str.islower, w)),
            1: lambda w: all(map(lambda x: w[x].islower(), range(1, len(w)))),
            3: lambda w: all(map(str.isupper, w)),
        })

    def detectCapitalUse(self, word: str) -> bool:
        return len(word) < 2 or Solution.state_lookup[word[0].isupper() + 2 *
                                                      word[1].isupper()](word)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.detectCapitalUse, Solution()),
        [
            (["U"], True),
            (["USA"], True),
            (["FlaG"], False),
        ],
    )
