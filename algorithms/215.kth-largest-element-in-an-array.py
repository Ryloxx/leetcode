#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (63.61%)
# Likes:    9653
# Dislikes: 504
# Total Accepted:    1.4M
# Total Submissions: 2.1M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
#
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
#
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
#
#
#
from heapq import heappush, heapreplace
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # Heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k < 1:
            return -1
        h = []
        for i in nums:
            if len(h) < k:
                heappush(h, i)
            elif h[0] < i:
                heapreplace(h, i)
        return h[0]

    # Sorting
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     return sorted(nums)[-k]

    # Quick Select
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     if not nums:
    #         return -1
    #     pivot = nums[0]
    #     lt, eq, gt = [], [], []
    #     for n in nums:
    #         if n < pivot:
    #             lt.append(n)
    #         elif n > pivot:
    #             gt.append(n)
    #         else:
    #             eq.append(n)
    #     if len(gt) >= k:
    #         return self.findKthLargest(gt, k)
    #     if k > len(gt) + len(eq):
    #         return self.findKthLargest(lt, k - len(gt) - len(eq))
    #     return pivot


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findKthLargest, Solution()),
        [
            [[[3, 2, 1, 5, 6, 4], 2], 5],
            [[[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], 4],
            [[[3, 2, 1, 4], 3], 2],
        ],
    )
