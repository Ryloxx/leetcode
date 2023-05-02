#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (47.00%)
# Likes:    2880
# Dislikes: 2279
# Total Accepted:    451.6K
# Total Submissions: 911.7K
# Testcase Example:  '"hello"'
#
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
# and upper cases, more than once.
#
#
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
#
#
# Constraints:
#
#
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def reverseVowels(self, s: str) -> str:
        l_s = list(s)
        vowels = set("aeiouAEIOU")
        left, right = 0, len(s) - 1
        while True:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            if left >= right:
                break
            l_s[left], l_s[right] = l_s[right], l_s[left]
            left += 1
            right -= 1
        return "".join(l_s)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.reverseVowels, Solution()),
        [
            (["hello"], "holle"),
            (["leetcode"], "leotcede"),
            (["l"], "l"),
            (["aeiou"], "uoiea"),
        ],
    )
