#
# @lc app=leetcode id=899 lang=python3
#
# [899] Orderly Queue
#
# https://leetcode.com/problems/orderly-queue/description/
#
# algorithms
# Hard (58.53%)
# Likes:    1452
# Dislikes: 556
# Total Accepted:    58.2K
# Total Submissions: 87.4K
# Testcase Example:  '"cba"\n1'
#
# You are given a string s and an integer k. You can choose one of the first k
# letters of s and append it at the end of the string..
#
# Return the lexicographically smallest string you could have after applying
# the mentioned step any number of moves.
#
#
# Example 1:
#
#
# Input: s = "cba", k = 1
# Output: "acb"
# Explanation:
# In the first move, we move the 1^st character 'c' to the end, obtaining the
# string "bac".
# In the second move, we move the 1^st character 'b' to the end, obtaining the
# final result "acb".
#
#
# Example 2:
#
#
# Input: s = "baaca", k = 3
# Output: "aaabc"
# Explanation:
# In the first move, we move the 1^st character 'b' to the end, obtaining the
# string "aacab".
# In the second move, we move the 3^rd character 'c' to the end, obtaining the
# final result "aaabc".
#
#
#
# Constraints:
#
#
# 1 <= k <= s.length <= 1000
# s consist of lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[x:] + s[:x] for x in range(len(s)))
        return "".join(sorted(s))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.orderlyQueue, Solution()),
        [
            (["cba", 1], "acb"),
            (["baaca", 3], "aaabc"),
        ],
    )
