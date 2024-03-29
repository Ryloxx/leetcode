#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
#
# algorithms
# Hard (50.90%)
# Likes:    4223
# Dislikes: 47
# Total Accepted:    149.8K
# Total Submissions: 288.7K
# Testcase Example:  '[1,2,3,3]\n[3,4,5,6]\n[50,10,40,70]'
#
# We have n jobs, where every job is scheduled to be done from startTime[i] to
# endTime[i], obtaining a profit of profit[i].
#
# You're given the startTime, endTime and profit arrays, return the maximum
# profit you can take such that there are no two jobs in the subset with
# overlapping time range.
#
# If you choose a job that ends at time X you will be able to start another job
# that starts at time X.
#
#
# Example 1:
#
#
#
#
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job.
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
#
#
# Example 2:
#
# ⁠
#
#
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit =
# [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job.
# Profit obtained 150 = 20 + 70 + 60.
#
#
# Example 3:
#
#
#
#
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
# 1 <= startTime[i] < endTime[i] <= 10^9
# 1 <= profit[i] <= 10^4
#
#
#
from algo_input import run
from types import MethodType
from typing import List
from bisect import bisect_right


# @lc code=start
class Solution:

    def jobScheduling(self, startTime: List[int], endTime: List[int],
                      profit: List[int]) -> int:
        dp = [[0, 0]]
        for e, s, p in sorted(zip(endTime, startTime, profit)):
            o = bisect_right(dp, [s + 1]) - 1
            if dp[o][1] + p > dp[-1][1]:
                dp.append([e, p + dp[o][1]])
        return dp[-1][1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.jobScheduling, Solution()),
        [([[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]], 120),
         ([[1, 2, 3, 3, 5], [3, 4, 5, 6, 6], [50, 10, 40, 70, 200]], 290),
         ([[1, 2, 3, 3, 4], [3, 4, 5, 6, 6], [50, 10, 40, 70, 200]], 250),
         ([[1, 2, 3, 3, 3], [3, 4, 5, 6, 6], [50, 10, 40, 70, 200]], 250),
         ([[1, 2, 3, 3, 2], [3, 4, 5, 6, 6], [50, 10, 40, 70, 200]], 200)],
    )
