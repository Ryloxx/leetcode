#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (38.69%)
# Likes:    19182
# Dislikes: 3873
# Total Accepted:    2.9M
# Total Submissions: 7.4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked
# list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
#
# Example 2:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
# Example 3:
#
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
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
        res = 0
        exp = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            res += (a + b) * 10**exp
            exp += 1

        def build(x, c=None):
            if not x:
                return ListNode(0) if c is None else None
            t = ListNode(x % 10)
            t.next = build(x // 10, t)
            return t

        return build(res)


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.addTwoNumbers, Solution()), [
        [[ListNode.create_list([2, 4, 3]),
          ListNode.create_list([5, 6, 4])],
         ListNode.create_list([7, 0, 8])],
        [[ListNode.create_list([0]),
          ListNode.create_list([0])],
         ListNode.create_list([0])],
        [[
            ListNode.create_list([9, 9, 9, 9, 9, 9, 9]),
            ListNode.create_list([9, 9, 9, 9])
        ],
         ListNode.create_list([8, 9, 9, 9, 0, 0, 0, 1])],
    ],
        comparator=lambda a, b: ListNode.are_equal(a, b))
