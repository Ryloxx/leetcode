#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (56.59%)
# Likes:    8259
# Dislikes: 167
# Total Accepted:    1.4M
# Total Submissions: 2.4M
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given the roots of two binary trees p and q, write a function to check if
# they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.
#
#
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#
#
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
#
#
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4
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

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                yield None
                return
            yield node.val
            yield from dfs(node.left)
            yield from dfs(node.right)

        return all(x == y for x, y in zip(dfs(p), dfs(q)))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isSameTree, Solution()),
        [
            ([
                TreeNode.create_tree([1, 2, 3]),
                TreeNode.create_tree([1, 2, 3])
            ], True),
            ([
                TreeNode.create_tree([1, 2]),
                TreeNode.create_tree([1, None, 2])
            ], False),
            ([
                TreeNode.create_tree([1, 2, 1]),
                TreeNode.create_tree([1, 1, 2])
            ], False),
        ],
    )
