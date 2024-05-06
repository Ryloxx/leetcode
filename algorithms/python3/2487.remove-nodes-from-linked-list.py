#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#
# https://leetcode.com/problems/remove-nodes-from-linked-list/description/
#
# algorithms
# Medium (65.79%)
# Likes:    1451
# Dislikes: 39
# Total Accepted:    73.5K
# Total Submissions: 108.1K
# Testcase Example:  '[5,2,13,3,8]'
#
# You are given the head of a linked list.
#
# Remove every node which has a node with a greater value anywhere to the right
# side of it.
#
# Return the head of the modified linked list.
#
#
# Example 1:
#
#
# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.
#
#
# Example 2:
#
#
# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.
#
#
#
# Constraints:
#
#
# The number of the nodes in the given list is in the range [1, 10^5].
# 1 <= Node.val <= 10^5
#
#
#

from typing import Optional
from algo_input import run, ListNode
from types import MethodType


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        node = self.removeNodes(head.next)
        if node and head.val < node.val:
            return node
        head.next = node
        return head


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.removeNodes, Solution()),
        [
            ([ListNode.create_list([5, 2, 13, 3, 8])], ListNode.create_list([13, 8])),
            ([ListNode.create_list([1, 1, 1, 1])], ListNode.create_list([1, 1, 1, 1])),
        ],
        comparator=ListNode.are_equal,
    )
