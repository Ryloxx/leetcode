#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (59.02%)
# Likes:    3724
# Dislikes: 638
# Total Accepted:    381.1K
# Total Submissions: 647.1K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order and return
# it.
#
# You must solve the problem without using any built-in functions in O(nlog(n))
# time complexity and with the smallest space complexity possible.
#
#
# Example 1:
#
#
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not
# changed (for example, 2 and 3), while the positions of other numbers are
# changed (for example, 1 and 5).
#
#
# Example 2:
#
#
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -5 * 10^4 <= nums[i] <= 5 * 10^4
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # Lazy, uses Tim Sort under the hood
    # O(NlogN) time complexity
    # O(N) space complexity
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums

    # O(NlogN) time complexity
    # O(1) space complexity
    # def sortArray(self, nums: List[int]) -> List[int]:

    #     def heapify(lo, hi):
    #         if lo >= hi:
    #             return
    #         m = max(lo,
    #                 lo * 2 + 1,
    #                 lo * 2 + 2,
    #                 key=lambda x: nums[x] if x < hi else -float('inf'))

    #         if m != lo:
    #             nums[m], nums[lo] = nums[lo], nums[m]
    #             heapify(m, hi)

    #     for i in range(len(nums) // 2, -1, -1):
    #         heapify(i, len(nums))

    #     for i in range(len(nums) - 1, -1, -1):
    #         nums[0], nums[i] = nums[i], nums[0]
    #         heapify(0, i)
    #     return nums

    # O(NlogN) time complexity
    # O(N) space complexity
    # def sortArray(self, nums: List[int]) -> List[int]:

    #     buffer = [0] * len(nums)

    #     def mergesort(lo, hi):
    #         if hi - lo <= 1:
    #             return
    #         mid = (lo + hi) // 2
    #         mergesort(lo, mid)
    #         mergesort(mid, hi)
    #         x = 0
    #         i = lo
    #         j = mid
    #         while i < mid and j < hi:
    #             if nums[i] < nums[j]:
    #                 buffer[x] = nums[i]
    #                 i += 1
    #             else:
    #                 buffer[x] = nums[j]
    #                 j += 1
    #             x += 1
    #         while i < mid:
    #             buffer[x] = nums[i]
    #             i += 1
    #             x += 1
    #         while j < hi:
    #             buffer[x] = nums[j]
    #             j += 1
    #             x += 1
    #         for x, idx in enumerate(range(lo, hi)):
    #             nums[idx] = buffer[x]

    #     mergesort(0, len(nums))
    #     return nums


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.sortArray, Solution()),
        [
            ([[5, 2, 3, 1]], [1, 2, 3, 5]),
            ([[5, 1, 1, 2, 0, 0]], [0, 0, 1, 1, 2, 5]),
            ([list(reversed(range(10)))], list(range(10))),
        ],
    )
