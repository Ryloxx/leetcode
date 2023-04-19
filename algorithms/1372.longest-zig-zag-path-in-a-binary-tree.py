#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
#
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
#
# algorithms
# Medium (59.90%)
# Likes:    1525
# Dislikes: 26
# Total Accepted:    47.3K
# Total Submissions: 78.2K
# Testcase Example:
# '[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]'
#
# You are given the root of a binary tree.
#
# A ZigZag path for a binary tree is defined as follow:
#
#
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current
# node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
#
#
# Zigzag length is defined as the number of nodes visited - 1. (A single node
# has a length of 0).
#
# Return the longest ZigZag path contained in that tree.
#
#
# Example 1:
#
#
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
#
#
# Example 2:
#
#
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left ->
# right).
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: 0
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 5 * 10^4].
# 1 <= Node.val <= 100
#
#
#
from typing import Optional
from algo_input import run, TreeNode
from types import MethodType


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr, dir, path):
            nonlocal res
            if not curr:
                return 0
            res = max(path, res)
            dfs(curr.left, False,
                path + 1 if dir else 1), dfs(curr.right, True,
                                             path + 1 if not dir else 1)

        dfs(root, True, 0)
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestZigZag, Solution()),
        [
            ([
                TreeNode.create_tree([
                    1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None,
                    None, 1, None, 1
                ])
            ], 3),
            ([
                TreeNode.create_tree(
                    [1, 1, 1, None, 1, None, None, 1, 1, None, 1])
            ], 4),
            ([TreeNode.create_tree([1])], 0),
            ([
                TreeNode.create_tree([
                    6, 9, 7, 3, None, 2, 8, 5, 8, 9, 7, 3, 9, 9, 4, 2, 10,
                    None, 5, 4, 3, 10, 10, 9, 4, 1, 2, None, None, 6, 5, None,
                    None, None, None, 9, None, 9, 6, 5, None, 5, None, None, 7,
                    7, 4, None, 1, None, None, 3, 7, None, 9, None, None, None,
                    None, None, None, None, None, 9, 9, None, None, None, 7,
                    None, None, None, None, None, None, None, None, None, 6, 8,
                    7, None, None, None, 3, 10, None, None, None, None, None,
                    1, None, 1, 2
                ])
            ], 5),
        ],
    )
