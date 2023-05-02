#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (53.12%)
# Likes:    12422
# Dislikes: 281
# Total Accepted:    1.5M
# Total Submissions: 2.9M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Could you solve it both recursively and iteratively?
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

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, dir):
            if not node:
                yield None
                return
            left, right = node.left, node.right
            if dir:
                left, right = right, left
            yield from dfs(left, dir)
            yield from dfs(right, dir)
            yield node.val

        return all(x == y for x, y in zip(dfs(root, False), dfs(root, True)))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isSymmetric, Solution()),
        [
            ([TreeNode.create_tree([1, 2, 2, 3, 4, 4, 3])], True),
            ([TreeNode.create_tree([1, 2, 2, None, 3, None, 3])], False),
            ([
                TreeNode.create_tree(
                    [2, 3, 3, 4, 5, 5, 4, 6, None, 8, 9, 9, 8, None, 6])
            ], True),
            ([TreeNode.create_tree([1, 0])], False),
            ([
                TreeNode.create_tree([
                    4, 63, 63, 3, 64, 3, 64, 39, -45, -57, 84, -45, 39, -57, 84
                ])
            ], False),
            ([
                TreeNode.create_tree(
                    [9, 25, 25, None, -95, -95, None, -100, None, None, -15])
            ], False),
            ([TreeNode.create_tree([1, 2, 2, 2, None, 2])], False),
        ],
    )
