#
# @lc app=leetcode id=2306 lang=python3
#
# [2306] Naming a Company
#
# https://leetcode.com/problems/naming-a-company/description/
#
# algorithms
# Hard (34.51%)
# Likes:    819
# Dislikes: 40
# Total Accepted:    19.2K
# Total Submissions: 46.6K
# Testcase Example:  '["coffee","donuts","time","toffee"]'
#
# You are given an array of strings ideas that represents a list of names to be
# used in the process of naming a company. The process of naming a company is
# as follows:
#
#
# Choose 2 distinct names from ideas, call them ideaA and ideaB.
# Swap the first letters of ideaA and ideaB with each other.
# If both of the new names are not found in the original ideas, then the name
# ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a
# valid company name.
# Otherwise, it is not a valid name.
#
#
# Return the number of distinct valid names for the company.
#
#
# Example 1:
#
#
# Input: ideas = ["coffee","donuts","time","toffee"]
# Output: 6
# Explanation: The following selections are valid:
# - ("coffee", "donuts"): The company name created is "doffee conuts".
# - ("donuts", "coffee"): The company name created is "conuts doffee".
# - ("donuts", "time"): The company name created is "tonuts dime".
# - ("donuts", "toffee"): The company name created is "tonuts doffee".
# - ("time", "donuts"): The company name created is "dime tonuts".
# - ("toffee", "donuts"): The company name created is "doffee tonuts".
# Therefore, there are a total of 6 distinct company names.
#
# The following are some examples of invalid selections:
# - ("coffee", "time"): The name "toffee" formed after swapping already exists
# in the original array.
# - ("time", "toffee"): Both names are still the same after swapping and exist
# in the original array.
# - ("coffee", "toffee"): Both names formed after swapping already exist in the
# original array.
#
#
# Example 2:
#
#
# Input: ideas = ["lack","back"]
# Output: 0
# Explanation: There are no valid selections. Therefore, 0 is returned.
#
#
#
# Constraints:
#
#
# 2 <= ideas.length <= 5 * 10^4
# 1 <= ideas[i].length <= 10
# ideas[i] consists of lowercase English letters.
# All the strings in ideas are unique.
#
#
#
# from collections import Counter, defaultdict
# from string import ascii_lowercase
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # N = word count; M = word length

    # O(N * M) time complexity
    # O(N * M) space complexity
    def distinctNames(self, ideas: List[str]) -> int:
        memo = [set() for _ in range(26)]
        res = 0
        for w in ideas:
            memo[ord(w[0]) - ord('a')].add(w[1:])
        for c_1 in range(26):
            for c_2 in range(c_1 + 1, 26):
                p = len(memo[c_1] & (memo[c_2]))
                res += 2 * (len(memo[c_1]) - p) * (len(memo[c_2]) - p)
        return res

    # O(N * M) time complexity
    # O(N * M) space complexity
    # def distinctNames(self, ideas: List[str]) -> int:
    #     memo = defaultdict(Counter)
    #     s_ideas = set(ideas)
    #     res = 0
    #     for w in ideas:
    #         for c in ascii_lowercase:
    #             n_idea = str(c + w[1:])
    #             if n_idea in s_ideas:
    #                 continue
    #             memo[c][w[0]] += 1

    #     for w in ideas:
    #         for c in ascii_lowercase:
    #             n_idea = str(c + w[1:])
    #             if n_idea in s_ideas:
    #                 continue
    #             res += memo[w[0]][c]
    #     return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.distinctNames, Solution()),
        [
            ([["coffee", "donuts", "time", "toffee"]], 6),
            ([["lack", "back"]], 0),
            ([["coffee", "donuts"]], 2),
            ([["coffee", "donuts", "doffee"]], 0),
            ([["donuts", "doffee"]], 0),
        ],
    )
