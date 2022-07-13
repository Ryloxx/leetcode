#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (61.04%)
# Likes:    9113
# Dislikes: 176
# Total Accepted:    1.3M
# Total Submissions: 2.2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
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
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
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

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        traversal, res, left = [root], [], 0
        while left < len(traversal):
            res.append([])
            for idx in range(left, len(traversal)):
                node = traversal[idx]
                node.left and traversal.append(node.left)
                node.right and traversal.append(node.right)
                res[-1].append(node.val)
                left += 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.levelOrder, Solution()),
        [
            [[TreeNode.createTree([3, 9, 20, None, None, 15, 7])],
             [[3], [9, 20], [15, 7]]],
            [[TreeNode.createTree([])], []],
        ],
    )
