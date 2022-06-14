#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#
# https://leetcode.com/problems/minimize-deviation-in-array/description/
#
# algorithms
# Hard (52.48%)
# Likes:    1610
# Dislikes: 85
# Total Accepted:    43.6K
# Total Submissions: 83.1K
# Testcase Example:  '[1,2,3,4]'
#
# You are given an array nums of n positive integers.
#
# You can perform two types of operations on any element of the array any
# number of times:
#
#
# If the element is even, divide it by 2.
#
#
# For example, if the array is [1,2,3,4], then you can do this operation on the
# last element, and the array will be [1,2,3,2].
#
#
# If the element is odd, multiply it by 2.
#
# For example, if the array is [1,2,3,4], then you can do this operation on the
# first element, and the array will be [2,2,3,4].
#
#
#
#
# The deviation of the array is the maximum difference between any two elements
# in the array.
#
# Return the minimum deviation the array can have after performing some number
# of operations.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2],
# then the deviation will be 3 - 2 = 1.
#
#
# Example 2:
#
#
# Input: nums = [4,1,5,20,3]
# Output: 3
# Explanation: You can transform the array after two operations to [4,2,5,5,3],
# then the deviation will be 5 - 2 = 3.
#
#
# Example 3:
#
#
# Input: nums = [2,10,8]
# Output: 3
#
#
#
# Constraints:
#
#
# n == nums.length
# 2 <= n <= 5 * 10^4
# 1 <= nums[i] <= 10^9
#
#
#
from heapq import heappop, heappush
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # There are nlog(max(nums)) steps
    # in wich we perform 2 * log(n) operations
    # Hence O(nlog(max(nums))log(n)) time complexity
    # O(n) space complexity
    def minimumDeviation(self, nums: List[int]) -> int:
        h = []
        max_value = (-float("inf"), -1)
        res = float('inf')
        all_power_of_two = True
        for x in nums:
            value = (x // (x & -x), x)
            max_value = max(max_value, value)
            heappush(h, value)
            all_power_of_two = all_power_of_two and value[0] == 1

        while not all_power_of_two:
            current_value, initial_value = heappop(h)
            res = min(res, max_value[0] - current_value)
            entry_value = current_value << 1
            if entry_value > initial_value << (initial_value % 2):
                return res
            entry = (entry_value, initial_value)
            max_value = max(max_value, entry)
            heappush(h, entry)
        return 0


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minimumDeviation, Solution()),
        [
            [[[8, 1, 2, 1]], 0],
            [[[7, 20]], 2],
            [[[2, 8, 6, 1, 6]], 1],
            [[[399, 908, 648, 357, 693, 502, 331, 649, 596, 698]], 315],
            [[[10, 4, 3]], 2],
            [[[1, 1, 1, 1]], 0],
            [[[4, 1, 5, 20, 3]], 3],
            [[[1, 2, 3, 4]], 1],
            [[[2, 10, 8]], 3],
        ],
    )
