#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (38.38%)
# Likes:    13174
# Dislikes: 546
# Total Accepted:    1.7M
# Total Submissions: 4.3M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, remove the n^th node from the end of the
# list and return its head.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
# Example 2:
#
#
# Input: head = [1], n = 1
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
#
# Follow up: Could you do this in one pass?
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

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        res = ListNode()
        res.next = head
        h1 = h2 = res
        while h1 and h1.next:
            h1 = h1.next
            if n:
                n -= 1
            else:
                h2 = h2.next
        h2.next.next, h2.next = None, h2.next.next
        return res.next


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.removeNthFromEnd, Solution()), [
        [[ListNode.create_list([1, 2, 3, 4, 5]), 2],
         ListNode.create_list([1, 2, 3, 5])],
        [[ListNode.create_list([1, 2]), 1],
         ListNode.create_list([1])],
        [[ListNode.create_list([1]), 1],
         ListNode.create_list([])],
        [[ListNode.create_list([1, 2, 3, 4, 5]), 5],
         ListNode.create_list([2, 3, 4, 5])],
        [[ListNode.create_list([1, 2, 3, 4, 5]), 1],
         ListNode.create_list([1, 2, 3, 4])],
    ],
        comparator=ListNode.are_equal)
