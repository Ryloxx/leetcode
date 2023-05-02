#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (56.88%)
# Likes:    2723
# Dislikes: 377
# Total Accepted:    184.8K
# Total Submissions: 316K
# Testcase Example:  '[4,2,6,1,3]'
#
# Given the root of a Binary Search Tree (BST), return the minimum difference
# between the values of any two different nodes in the tree.
#
#
# Example 1:
#
#
# Input: root = [4,2,6,1,3]
# Output: 1
#
#
# Example 2:
#
#
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 100].
# 0 <= Node.val <= 10^5
#
#
#
# Note: This question is the same as 530:
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
#
#
from sys import maxsize
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

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = maxsize
        prev = -maxsize
        stack: List[TreeNode] = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res = min(res, node.val - prev)
            prev = node.val
            root = node.right
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minDiffInBST, Solution()),
        [
            ([TreeNode.create_tree([4, 2, 6, 1, 3])], 1),
            ([TreeNode.create_tree([1, 0, 48, None, None, 12, 49])], 1),
            ([TreeNode.create_tree([27, None, 34, None, 58, 50, None, 44])
              ], 6),
        ],
    )
