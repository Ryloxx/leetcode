#
# @lc app=leetcode id=732 lang=python3
#
# [732] My Calendar III
#
# https://leetcode.com/problems/my-calendar-iii/description/
#
# algorithms
# Hard (66.70%)
# Likes:    1614
# Dislikes: 236
# Total Accepted:    75.6K
# Total Submissions: 105.7K
# Testcase Example:
# '["MyCalendarThree","book","book","book","book","book","book"]\n' +
#  '[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]'
#
# A k-booking happens when k events have some non-empty intersection (i.e.,
# there is some time that is common to all k events.)
#
# You are given some events [start, end), after each given event, return an
# integer k representing the maximum k-booking between all the previous
# events.
#
# Implement the MyCalendarThree class:
#
#
# MyCalendarThree() Initializes the object.
# int book(int start, int end) Returns an integer k representing the largest
# integer such that there exists a k-booking in the calendar.
#
#
#
# Example 1:
#
#
# Input
# ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
# [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
# Output
# [null, 1, 1, 2, 3, 3, 3]
#
# Explanation
# MyCalendarThree myCalendarThree = new MyCalendarThree();
# myCalendarThree.book(10, 20); // return 1, The first event can be booked and
# is disjoint, so the maximum k-booking is a 1-booking.
# myCalendarThree.book(50, 60); // return 1, The second event can be booked and
# is disjoint, so the maximum k-booking is a 1-booking.
# myCalendarThree.book(10, 40); // return 2, The third event [10, 40)
# intersects the first event, and the maximum k-booking is a 2-booking.
# myCalendarThree.book(5, 15); // return 3, The remaining events cause the
# maximum K-booking to be only a 3-booking.
# myCalendarThree.book(5, 10); // return 3
# myCalendarThree.book(25, 55); // return 3
#
#
#
# Constraints:
#
#
# 0 <= start < end <= 10^9
# At most 400 calls will be made to book.
#
#
#
from algo_input import run, wrapp_class
# @lc code=start
from sortedcontainers import SortedDict


class MyCalendarThree:

    def __init__(self):

        self.memo = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.memo[start] = self.memo.setdefault(start, 0) + 1
        self.memo[end] = self.memo.setdefault(end, 0) - 1
        res = s = 0
        for value in self.memo.values():
            s += value
            res = max(res, s)
        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
# @lc code=end
if __name__ == "__main__":
    run(
        wrapp_class(MyCalendarThree),
        [
            [[[],
              [
                  ["book", [10, 20]],
                  ["book", [50, 60]],
                  ["book", [10, 40]],
                  ["book", [5, 15]],
                  ["book", [5, 10]],
                  ["book", [25, 55]],
              ]], [1, 1, 2, 3, 3, 3]],
        ],
    )
