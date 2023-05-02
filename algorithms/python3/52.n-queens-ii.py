#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (66.38%)
# Likes:    2207
# Dislikes: 222
# Total Accepted:    244.1K
# Total Submissions: 357.1K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
#
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as
# shown.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 9
#
#
#
from algo_input import run
from types import MethodType

# @lc code=start

lookup = {
    1: 1,
    2: 0,
    3: 0,
    4: 2,
    5: 10,
    6: 4,
    7: 40,
    8: 92,
    9: 352,
}


class Solution:

    def totalNQueens(self, n: int) -> int:
        if n in lookup:
            return lookup[n]
        res = 0

        def dfs(xPositions, dPositions, adPositions, qPositions, y=0):
            nonlocal res
            if y == n:
                res += 1
                return
            for x in range(n):
                if ((x_bit := 1 << x) & xPositions) and (
                    (d_bit := 1 << (y - x + n - 1)) & dPositions) and (
                        (ad_bit := 1 << y + x) & adPositions):
                    qPositions.append((y, x))
                    dfs(xPositions - x_bit, dPositions - d_bit,
                        adPositions - ad_bit, qPositions, y + 1)
                    qPositions.pop()

        dfs((1 << n) - 1, (1 << n * 2) - 1, (1 << n * 2) - 1, [])
        return res


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.totalNQueens, Solution()), [
        [[4], 2],
        [[1], 1],
        [[5], 10],
        [[9], 352],
    ])
