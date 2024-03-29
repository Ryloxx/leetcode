#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#
# https://leetcode.com/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (85.10%)
# Likes:    5441
# Dislikes: 347
# Total Accepted:    741.3K
# Total Submissions: 864K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range
# [low, high].
#
#
# Example 1:
#
#
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 =
# 32.
#
#
# Example 2:
#
#
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 =
# 23.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 2 * 10^4].
# 1 <= Node.val <= 10^5
# 1 <= low <= high <= 10^5
# All Node.val are unique.
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

    def rangeSumBST(self, root: Optional[TreeNode], low: int,
                    high: int) -> int:
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(
            root.right, low, high) + self.rangeSumBST(root.left, low, high)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.rangeSumBST, Solution()),
        [
            ([TreeNode.create_tree([10, 5, 15, 3, 7, None, 18]), 7, 15], 32),
            ([
                TreeNode.create_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6,
                10
            ], 23),
        ],
    )
