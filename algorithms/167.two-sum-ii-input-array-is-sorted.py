#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Medium (58.83%)
# Likes:    6197
# Dislikes: 980
# Total Accepted:    1M
# Total Submissions: 1.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given a 1-indexed array of integers numbers that is already sorted in
# non-decreasing order, find two numbers such that they add up to a specific
# target number. Let these two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an
# integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not
# use the same element twice.
#
# Your solution must use only constant extra space.
#
#
# Example 1:
#
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We
# return [1, 2].
#
#
# Example 2:
#
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We
# return [1, 3].
#
#
# Example 3:
#
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We
# return [1, 2].
#
#
#
# Constraints:
#
#
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
#
#
#
from typing import List
from algo_input import run, any_order
from types import MethodType


# @lc code=start
class Solution:

    # O(n) time, O(1) space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return [-1, -1]


# @lc code=end
# O(nlogn) time, O(1) space
# def twoSum(self, numbers: List[int], target: int) -> List[int]:
#     for idx in range(len(numbers) - 1):
#         current = numbers[idx]
#         other = target - current
#         otherIdx = bisect_left(numbers, other, idx + 1)
#         if otherIdx != len(
#                 numbers) and current + numbers[otherIdx] == target:
#             return [idx + 1, otherIdx + 1]
#     return [-1, -1]
# O(n) time, O(n) space
# def twoSum(self, numbers: List[int], target: int) -> List[int]:
#     memo = {}
#     for idx, current in enumerate(numbers):
#         other = target - current
#         if other in memo:
#             return [memo[other] + 1, idx + 1]
#         memo[current] = idx
#     return [-1, -1]

if __name__ == "__main__":
    run(MethodType(Solution.twoSum, Solution()), [
        [[[2, 7, 11, 15], 9], [1, 2]],
        [[[2, 3, 4], 6], [1, 3]],
        [[[-1, 0], -1], [1, 2]],
        [[[-1, 0], -2], [-1, -1]],
        [[[1, 2, 3, 4, 5], 9], [4, 5]],
    ],
        comparator=any_order)
