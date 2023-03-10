#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (41.24%)
# Likes:    2721
# Dislikes: 660
# Total Accepted:    210.5K
# Total Submissions: 498.7K
# Testcase Example:  '[1,2,2,4]'
#
# You have a set of integers s, which originally contains all the numbers from
# 1 to n. Unfortunately, due to some error, one of the numbers in s got
# duplicated to another number in the set, which results in repetition of one
# number and loss of another number.
#
# You are given an integer array nums representing the data status of this set
# after the error.
#
# Find the number that occurs twice and the number that is missing and return
# them in the form of an array.
#
#
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:
# Input: nums = [1,1]
# Output: [1,2]
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^4
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(N) time complexity
    # O(N) space complexity
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rep = 0
        s = len(nums) * (len(nums) + 1) // 2
        seen = set()
        for i in nums:
            if i in seen:
                rep = i
            seen.add(i)
            s -= i
        return [rep, s + rep]

    # O(N) time complexity
    # O(1) space complexity
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    #     rep = 0
    #     s = len(nums) * (len(nums) + 1) // 2
    #     for i in nums:
    #         i = abs(i)
    #         s -= i
    #         curr = nums[i - 1]
    #         if curr < 0:
    #             rep = i
    #         nums[i - 1] = -curr
    #     return [rep, s + rep]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findErrorNums, Solution()),
        [
            ([[1, 2, 2, 4]], [2, 3]),
            ([[1, 1]], [1, 2]),
            ([[1, 2, 4, 4]], [4, 3]),
            ([[1, 4, 4, 2]], [4, 3]),
            ([[4, 4, 2, 1]], [4, 3]),
            ([[4, 4, 2, 1]], [4, 3]),
            ([[2, 2]], [2, 1]),
        ],
    )
