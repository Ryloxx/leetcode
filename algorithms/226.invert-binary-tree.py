#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (73.50%)
# Likes:    11568
# Dislikes: 162
# Total Accepted:    1.5M
# Total Submissions: 2M
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Given the root of a binary tree, invert the tree, and return its root.
#
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
#
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
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

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(
            root.left)
        return root


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.invertTree, Solution()), [
        ([TreeNode.create_tree([4, 2, 7, 1, 3, 6, 9])
          ], TreeNode.create_tree([4, 7, 2, 9, 6, 3, 1])),
        ([TreeNode.create_tree([2, 1, 3])], TreeNode.create_tree([2, 3, 1])),
        ([TreeNode.create_tree([])], TreeNode.create_tree([])),
    ],
        comparator=TreeNode.are_equal)
