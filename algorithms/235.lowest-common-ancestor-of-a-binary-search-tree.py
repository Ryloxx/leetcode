#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#
# algorithms
# Easy (57.19%)
# Likes:    7400
# Dislikes: 221
# Total Accepted:    928.7K
# Total Submissions: 1.6M
# Testcase Example:  '[6,2,8,0,4,7,9,null,null,3,5]\n2\n8'
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node
# of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of
# itself).”
#
#
# Example 1:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
#
# Example 2:
#
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant
# of itself according to the LCA definition.
#
#
# Example 3:
#
#
# Input: root = [2,1], p = 2, q = 1
# Output: 2
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q will exist in the BST.
#
#
#
from algo_input import run, TreeNode
from types import MethodType
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if (left and right) or root.val == p.val or root.val == q.val:
            return root
        return left or right


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.lowestCommonAncestor, Solution()), [
        [[
            TreeNode.create_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
            TreeNode(2),
            TreeNode(8)
        ], 6],
        [[
            TreeNode.create_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
            TreeNode(2),
            TreeNode(4)
        ], 2],
        [[TreeNode.create_tree([2, 1]),
          TreeNode(2), TreeNode(1)], 2],
    ],
        comparator=lambda a, b:
        (a is None and b is None) or (a is not None and a.val == b))
