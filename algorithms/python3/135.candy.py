#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (37.12%)
# Likes:    2972
# Dislikes: 260
# Total Accepted:    220.7K
# Total Submissions: 588.9K
# Testcase Example:  '[1,0,2]'
#
# There are n children standing in a line. Each child is assigned a rating
# value given in the integer array ratings.
#
# You are giving candies to these children subjected to the following
# requirements:
#
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
#
#
# Return the minimum number of candies you need to have to distribute the
# candies to the children.
#
#
# Example 1:
#
#
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1,
# 2 candies respectively.
#
#
# Example 2:
#
#
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2,
# 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two
# conditions.
#
#
#
# Constraints:
#
#
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
#
#
#
from operator import itemgetter
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # One pass
    # O(N) time complexity
    # O(1) space complexity
    def candy(self, ratings: List[int]) -> int:
        m = res = 0
        d = deltas = 1
        for prev, curr in (itemgetter(x - 1, x)(ratings)
                           for x in range(1, len(ratings))):
            res += deltas
            if curr > prev:
                deltas = m = deltas + 1
                d = 1
            elif curr == prev:
                deltas = m = d = 1
            else:
                if deltas == 1:
                    res += d - (d < m)
                deltas = 1
                d += 1
        return len(ratings) and res + deltas

    # Two pass
    # O(N) time complexity
    # O(N) space complexity
    # def candy(self, ratings: List[int]) -> int:
    #     ans = [1] * len(ratings)
    #     for i in range(len(ratings) - 1):
    #         if ratings[i] < ratings[i + 1]:
    #             ans[i + 1] = ans[i] + 1
    #     res = 0
    #     for i in range(len(ratings) - 1, 0, -1):
    #         if ratings[i] < ratings[i - 1]:
    #             ans[i - 1] = max(ans[i] + 1, ans[i - 1])
    #         res += ans[i - 1]
    #     return len(ans) and ans[-1] + res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.candy, Solution()),
        [
            [[[1, 2, 2]], 4],
            [[[1, 1, 1]], 3],
            [[[1, 5, 4, 3, 2, 1, 2, 3, 2, 3, 4, 5]], 31],
            [[[1, 0, 2]], 5],
            [[[]], 0],
            [[[0]], 1],
            [[[10000]], 1],
            [[[3, 3, 3]], 3],
            [[[3, 3, 3, 4]], 5],
            [[[3, 3, 3, 4, 4]], 6],
            [[[3, 3, 3, 2, 2]], 6],
            [[[3, 3, 3, 2, 2, 1]], 8],
            [[[0, 1, 0]], 4],
            [[[1, 0, 1]], 5],
            [[[1, 3, 2, 2, 1]], 7],
            [[[1, 2, 87, 87, 87, 2, 1]], 13],
            [[[1, 2, 3, 1, 0]], 9],
        ],
    )
