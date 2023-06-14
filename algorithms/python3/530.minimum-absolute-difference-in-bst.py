#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (56.80%)
# Likes:    3259
# Dislikes: 163
# Total Accepted:    234.8K
# Total Submissions: 404.6K
# Testcase Example:  '[4,2,6,1,3]'
#
# Given the root of a Binary Search Tree (BST), return the minimum absolute
# difference between the values of any two different nodes in the tree.
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
# The number of nodes in the tree is in the range [2, 10^4].
# 0 <= Node.val <= 10^5
#
#
#
# Note: This question is the same as 783:
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
#
#
from sys import maxsize
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

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        curr = -maxsize
        res = maxsize
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res = min(res, node.val - curr)
            curr = node.val
            root = node.right
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.getMinimumDifference, Solution()),
        [
            ([TreeNode.create_tree([4, 2, 6, 1, 3])], 1),
            ([TreeNode.create_tree([1, 0, 48, None, None, 12, 49])], 1),
            ([TreeNode.create_tree([236, 104, 701, None, 227, None, 911])], 9),
            ([TreeNode.create_tree([0, None, 2236, 1277, 2776, 519])], 519),
        ],
    )
