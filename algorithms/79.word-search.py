#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (39.72%)
# Likes:    11883
# Dislikes: 482
# Total Accepted:    1.2M
# Total Submissions: 2.9M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# \n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#
from algo_input import run
from types import MethodType
from typing import List
from itertools import product


# @lc code=start
class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        def dfs(i, y, x, mask):
            cell = 1 << (y * 6 + x)
            if mask & cell or board[y][x] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            mask |= cell
            return any(
                dfs(i + 1, ny, nx, mask) for d_y, d_x in directions
                for ny, nx in [[y + d_y, x + d_x]]
                if 0 <= ny < m and 0 <= nx < n)

        return any(dfs(0, y, x, 0) for y, x in product(range(m), range(n)))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.exist, Solution()),
        [
            ([[["A", "B", "C", "E"], ["S", "F", "C", "S"],
               ["A", "D", "E", "E"]], "ABCCED"], True),
            ([[["A", "B", "C", "E"], ["S", "F", "C", "S"],
               ["A", "D", "E", "E"]], "SEE"], True),
            ([[["A", "B", "C", "E"], ["S", "F", "C", "S"],
               ["A", "D", "E", "E"]], "ABCB"], False),
        ],
    )
