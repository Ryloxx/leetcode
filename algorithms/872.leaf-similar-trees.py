#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (64.97%)
# Likes:    2776
# Dislikes: 63
# Total Accepted:    237.8K
# Total Submissions: 352.4K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' +
# '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree, from left to right order, the
# values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
#
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
#
#
# Example 1:
#
#
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =
# [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
#
# Example 2:
#
#
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
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
from itertools import zip_longest


class Solution:

    def leafSimilar(self, root1: Optional[TreeNode],
                    root2: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
                return
            yield from dfs(node.left)
            yield from dfs(node.right)

        return all(x == y for x, y in zip_longest(dfs(root1), dfs(root2)))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.leafSimilar, Solution()),
        [
            ([
                TreeNode.create_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]),
                TreeNode.create_tree([
                    3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9,
                    8
                ])
            ], True),
            ([
                TreeNode.create_tree([1, 2, 3]),
                TreeNode.create_tree([1, 3, 2])
            ], False),
        ],
    )
