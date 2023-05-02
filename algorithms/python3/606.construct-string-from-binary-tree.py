#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#
# https://leetcode.com/problems/construct-string-from-binary-tree/description/
#
# algorithms
# Easy (57.75%)
# Likes:    1557
# Dislikes: 1970
# Total Accepted:    143K
# Total Submissions: 242.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given the root of a binary tree, construct a string consisting of parenthesis
# and integers from a binary tree with the preorder traversal way, and return
# it.
#
# Omit all the empty parenthesis pairs that do not affect the one-to-one
# mapping relationship between the string and the original binary tree.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to
# omit all the unnecessary empty parenthesis pairs. And it will be
# "1(2(4))(3)"
#
#
# Example 2:
#
#
# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except we cannot omit the
# first parenthesis pair to break the one-to-one mapping relationship between
# the input and the output.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -1000 <= Node.val <= 1000
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

    def tree2str(self, root: Optional[TreeNode]) -> str:

        return (("%s%s%s" %
                 (root.val, f"({self.tree2str(root.left)})"
                  if root.left or root.right else "",
                  f"({self.tree2str(root.right)})" if root.right else ""))
                if root else "")


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.tree2str, Solution()),
        [
            [[TreeNode.create_tree([])], ""],
            [[TreeNode.create_tree([1, 2, 3, 4])], "1(2(4))(3)"],
            [[TreeNode.create_tree([1, 2, 3, None, 4])], "1(2()(4))(3)"],
        ],
    )
