#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (37.87%)
# Likes:    7792
# Dislikes: 359
# Total Accepted:    520.6K
# Total Submissions: 1.4M
# Testcase Example:
# '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n'
#  +
# '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
#
#
# Example 1:
#
#
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
#
#
#
from algo_input import run, any_order
from types import MethodType
from typing import List


# @lc code=start
class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def del_w(trie, w):
            node = (trie, 0)
            temp = trie
            w += "#"
            for i in range(len(w)):
                if len(temp) > 1:
                    node = (temp, i)
                temp = temp[w[i]]
            prev = None
            temp = node[0]
            for i in range(node[1], len(w)):
                prev = temp
                temp = temp[w[i]]
                del prev[w[i]]

        def f(curr, path, grid, i, j, trie):
            if "#" in curr:
                w = "".join(path)
                self.ans.append(w)
                del_w(trie, w)
            if not (0 <= i < len(board)
                    and 0 <= j < len(board[i])) or grid[i][j] not in curr:
                return
            t = grid[i][j]
            n = curr[t]
            grid[i][j] = "."
            path.append(t)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                f(n, path, grid, x, y, trie)
            path.pop()
            grid[i][j] = t

        if not words:
            return []
        self.ans = []
        trie = {}
        for w in words:
            curr = trie
            for c in w + "#":
                curr = curr.setdefault(c, {})
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie:
                    f(trie, [], board, i, j, trie)
        return self.ans


# @lc code=end

if __name__ == "__main__":
    run(MethodType(Solution.findWords, Solution()), [
        ([[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"],
           ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]
          ], ["eat", "oath"]),
        ([[["a", "b"], ["c", "d"]], ["abcb"]], []),
    ],
        comparator=any_order)
