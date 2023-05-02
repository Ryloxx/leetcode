#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#
# https://leetcode.com/problems/course-schedule-iii/description/
#
# algorithms
# Hard (35.74%)
# Likes:    2040
# Dislikes: 57
# Total Accepted:    59.3K
# Total Submissions: 164.6K
# Testcase Example:  '[[100,200],[200,1300],[1000,1250],[2000,3200]]'
#
# There are n different online courses numbered from 1 to n. You are given an
# array courses where courses[i] = [durationi, lastDayi] indicate that the i^th
# course should be taken continuously for durationi days and must be finished
# before or on lastDayi.
#
# You will start on the 1^st day and you cannot take two or more courses
# simultaneously.
#
# Return the maximum number of courses that you can take.
#
#
# Example 1:
#
#
# Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output: 3
# Explanation:
# There are totally 4 courses, but you can take 3 courses at most:
# First, take the 1^st course, it costs 100 days so you will finish it on the
# 100^th day, and ready to take the next course on the 101^st day.
# Second, take the 3^rd course, it costs 1000 days so you will finish it on the
# 1100^th day, and ready to take the next course on the 1101^st day.
# Third, take the 2^nd course, it costs 200 days so you will finish it on the
# 1300^th day.
# The 4^th course cannot be taken now, since you will finish it on the 3300^th
# day, which exceeds the closed date.
#
#
# Example 2:
#
#
# Input: courses = [[1,2]]
# Output: 1
#
#
# Example 3:
#
#
# Input: courses = [[3,2],[4,3]]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= courses.length <= 10^4
# 1 <= durationi, lastDayi <= 10^4
#
#
#
from heapq import heappush, heapreplace
from operator import itemgetter
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(NlogN) time complexity
    # O(N) space complexity
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        h, cumulated_durations = [], 0
        for duration, last_day in sorted(courses, key=itemgetter(1)):
            cumulated_durations += duration
            if cumulated_durations <= last_day:
                heappush(h, -duration)
                continue
            cumulated_durations += heapreplace(
                h, -duration) if h and duration < -h[0] else -duration
        return len(h)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.scheduleCourse, Solution()),
        [
            [[[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]], 3],
            [[[[100, 200], [200, 1300], [1000, 1250], [900, 2100]]], 3],
            [[[[1, 2]]], 1],
            [[[[3, 2], [4, 3]]], 0],
            [[[[9, 14], [7, 12], [1, 11], [4, 7]]], 3],
            [[[[100, 2], [32, 50]]], 1],
        ],
    )
