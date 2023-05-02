#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (57.52%)
# Likes:    6255
# Dislikes: 139
# Total Accepted:    443.6K
# Total Submissions: 751.4K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height-balanced binary search tree.
#
#
# Example 1:
#
#
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in head is in the range [0, 2 * 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#
from typing import Optional
from algo_input import run, TreeNode, ListNode
from types import MethodType


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        mid, tail = head, head.next.next
        while tail and tail.next:
            tail = tail.next.next
            mid = mid.next  # type: ignore
        root = mid.next  # type: ignore
        mid.next = None  # type: ignore
        node = TreeNode(root.val)  # type: ignore
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(root.next)  # type: ignore
        return node


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.sortedListToBST, Solution()), [
        ([ListNode.create_list([-10, -3, 0, 5, 9])
          ], TreeNode.create_tree([0, -3, 9, -10, None, 5])),
        ([ListNode.create_list([-10, -4, -3, 0, 5, 9])
          ], TreeNode.create_tree([0, -4, 9, -10, -3, 5])),
        ([ListNode.create_list([])], TreeNode.create_tree([])),
        ([ListNode.create_list([1])], TreeNode.create_tree([1])),
        ([ListNode.create_list([1, 2])], TreeNode.create_tree([2, 1])),
        ([ListNode.create_list([1, 2, 3])], TreeNode.create_tree([2, 1, 3])),
        ([ListNode.create_list([1, 2, 3, 4])
          ], TreeNode.create_tree([3, 2, 4, 1])),
    ],
        comparator=TreeNode.are_equal)
