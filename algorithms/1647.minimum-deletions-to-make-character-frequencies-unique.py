#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/
#
# algorithms
# Medium (56.41%)
# Likes:    1495
# Dislikes: 31
# Total Accepted:    92.5K
# Total Submissions: 163.6K
# Testcase Example:  '"aab"'
#
# A string s is called good if there are no two different characters in s that
# have the same frequency.
#
# Given a string s, return the minimum number of characters you need to delete
# to make s good.
#
# The frequency of a character in a string is the number of times it appears in
# the string. For example, in the string "aab", the frequency of 'a' is 2,
# while the frequency of 'b' is 1.
#
#
# Example 1:
#
#
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
#
#
# Example 2:
#
#
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string
# "aaabbc".
#
# Example 3:
#
#
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the
# end (i.e. frequency of 0 is ignored).
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.
#
#
#
from typing import Counter
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # N = len(s), K = len(charset)

    # O(N + K log K) time complexity
    # O(K) space complexity
    #  def minDeletions(self, s: str) -> int:
    #     m, res = float('inf'), 0
    #     for freq in sorted(Counter(s).values(), reverse=True):
    #         if freq > m:
    #             res += freq - m
    #             freq = m
    #         m = max(0, freq - 1)
    #     return res

    # O(N) time complexity
    # O(N + K) space complexity
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        m = max(c.values())
        buckets = [0] * (m + 1)
        for freq in c.values():
            buckets[freq] += 1
        res = 0
        for freq in range(len(buckets) - 1, 0, -1):
            diff = max(0, buckets[freq] - 1)
            buckets[freq - 1] += diff
            res += diff
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minDeletions, Solution()),
        [
            [["aaabbbcc"], 2],
            [[
                "ridkfsqtwfjtqxbyjiknwnxoskhapnecctrhuxrodmedacfywjj"
                "abiwvmvhsqyurmzopzsnuolsmjybmeedcyvdsnrcogmhothjd"
            ], 79],
            [["aab"], 0],
            [["ceabaacb"], 2],
            [[
                "jbhdceaiegbfbfbecfaejhhhafhagjhejgbcaejjcdbebgjahba"
                "dejidghjbgagbjaehgbfdbijajjihbhffhgjegjgfedhjggjh"
            ], 2],
        ],
    )
