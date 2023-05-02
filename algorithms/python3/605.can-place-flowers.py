#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (32.81%)
# Likes:    4106
# Dislikes: 776
# Total Accepted:    378.2K
# Total Submissions: 1.2M
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# You have a long flowerbed in which some of the plots are planted, and some
# are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty
# and 1 means not empty, and an integer n, return if n new flowers can be
# planted in the flowerbed without violating the no-adjacent-flowers rule.
#
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
# Constraints:
#
#
# 1 <= flowerbed.length <= 2 * 10^4
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        if n > (len(flowerbed) + 1) // 2:
            return False
        res = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] or (i > 0 and flowerbed[i - 1]) or (
                    i < len(flowerbed) - 1 and flowerbed[i + 1]):
                continue
            flowerbed[i] = 1
            res += 1
            if n <= res:
                return True
        return False


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.canPlaceFlowers, Solution()),
        [
            ([[1, 0, 0, 0, 1], 1], True),
            ([[1, 0, 0, 0, 1], 2], False),
            ([[1, 0, 0, 0, 0, 1], 2], False),
            ([[1, 0, 1, 0, 1, 0, 1], 0], True),
            ([[0, 0, 1, 0, 1], 1], True),
        ],
    )
