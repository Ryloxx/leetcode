#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (57.97%)
# Likes:    8074
# Dislikes: 476
# Total Accepted:    651.6K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given the root of a binary tree, flatten the tree into a "linked list":
#
#
# The "linked list" should use the same TreeNode class where the right child
# pointer points to the next node in the list and the left child pointer is
# always null.
# The "linked list" should be in the same order as a pre-order traversal of the
# binary tree.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
#
#
# Example 2:
#
#
# Input: root = []
# Output: []
#
#
# Example 3:
#
#
# Input: root = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Can you flatten the tree in-place (with O(1) extra space)?
#
from typing import Optional
from algo_input import run, TreeNode


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Iterative
    # O(N) time complexity
    # O(1) space complexity
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                right = root.left
                while right and right.right:
                    right = right.right
                right.right = root.right
                root.right = root.left
                root.left = None
            root = root.right

    # Recursive
    # O(N) time complexity
    # O(logN) space complexity
    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     if not root:
    #         return
    #     if not root.left and not root.right:
    #         return root
    #     left = self.flatten(root.left)
    #     right = self.flatten(root.right)
    #     if left:
    #         root.right, left.right, root.left = root.left, root.right, None
    #     return right or left


def process(root):
    Solution().flatten(root)
    return root


# @lc code=end
if __name__ == "__main__":
    run(process, [
        [[TreeNode.createTree([1, 2, 5, 3, 4, None, 6])],
         TreeNode.createTree([1, None, 2, None, 3, None, 4, None, 5, None, 6])
         ],
        [[TreeNode.createTree([1, 2, 4, 3, None, None, 5])],
         TreeNode.createTree([1, None, 2, None, 3, None, 4, None, 5])],
        [[TreeNode.createTree([])],
         TreeNode.createTree([])],
        [[TreeNode.createTree([0])],
         TreeNode.createTree([0])],
    ],
        comparator=lambda a, b: TreeNode.are_equal(a, b))
