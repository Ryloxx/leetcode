#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (57.19%)
# Likes:    6347
# Dislikes: 220
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '"leetcode"'
#
# Given a string s, find the first non-repeating character in it and return its
# index. If it does not exist, return -1.
#
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
#
#
#
from collections import Counter
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for idx, c in enumerate(s):
            if count[c] == 1:
                return idx
        return -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.firstUniqChar, Solution()),
        [
            [["leetcode"], 0],
            [["loveleetcode"], 2],
            [["aabb"], -1],
        ],
    )
