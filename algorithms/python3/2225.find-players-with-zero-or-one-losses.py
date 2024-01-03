#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
#
# algorithms
# Medium (67.85%)
# Likes:    763
# Dislikes: 67
# Total Accepted:    51.2K
# Total Submissions: 70.4K
# Testcase Example:
# '[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]'
#
# You are given an integer array matches where matches[i] = [winneri, loseri]
# indicates that the player winneri defeated player loseri in a match.
#
# Return a list answer of size 2 where:
#
#
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
#
#
# The values in the two lists should be returned in increasing order.
#
# Note:
#
#
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same
# outcome.
#
#
#
# Example 1:
#
#
# Input: matches =
# [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
#
#
# Example 2:
#
#
# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].
#
#
#
# Constraints:
#
#
# 1 <= matches.length <= 10^5
# matches[i].length == 2
# 1 <= winneri, loseri <= 10^5
# winneri != loseri
# All matches[i] are unique.
#
#
#
# from collections import Counter
from types import MethodType
from typing import List

from algo_input import run


# @lc code=start
class Solution:
    # O(N) time complexity
    # O(N) space complexity
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        scores, zero_losses, one_losses = {}, [], []
        for winner, looser in matches:
            scores.setdefault(winner, 0)
            scores[looser] = scores.get(looser, 0) + 1

        for player in range(10**5 + 1):
            if player not in scores:
                continue
            losses = scores[player]
            if not losses:
                zero_losses.append(player)
            elif losses == 1:
                one_losses.append(player)
        return [zero_losses, one_losses]

    # O(NlogN) time complexity
    # O(N) space complexity
    # def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    #     scores, zero_losses, one_losses = {}, [], []
    #     for winner, looser in matches:
    #         scores.setdefault(winner, 0)
    #         scores[looser] = scores.get(looser, 0) + 1

    #     for player in sorted(scores):
    #         losses = scores[player]
    #         if not losses:
    #             zero_losses.append(player)
    #         elif losses == 1:
    #             one_losses.append(player)
    #     return [zero_losses, one_losses]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findWinners, Solution()),
        [
            (
                [
                    [
                        [1, 3],
                        [2, 3],
                        [3, 6],
                        [5, 6],
                        [5, 7],
                        [4, 5],
                        [4, 8],
                        [4, 9],
                        [10, 4],
                        [10, 9],
                    ]
                ],
                [[1, 2, 10], [4, 5, 7, 8]],
            ),
            ([[[2, 3], [1, 3], [5, 4], [6, 4]]], [[1, 2, 5, 6], []]),
        ],
    )
