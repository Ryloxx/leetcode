#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (57.83%)
# Likes:    9199
# Dislikes: 254
# Total Accepted:    751.6K
# Total Submissions: 1.3M
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
#
#
# Example 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
#
# Example 2:
#
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
#
# Constraints:
#
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
#
#
#
from typing import List, Optional
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

    def buildTree(self, preorder: List[int],
                  inorder: List[int]) -> Optional[TreeNode]:
        idx, inorder_idxes = 0, {val: idx for idx, val in enumerate(inorder)}

        def dfs(left, right):
            nonlocal idx
            if left >= right:
                return None
            node = TreeNode(preorder[idx])
            mid = inorder_idxes[node.val]
            idx += 1
            node.left = dfs(left, mid)
            node.right = dfs(mid + 1, right)
            return node

        return dfs(0, len(inorder))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.buildTree, Solution()),
        [
            [[[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
             TreeNode.createTree([3, 9, 20, None, None, 15, 7])],
            [[[-1], [-1]], TreeNode.createTree([-1])],
        ],
    )
