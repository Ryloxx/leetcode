#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (37.74%)
# Likes:    12328
# Dislikes: 603
# Total Accepted:    874.7K
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,3]'
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass through
# the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty
# path.
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
# 6.
#
#
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7
# = 42.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000
#
#
#
from algo_input import run, TreeNode
from types import MethodType
from typing import Optional
from sys import maxsize


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -maxsize

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            p = max(left, right, 0) + node.val
            res = max(res, left + right + node.val, p)
            return p

        dfs(root)
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxPathSum, Solution()),
        [
            ([TreeNode.create_tree([1, 2, 3])], 6),
            ([TreeNode.create_tree([-10, 9, 20, None, None, 15, 7])], 42),
            ([TreeNode.create_tree([2, -1])], 2),
        ],
    )
