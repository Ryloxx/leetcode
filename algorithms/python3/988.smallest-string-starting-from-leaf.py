#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#
# https://leetcode.com/problems/smallest-string-starting-from-leaf/description/
#
# algorithms
# Medium (51.02%)
# Likes:    1956
# Dislikes: 278
# Total Accepted:    120.4K
# Total Submissions: 214.6K
# Testcase Example:  '[0,1,2,3,4,3,4]'
#
# You are given the root of a binary tree where each node has a value in the
# range [0, 25] representing the letters 'a' to 'z'.
#
# Return the lexicographically smallest string that starts at a leaf of this
# tree and ends at the root.
#
# As a reminder, any shorter prefix of a string is lexicographically
# smaller.
#
#
# For example, "ab" is lexicographically smaller than "aba".
#
#
# A leaf of a node is a node that has no children.
#
#
# Example 1:
#
#
# Input: root = [0,1,2,3,4,3,4]
# Output: "dba"
#
#
# Example 2:
#
#
# Input: root = [25,1,3,1,3,0,2]
# Output: "adz"
#
#
# Example 3:
#
#
# Input: root = [2,2,1,null,1,0,null,0]
# Output: "abc"
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 8500].
# 0 <= Node.val <= 25
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
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        best = ""

        def dfs(curr, path):
            nonlocal best
            if not curr:
                return
            path.append(curr.val)
            if not curr.left and not curr.right:
                s = "".join(chr(97 + c) for c in reversed(path))
                best = min(s, best) or s
            dfs(curr.left, path)
            dfs(curr.right, path)
            path.pop()

        dfs(root, [])
        return best


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.smallestFromLeaf, Solution()),
        [
            [
                [TreeNode.create_tree([0, 1, 2, 3, 4, 3, 4])],
                "dba",
            ],
            [
                [TreeNode.create_tree([25, 1, 3, 1, 3, 0, 2])],
                "adz",
            ],
            [
                [TreeNode.create_tree([2, 2, 1, None, 1, 0, None, 0])],
                "abc",
            ],
            [
                [TreeNode.create_tree([0, None, 1])],
                "ba",
            ],
            [
                [TreeNode.create_tree([4, 0, 1, 1])],
                "bae",
            ],
            [
                [
                    TreeNode.create_tree(
                        [
                            ##
                            25,
                            1,
                            None,
                            0,
                            0,
                            1,
                            None,
                            None,
                            None,
                            0,
                        ]
                    )
                ],
                "ababz",
            ],
            [
                [TreeNode.create_tree([2, 0, 1, None, None, 0])],
                "abc",
            ],
            [
                [TreeNode.create_tree([5, 25])],
                "zf",
            ],
        ],
    )
