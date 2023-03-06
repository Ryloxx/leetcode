#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#
# https://leetcode.com/problems/kth-missing-positive-number/description/
#
# algorithms
# Easy (56.00%)
# Likes:    4176
# Dislikes: 291
# Total Accepted:    243K
# Total Submissions: 423.9K
# Testcase Example:  '[2,3,4,7,11]\n5'
#
# Given an array arr of positive integers sorted in a strictly increasing
# order, and an integer k.
#
# Return the k^th positive integer that is missing from this array.
#
#
# Example 1:
#
#
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The
# 5^th missing positive integer is 9.
#
#
# Example 2:
#
#
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2^nd missing
# positive integer is 6.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length
#
#
#
# Follow up:
#
# Could you solve this problem in less than O(n) complexity?
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = -1, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            diff = arr[mid] - mid - 1
            if diff < k and lo != mid:
                lo = mid
            else:
                hi = mid
        return k + lo + 1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findKthPositive, Solution()),
        [
            ([[2, 3, 4, 7, 11], 5], 9),
            ([[1, 2, 3, 4], 2], 6),
            ([[2], 1], 1),
            ([[3], 1], 1),
            ([[2], 3], 4),
            ([[1], 1], 2),
            ([[1, 3], 1], 2),
            ([[1, 10, 21, 22, 25], 12], 14),
        ],
    )
