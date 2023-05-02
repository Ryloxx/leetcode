#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (59.74%)
# Likes:    6728
# Dislikes: 252
# Total Accepted:    422.5K
# Total Submissions: 698.9K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given an n x n matrix where each of the rows and columns is sorted in
# ascending order, return the k^th smallest element in the matrix.
#
# Note that it is the k^th smallest element in the sorted order, not the k^th
# distinct element.
#
# You must find a solution with a memory complexity better than O(n^2).
#
#
# Example 1:
#
#
# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and
# the 8^th smallest number is 13
#
#
# Example 2:
#
#
# Input: matrix = [[-5]], k = 1
# Output: -5
#
#
#
# Constraints:
#
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the rows and columns of matrix are guaranteed to be sorted in
# non-decreasing order.
# 1 <= k <= n^2
#
#
#
# Follow up:
#
#
# Could you solve the problem with a constant memory (i.e., O(1) memory
# complexity)?
# Could you solve the problem in O(n) time complexity? The solution may be too
# advanced for an interview but you may find reading this paper fun.
#
#
#
# from heapq import heappop, heappush
from copy import deepcopy
from itertools import chain
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(N**2) time complexity
    # O(1) space complexity
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def kth(num):
            i = 0
            j = n - 1
            res = (0, -float('inf'))
            while i < n and j >= 0:
                if matrix[i][j] <= num:
                    i += 1
                    res = (res[0] + j + 1, max(res[1], num))
                else:
                    j -= 1
            return res

        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            pos, m = kth(mid)
            if k <= pos:
                hi = m
            else:
                lo = m + 1
        return lo

    # O(N**2logN**2) time complexity
    # O(K) space complexity
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     h = []
    #     for num in chain.from_iterable(matrix):
    #         heappush(h, -num)
    #         if len(h) == k + 1:
    #             heappop(h)
    #     return -h[0]


# @lc code=end
if __name__ == "__main__":
    base = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    base_sorted = sorted(list(chain.from_iterable(base)))
    run(
        MethodType(Solution.kthSmallest, Solution()),
        [
            [[[[-5, -4], [-5, -4]], 2], -5],
            [[[[1, 4, 7], [2, 6, 9], [5, 8, 10]], 9], 10],
            [[[[1, 4, 7], [2, 5, 8], [3, 6, 9]], 9], 9],
            [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9], 9],
            [[[[1, 4], [2, 5]], 2], 2],
            [[[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8], 13],
            [[[[-5]], 1], -5],
            [[[[1, 2], [1, 3]], 2], 1],
            [[[[1, 2, 3], [1, 2, 3], [1, 2, 3]], 1], 1],
            [[[[1, 2, 3], [1, 2, 3], [1, 2, 3]], 2], 1],
            [[[[1, 2, 3], [1, 2, 3], [1, 2, 3]], 3], 1],
            [[[[1, 2, 3], [1, 2, 3], [1, 2, 3]], 4], 2],
            [[[[1, 2, 3], [1, 2, 3], [1, 2, 3]], 5], 2],
            [[[[1, 2, 3], [1, 2, 3], [1, 2, 3]], 6], 2],
            [[[[1, 2, 3], [1, 2, 3], [1, 2, 3]], 7], 3],
            [[[[1, 2, 3], [1, 2, 3], [1, 2, 3]], 8], 3],
            [[[[1, 2, 3], [1, 2, 3], [1, 2, 3]], 9], 3],
            *[[[deepcopy(base), x], base_sorted[x - 1]]
              for x in range(1, 1 + len(base) * len(base[0]))],
        ],
    )
