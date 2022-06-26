#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
#
# algorithms
# Medium (50.08%)
# Likes:    3133
# Dislikes: 125
# Total Accepted:    140.9K
# Total Submissions: 280.1K
# Testcase Example:  '[1,2,3,4,5,6,1]\n3'
#
# There are several cards arranged in a row, and each card has an associated
# number of points. The points are given in the integer array cardPoints.
#
# In one step, you can take one card from the beginning or from the end of the
# row. You have to take exactly k cards.
#
# Your score is the sum of the points of the cards you have taken.
#
# Given the integer array cardPoints and the integer k, return the maximum
# score you can obtain.
#
#
# Example 1:
#
#
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However,
# choosing the rightmost card first will maximize your total score. The optimal
# strategy is to take the three cards on the right, giving a final score of 1 +
# 6 + 5 = 12.
#
#
# Example 2:
#
#
# Input: cardPoints = [2,2,2], k = 2
# Output: 4
# Explanation: Regardless of which two cards you take, your score will always
# be 4.
#
#
# Example 3:
#
#
# Input: cardPoints = [9,7,7,9,7,7,9], k = 7
# Output: 55
# Explanation: You have to take all the cards. Your score is the sum of points
# of all cards.
#
#
#
# Constraints:
#
#
# 1 <= cardPoints.length <= 10^5
# 1 <= cardPoints[i] <= 10^4
# 1 <= k <= cardPoints.length
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        return [self.maxScoreN,
                self.maxScoreK][k >> 1 < len(cardPoints)](cardPoints, k)

    # O(K) time complexity
    def maxScoreK(self, cardPoints: List[int], k: int) -> int:
        curr = res = 0
        for i in range(-k, k):
            curr += cardPoints[i]
            i >= 0 and (curr := curr - cardPoints[i - k])
            res = max(res, curr)
        return res

    # O(N) time complexity
    def maxScoreN(self, cardPoints: List[int], k: int) -> int:
        res, p, curr = float('inf'), len(cardPoints) - k, 0
        cardPoints.append(0)
        for i in range(len(cardPoints) - 1):
            curr += cardPoints[i]
            cardPoints[i] = curr
            i >= p - 1 and (res := min(res, curr - cardPoints[i - p]))
        return cardPoints[-2] - res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxScore, Solution()),
        [
            [[[2, 2, 2], 2], 4],
            [[[1, 2, 3, 4, 5, 6, 1], 3], 12],
            [[[9, 7, 7, 9, 7, 7, 9], 7], 55],
            [[[0, 0, 0, 0], 1], 0],
            [[[0, 0, 1, 0, 0], 1], 0],
            [[[0], 1], 0],
            [[[1, 2, 3, 4, 5], 5], 15],
        ],
    )
