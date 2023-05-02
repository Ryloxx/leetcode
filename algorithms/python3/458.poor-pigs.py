#
# @lc app=leetcode id=458 lang=python3
#
# [458] Poor Pigs
#
# https://leetcode.com/problems/poor-pigs/description/
#
# algorithms
# Hard (55.61%)
# Likes:    927
# Dislikes: 1904
# Total Accepted:    47K
# Total Submissions: 77K
# Testcase Example:  '1000\n15\n60'
#
# There are buckets buckets of liquid, where exactly one of the buckets is
# poisonous. To figure out which one is poisonous, you feed some number of
# (poor) pigs the liquid to see whether they will die or not. Unfortunately,
# you only have minutesToTest minutes to determine which bucket is poisonous.
#
# You can feed the pigs according to these steps:
#
#
# Choose some live pigs to feed.
# For each pig, choose which buckets to feed it. The pig will consume all the
# chosen buckets simultaneously and will take no time.
# Wait for minutesToDie minutes. You may not feed any other pigs during this
# time.
# After minutesToDie minutes have passed, any pigs that have been fed the
# poisonous bucket will die, and all others will survive.
# Repeat this process until you run out of time.
#
#
# Given buckets, minutesToDie, and minutesToTest, return the minimum number of
# pigs needed to figure out which bucket is poisonous within the allotted
# time.
#
#
# Example 1:
# Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
# Output: 5
# Example 2:
# Input: buckets = 4, minutesToDie = 15, minutesToTest = 15
# Output: 2
# Example 3:
# Input: buckets = 4, minutesToDie = 15, minutesToTest = 30
# Output: 2
#
#
# Constraints:
#
#
# 1 <= buckets <= 1000
# 1 <= minutesToDie <= minutesToTest <= 100
#
#
#
# from math import ceil, log2
from math import ceil, log
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # N = buckets

    # O(1) time complexity
    # O(1) space complexity
    def poorPigs(self, buckets: int, minutesToDie: int,
                 minutesToTest: int) -> int:
        return ceil(log(buckets, 1 + minutesToTest // minutesToDie))

    # O(loglogN) time complexity
    # O(1) space complexity
    # def poorPigs(self, buckets: int, minutesToDie: int,
    #              minutesToTest: int) -> int:
    #     retries = 1 + minutesToTest // minutesToDie
    #     lo, hi = 0, ceil(log2(buckets))
    #     while lo < hi:
    #         mid = (lo + hi) // 2
    #         if retries**mid >= buckets:
    #             hi = mid
    #         else:
    #             lo = mid + 1
    #     return lo


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.poorPigs, Solution()),
        [
            [[1000, 15, 60], 5],
            [[4, 15, 30], 2],
            [[4, 15, 15], 2],
            [[8, 15, 40], 2],
        ],
    )
