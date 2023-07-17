#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (59.56%)
# Likes:    4637
# Dislikes: 250
# Total Accepted:    379.3K
# Total Submissions: 633.5K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Example 1:
#
#
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
#
#
# Example 2:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
#
#
# Example 3:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
#
# Constraints:
#
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading
# zeros.
#
#
#
# Follow up: Could you solve it without reversing the input lists?
#
#
from itertools import zip_longest
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

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:

        def tail(head: Optional[ListNode]):
            if not head:
                return
            yield from tail(head.next)
            yield head.val

        prev = None
        carry = 0
        for a, b in zip_longest(tail(l1), tail(l2), fillvalue=0):
            s = a + b + carry  # type: ignore
            carry = s // 10
            node = ListNode(s % 10)
            node.next, prev = prev, node
        if carry:
            node = ListNode(carry)
            node.next, prev = prev, node
        return prev


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.addTwoNumbers, Solution()), [
        ([ListNode.create_list([7, 2, 4, 3]),
          ListNode.create_list([5, 6, 4])], ListNode.create_list([7, 8, 0, 7
                                                                  ])),
        ([ListNode.create_list([2, 4, 3]),
          ListNode.create_list([5, 6, 4])], ListNode.create_list([8, 0, 7])),
        ([ListNode.create_list([0]),
          ListNode.create_list([0])], ListNode.create_list([0])),
        ([ListNode.create_list([4, 9, 6]),
          ListNode.create_list([6, 1, 2])], ListNode.create_list([1, 1, 0, 8
                                                                  ])),
        ([ListNode.create_list([9]),
          ListNode.create_list([1])], ListNode.create_list([1, 0])),
        ([ListNode.create_list([]),
          ListNode.create_list([])], ListNode.create_list([])),
    ],
        comparator=ListNode.are_equal)
