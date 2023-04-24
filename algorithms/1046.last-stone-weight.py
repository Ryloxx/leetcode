#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
# https://leetcode.com/problems/last-stone-weight/description/
#
# algorithms
# Easy (64.76%)
# Likes:    4227
# Dislikes: 83
# Total Accepted:    387.7K
# Total Submissions: 598.2K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# You are given an array of integers stones where stones[i] is the weight of
# the i^th stone.
#
# We are playing a game with the stones. On each turn, we choose the heaviest
# two stones and smash them together. Suppose the heaviest two stones have
# weights x and y with x <= y. The result of this smash is:
#
#
# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has
# new weight y - x.
#
#
# At the end of the game, there is at most one stone left.
#
# Return the weight of the last remaining stone. If there are no stones left,
# return 0.
#
#
# Example 1:
#
#
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the
# value of the last stone.
#
#
# Example 2:
#
#
# Input: stones = [1]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
#
#
#
from heapq import heapify, heappop, heappush
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        for x in range(len(stones)):
            stones[x] = -stones[x]
        heapify(stones)
        while len(stones) > 1:
            heappush(stones, heappop(stones) - heappop(stones))
        return -stones[-1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.lastStoneWeight, Solution()),
        [
            ([[2, 7, 4, 1, 8, 1]], 1),
            ([[1]], 1),
        ],
    )
