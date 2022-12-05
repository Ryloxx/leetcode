#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# https://leetcode.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (72.72%)
# Likes:    8079
# Dislikes: 220
# Total Accepted:    1.1M
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, return the middle node of the linked
# list.
#
# If there are two middle nodes, return the second middle node.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we
# return the second one.
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100
#
#
#
from algo_input import run, ListNode
from types import MethodType
from typing import Optional


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        length = 0
        while head:
            if length % 2:
                curr = curr.next  # type: ignore
            length += 1
            head = head.next
        return curr


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.middleNode, Solution()), [
        ([ListNode.create_list([1, 2, 3, 4, 5])
          ], ListNode.create_list([3, 4, 5])),
        ([ListNode.create_list([1, 2, 3, 4, 5, 6])
          ], ListNode.create_list([4, 5, 6])),
    ],
        comparator=ListNode.are_equal)
