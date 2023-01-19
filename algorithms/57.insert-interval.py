#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (38.03%)
# Likes:    7415
# Dislikes: 511
# Total Accepted:    689.7K
# Total Submissions: 1.8M
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the i^th
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and
# end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
#
#
#
# Constraints:
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
#
#
#
from bisect import bisect_left
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def insert(self, vals: List[List[int]], val: List[int]) -> List[List[int]]:
        if not val:
            return []
        start = [x[0] for x in vals]
        index = bisect_left(start, val[0])
        vals.insert(index, val)
        res = [vals[0]]
        for i in vals[1:]:
            if i[0] > res[-1][1]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.insert, Solution()),
        [
            ([[[1, 3], [6, 9]], [2, 5]], [[1, 5], [6, 9]]),
            ([[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
              ], [[1, 2], [3, 10], [12, 16]]),
        ],
    )
