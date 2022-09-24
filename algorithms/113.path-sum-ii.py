#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (54.14%)
# Likes:    5553
# Dislikes: 121
# Total Accepted:    638.1K
# Total Submissions: 1.2M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given the root of a binary tree and an integer targetSum, return all
# root-to-leaf paths where the sum of the node values in the path equals
# targetSum. Each path should be returned as a list of the node values, not
# node references.
#
# A root-to-leaf path is a path starting from the root and ending at any leaf
# node. A leaf is a node with no children.
#
#
# Example 1:
#
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
#
#
# Example 2:
#
#
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
#
# Example 3:
#
#
# Input: root = [1,2], targetSum = 0
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
#
#
#
from typing import List, Optional
from algo_input import run, TreeNode, any_order
from types import MethodType


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: Optional[TreeNode],
                targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, s, path):
            if not node:
                return
            s += node.val
            path.append(node.val)
            if not node.left and not node.right and s == targetSum:
                res.append(path[:])
            dfs(node.left, s, path)
            dfs(node.right, s, path)
            path.pop()

        dfs(root, 0, [])
        return res


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.pathSum, Solution()), [
        [[
            TreeNode.create_tree(
                [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22
        ], [[5, 4, 11, 2], [5, 8, 4, 5]]],
        [[TreeNode.create_tree([1, 2, 3]), 5], []],
        [[TreeNode.create_tree([1, 2]), 0], []],
        [[TreeNode.create_tree([0, 0]), 0], [[0, 0]]],
        [[TreeNode.create_tree([0]), 0], [[0]]],
        [[TreeNode.create_tree([]), 100], []],
    ],
        comparator=any_order)
