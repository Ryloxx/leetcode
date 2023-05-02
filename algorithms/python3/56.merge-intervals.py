#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (45.00%)
# Likes:    14340
# Dislikes: 538
# Total Accepted:    1.5M
# Total Submissions: 3.3M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        intervals += [[float('inf')] * 2]
        res, curr = [], intervals[0]
        for start, end in intervals:
            if curr[1] < start:
                res.append(curr)
                curr = [start, end]
            else:
                curr = [curr[0], max(curr[1], end)]
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.merge, Solution()),
        [
            [[[[1, 3], [2, 6], [8, 10], [15, 18]]], [[1, 6], [8, 10], [15, 18]]
             ],
            [[[[1, 4], [4, 5]]], [[1, 5]]],
            [[[[1, 4], [0, 5]]], [[0, 5]]],
            [[[[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]], [[1, 10]]],
        ],
    )
