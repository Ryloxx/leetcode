#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
#
# algorithms
# Hard (41.62%)
# Likes:    4436
# Dislikes: 3707
# Total Accepted:    259.5K
# Total Submissions: 607.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, calculate the vertical order traversal of
# the binary tree.
#
# For each node at position (row, col), its left and right children will be at
# positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of
# the tree is at (0, 0).
#
# The vertical order traversal of a binary tree is a list of top-to-bottom
# orderings for each column index starting from the leftmost column and ending
# on the rightmost column. There may be multiple nodes in the same row and same
# column. In such a case, sort these nodes by their values.
#
# Return the vertical order traversal of the binary tree.
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation:
# Column -1: Only node 9 is in this column.
# Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
# Column 1: Only node 20 is in this column.
# Column 2: Only node 7 is in this column.
#
# Example 2:
#
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# Column -2: Only node 4 is in this column.
# Column -1: Only node 2 is in this column.
# Column 0: Nodes 1, 5, and 6 are in this column.
# ⁠         1 is at the top, so it comes first.
# ⁠         5 and 6 are at the same position (2, 0), so we order them by their
# value, 5 before 6.
# Column 1: Only node 3 is in this column.
# Column 2: Only node 7 is in this column.
#
#
# Example 3:
#
#
# Input: root = [1,2,3,4,6,5,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation:
# This case is the exact same as example 2, but with nodes 5 and 6 swapped.
# Note that the solution remains the same since 5 and 6 are in the same
# location and should be ordered by their values.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 1000
#
#
#
from collections import defaultdict
from typing import List, Optional
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
    # O(N) time complexity
    # O(N) space complexity
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        grid = defaultdict(list)
        Mc, Mr, mc = -float('inf'), -float('inf'), float('inf')

        def dfs(node, row=0, col=0):
            nonlocal Mc, Mr, mc
            if not node:
                return
            grid[row, col].append(node.val)
            Mc, Mr, mc = max(Mc, col), max(Mr, row), min(col, mc)
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root)
        res = []
        for x in range(mc, Mc + 1):
            col = []
            for y in range(Mr + 1):
                node = grid[y, x]
                node.sort()
                col += node
            res.append(col)

        return res

    # O(NlogN) time complexity
    # O(N) space complexity
    # def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     nodes = []

    #     def dfs(node, row=0, col=0):
    #         if not node:
    #             return
    #         nodes.append((col, row, node.val))
    #         dfs(node.left, row + 1, col - 1)
    #         dfs(node.right, row + 1, col + 1)

    #     dfs(root)
    #     nodes.sort(reverse=True)
    #     res = []
    #     curr = []
    #     while nodes:
    #         x, _, val = nodes.pop()
    #         curr.append(val)
    #         if not nodes or nodes[-1][0] > x:
    #             res.append(curr)
    #             curr = []
    #     return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.verticalTraversal, Solution()),
        [
            [[TreeNode.createTree([3, 9, 20, None, None, 15, 7])],
             [[9], [3, 15], [20], [7]]],
            [[TreeNode.createTree([1, 2, 3, 4, 5, 6, 7])],
             [[4], [2], [1, 5, 6], [3], [7]]],
            [[TreeNode.createTree([1, 2, 3, 4, 6, 5, 7])],
             [[4], [2], [1, 5, 6], [3], [7]]],
            [[TreeNode.createTree([3, 1, 4, 0, 2, 2])],
             [[0], [1], [3, 2, 2], [4]]],
        ],
    )
