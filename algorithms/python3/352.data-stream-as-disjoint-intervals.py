#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (51.67%)
# Likes:    1195
# Dislikes: 261
# Total Accepted:    73.1K
# Total Submissions: 131.4K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum",
# "getIntervals","addNum","getIntervals","addNum","getIntervals","addNum",
# "getIntervals"]\n' +
#  '[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
# Given a data stream input of non-negative integers a1, a2, ..., an, summarize
# the numbers seen so far as a list of disjoint intervals.
#
# Implement the SummaryRanges class:
#
#
# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int value) Adds the integer value to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream
# currently as a list of disjoint intervals [starti, endi]. The answer should
# be sorted by starti.
#
#
#
# Example 1:
#
#
# Input
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
# "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# Output
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7,
# 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
#
# Explanation
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // return [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
#
#
#
# Constraints:
#
#
# 0 <= value <= 10^4
# At most 3 * 10^4 calls will be made to addNum and getIntervals.
#
#
#
# Follow up: What if there are lots of merges and the number of disjoint
# intervals is small compared to the size of the data stream?
#
#
from bisect import bisect_left
from functools import cache
from typing import List
from algo_input import run, wrapp_class


# @lc code=start
class SummaryRanges:

    def __init__(self):
        self.arr = []

    @cache
    def addNum(self, value: int) -> None:
        m = bisect_left(self.arr, value, key=lambda x: x[0])
        self.arr.insert(m, [value, value])
        after = m > 0 and self.arr[m - 1][1] == value - 1
        before = m < len(self.arr) - 1 and self.arr[m + 1][0] == value + 1
        if after and before:
            self.arr[m - 1][1] = self.arr[m + 1][1]
            del self.arr[m:m + 2]
        elif after:
            self.arr[m][0] = self.arr[m - 1][0]
            del self.arr[m - 1]
        elif before:
            self.arr[m][1] = self.arr[m + 1][1]
            del self.arr[m + 1]

    def getIntervals(self) -> List[List[int]]:
        return self.arr


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
# @lc code=end


class _SummaryRanges(SummaryRanges):

    def getIntervals(self) -> str:
        return str(super().getIntervals())


if __name__ == "__main__":
    run(
        wrapp_class(_SummaryRanges),
        [
            ([[],
              [["addNum", [1]], ["getIntervals", []], ["addNum", [3]],
               ["getIntervals", []], ["addNum", [7]], ["getIntervals", []],
               ["addNum", [2]], ["getIntervals", []], ["addNum", [6]],
               ["getIntervals", []]]], [
                   None,
                   "[[1, 1]]",
                   None,
                   "[[1, 1], [3, 3]]",
                   None,
                   "[[1, 1], [3, 3], [7, 7]]",
                   None,
                   "[[1, 3], [7, 7]]",
                   None,
                   "[[1, 3], [6, 7]]",
               ]),
            ([[],
              [["addNum", [1]], ["getIntervals", []], ["addNum", [2]],
               ["getIntervals", []], ["addNum", [3]], ["getIntervals", []],
               ["addNum", [4]], ["getIntervals", []], ["addNum", [5]],
               ["getIntervals", []]]], [
                   None,
                   "[[1, 1]]",
                   None,
                   "[[1, 2]]",
                   None,
                   "[[1, 3]]",
                   None,
                   "[[1, 4]]",
                   None,
                   "[[1, 5]]",
               ]),
            ([[],
              [["addNum", [1]], ["getIntervals", []], ["addNum", [3]],
               ["getIntervals", []], ["addNum", [4]], ["getIntervals", []],
               ["addNum", [5]], ["getIntervals", []]]], [
                   None,
                   "[[1, 1]]",
                   None,
                   "[[1, 1], [3, 3]]",
                   None,
                   "[[1, 1], [3, 4]]",
                   None,
                   "[[1, 1], [3, 5]]",
               ]),
            ([[],
              [["addNum", [5]], ["getIntervals", []], ["addNum", [4]],
               ["getIntervals", []], ["addNum", [3]], ["getIntervals", []],
               ["addNum", [1]], ["getIntervals", []]]], [
                   None,
                   "[[5, 5]]",
                   None,
                   "[[4, 5]]",
                   None,
                   "[[3, 5]]",
                   None,
                   "[[1, 1], [3, 5]]",
               ]),
            ([[],
              [["addNum", [6]], ["getIntervals", []], ["addNum", [6]],
               ["getIntervals", []], ["addNum", [0]], ["getIntervals", []],
               ["addNum", [4]], ["getIntervals", []], ["addNum", [8]],
               ["getIntervals", []], ["addNum", [7]], ["getIntervals", []],
               ["addNum", [6]], ["getIntervals", []], ["addNum", [4]],
               ["getIntervals", []], ["addNum", [7]], ["getIntervals", []],
               ["addNum", [5]], ["getIntervals", []]]
              ], [
                  None, "[[6, 6]]", None, "[[6, 6]]", None, "[[0, 0], [6, 6]]",
                  None, "[[0, 0], [4, 4], [6, 6]]", None,
                  "[[0, 0], [4, 4], [6, 6], [8, 8]]", None,
                  "[[0, 0], [4, 4], [6, 8]]", None, "[[0, 0], [4, 4], [6, 8]]",
                  None, "[[0, 0], [4, 4], [6, 8]]", None,
                  "[[0, 0], [4, 4], [6, 8]]", None, "[[0, 0], [4, 8]]"
              ]),
        ],
    )
