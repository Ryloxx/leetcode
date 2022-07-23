#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (42.06%)
# Likes:    5995
# Dislikes: 171
# Total Accepted:    237.2K
# Total Submissions: 563.6K
# Testcase Example:  '[5,2,6,1]'
#
# You are given an integer array nums and you have to return a new counts
# array. The counts array has the property where counts[i] is the number of
# smaller elements to the right of nums[i].
#
#
# Example 1:
#
#
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#
#
# Example 2:
#
#
# Input: nums = [-1]
# Output: [0]
#
#
# Example 3:
#
#
# Input: nums = [-1,-1]
# Output: [0,0]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # N = len(nums)
    # O(NlogN) time complexity
    # O(N) space complexity
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = list(
            map({x: idx
                 for idx, x in enumerate(sorted(nums))}.get, nums))
        fenwick = [0] * (len(nums) + 1)

        def update(idx):
            idx += 1
            while idx < len(fenwick):
                fenwick[idx] += 1
                idx += idx & -idx

        def query(idx):
            res = 0
            idx += 1
            while idx > 0:
                res += fenwick[idx]
                idx -= idx & -idx
            return res

        res = []
        for i in reversed(nums):
            res.append(query(i - 1))
            update(i)

        return res[::-1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.countSmaller, Solution()),
        [
            [[[5, 2, 6, 1]], [2, 1, 1, 0]],
            [[[-1, -1]], [0, 0]],
            [[list(range(-(10**5 >> 1), 10**5 >> 1))], [0] * 10**5],
            [[[
                6918, -7883, 1372, 3128, -4599, -6184, 671, -8327, -1478, 5570,
                -3332, -8478, 8625, 5135, -4681, -2044, -5905, 5808, 1334,
                -4766, -5018, 1955, 6806, 1975, -7312, 6545, -1601, -5631,
                7278, 8232, -8855, 6175, -9041, -1481, -4795, 399, 8378, -8376,
                3412, -1420, -8409, 3398, -6192, -1654, -9147, -4208, 6499,
                -3771, -3451, -7011, -3211, 7134, 8544, -5242, -352, -740,
                4967, -6793, 9235, 6990, 4144, -1461, 482, -4938, -5879, 4714,
                -3390, 938, 6515, 4717, 9947, -7376, -7915, 115, -9195, -2694,
                234, 8161, 5113, 1416, 1034, -7012, 1172, -1394, 6566, 9781,
                -4585, 2467, 3986, -7878, 776, 9288, -3824, -279, -8702, -9004,
                -618, -6905, -8334, 1381
            ]],
             [
                 87, 12, 62, 67, 30, 20, 54, 10, 41, 71, 34, 6, 83, 68, 26, 34,
                 18, 65, 51, 24, 21, 51, 66, 51, 12, 62, 31, 18, 63, 64, 4, 56,
                 2, 28, 18, 36, 58, 5, 44, 27, 4, 41, 12, 23, 1, 15, 43, 16,
                 16, 8, 16, 42, 43, 11, 20, 18, 34, 9, 38, 36, 30, 15, 20, 10,
                 9, 26, 11, 18, 26, 24, 29, 6, 4, 13, 0, 8, 11, 20, 18, 15, 12,
                 4, 11, 7, 13, 14, 5, 10, 10, 3, 7, 8, 4, 5, 1, 0, 2, 1, 0, 0
             ]],
            [[[
                6056, -1560, 224, -5968, -7846, 7173, -5499, -7609, 7300,
                -6713, 8891, 3089, 5121, 2006, -8261, 4674, 1806, -3050, -434,
                237, 6178, -9038, 9266, -7302, 8409, 8710, -8895, 4728, 4709,
                7060, 4, 7399, 5176, -1869, 4617, 5511, 1277, 7513, 582, 5837,
                -9506, -9586, 9676, -3092, -6796, 6939, -6486, -5722, 9458,
                -3570, -1315, 7882
            ]],
             [
                 37, 18, 21, 11, 5, 36, 11, 5, 34, 7, 38, 21, 25, 20, 4, 20,
                 18, 10, 12, 13, 21, 2, 27, 3, 24, 24, 2, 14, 13, 17, 9, 16,
                 12, 7, 10, 10, 9, 11, 8, 8, 1, 0, 9, 4, 0, 4, 0, 0, 3, 0, 0, 0
             ]],
        ],
    )
