#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (43.48%)
# Likes:    6621
# Dislikes: 309
# Total Accepted:    504.8K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Given the head of a singly linked list and two integers left and right where
# left <= right, reverse the nodes of the list from position left to position
# right, and return the reversed list.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
#
# Example 2:
#
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
#
# Follow up: Could you do it in one pass?
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

    # One pass
    # O(N) time complexity
    # O(N) space complexity
    def reverseBetween(self, head: Optional[ListNode], left: int,
                       right: int) -> Optional[ListNode]:

        def reverse_list(node, pos):
            if not pos:
                return node, node.next
            head, tail = reverse_list(node.next, pos - 1)
            node.next.next = node
            node.next = tail
            return head, tail

        if left == 1:
            return reverse_list(head, right - 1)[0]
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.reverseBetween, Solution()), [
        [[ListNode.create_list([1, 2, 3, 4, 5]), 2, 4],
         ListNode.create_list([1, 4, 3, 2, 5])],
        [[ListNode.create_list([5]), 1, 1],
         ListNode.create_list([5])],
        [[ListNode.create_list([1, 2, 1]), 2, 2],
         ListNode.create_list([1, 2, 1])],
        [[ListNode.create_list([1, 2, 2, 2, 1]), 2, 4],
         ListNode.create_list([1, 2, 2, 2, 1])],
        [[ListNode.create_list([1, 2, 3, 4]), 4, 4],
         ListNode.create_list([1, 2, 3, 4])],
        [[ListNode.create_list([1, 2, 3, 4]), 3, 4],
         ListNode.create_list([1, 2, 4, 3])],
        [[ListNode.create_list([1, 2, 3, 4]), 1, 1],
         ListNode.create_list([1, 2, 3, 4])],
        [[ListNode.create_list([1, 2, 3, 4]), 1, 2],
         ListNode.create_list([2, 1, 3, 4])],
        [[ListNode.create_list([1, 2, 3, 4]), 1, 4],
         ListNode.create_list([4, 3, 2, 1])],
    ],
        comparator=lambda a, b: ListNode.are_equal(a, b))
