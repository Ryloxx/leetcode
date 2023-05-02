#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#
# https://leetcode.com/problems/furthest-building-you-can-reach/description/
#
# algorithms
# Medium (45.15%)
# Likes:    1813
# Dislikes: 50
# Total Accepted:    51.5K
# Total Submissions: 113.6K
# Testcase Example:  '[4,2,7,6,9,14,12]\n5\n1'
#
# You are given an integer array heights representing the heights of buildings,
# some bricks, and some ladders.
#
# You start your journey from building 0 and move to the next building by
# possibly using bricks or ladders.
#
# While moving from building i to building i+1 (0-indexed),
#
#
# If the current building's height is greater than or equal to the next
# building's height, you do not need a ladder or bricks.
# If the current building's height is less than the next building's height, you
# can either use one ladder or (h[i+1] - h[i]) bricks.
#
#
# Return the furthest building index (0-indexed) you can reach if you use the
# given ladders and bricks optimally.
#
#
# Example 1:
#
#
# Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
# Output: 4
# Explanation: Starting at building 0, you can follow these steps:
# - Go to building 1 without using ladders nor bricks since 4 >= 2.
# - Go to building 2 using 5 bricks. You must use either bricks or ladders
# because 2 < 7.
# - Go to building 3 without using ladders nor bricks since 7 >= 6.
# - Go to building 4 using your only ladder. You must use either bricks or
# ladders because 6 < 9.
# It is impossible to go beyond building 4 because you do not have any more
# bricks or ladders.
#
#
# Example 2:
#
#
# Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
# Output: 7
#
#
# Example 3:
#
#
# Input: heights = [14,3,19,3], bricks = 17, ladders = 0
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= heights.length <= 10^5
# 1 <= heights[i] <= 10^6
# 0 <= bricks <= 10^9
# 0 <= ladders <= heights.length
#
#
#
from heapq import heappush, heapreplace
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def furthestBuilding(self, heights: List[int], bricks: int,
                         ladders: int) -> int:
        h = []
        for idx in range(len(heights) - 1):
            d_h = heights[idx + 1] - heights[idx]
            if d_h <= 0:
                continue
            if len(h) < ladders:
                heappush(h, d_h)
            else:
                bricks -= heapreplace(h, d_h) if h and h[0] < d_h else d_h
            if bricks < 0:
                return idx

        return len(heights) - 1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.furthestBuilding, Solution()),
        [
            [[[4, 2, 7, 6, 9, 14, 12], 5, 1], 4],
            [[[4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2], 7],
            [[[14, 3, 19, 3], 17, 0], 3],
            [[[0, 0, 0, 0, 0], 0, 0], 4],
            [[[4, 3, 2, 1], 0, 0], 3],
            [[[1, 4, 8, 8], 3, 1], 3],
        ],
    )
