#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
#
# algorithms
# Medium (53.85%)
# Likes:    3001
# Dislikes: 36
# Total Accepted:    153.9K
# Total Submissions: 281.1K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a binary tree, determine if it is a complete binary tree.
#
# In a complete binary tree, every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level
# h.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values
# {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left
# as possible.
#
#
# Example 2:
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 1000
#
#
#
from typing import List, Optional, Tuple
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

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        res: List[Tuple[Optional[TreeNode], int]] = [(root, 1)]
        i = 0
        while i < len(res):
            n, d = res[i]
            if n:
                res.append((n.left, 2 * d))
                res.append((n.right, 2 * d + 1))
            i += 1
        return res[-1][1] == len(res)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isCompleteTree, Solution()),
        [
            ([TreeNode.create_tree([1, 2, 3, 4, 5, 6])], True),
            ([TreeNode.create_tree([1, 2, 3, 4, 5, None, 7])], False),
        ],
    )
