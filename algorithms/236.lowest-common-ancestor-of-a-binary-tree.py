#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (55.52%)
# Likes:    10863
# Dislikes: 287
# Total Accepted:    1.1M
# Total Submissions: 1.9M
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
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
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
#
# Example 2:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
#
#
# Example 3:
#
#
# Input: root = [1,2], p = 1, q = 2
# Output: 1
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
# p and q will exist in the tree.
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
            TreeNode.createTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
            TreeNode(5),
            TreeNode(1)
        ], 3],
        [[
            TreeNode.createTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
            TreeNode(5),
            TreeNode(4)
        ], 5],
        [[TreeNode.createTree([1, 2]),
          TreeNode(1), TreeNode(2)], 1],
    ],
        comparator=lambda a, b:
        (a is None and b is None) or (a is not None and a.val == b))
