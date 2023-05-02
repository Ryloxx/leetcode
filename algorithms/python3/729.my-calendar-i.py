#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#
# https://leetcode.com/problems/my-calendar-i/description/
#
# algorithms
# Medium (55.19%)
# Likes:    2301
# Dislikes: 67
# Total Accepted:    166.3K
# Total Submissions: 297.8K
# Testcase Example:  '["MyCalendar","book","book","book"]\n
# [[],[10,20],[15,25],[20,30]]'
#
# You are implementing a program to use as your calendar. We can add a new
# event if adding the event will not cause a double booking.
#
# A double booking happens when two events have some non-empty intersection
# (i.e., some moment is common to both events.).
#
# The event can be represented as a pair of integers start and end that
# represents a booking on the half-open interval [start, end), the range of
# real numbers x such that start <= x < end.
#
# Implement the MyCalendar class:
#
#
# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to
# the calendar successfully without causing a double booking. Otherwise, return
# false and do not add the event to the calendar.
#
#
#
# Example 1:
#
#
# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]
#
# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time
# 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the
# first event takes every time less than 20, but not including 20.
#
#
# Constraints:
#
#
# 0 <= start < end <= 10^9
# At most 1000 calls will be made to book.
#

from algo_input import run, wrapp_class

# @lc code=start
from sortedcontainers.sortedlist import SortedList


# N = number of call to book()
# O(NlogN) time complexity
# O(N) space complexity
class MyCalendar:

    def __init__(self):
        self.intervals = SortedList()

    def overlap(self, a, b):
        return max(a[0], b[0]) < min(a[1], b[1])

    def book(self, start: int, end: int) -> bool:
        n, i_1 = len(self.intervals), (start, end)
        insert_point = self.intervals.bisect_left(i_1)
        if (insert_point > 0
                and self.overlap(i_1, self.intervals[insert_point - 1])
                or insert_point < n
                and self.overlap(i_1, self.intervals[insert_point])):
            return False
        self.intervals.add(i_1)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end
if __name__ == "__main__":
    run(
        wrapp_class(MyCalendar),
        [[[[],
           [
               ["book", [10, 20]],
               ["book", [15, 25]],
               ["book", [20, 30]],
               ["book", [10, 20]],
               ["book", [15, 25]],
               ["book", [20, 30]],
               ["book", [40, 50]],
               ["book", [30, 35]],
               ["book", [35, 40]],
           ]], [True, False, True, False, False, False, True, True, True]],
         [[[],
           [
               ["book", [47, 50]],
               ["book", [33, 41]],
               ["book", [39, 45]],
               ["book", [33, 42]],
               ["book", [25, 32]],
               ["book", [26, 35]],
               ["book", [19, 25]],
               ["book", [3, 8]],
               ["book", [8, 13]],
               ["book", [18, 27]],
           ]],
          [True, True, False, False, True, False, True, True, True, False]]],
    )
