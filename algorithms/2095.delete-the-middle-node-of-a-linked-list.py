#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
#
# algorithms
# Medium (56.77%)
# Likes:    1758
# Dislikes: 34
# Total Accepted:    102.7K
# Total Submissions: 178.1K
# Testcase Example:  '[1,3,4,7,1,2,6]'
#
# You are given the head of a linked list. Delete the middle node, and return
# the head of the modified linked list.
#
# The middle node of a linked list of size n is the ⌊n / 2⌋^th node from the
# start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than
# or equal to x.
#
#
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2,
# respectively.
#
#
#
# Example 1:
#
#
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. The indices of the nodes
# are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.
#
#
# Example 3:
#
#
# Input: head = [2,1]
# Output: [2]
# Explanation:
# The above figure represents the given linked list.
# For n = 2, node 1 with value 1 is the middle node, which is marked in red.
# Node 0 with value 2 is the only node remaining after removing node 1.
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^5].
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

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            if slow.next:
                slow.val, slow.next = slow.next.val, slow.next.next
            elif head and head.next:
                head.next = None
            else:
                head = None
        return head


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.deleteMiddle, Solution()), [
        ([ListNode.create_list([1, 3, 4, 7, 1, 2, 6])
          ], ListNode.create_list([1, 3, 4, 1, 2, 6])),
        ([ListNode.create_list([1, 2, 3, 4])], ListNode.create_list([1, 2, 4
                                                                     ])),
        ([ListNode.create_list([2, 1])], ListNode.create_list([2])),
        ([ListNode.create_list([2])], ListNode.create_list([])),
    ],
        comparator=ListNode.are_equal)
