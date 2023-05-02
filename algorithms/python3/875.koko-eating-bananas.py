#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# https://leetcode.com/problems/koko-eating-bananas/description/
#
# algorithms
# Medium (51.98%)
# Likes:    6575
# Dislikes: 313
# Total Accepted:    300.6K
# Total Submissions: 579.4K
# Testcase Example:  '[3,6,7,11]\n8'
#
# Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
# piles[i] bananas. The guards have gone and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the pile
# has less than k bananas, she eats all of them instead and will not eat any
# more bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas
# before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h
# hours.
#
#
# Example 1:
#
#
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#
#
# Example 2:
#
#
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
#
#
# Example 3:
#
#
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#
#
#
# Constraints:
#
#
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9
#
#
#
from math import ceil
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum(ceil(d / mid) for d in piles) <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minEatingSpeed, Solution()),
        [
            ([[3, 6, 7, 11], 8], 4),
            ([[30, 11, 23, 4, 20], 5], 30),
            ([[30, 11, 23, 4, 20], 6], 23),
        ],
    )
