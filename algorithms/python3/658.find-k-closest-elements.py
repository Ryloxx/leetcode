#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (44.58%)
# Likes:    6095
# Dislikes: 500
# Total Accepted:    379.1K
# Total Submissions: 812.5K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# Given a sorted integer array arr, two integers k and x, return the k closest
# integers to x in the array. The result should also be sorted in ascending
# order.
#
# An integer a is closer to x than an integer b if:
#
#
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
#
#
#
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
#
#
# Constraints:
#
#
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# arr is sorted in ascending order.
# -10^4 <= arr[i], x <= 10^4
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(log(N-K) + K) time complexity
    # O(1) space complexity
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo + k]

    # O(NlogN) time complexity
    # O(N) space complexity
    # def findClosestElements(self,
    # arr: List[int], k: int, x: int) -> List[int]:
    #     return sorted(sorted(arr, key=lambda y: [abs(x - y), y])[:k])


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findClosestElements, Solution()),
        [
            [[[1, 2, 3, 4, 5], 4, 3], [1, 2, 3, 4]],
            [[[1, 2, 3, 4, 5], 4, -1], [1, 2, 3, 4]],
            [[[0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9], [3, 6, 8, 8, 9]],
        ],
    )
