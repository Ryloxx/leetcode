#
# @lc app=leetcode id=2385 lang=python3
#
# [2385] Amount of Time for Binary Tree to Be Infected
#
# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/
#
# algorithms
# Medium (58.65%)
# Likes:    2373
# Dislikes: 57
# Total Accepted:    109.2K
# Total Submissions: 171.2K
# Testcase Example:  '[1,5,3,null,4,10,6,9,2]\n3'
#
# You are given the root of a binary tree with unique values, and an integer
# start. At minute 0, an infection starts from the node with value start.
#
# Each minute, a node becomes infected if:
#
#
# The node is currently uninfected.
# The node is adjacent to an infected node.
#
#
# Return the number of minutes needed for the entire tree to be infected.
#
#
# Example 1:
#
#
# Input: root = [1,5,3,null,4,10,6,9,2], start = 3
# Output: 4
# Explanation: The following nodes are infected during:
# - Minute 0: Node 3
# - Minute 1: Nodes 1, 10 and 6
# - Minute 2: Node 5
# - Minute 3: Node 4
# - Minute 4: Nodes 9 and 2
# It takes 4 minutes for the whole tree to be infected so we return 4.
#
#
# Example 2:
#
#
# Input: root = [1], start = 1
# Output: 0
# Explanation: At minute 0, the only node in the tree is infected so we return
# 0.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^5].
# 1 <= Node.val <= 10^5
# Each node has a unique value.
# A node with a value of start exists in the tree.
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
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0

        parents = []
        start_node = None

        def fill_nodes(current: Optional[TreeNode], parent: Optional[int]):
            nonlocal parents, start_node
            if not current:
                return
            if current.val == start:
                start_node = current
            if len(parents) <= current.val:
                parents += [0] * (current.val - len(parents) + 1)
            parents[current.val] = parent
            fill_nodes(current.left, current)
            fill_nodes(current.right, current)

        def dfs(current: Optional[TreeNode], prev: Optional[TreeNode]):
            if not current:
                return 0
            length = 0
            for p in [current.left, current.right, parents[current.val]]:
                if p == prev:
                    continue
                length = max(length, dfs(p, current))
            return 1 + length

        fill_nodes(root, None)
        return dfs(start_node, None) - 1


# @lc code=end


if __name__ == "__main__":
    run(
        MethodType(Solution.amountOfTime, Solution()),
        [
            ((TreeNode.create_tree([1, 5, 3, None, 4, 10, 6, 9, 2]), 3), 4),
            ((TreeNode.create_tree([1]), 1), 0),
            ((TreeNode.create_tree([]), 0), 0),
        ],
    )
