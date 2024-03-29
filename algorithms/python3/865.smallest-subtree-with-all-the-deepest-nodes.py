#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
#
# algorithms
# Medium (67.93%)
# Likes:    2063
# Dislikes: 331
# Total Accepted:    107.2K
# Total Submissions: 157.1K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]'
#
# Given the root of a binary tree, the depth of each node is the shortest
# distance to the root.
#
# Return the smallest subtree such that it contains all the deepest nodes in
# the original tree.
#
# A node is called the deepest if it has the largest depth possible among any
# node in the entire tree.
#
# The subtree of a node is a tree consisting of that node, plus the set of all
# descendants of that node.
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation: We return the node with value 2, colored in yellow in the
# diagram.
# The nodes coloured in blue are the deepest nodes of the tree.
# Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2
# is the smallest subtree among them, so we return it.
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [1]
# Explanation: The root is the deepest node in the tree.
#
#
# Example 3:
#
#
# Input: root = [0,1,3,null,2]
# Output: [2]
# Explanation: The deepest node in the tree is 2, the valid subtrees are the
# subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree will be in the range [1, 500].
# 0 <= Node.val <= 500
# The values of the nodes in the tree are unique.
#
#
#
# Note: This question is the same as 1123:
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
#
#
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

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        height = 0

        def dfs(node, current_height):
            nonlocal height
            if not node:
                return -float('inf'), None
            if not node.right and not node.left:
                height = max(height, current_height)
                return current_height, node
            left = dfs(node.left, current_height + 1)
            right = dfs(node.right, current_height + 1)
            if left[0] == right[0]:
                return left[0], node
            return max(left, right)

        return dfs(root, 0)[1]


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.subtreeWithAllDeepest, Solution()), [
        [[TreeNode.create_tree([0, 1, 3, None, 2])],
         TreeNode.create_tree([2])],
        [[TreeNode.create_tree([])],
         TreeNode.create_tree([])],
        [[TreeNode.create_tree([1])],
         TreeNode.create_tree([1])],
        [[TreeNode.create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])],
         TreeNode.create_tree([2, 7, 4])],
    ],
        comparator=lambda a, b: TreeNode.are_equal(a, b))
