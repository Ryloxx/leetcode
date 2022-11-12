#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (50.38%)
# Likes:    9346
# Dislikes: 182
# Total Accepted:    579.7K
# Total Submissions: 1.1M
# Testcase Example:  '["MedianFinder",
# addNum","addNum","findMedian","addNum","findMedian"]\n' +
# '[[],[1],[2],[],[3],[]]'
#
# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value, and the median is the mean of the two
# middle values.
#
#
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
#
#
# Implement the MedianFinder class:
#
#
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data
# structure.
# double findMedian() returns the median of all elements so far. Answers within
# 10^-5 of the actual answer will be accepted.
#
#
#
# Example 1:
#
#
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
#
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#
#
#
# Constraints:
#
#
# -10^5 <= num <= 10^5
# There will be at least one element in the data structure before calling
# findMedian.
# At most 5 * 10^4 calls will be made to addNum and findMedian.
#
#
#
# Follow up:
#
#
# If all integer numbers from the stream are in the range [0, 100], how would
# you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how
# would you optimize your solution?
#
#
#
from algo_input import run, wrapp_class
# @lc code=start
from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        self.d = SortedList()

    @property
    def length(self):
        return len(self.d)

    @property
    def mid(self):
        return self.length // 2

    def addNum(self, num: int) -> None:
        self.d.add(num)

    def findMedian(self) -> float:
        if self.length == 0:
            return 0
        if self.length % 2:
            return self.d[self.mid]  # type: ignore
        else:
            return (self.d[self.mid] +
                    self.d[self.mid - 1]) / 2  # type: ignore


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
if __name__ == "__main__":
    run(wrapp_class(MedianFinder), [([[],
                                      [
                                          ["addNum", [1]],
                                          ["addNum", [2]],
                                          ["findMedian", []],
                                          ["addNum", [3]],
                                          ["findMedian", []],
                                      ]], [None, None, 1.5, None, 2])])
