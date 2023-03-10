#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (55.41%)
# Likes:    5928
# Dislikes: 337
# Total Accepted:    458.4K
# Total Submissions: 796.1K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a complete binary tree, return the number of the nodes in
# the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely
# filled in a complete binary tree, and all nodes in the last level are as far
# left as possible. It can have between 1 and 2^h nodes inclusive at the last
# level h.
#
# Design an algorithm that runs in less than O(n) time complexity.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 6
#
#
# Example 2:
#
#
# Input: root = []
# Output: 0
#
#
# Example 3:
#
#
# Input: root = [1]
# Output: 1
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.
#
#
#
from algo_input import run, TreeNode
from types import MethodType
from typing import Optional


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = [root]
        for i in q:
            if i is not None:
                res += 1
                q.append(i.left)
                q.append(i.right)
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.countNodes, Solution()),
        [
            ([TreeNode.create_tree([1, 2, 3, 4, 5, 6])], 6),
            ([TreeNode.create_tree([])], 0),
            ([TreeNode.create_tree([1])], 1),
        ],
    )
