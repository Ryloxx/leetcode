#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (47.05%)
# Likes:    7859
# Dislikes: 432
# Total Accepted:    932.3K
# Total Submissions: 2M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#
# Example 1:
#
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#
# Example 2:
#
#
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
#
#
#
# Constraints:
#
#
# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
#
#
#
from bisect import bisect_left
from sys import maxsize
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res, seen = maxsize, set()
        nums.sort()
        for idx in range(len(nums) - 2):
            k, lo, hi = nums[idx], idx + 1, len(nums) - 1
            if k in seen:
                continue
            seen.add(k)
            while lo < hi:
                c_sum = nums[lo] + nums[hi] + k
                res = min(res, c_sum, key=lambda x: abs(target - x))
                diff = target - c_sum
                if diff <= 0:
                    if hi == lo + 1:
                        break
                    hi = bisect_left(nums, target - k - nums[lo], lo + 1,
                                     hi - 1)
                else:
                    lo = bisect_left(nums, target - k - nums[hi], lo + 1,
                                     hi - 1)
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.threeSumClosest, Solution()),
        [
            ([[-1, 2, 1, -4], 1], 2),
            ([[0, 0, 0], 1], 0),
            ([[1, 1, 1, 0], -100], 2),
            ([[
                321, 413, 82, 812, -646, -858, 729, 609, -339, 483, -323, -399,
                -82, -455, 18, 661, 890, -328, -311, 520, -865, -174, 55, 685,
                -636, 462, -172, -696, -296, -832, 766, -808, -763, 853, 482,
                411, 703, 655, -793, -121, -726, 105, -966, -471, 612, 551,
                -257, 836, -94, -213, 511, 317, -293, 279, -571, 242, -519,
                386, -670, -806, -612, -433, -481, 794, 712, 378, -325, -564,
                477, 169, 601, 971, -300, -431, -152, 285, -899, 978, -419,
                708, 536, -816, -335, 284, 384, -922, -941, 633, 934, 497,
                -351, 62, 392, -493, -44, -400, 646, -912, -864, 835, 713, -12,
                322, -228, 340, -42, -307, -580, -802, -914, -142, 575, -684,
                -415, 718, -579, 759, 579, 732, -645, 525, 114, -880, -603,
                -699, -101, -738, -887, 327, 192, 747, -614, 393, 97, -569,
                160, 782, -69, 235, -598, -116, 928, -805, -76, -521, 671, 417,
                600, -442, 236, 831, 637, -562, 613, -705, -158, -237, -299,
                808, -734, 364, 919, 251, -163, -343, 899
            ], 2218], 2218),
            ([[
                13, 252, -87, -431, -148, 387, -290, 572, -311, -721, 222, 673,
                538, 919, 483, -128, -518, 7, -36, -840, 233, -184, -541, 522,
                -162, 127, -935, -397, 761, 903, -217, 543, 906, -503, -826,
                -342, 599, -726, 960, -235, 436, -91, -511, -793, -658, -143,
                -524, -609, -728, -734, 273, -19, -10, 630, -294, -453, 149,
                -581, -405, 984, 154, -968, 623, -631, 384, -825, 308, 779, -7,
                617, 221, 394, 151, -282, 472, 332, -5, -509, 611, -116, 113,
                672, -497, -182, 307, -592, 925, 766, -62, 237, -8, 789, 318,
                -314, -792, -632, -781, 375, 939, -304, -149, 544, -742, 663,
                484, 802, 616, 501, -269, -458, -763, -950, -390, -816, 683,
                -219, 381, 478, -129, 602, -931, 128, 502, 508, -565, -243,
                -695, -943, -987, -692, 346, -13, -225, -740, -441, -112, 658,
                855, -531, 542, 839, 795, -664, 404, -844, -164, -709, 167,
                953, -941, -848, 211, -75, 792, -208, 569, -647, -714, -76,
                -603, -852, -665, -897, -627, 123, -177, -35, -519, -241, -711,
                -74, 420, -2, -101, 715, 708, 256, -307, 466, -602, -636, 990,
                857, 70, 590, -4, 610, -151, 196, -981, 385, -689, -617, 827,
                360, -959, -289, 620, 933, -522, 597, -667, -882, 524, 181,
                -854, 275, -600, 453, -942, 134
            ], -2805], -2805),
            ([[
                -491, 746, 85, -957, -421, 996, 513, -846, 967, 464, 885, 275,
                5, -598, -574, -633, -726, -855, -552, 545, 245, -272, -523,
                796, 156, -423, -935, -414, -541, -915, -889, -19, -164, -474,
                -663, -329, -551, -143, -938, 560, 649, -410, -649, 981, 247,
                598, -216, -179, -655, -55, 861, 196, -563, -972, -665, 333,
                679, -687, 814, -921, -503, -223, 898, -477, -561, -576, 847,
                890, 570, -573, 291, -586, -929, 251, -864, 298, 787, 437, 465,
                97, -964, 825, -355, -462, 773, 101, 269, -325, -29, -138, 694,
                153, -700, 91, -271, 249, -527, -988, -499, -907, 154, 347,
                616, -995, 274, 521, -807, 983, -255, -763, -587, 705, 518,
                -349, -384, -221, 654, 31, -515, -356, 157, -134, -530, 668,
                -317, -64, 839, -472, -647, 784, -553, -295, 49, 315, -934,
                715, -268, -380, 867, 316, 364, 0, -955, 515, 863, 894, -664,
                113, -209, -238, 524, 769, 41, -803, 501, -721, -795, -494,
                759, 376, -816, -658, 632, 697, 749, 488, -969, 500, 772, 211,
                371, 430, -492, -292, -51, -794, 78, -352, -711, 754, 178,
                -438, -311, -532, 340, -367, 7, -314, -811, 977, 47, 548, 342,
                879, 224, -141, -872, 46, 489, -660, -618, -284, -25, -24,
                -692, 934, -274, -729, 596, -193, 51, 207, 270, -676, -680,
                906, -148, 25, -1, 392, -282, -388, 990, 314, 737, -98, 970,
                547, 923, -575, 805, 709, -69, -919, -366, -776, 433, 860, 785,
                -667, -35, 963, 391, -344, -170, 212, -710, -1000, -251, -186,
                622, -671, -924, -187, -580, 172, -537, 82, -639, 718, -188,
                536, 440, -568, -798, 382, -877, -17, -190, 972, 72, -998,
                -364, -868, -620, 20, -151, -785, -112, -822, 538, -237, -506,
                517, 933, 882, 325, 192, -823, 589, -567, 337, 592, -959, 125,
                866, -157, -115, -838, -828, -330, 187, -765, -994, -486, 422,
                -16, 938, 858, 456, 771, 776, -542, 126, -14, -783, -287, -842,
                550, -87, 751, -510, 899, 873, 666, -557, 175, -890, -740, 26,
                -599, -637, -849, -61, 604, 53, 260, 845, 514, -696, 36, 653,
                -927, -836, 833, -320, 611, 293, -443, -465, -471, 676, -259,
                944, -743, 778, -966, -535, -110, 854, -454, -312, -322, -225,
                665, 398, 374, 105, -207, 310, 788, 961, 400, 454, 552, -453,
                -131, -47, -286, -205, -240, 145, -685, 11, -375, -2, 455, 790,
                -211, -885, -146, -264, 37, 733, 642, 557, 711, -113, 562,
                -392, -38, 765, -875, -374, -239, 33, -772, 404, -451, -790,
                -96, 98, 965, -150, -114, 104, 641, -341, 872, -100, 979, -476,
                203, 742, 786, 618, 281, 634, 35, -43, 491, -933, 724, 73, 939,
                120, -595, -962, 959, 232, -89, -653, -460, 164, -832, 412,
                184, -104, -737, -60, 643, 716, -253, -159, 416, 180, -965,
                -65, -704, -180, 954, 285, -808, 74, -319, -307, 237, -15,
                -690, -953, 44, -298, 798, -871, 32, -732, -161, -495, -416,
                884, -74, 757, 920, 941, 227, -397, 168, 541, -850, -797, -385,
                280, 282, -215, -433, -309, 417, -723, 909, -834
            ], 5171], 2969),
        ],
    )
