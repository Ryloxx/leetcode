#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#
# https://leetcode.com/problems/binary-tree-pruning/description/
#
# algorithms
# Medium (70.95%)
# Likes:    3247
# Dislikes: 88
# Total Accepted:    178.1K
# Total Submissions: 248.1K
# Testcase Example:  '[1,null,0,0,1]'
#
# Given the root of a binary tree, return the same tree where every subtree (of
# the given tree) not containing a 1 has been removed.
#
# A subtree of a node node is node plus every node that is a descendant of
# node.
#
#
# Example 1:
#
#
# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# Explanation:
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
#
#
# Example 2:
#
#
# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
#
#
# Example 3:
#
#
# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 200].
# Node.val is either 0 or 1.
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

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.left or root.right or root.val:
            return root


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.pruneTree, Solution()), [
        [[TreeNode.create_tree([1, None, 0, 0, 1])],
         TreeNode.create_tree([1, None, 0, None, 1])],
        [[TreeNode.create_tree([1, 0, 1, 0, 0, 0, 1])],
         TreeNode.create_tree([1, None, 1, None, 1])],
        [[TreeNode.create_tree([1, 1, 0, 1, 1, 0, 1, 0])],
         TreeNode.create_tree([1, 1, 0, 1, 1, None, 1])],
    ],
        comparator=TreeNode.are_equal)
