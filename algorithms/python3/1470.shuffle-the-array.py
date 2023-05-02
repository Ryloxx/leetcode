#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#
# https://leetcode.com/problems/shuffle-the-array/description/
#
# algorithms
# Easy (88.47%)
# Likes:    3447
# Dislikes: 224
# Total Accepted:    412K
# Total Submissions: 465.9K
# Testcase Example:  '[2,5,1,3,4,7]\n3'
#
# Given the array nums consisting of 2n elements in the form
# [x1,x2,...,xn,y1,y2,...,yn].
#
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
#
#
# Example 1:
#
#
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is
# [2,3,5,4,1,7].
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]
#
#
# Example 3:
#
#
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
#
#
#
# Constraints:
#
#
# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10^3
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # O(N) time complexity
    # O(1) space complexity
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        def find_idx(idx):
            if idx < n:
                return 2 * idx
            return (idx - n) * 2 + 1

        for idx in range(2 * n):
            next_idx = idx
            while nums[idx] >= 0:
                next_idx = find_idx(next_idx)
                nums[idx], nums[next_idx] = nums[next_idx], -nums[
                    idx]  # Order matters
        for idx in range(2 * n):
            nums[idx] = -nums[idx]
        return nums

    # O(N) time complexity
    # O(N) space complexity
    # def shuffle(self, nums: List[int], n: int) -> List[int]:
    #     return [nums[idx] for i in range(n) for idx in [i, i + n]]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.shuffle, Solution()),
        [
            ([[2, 5, 1, 3, 4, 7], 3], [2, 3, 5, 4, 1, 7]),
            ([[1, 2, 3, 4, 4, 3, 2, 1], 4], [1, 4, 2, 3, 3, 2, 4, 1]),
            ([[1, 1, 2, 2], 2], [1, 2, 1, 2]),
        ],
    )
