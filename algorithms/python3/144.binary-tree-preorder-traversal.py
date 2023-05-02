#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Easy (65.01%)
# Likes:    6043
# Dislikes: 158
# Total Accepted:    1.2M
# Total Submissions: 1.8M
# Testcase Example:  '[1,null,2,3]'
#
# Given the root of a binary tree, return the preorder traversal of its nodes'
# values.
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,2,3]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: [1]
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
# Follow up: Recursive solution is trivial, could you do it iteratively?
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

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def pre(node):
            if not node:
                return
            yield node.val
            yield from pre(node.left)
            yield from pre(node.right)

        return list(pre(root))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.preorderTraversal, Solution()),
        [
            ([TreeNode.create_tree([1, None, 2, 3])], [1, 2, 3]),
            ([TreeNode.create_tree([])], []),
            ([TreeNode.create_tree([1])], [1]),
            ([TreeNode.create_tree([3, 1, 2])], [3, 1, 2]),
        ],
    )
