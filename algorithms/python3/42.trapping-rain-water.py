#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (56.65%)
# Likes:    22446
# Dislikes: 301
# Total Accepted:    1.3M
# Total Submissions: 2.2M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # Two Pointers
    # O(N) time complexity
    # O(1) space complexity
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        lm = rm = res = 0
        while i < j:
            hi, hj = height[i], height[j]
            if hi < hj:
                res += max(0, lm - hi)
                lm = max(lm, hi)
                i += 1
            else:
                res += max(0, rm - hj)
                rm = max(rm, hj)
                j -= 1
        return res

    # Monotonic stack
    # O(N) time complexity
    # O(N) space complexity
    # def trap(self, height: List[int]) -> int:
    #     stack = []
    #     res = m = 0
    #     for h in height:
    #         t = 1
    #         q = min(h, m)
    #         m = max(m, h)
    #         while stack and stack[-1][0] <= q:
    #             a, b = stack.pop()
    #             res += b * (q - a)
    #             t += b
    #         stack.append([h, t])
    #     return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.trap, Solution()),
        [
            [[[3, 2, 1, 0, 1, 2, 3]], 9],
            [[[3, 2, 1, 10, 1, 2, 3]], 6],
            [[[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], 6],
            [[[4, 2, 0, 3, 2, 5]], 9],
            [[[1, 1, 1, 1]], 0],
            [[[1, 2, 3, 4]], 0],
            [[[4, 3, 2, 1]], 0],
            [[[1, 1, 5, 1, 1]], 0],
            [[[1, 3, 5, 2, 1]], 0],
            [[[5, 4, 1, 2]], 1],
            [[[4, 2, 3]], 1],
            [[[5, 2, 1, 2, 1, 5]], 14],
            [[[4, 2, 0, 3, 2, 5]], 9],
            [[[2, 0, 2]], 2],
        ],
    )
