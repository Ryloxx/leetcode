#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#
# https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
#
# algorithms
# Easy (77.95%)
# Likes:    1047
# Dislikes: 65
# Total Accepted:    129.2K
# Total Submissions: 165.7K
# Testcase Example:  '"book"'
#
# You are given a string s of even length. Split this string into two halves of
# equal lengths, and let a be the first half and b be the second half.
#
# Two strings are alike if they have the same number of vowels ('a', 'e', 'i',
# 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and
# lowercase letters.
#
# Return true if a and b are alike. Otherwise, return false.
#
#
# Example 1:
#
#
# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel.
# Therefore, they are alike.
#
#
# Example 2:
#
#
# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2.
# Therefore, they are not alike.
# Notice that the vowel o is counted twice.
#
#
#
# Constraints:
#
#
# 2 <= s.length <= 1000
# s.length is even.
# s consists of uppercase and lowercase letters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def halvesAreAlike(self, s: str) -> bool:
        cnt, mid = 0, len(s) // 2
        for idx, c in enumerate(s):
            if c not in "aeiouAEIOU":
                continue
            if idx < mid:
                cnt += 1
            else:
                cnt -= 1
        return not cnt


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.halvesAreAlike, Solution()),
        [(["book"], True), (["textbook"], False), (["AbCdEfGh"], True),
         (["AbCdpppp"], False)])
