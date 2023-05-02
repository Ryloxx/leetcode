#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
#
# algorithms
# Easy (45.09%)
# Likes:    1921
# Dislikes: 1734
# Total Accepted:    219.7K
# Total Submissions: 491K
# Testcase Example:  '["c","f","j"]\n"a"'
#
# Given a characters array letters that is sorted in non-decreasing order and a
# character target, return the smallest character in the array that is larger
# than target.
#
# Note that the letters wrap around.
#
#
# For example, if target == 'z' and letters == ['a', 'b'], the answer is
# 'a'.
#
#
#
# Example 1:
#
#
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
#
#
# Example 2:
#
#
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
#
#
# Example 3:
#
#
# Input: letters = ["c","f","j"], target = "d"
# Output: "f"
#
#
#
# Constraints:
#
#
# 2 <= letters.length <= 10^4
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo, hi = -len(letters), 0
        target = chr(ord(target) + 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if target <= letters[mid]:
                hi = mid
            else:
                lo = mid + 1
        return letters[lo]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.nextGreatestLetter, Solution()),
        [
            [[["a", "b"], "z"], "a"],
            [[["c", "f", "j"], "a"], "c"],
            [[["c", "f", "j"], "c"], "f"],
            [[["c", "f", "j"], "d"], "f"],
            [[["c", "f", "j"], "f"], "j"],
        ],
    )
