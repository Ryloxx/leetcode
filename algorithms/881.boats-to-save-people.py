#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#
# https://leetcode.com/problems/boats-to-save-people/description/
#
# algorithms
# Medium (52.79%)
# Likes:    4963
# Dislikes: 117
# Total Accepted:    224.8K
# Total Submissions: 407K
# Testcase Example:  '[1,2]\n3'
#
# You are given an array people where people[i] is the weight of the i^th
# person, and an infinite number of boats where each boat can carry a maximum
# weight of limit. Each boat carries at most two people at the same time,
# provided the sum of the weight of those people is at most limit.
#
# Return the minimum number of boats to carry every given person.
#
#
# Example 1:
#
#
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
#
#
# Example 2:
#
#
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
#
#
# Example 3:
#
#
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
#
#
#
# Constraints:
#
#
# 1 <= people.length <= 5 * 10^4
# 1 <= people[i] <= limit <= 3 * 10^4
#
#
#
from types import MethodType
from typing import List

from algo_input import run


# @lc code=start
class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        lo, hi = 0, n - 1
        people.sort()
        while lo < hi:
            while lo < hi and people[hi] + people[lo] > limit:
                hi -= 1
            lo += lo < hi
            hi -= 1
        return n - lo


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numRescueBoats, Solution()),
        [
            ([[1, 2], 3], 1),
            ([[3, 2, 2, 1], 3], 3),
            ([[3, 5, 3, 4], 5], 4),
            ([[], 5], 0),
            ([[1], 5], 1),
            ([[5], 5], 1),
            ([[5, 5], 5], 2),
            ([[2, 2], 5], 1),
            ([[1, 2, 3, 4, 5], 5], 3),
            ([[2, 4], 5], 2),
            ([[2, 2, 2, 3, 3, 3], 5], 3),
            ([[3, 2, 3, 2, 2], 6], 3),
        ],
    )
