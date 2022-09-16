#
# @lc app=leetcode id=2007 lang=python3
#
# [2007] Find Original Array From Doubled Array
#
# https://leetcode.com/problems/find-original-array-from-doubled-array/description/
#
# algorithms
# Medium (38.12%)
# Likes:    1707
# Dislikes: 95
# Total Accepted:    95.1K
# Total Submissions: 232.1K
# Testcase Example:  '[1,3,4,2,6,8]'
#
# An integer array original is transformed into a doubled array changed by
# appending twice the value of every element in original, and then randomly
# shuffling the resulting array.
#
# Given an array changed, return original if changed is a doubled array. If
# changed is not a doubled array, return an empty array. The elements in
# original may be returned in any order.
#
#
# Example 1:
#
#
# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].
#
#
# Example 2:
#
#
# Input: changed = [6,3,0,1]
# Output: []
# Explanation: changed is not a doubled array.
#
#
# Example 3:
#
#
# Input: changed = [1]
# Output: []
# Explanation: changed is not a doubled array.
#
#
#
# Constraints:
#
#
# 1 <= changed.length <= 10^5
# 0 <= changed[i] <= 10^5
#
#
#
from itertools import chain
from random import shuffle
from typing import List
from algo_input import run, any_order
from types import MethodType


# @lc code=start
class Solution:

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        changed.sort()
        right = len(changed) // 2
        res = []
        for i in range(right):
            if changed[right] != changed[i] * 2:
                return []
            res.append(i)
        return res


# @lc code=end
if __name__ == "__main__":
    arr = list(
        chain.from_iterable(
            [range((10**5) >> 1),
             map(lambda x: x * 2, range((10**5) >> 1))]))
    shuffle(arr)
    run(MethodType(Solution.findOriginalArray, Solution()), [
        [[[0, 0, 0, 0]], [0, 0]],
        [[[0, 0, 0, 0, 1, 2]], [0, 0, 1]],
        [[[6, 3, 0, 1]], []],
        [[[1, 3, 4, 2, 6, 8]], [1, 3, 4]],
        [[[1]], []],
        [[[]], []],
        [[[
            1, 1 << 1, 1 << 2, 1 << 3, 1 << 4, 1 << 1, 1 << 2, 1 << 3, 1 << 4,
            1 << 5
        ]], [1, 1 << 1, 1 << 2, 1 << 3, 1 << 4]],
        [[[1, 1, 1, 1]], []],
        [[[1, 1, 1, 1, 1]], []],
        [[arr], list(range((10**5) >> 1))],
    ],
        comparator=any_order)
