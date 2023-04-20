#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (40.65%)
# Likes:    6607
# Dislikes: 910
# Total Accepted:    252.8K
# Total Submissions: 615.6K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given the root of a binary tree, return the maximum width of the given tree.
#
# The maximum width of a tree is the maximum width among all levels.
#
# The width of one level is defined as the length between the end-nodes (the
# leftmost and rightmost non-null nodes), where the null nodes between the
# end-nodes that would be present in a complete binary tree extending down to
# that level are also counted into the length calculation.
#
# It is guaranteed that the answer will in the range of a 32-bit signed
# integer.
#
#
# Example 1:
#
#
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4
# (5,3,null,9).
#
#
# Example 2:
#
#
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7
# (6,null,null,null,null,null,7).
#
#
# Example 3:
#
#
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2
# (3,2).
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100
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

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level, res = [[root, 0]], 0
        while level:
            res = max(res, level[-1][1] - level[0][1] + 1)
            temp = []
            for node, idx in level:
                node.left and temp.append([node.left, idx * 2])
                node.right and temp.append([node.right, idx * 2 + 1])
            level = temp
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.widthOfBinaryTree, Solution()),
        [
            ([TreeNode.create_tree([1, 3, 2, 5, 3, None, 9])], 4),
            ([TreeNode.create_tree([1, 3, 2, 5, None, None, 9, 6, None, 7])
              ], 7),
            ([TreeNode.create_tree([1, 3, 2, 5])], 2),
            ([
                TreeNode.create_tree([
                    0, 0, 0, None, 0, 0, None, None, 0, 0, None, None, 0, 0,
                    None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None,
                    None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None,
                    0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0,
                    None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None,
                    None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None,
                    0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0,
                    None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None,
                    None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None,
                    0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0,
                    None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None,
                    None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None,
                    0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0,
                    None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None,
                    None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None,
                    0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0,
                    None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None,
                    None, 0, 0, None, None, 0, 0, None, None, 0, 0, None, None,
                    0, 0, None, None, 0, 0, None, None, 0, 0, None, None, 0, 0,
                    None, None, 0, 0, None, None, 0, 0, None, None, 0, 0, None,
                    None, 0, 0, None
                ])
            ], 2),
            ([TreeNode.create_tree([1])], 1),
            ([TreeNode.create_tree([])], 0),
            ([TreeNode.create_tree([1, 1])], 1),
        ],
    )
