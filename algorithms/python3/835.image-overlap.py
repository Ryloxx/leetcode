#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#
# https://leetcode.com/problems/image-overlap/description/
#
# algorithms
# Medium (61.23%)
# Likes:    618
# Dislikes: 197
# Total Accepted:    63.5K
# Total Submissions: 101.6K
# Testcase Example:  '[[1,1,0],[0,1,0],[0,1,0]]\n[[0,0,0],[0,1,1],[0,0,1]]'
#
# You are given two images, img1 and img2, represented as binary, square
# matrices of size n x n. A binary matrix has only 0s and 1s as values.
#
# We translate one image however we choose by sliding all the 1 bits left,
# right, up, and/or down any number of units. We then place it on top of the
# other image. We can then calculate the overlap by counting the number of
# positions that have a 1 in both images.
#
# Note also that a translation does not include any kind of rotation. Any 1
# bits that are translated outside of the matrix borders are erased.
#
# Return the largest possible overlap.
#
#
# Example 1:
#
#
# Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
# Output: 3
# Explanation: We translate img1 to right by 1 unit and down by 1 unit.
#
# The number of positions that have a 1 in both images is 3 (shown in red).
#
#
#
# Example 2:
#
#
# Input: img1 = [[1]], img2 = [[1]]
# Output: 1
#
#
# Example 3:
#
#
# Input: img1 = [[0]], img2 = [[0]]
# Output: 0
#
#
#
# Constraints:
#
#
# n == img1.length == img1[i].length
# n == img2.length == img2[i].length
# 1 <= n <= 30
# img1[i][j] is either 0 or 1.
# img2[i][j] is either 0 or 1.
#
#
#
from itertools import product
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def largestOverlap(self, img1: List[List[int]],
                       img2: List[List[int]]) -> int:
        m, n = len(img1), len(img1[0])
        c_1 = [(y, x) for y, x in product(range(m), range(n)) if img1[y][x]]
        res = 0
        for d_y, d_x in product(range(-m + 1, m), range(-n + 1, n)):
            # Skip if the overlap surface is lower than current max
            if res >= (m - abs(d_y)) * (n - abs(d_x)):
                continue
            res = max(
                res,
                sum(img2[y + d_y][x + d_x] for y, x in c_1
                    if 0 <= y + d_y < m and 0 <= x + d_x < n))
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.largestOverlap, Solution()),
        [
            ([[[1, 1, 0], [0, 1, 0], [0, 1, 0]],
              [[0, 0, 0], [0, 1, 1], [0, 0, 1]]], 3),
            ([[[1]], [[1]]], 1),
            ([[[0]], [[0]]], 0),
            ([[[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
              [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]]], 1),
        ],
    )
