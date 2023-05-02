#
# @lc app=leetcode id=1335 lang=python3
#
# [1335] Minimum Difficulty of a Job Schedule
#
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/
#
# algorithms
# Hard (56.40%)
# Likes:    1842
# Dislikes: 183
# Total Accepted:    91.9K
# Total Submissions: 161.3K
# Testcase Example:  '[6,5,4,3,2,1]\n2'
#
# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To
# work on the i^th job, you have to finish all the jobs j where 0 <= j < i).
#
# You have to finish at least one task every day. The difficulty of a job
# schedule is the sum of difficulties of each day of the d days. The difficulty
# of a day is the maximum difficulty of a job done on that day.
#
# You are given an integer array jobDifficulty and an integer d. The difficulty
# of the i^th job is jobDifficulty[i].
#
# Return the minimum difficulty of a job schedule. If you cannot find a
# schedule for the jobs return -1.
#
#
# Example 1:
#
#
# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7
#
#
# Example 2:
#
#
# Input: jobDifficulty = [9,9,9], d = 4
# Output: -1
# Explanation: If you finish a job per day you will still have a free day. you
# cannot find a schedule for the given jobs.
#
#
# Example 3:
#
#
# Input: jobDifficulty = [1,1,1], d = 3
# Output: 3
# Explanation: The schedule is one job per day. total difficulty will be 3.
#
#
#
# Constraints:
#
#
# 1 <= jobDifficulty.length <= 300
# 0 <= jobDifficulty[i] <= 1000
# 1 <= d <= 10
#
#
#
from functools import cache
from types import MethodType
from typing import List

from algo_input import run


# @lc code=start
class Solution:

    # The problem boils down to find the right spot where
    # to place d - 1 bar that minimize the sum of
    # the maximum of numbers between each bar
    # Example: arr = 6,5,4,3,2,1, d = 3
    # 3 - 1 bar to place that gives us the following possibilities
    # => 6 | 5 | 4 3 2 1 -> 6 + 5 + 4
    # => 6 | 5 4 | 3 2 1 -> 6 + 5 + 3
    # => 6 | 5 4 3 | 2 1 -> 6 + 5 + 2
    # => 6 | 5 4 3 2 | 1 -> 6 + 5 + 1
    # => 6 5 | 4 | 3 2 1 -> 6 + 4 + 3
    # => 6 5 | 4 3 | 2 1 -> 6 + 4 + 2
    # => 6 5 | 4 3 2 | 1 -> 6 + 4 + 1
    # => 6 5 4 | 3 | 2 1 -> 6 + 3 + 2
    # => 6 5 4 | 3 2 | 1 -> 6 + 3 + 1
    # => 6 5 4 3 | 2 | 1 -> 6 + 2 + 1
    # The best option is the last
    # Looking at that we can see that the space of possible solution
    # is (almost) equal to the number of ways to place d - 1 bars into n - 1
    # spot
    # Thanks to the combination formula we know it is in the order
    # of n!/r!(n - r)!
    # where n is the number of spots and r the number of bars
    # So the brute force algorithm would be to generate all those
    # possibilities and keep
    # track of the result of each one of them and taking the best which is not
    # good enough
    # We can do better. If we look closely, we can see that some part of the
    # possibilities repeat.
    # If we memoize the repeating part we could probably reach a better time
    # complexity.
    # But what do we memoize?
    # We could memoize the start of a group and its end along with its group
    # number
    # like so:
    # S K=0 E S K=1 S E K=2
    # 6 5 4 | 3 2 | 1
    # with K = group number, S = start, E = end
    # And we find the maximum for each different group in the possible
    # solution then add them up and take the best out of all solution we have
    # our final answer. The time complexity of this algorithm would be N^3*D
    # We could optimize this by instead of taking the start and the end of
    # each group we can take the current job index and the current maximum
    # of the group
    # and at job i we either put it in the current group then compare it to
    # the current maximum and expand the group or we say that job i initiate
    # a new group with its value as the current maximum
    # The final algorithm would have
    # O(N²*D) time complexity
    # O(N²*D) space complexity

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        @cache
        def dp(i, curr_max, group_number):
            if i >= len(jobDifficulty) or group_number < 0:
                return curr_max if group_number == 1 else float('inf')
            return min(
                dp(i + 1, max(jobDifficulty[i], curr_max), group_number),
                dp(i + 1, jobDifficulty[i], group_number - 1) + curr_max)

        return int(res) if (res := dp(1, jobDifficulty[0],
                                      d)) != float('inf') else -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minDifficulty, Solution()),
        [
            ([[9, 9, 9], 4], -1),
            ([[1, 1, 1], 3], 3),
            ([[11, 111, 22, 222, 33, 333, 44, 444], 6], 843),
            ([[6, 5, 4, 3, 2, 1], 2], 7),
            ([[0] * 100, 10], 0),
        ],
    )
