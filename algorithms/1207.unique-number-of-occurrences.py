#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
# https://leetcode.com/problems/unique-number-of-occurrences/description/
#
# algorithms
# Easy (71.93%)
# Likes:    2573
# Dislikes: 57
# Total Accepted:    202.4K
# Total Submissions: 278.9K
# Testcase Example:  '[1,2,2,1,1,3]'
#
# Given an array of integers arr, return true if the number of occurrences of
# each value in the array is unique, or false otherwise.
#
#
# Example 1:
#
#
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two
# values have the same number of occurrences.
#
# Example 2:
#
#
# Input: arr = [1,2]
# Output: false
#
#
# Example 3:
#
#
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000
#
#
#
from algo_input import run
from types import MethodType
from typing import List
from collections import Counter


# @lc code=start
class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len((cnt := Counter(arr))) == len(set(cnt.values()))

    # def uniqueOccurrences(self, arr: List[int]) -> bool:
    #     cnt = [0] * 2000
    #     freqs = [-1] * 501
    #     for n in arr:
    #         cnt[n] += 1
    #     for n in cnt:
    #         if not n or n > 500:
    #             continue
    #         freqs[n] += 1
    #         if freqs[n]:
    #             return False
    #     return True


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.uniqueOccurrences, Solution()),
        [
            ([[1, 2, 2, 1, 1, 3]], True),
            ([[1, 2]], False),
            ([[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]], True),
            ([[1] * 46 + [2] * 46], False),
            ([[1] * 46 + [2] * 47], True),
            ([[1] * 500 + [2] * 500], False),
            ([[1] * 600 + [2] * 400], True),
        ],
    )
