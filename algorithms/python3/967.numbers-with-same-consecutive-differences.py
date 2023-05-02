#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/description/
#
# algorithms
# Medium (47.37%)
# Likes:    882
# Dislikes: 131
# Total Accepted:    50.5K
# Total Submissions: 106.6K
# Testcase Example:  '3\n7'
#
# Return all non-negative integers of length n such that the absolute
# difference between every two consecutive digits is k.
#
# Note that every number in the answer must not have leading zeros. For
# example, 01 has one leading zero and is invalid.
#
# You may return the answer in any order.
#
#
# Example 1:
#
#
# Input: n = 3, k = 7
# Output: [181,292,707,818,929]
# Explanation: Note that 070 is not a valid number, because it has leading
# zeroes.
#
#
# Example 2:
#
#
# Input: n = 2, k = 1
# Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
#
#
#
# Constraints:
#
#
# 2 <= n <= 9
# 0 <= k <= 9
#
#
#
from typing import List
from algo_input import run, any_order
from types import MethodType


# @lc code=start
class Solution:

    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        m = 10**n

        def dfs(p):
            if p * 10 >= m:
                res.append(p)
                return
            c = p % 10
            for x in set([c + k, c - k]):
                if 0 <= x <= 9:
                    dfs(p * 10 + x)

        for x in range(1, 10):
            dfs(x)
        return res


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.numsSameConsecDiff, Solution()),
        [[[3, 7], [181, 292, 707, 818, 929]],
         [[2, 0], [11, 22, 33, 44, 55, 66, 77, 88, 99]],
         [[2, 1],
          [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]]
         ],
        comparator=any_order)
