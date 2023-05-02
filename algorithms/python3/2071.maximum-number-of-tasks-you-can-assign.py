#
# @lc app=leetcode id=2071 lang=python3
#
# [2071] Maximum Number of Tasks You Can Assign
#
# https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/description/
#
# algorithms
# Hard (36.69%)
# Likes:    330
# Dislikes: 15
# Total Accepted:    5.8K
# Total Submissions: 16.4K
# Testcase Example:  '[3,2,1]\n[0,3,3]\n1\n1'
#
# You have n tasks and m workers. Each task has a strength requirement stored
# in a 0-indexed integer array tasks, with the i^th task requiring tasks[i]
# strength to complete. The strength of each worker is stored in a 0-indexed
# integer array workers, with the j^th worker having workers[j] strength. Each
# worker can only be assigned to a single task and must have a strength greater
# than or equal to the task's strength requirement (i.e., workers[j] >=
# tasks[i]).
#
# Additionally, you have pills magical pills that will increase a worker's
# strength by strength. You can decide which workers receive the magical pills,
# however, you may only give each worker at most one magical pill.
#
# Given the 0-indexed integer arrays tasks and workers and the integers pills
# and strength, return the maximum number of tasks that can be completed.
#
#
# Example 1:
#
#
# Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# Output: 3
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 2 (0 + 1 >= 1)
# - Assign worker 1 to task 1 (3 >= 2)
# - Assign worker 2 to task 0 (3 >= 3)
#
#
# Example 2:
#
#
# Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
# Output: 1
# Explanation:
# We can assign the magical pill and tasks as follows:
# - Give the magical pill to worker 0.
# - Assign worker 0 to task 0 (0 + 5 >= 5)
#
#
# Example 3:
#
#
# Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength =
# 10
# Output: 2
# Explanation:
# We can assign the magical pills and tasks as follows:
# - Give the magical pill to worker 0 and worker 1.
# - Assign worker 0 to task 0 (0 + 10 >= 10)
# - Assign worker 1 to task 1 (10 + 10 >= 15)
# The last pill is not given because it will not make any worker strong enough
# for the last task.
#
#
#
# Constraints:
#
#
# n == tasks.length
# m == workers.length
# 1 <= n, m <= 5 * 10^4
# 0 <= pills <= m
# 0 <= tasks[i], workers[j], strength <= 10^9
#
#
#
from collections import deque
from typing import List
from algo_input import run
from types import MethodType

# @lc code=start


class Solution:

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int,
                      strength: int) -> int:
        tasks.sort()
        workers.sort()

        def check(k):
            right = used_pills = 0
            q = deque()
            for i in range(k):
                val = tasks[k - i - 1]
                while (right < k and workers[-right - 1] + strength >= val):
                    q.append(workers[-right - 1])
                    right += 1
                if not q:
                    return False
                if q[0] >= val:
                    q.popleft()
                else:
                    q.pop()
                    used_pills += 1
            return used_pills <= pills

        lo, hi = 0, min(len(workers), len(tasks))
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxTaskAssign, Solution()),
        [
            [[[74, 41, 64, 20, 28, 52, 30, 4, 4, 63], [38], 0, 68], 1],
            [[[5, 4], [0, 0, 0], 1, 5], 1],
            [[[1, 3, 5, 8], [0, 0, 2, 4], 2, 3], 3],
            [[[33, 58, 22, 87, 38], [84, 46, 17, 58, 98, 30, 56, 78, 48], 0, 74
              ], 5],
            [[[10, 15, 30], [0, 10, 10, 10, 10], 3, 10], 2],
            [[[3, 2, 1], [0, 3, 3], 1, 1], 3],
            [[[
                8931, 7236, 4889, 6590, 9849, 4673, 6892, 1592, 1132, 3403,
                1214, 3159, 4350, 5456, 4998, 2235, 9016, 7766, 1979, 8420,
                7056, 1056, 4493, 3899, 4344, 6707, 1474, 5846, 3535, 9493,
                9015, 7291, 2462, 3057, 8737, 2269, 5949, 4003, 9122, 8786,
                5790, 1897, 8809, 5819, 1767, 6896, 2102, 2280, 6778, 9635,
                8006, 1631, 2822, 3792, 3103, 1721, 4738, 7867, 1820, 2252,
                5896, 1751, 7783, 7045, 6460, 9433, 5851, 7332, 5161, 7359,
                1255, 9876, 1009, 8631, 4721, 2146, 7166, 9858, 6820, 5393,
                9946, 1576, 1807, 6362, 8644, 6088, 6274, 3787, 3589, 6646,
                9108, 2538, 6912, 4629, 6178, 1859, 6004, 1118, 9436, 5667,
                2855, 6940, 1871, 3171, 1496, 5470, 4725, 6796, 9775, 1299,
                5897, 9921
            ],
              [
                  3606, 4962, 3702, 4169, 3101, 563, 1551, 2906, 2061, 3382,
                  3340, 4599, 2826, 3894, 1287, 4191, 1670, 2346, 3634, 4887,
                  3203, 2960, 2530, 4080, 674, 1031, 2387, 3611, 2222, 1796,
                  906, 1191, 3473, 3551, 1383, 2029, 980, 1133, 688, 3881,
                  2423, 1053, 4056, 4567, 2640, 1419, 639, 4942, 1335, 2111,
                  1139, 3596, 2675, 1114, 3171, 1428, 2950, 2414, 2471, 4177,
                  1552, 4452, 3154, 2907, 2148, 4044, 942, 4058, 1537, 4063,
                  2580, 1665, 3486, 1653, 2841, 4682, 3815, 2174, 4530, 3807,
                  1291, 2624, 907, 1809, 3723, 4917, 1314, 1682, 4740, 2334,
                  2743, 2318, 1413, 996, 975, 3937, 3766, 4597, 760, 1314,
                  1573, 3974, 3008, 901, 2319, 3958, 3069, 2808, 4087, 4920,
                  4020, 662, 2279, 1831, 2196, 1083, 767, 1682, 2726, 3126,
                  2549, 4788, 3323, 906, 4964, 1641, 2203, 3732, 2553, 4481,
                  3969, 3726, 4101, 3429, 3897, 3154, 2356, 3096, 4902, 3719,
                  837, 685, 4471, 4306, 1888, 804, 4175, 2480, 777, 4396, 1896,
                  1125, 2471, 1362, 4940, 1803, 4903, 2248, 3542, 1816, 895,
                  4731, 4337, 2482, 1656, 4312, 1088, 2499, 4558, 1322, 973,
                  1916, 1902, 1600, 2429, 1134, 4297, 827, 1459, 1270, 1102,
                  997, 1326, 4424, 4114, 1134, 2221, 1376, 2143, 1409, 3555,
                  1849, 4843, 2751, 3093, 2048, 4604, 4922, 2210, 4069, 2140,
                  4870, 4153, 4327, 4976, 2954, 4157, 504, 3321, 523
              ], 66, 9620], 112],
        ],
    )
