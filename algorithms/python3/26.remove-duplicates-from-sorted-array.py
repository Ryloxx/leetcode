#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (49.01%)
# Likes:    9155
# Dislikes: 12719
# Total Accepted:    2.6M
# Total Submissions: 5.1M
# Testcase Example:  '[1,1,2]'
#
# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once. The
# relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array
# nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not
# matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:
#
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
# ⁠   assert nums[i] == expectedNums[i];
# }
#
#
# If all assertions pass, then your solution will be accepted.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements
# of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
#
#
# Example 2:
#
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements
# of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are
# underscores).
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
#
#
#
from bisect import bisect_left
from algo_input import run
from typing import List


# @lc code=start
class Solution:

    # Using bisect (better if the array contains long sequences of duplicate)
    # O(KlogN) time complexity, where K = unique elements in the array
    # O(1) space complexity
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            j = bisect_left(nums, nums[i] + 1, j)
        return i + 1

    # O(N) time complexity
    # O(1) space complexity
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     i = 0
    #     for j in range(len(nums)):
    #         if nums[j] != nums[i]:
    #             i += 1
    #             nums[i] = nums[j]
    #     return i + 1


# @lc code=end
if __name__ == "__main__":

    def judge(nums):
        res = Solution().removeDuplicates(nums)
        for i in range(res, len(nums)):
            nums[i] = None
        return [res, nums]

    run(
        judge,
        [
            ([[1, 1, 2]], [2, [1, 2, None]]),
            ([[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
              ], [5, [0, 1, 2, 3, 4, None, None, None, None, None]]),
            ([[1]], [1, [1]]),
        ],
    )