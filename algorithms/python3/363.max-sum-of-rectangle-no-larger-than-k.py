#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (40.15%)
# Likes:    2671
# Dislikes: 132
# Total Accepted:    96.5K
# Total Submissions: 229.2K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# Given an m x n matrix matrix and an integer k, return the max sum of a
# rectangle in the matrix such that its sum is no larger than k.
#
# It is guaranteed that there will be a rectangle with a sum no larger than
# k.
#
#
# Example 1:
#
#
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2
# Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2,
# and 2 is the max number no larger than k (k = 2).
#
#
# Example 2:
#
#
# Input: matrix = [[2,2,-1]], k = 3
# Output: 3
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -100 <= matrix[i][j] <= 100
# -10^5 <= k <= 10^5
#
#
#
# Follow up: What if the number of rows is much larger than the number of
# columns?
#
#
from typing import List
from algo_input import run
from types import MethodType

# @lc code=start
from sortedcontainers import SortedSet


class Solution:

    # O(min(M, N)**2 * max(M, N) * log(max(M, N))) time complexity
    # O(max(M, N)) space complexity
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = sorted([len(matrix), len(matrix[0])])
        res = -float('inf')
        for y1 in range(m):
            row = [0] * n
            for y2 in range(y1, -1, -1):
                max_sub_sum, curr_sub_sum = -float('inf'), 0
                for x in range(n):
                    row[x] += matrix[y2][x] if len(matrix) < len(
                        matrix[0]) else matrix[x][y2]
                    curr_sub_sum = max(curr_sub_sum + row[x], row[x])
                    max_sub_sum = max(curr_sub_sum, max_sub_sum)
                if max_sub_sum <= k:
                    res = max(res, max_sub_sum)
                    pass
                else:
                    current_sum = 0
                    previous_sums = SortedSet([0])
                    for x in range(n):
                        current_sum += row[x]
                        idx = min(
                            len(previous_sums) - 1,
                            previous_sums.bisect_left(current_sum - k))
                        maybe_good_sum = current_sum - previous_sums[idx]
                        if maybe_good_sum <= k:
                            res = max(res, maybe_good_sum)
                        previous_sums.add(current_sum)
                if res == k:
                    return res
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxSumSubmatrix, Solution()),
        [
            [[[[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 8], 8],
            [[[[1, 0, 1], [0, -2, 3]], 2], 2],
            [[[[2, 2, -1]], 3], 3],
            [[[[10, 3, 10]], 3], 3],
            [[[[10, 0, 10]], 3], 0],
            [[[[-100, -100, -100], [-100, -100, -100], [-100, -100, -100]], 3],
             -100],
            [[[[1] * 100 for _ in range(100)],
              float('inf')], 100 * 100],
        ],
    )
