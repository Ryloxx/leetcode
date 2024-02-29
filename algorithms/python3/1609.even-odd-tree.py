#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#
# https://leetcode.com/problems/even-odd-tree/description/
#
# algorithms
# Medium (55.90%)
# Likes:    1420
# Dislikes: 70
# Total Accepted:    83K
# Total Submissions: 136.5K
# Testcase Example:  '[1,10,4,3,null,7,9,12,8,6,null,null,2]'
#
# A binary tree is named Even-Odd if it meets the following conditions:
#
#
# The root of the binary tree is at level index 0, its children are at level
# index 1, their children are at level index 2, etc.
# For every even-indexed level, all nodes at the level have odd integer values
# in strictly increasing order (from left to right).
# For every odd-indexed level, all nodes at the level have even integer values
# in strictly decreasing order (from left to right).
#
#
# Given the root of a binary tree, return true if the binary tree is Even-Odd,
# otherwise return false.
#
#
# Example 1:
#
#
# Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
# Output: true
# Explanation: The node values on each level are:
# Level 0: [1]
# Level 1: [10,4]
# Level 2: [3,7,9]
# Level 3: [12,8,6,2]
# Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all
# even and decreasing, the tree is Even-Odd.
#
#
# Example 2:
#
#
# Input: root = [5,4,2,3,3,7]
# Output: false
# Explanation: The node values on each level are:
# Level 0: [5]
# Level 1: [4,2]
# Level 2: [3,3,7]
# Node values in level 2 must be in strictly increasing order, so the tree is
# not Even-Odd.
#
#
# Example 3:
#
#
# Input: root = [5,9,1,3,5,7]
# Output: false
# Explanation: Node values in the level 1 should be even integers.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^5].
# 1 <= Node.val <= 10^6
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
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q1 = [root]
        q2 = []
        preds = (
            lambda node, prev: (node.val % 2 != 0 or prev.val <= node.val),
            lambda node, prev: (node.val % 2 != 1 or prev.val >= node.val),
        )
        level = 0
        while q1:
            prev = TreeNode(1000001 * level)
            for node in q1:
                if node is None:
                    continue
                if preds[level % 2 == 0](node, prev):
                    return False
                prev = node
                q2.append(node.left)
                q2.append(node.right)
            q1, q2 = q2, q1
            q2.clear()
            level = not level
        return True


# @lc code=end


if __name__ == "__main__":
    run(
        MethodType(Solution.isEvenOddTree, Solution()),
        [
            [
                [
                    (
                        TreeNode.create_tree(
                            [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]
                        )
                    )
                ],
                True,
            ],
            [[(TreeNode.create_tree([5, 4, 2, 3, 3, 7]))], False],
            [[(TreeNode.create_tree([5, 9, 1, 3, 5, 7]))], False],
            [[(TreeNode.create_tree([]))], True],
            [[(TreeNode.create_tree([3, 1000000]))], True],
        ],
    )
