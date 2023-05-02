#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#
# https://leetcode.com/problems/uncrossed-lines/description/
#
# algorithms
# Medium (58.00%)
# Likes:    1773
# Dislikes: 28
# Total Accepted:    71K
# Total Submissions: 121.6K
# Testcase Example:  '[1,4,2]\n[1,2,4]'
#
# You are given two integer arrays nums1 and nums2. We write the integers of
# nums1 and nums2 (in the order they are given) on two separate horizontal
# lines.
#
# We may draw connecting lines: a straight line connecting two numbers nums1[i]
# and nums2[j] such that:
#
#
# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal)
# line.
#
#
# Note that a connecting line cannot intersect even at the endpoints (i.e.,
# each number can only belong to one connecting line).
#
# Return the maximum number of connecting lines we can draw in this way.
#
#
# Example 1:
#
#
# Input: nums1 = [1,4,2], nums2 = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to
# nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
#
#
# Example 2:
#
#
# Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
# Output: 3
#
#
# Example 3:
#
#
# Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 500
# 1 <= nums1[i], nums2[j] <= 2000
#
#
#
from functools import cache
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(M * N) time complexity
    # O(M * N) space complexity
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def dp(i, j):
            return (0 if i >= len(nums1) or j >= len(nums2) else 1 +
                    dp(i + 1, j + 1) if nums1[i] == nums2[j] else max(
                        dp(i + 1, j), dp(i, j + 1)))

        return dp(0, 0)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxUncrossedLines, Solution()),
        [
            [[[1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]], 2],
            [[[1] * 500, [1] * 500], 500],
            [[[2, 1], [1, 2, 1, 3, 3, 2]], 2],
            [[[1, 2], [4, 1, 2, 4, 1, 1, 2]], 2],
            [[[3], [3, 3, 1]], 1],
            [[[3, 3], [3]], 1],
            [[[2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]], 3],
            [[[1, 4, 2], [1, 2, 4]], 2],
        ],
    )
