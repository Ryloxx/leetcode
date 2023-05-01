#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
#
# algorithms
# Easy (62.45%)
# Likes:    1735
# Dislikes: 159
# Total Accepted:    252.2K
# Total Submissions: 399.7K
# Testcase Example:  '[4000,3000,1000,2000]'
#
# You are given an array of unique integers salary where salary[i] is the
# salary of the i^th employee.
#
# Return the average salary of employees excluding the minimum and maximum
# salary. Answers within 10^-5 of the actual answer will be accepted.
#
#
# Example 1:
#
#
# Input: salary = [4000,3000,1000,2000]
# Output: 2500.00000
# Explanation: Minimum salary and maximum salary are 1000 and 4000
# respectively.
# Average salary excluding minimum and maximum salary is (2000+3000) / 2 =
# 2500
#
#
# Example 2:
#
#
# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000
# respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
#
#
#
# Constraints:
#
#
# 3 <= salary.length <= 100
# 1000 <= salary[i] <= 10^6
# All the integers of salary are unique.
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)

    # def average(self, salary: List[int]) -> float:
    #     m, M, res = float("inf"), -float("inf"), 0
    #     for s in salary:
    #         m = min(m, s)
    #         M = max(M, s)
    #         res += s
    #     return (res - m - M) / (len(salary) - 2)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.average, Solution()),
        [
            ([[4000, 3000, 1000, 2000]], 2500.),
            ([[1000, 2000, 3000]], 2000.),
        ],
    )
