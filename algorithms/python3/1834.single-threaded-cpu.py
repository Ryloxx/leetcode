#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#
# https://leetcode.com/problems/single-threaded-cpu/description/
#
# algorithms
# Medium (42.03%)
# Likes:    1409
# Dislikes: 144
# Total Accepted:    50.3K
# Total Submissions: 116.6K
# Testcase Example:  '[[1,2],[2,4],[3,2],[4,1]]'
#
# You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D
# integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means
# that the i^​​​​​​th​​​​ task will be available to process at enqueueTimei and
# will take processingTimei to finish processing.
#
# You have a single-threaded CPU that can process at most one task at a time
# and will act in the following way:
#
#
# If the CPU is idle and there are no available tasks to process, the CPU
# remains idle.
# If the CPU is idle and there are available tasks, the CPU will choose the one
# with the shortest processing time. If multiple tasks have the same shortest
# processing time, it will choose the task with the smallest index.
# Once a task is started, the CPU will process the entire task without
# stopping.
# The CPU can finish a task then start a new one instantly.
#
#
# Return the order in which the CPU will process the tasks.
#
#
# Example 1:
#
#
# Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
# Output: [0,2,3,1]
# Explanation: The events go as follows:
# - At time = 1, task 0 is available to process. Available tasks = {0}.
# - Also at time = 1, the idle CPU starts processing task 0. Available tasks =
# {}.
# - At time = 2, task 1 is available to process. Available tasks = {1}.
# - At time = 3, task 2 is available to process. Available tasks = {1, 2}.
# - Also at time = 3, the CPU finishes task 0 and starts processing task 2 as
# it is the shortest. Available tasks = {1}.
# - At time = 4, task 3 is available to process. Available tasks = {1, 3}.
# - At time = 5, the CPU finishes task 2 and starts processing task 3 as it is
# the shortest. Available tasks = {1}.
# - At time = 6, the CPU finishes task 3 and starts processing task 1.
# Available tasks = {}.
# - At time = 10, the CPU finishes task 1 and becomes idle.
#
#
# Example 2:
#
#
# Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# Output: [4,3,2,0,1]
# Explanation: The events go as follows:
# - At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
# - Also at time = 7, the idle CPU starts processing task 4. Available tasks =
# {0,1,2,3}.
# - At time = 9, the CPU finishes task 4 and starts processing task 3.
# Available tasks = {0,1,2}.
# - At time = 13, the CPU finishes task 3 and starts processing task 2.
# Available tasks = {0,1}.
# - At time = 18, the CPU finishes task 2 and starts processing task 0.
# Available tasks = {1}.
# - At time = 28, the CPU finishes task 0 and starts processing task 1.
# Available tasks = {}.
# - At time = 40, the CPU finishes task 1 and becomes idle.
#
#
#
# Constraints:
#
#
# tasks.length == n
# 1 <= n <= 10^5
# 1 <= enqueueTimei, processingTimei <= 10^9
#
#
#
from heapq import heappop, heappush
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res, available, q, t = [], [], sorted(range(len(tasks)),
                                              key=lambda x: -tasks[x][0]), 0
        while q:
            while q and tasks[q[-1]][0] <= t:
                heappush(available, (tasks[q[-1]][1], q[-1]))
                q.pop()
            if available:
                res.append(heappop(available)[1])
                t += tasks[res[-1]][1]
            if q and not available:
                t = max(t, tasks[q[-1]][0])
        while available:
            res.append(heappop(available)[1])
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.getOrder, Solution()),
        [
            ([[[1, 2], [2, 4], [3, 2], [4, 1]]], [0, 2, 3, 1]),
            ([[[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]], [4, 3, 2, 0, 1]),
        ],
    )
