#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (38.86%)
# Likes:    3330
# Dislikes: 81
# Total Accepted:    142.3K
# Total Submissions: 367K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
# represents the width and the height of an envelope.
#
# One envelope can fit into another if and only if both the width and height of
# one envelope are greater than the other envelope's width and height.
#
# Return the maximum number of envelopes you can Russian doll (i.e., put one
# inside the other).
#
# Note: You cannot rotate an envelope.
#
#
# Example 1:
#
#
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
#
#
# Example 2:
#
#
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= envelopes.length <= 10^5
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^5
#
#
#

from bisect import bisect_left
from types import MethodType
from typing import List
from algo_input import run


# @lc code=start
class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        res = []
        for _, w in envelopes:
            if not res or res[-1] < w:
                res.append(w)
                continue
            res[bisect_left(res, w)] = w
        return len(res)


# @lc code=end

if __name__ == "__main__":
    run(
        MethodType(Solution.maxEnvelopes, Solution()),
        [
            [[[[46, 89], [50, 53], [52, 68], [72, 45], [77, 81]]], 3],
            [[[[1, 2], [2, 3], [3, 4], [3, 5], [4, 5], [5, 5], [5, 6], [6, 7],
               [7, 8]]], 7],
            [[[[10, 8], [1, 12], [6, 15], [2, 18]]], 2],
            [[[[7, 8], [12, 16], [12, 5], [1, 8], [4, 19], [3, 15], [4, 10],
               [9, 16]]], 3],
            [[[[5, 4], [6, 4], [6, 7], [2, 3]]], 3],
            [[[[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250],
               [6, 370], [6, 360], [7, 380]]], 5],
            [[[[1, 1], [1, 1], [1, 1]]], 1],
            [[[[1, 1]]], 1],
            [[list([x, x] for x in range(10**5))], 10**5],
        ])
