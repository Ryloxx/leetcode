#
# @lc app=leetcode id=1964 lang=python3
#
# [1964] Find the Longest Valid Obstacle Course at Each Position
#
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/description/
#
# algorithms
# Hard (47.02%)
# Likes:    986
# Dislikes: 36
# Total Accepted:    25.7K
# Total Submissions: 43.8K
# Testcase Example:  '[1,2,3,2]'
#
# You want to build some obstacle courses. You are given a 0-indexed integer
# array obstacles of length n, where obstacles[i] describes the height of the
# i^th obstacle.
#
# For every index i between 0 and n - 1 (inclusive), find the length of the
# longest obstacle course in obstacles such that:
#
#
# You choose any number of obstacles between 0 and i inclusive.
# You must include the i^th obstacle in the course.
# You must put the chosen obstacles in the same order as they appear in
# obstacles.
# Every obstacle (except the first) is taller than or the same height as the
# obstacle immediately before it.
#
#
# Return an array ans of length n, where ans[i] is the length of the longest
# obstacle course for index i as described above.
#
#
# Example 1:
#
#
# Input: obstacles = [1,2,3,2]
# Output: [1,2,3,3]
# Explanation: The longest valid obstacle course at each position is:
# - i = 0: [1], [1] has length 1.
# - i = 1: [1,2], [1,2] has length 2.
# - i = 2: [1,2,3], [1,2,3] has length 3.
# - i = 3: [1,2,3,2], [1,2,2] has length 3.
#
#
# Example 2:
#
#
# Input: obstacles = [2,2,1]
# Output: [1,2,1]
# Explanation: The longest valid obstacle course at each position is:
# - i = 0: [2], [2] has length 1.
# - i = 1: [2,2], [2,2] has length 2.
# - i = 2: [2,2,1], [1] has length 1.
#
#
# Example 3:
#
#
# Input: obstacles = [3,1,5,6,4,2]
# Output: [1,1,2,3,2,2]
# Explanation: The longest valid obstacle course at each position is:
# - i = 0: [3], [3] has length 1.
# - i = 1: [3,1], [1] has length 1.
# - i = 2: [3,1,5], [3,5] has length 2. [1,5] is also valid.
# - i = 3: [3,1,5,6], [3,5,6] has length 3. [1,5,6] is also valid.
# - i = 4: [3,1,5,6,4], [3,4] has length 2. [1,4] is also valid.
# - i = 5: [3,1,5,6,4,2], [1,2] has length 2.
#
#
#
# Constraints:
#
#
# n == obstacles.length
# 1 <= n <= 10^5
# 1 <= obstacles[i] <= 10^7
#
#
#
from bisect import bisect_right
from typing import List
from algo_input import run
from types import MethodType

# @lc code=start


class Solution:

    def longestObstacleCourseAtEachPosition(self,
                                            obstacles: List[int]) -> List[int]:
        lic = []
        res = [0] * len(obstacles)
        for i, obstacle in enumerate(obstacles):
            idx = bisect_right(lic, obstacle)
            if idx < len(lic):
                lic[idx] = obstacle
            else:
                lic.append(obstacle)
            res[i] = idx + 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestObstacleCourseAtEachPosition, Solution()),
        [
            ([[1, 2, 3, 2]], [1, 2, 3, 3]),
            ([[2, 2, 1]], [1, 2, 1]),
            ([[3, 1, 5, 6, 4, 2]], [1, 1, 2, 3, 2, 2]),
            ([[5, 1, 5, 5, 1, 3, 4, 5, 1, 4]], [1, 1, 2, 3, 2, 3, 4, 5, 3, 5]),
            ([[5, 2, 1, 3, 3, 5, 2, 1, 1, 2]], [1, 1, 1, 2, 3, 4, 2, 2, 3, 4]),
            ([list(range(1, 10**5 + 1))], list(range(1, 10**5 + 1))),
        ],
    )
