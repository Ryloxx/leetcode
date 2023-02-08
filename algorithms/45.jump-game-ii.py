#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (38.70%)
# Likes:    11062
# Dislikes: 383
# Total Accepted:    800.1K
# Total Submissions: 2M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i +
# j] where:
#
#
# 0 <= j <= nums[i] and
# i + j < n
#
#
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i = res = m = 0
        while m < n - 1:
            m, i = i + nums[i], max(range(m + 1, min(n, i + nums[i] + 1)),
                                    key=lambda x: x + nums[x])
            res += 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.jump, Solution()),
        [
            ([[7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]], 2),
            ([[2, 3, 1, 1, 4]], 2),
            ([[2, 3, 0, 1, 4]], 2),
            ([[3, 2, 1]], 1),
            ([[0]], 0),
        ],
    )
