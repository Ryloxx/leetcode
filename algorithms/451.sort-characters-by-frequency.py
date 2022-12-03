#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# algorithms
# Medium (67.83%)
# Likes:    5659
# Dislikes: 211
# Total Accepted:    443.9K
# Total Submissions: 640.2K
# Testcase Example:  '"tree"'
#
# Given a string s, sort it in decreasing order based on the frequency of the
# characters. The frequency of a character is the number of times it appears in
# the string.
#
# Return the sorted string. If there are multiple answers, return any of
# them.
#
#
# Example 1:
#
#
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
#
#
# Example 2:
#
#
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and
# "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
#
#
# Example 3:
#
#
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^5
# s consists of uppercase and lowercase English letters and digits.
#
#
#
from algo_input import run
from types import MethodType
from collections import Counter


# @lc code=start
class Solution:

    def frequencySort(self, s: str) -> str:
        return "".join(
            (char * char_count for char_count, char in sorted((
                (char_count, char) for char, char_count in Counter(s).items()),
                                                              reverse=True)))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.frequencySort, Solution()),
        [
            (["tree"], "eetr"),
            (["cccaaa"], "cccaaa"),
            (["Aabb"], "bbaA"),
            (["z"], "z"),
            (["2a554442f544asfasssffffasss"], "sssssssffffff44444aaaa55522"),
        ],
    )
