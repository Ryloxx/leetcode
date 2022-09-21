#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#
# https://leetcode.com/problems/spiral-matrix-iii/description/
#
# algorithms
# Medium (72.46%)
# Likes:    616
# Dislikes: 653
# Total Accepted:    37.5K
# Total Submissions: 51.4K
# Testcase Example:  '1\n4\n0\n0'
#
# You start at the cell (rStart, cStart) of an rows x cols grid facing east.
# The northwest corner is at the first row and column in the grid, and the
# southeast corner is at the last row and column.
#
# You will walk in a clockwise spiral shape to visit every position in this
# grid. Whenever you move outside the grid's boundary, we continue our walk
# outside the grid (but may return to the grid boundary later.). Eventually, we
# reach all rows * cols spaces of the grid.
#
# Return an array of coordinates representing the positions of the grid in the
# order you visited them.
#
#
# Example 1:
#
#
# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
#
#
# Example 2:
#
#
# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output:
# [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5]
# ,[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4]
# ,[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0]
# ,[2,0],[1,0],[0,0]]
#
#
#
# Constraints:
#
#
# 1 <= rows, cols <= 100
# 0 <= rStart < rows
# 0 <= cStart < cols
#
#
#
from itertools import cycle
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int,
                        cStart: int) -> List[List[int]]:
        directions, res, limit, p, step = (cycle([[0, 1], [1, 0], [0, -1],
                                                  [-1, 0]]), [[rStart,
                                                               cStart]],
                                           rows * cols - 1, 0, 1)
        while limit > 0:
            dy, dx = next(directions)
            for _ in range(step):
                rStart += dy
                cStart += dx
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
                    limit -= 1
            p += 1
            if not p % 2:
                step += 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.spiralMatrixIII, Solution()),
        [
            [[1, 4, 0, 0], [[0, 0], [0, 1], [0, 2], [0, 3]]],
            [[5, 6, 1, 4],
             [[1, 4], [1, 5], [2, 5], [2, 4], [2, 3], [1, 3], [0, 3], [0, 4],
              [0, 5], [3, 5], [3, 4], [3, 3], [3, 2], [2, 2], [1, 2], [0, 2],
              [4, 5], [4, 4], [4, 3], [4, 2], [4, 1], [3, 1], [2, 1], [1, 1],
              [0, 1], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]],
        ],
    )
