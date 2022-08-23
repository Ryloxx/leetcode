#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (46.77%)
# Likes:    10722
# Dislikes: 626
# Total Accepted:    1.1M
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome.
#
#
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
#
#
#
# Follow up: Could you do it in O(n) time and O(1) space?
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

    def reverse(self, head: Optional[ListNode]):
        if not head:
            return
        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        return tail

    def length(self, head: Optional[ListNode]):
        if not head:
            return 0
        res = 0
        while head:
            res += 1
            head = head.next
        return res

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = (self.length(head)) // 2
        mid_head = head
        for _ in range(mid):
            mid_head = mid_head.next
        mid_head = self.reverse(mid_head)
        for _ in range(mid):
            if head.val != mid_head.val:
                return False
            head = head.next
            mid_head = mid_head.next
        return True


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isPalindrome, Solution()),
        [
            [[ListNode.createList([1, 2, 3, 4, 5, 4, 3, 2, 1])], True],
            [[ListNode.createList([1, 2, 3, 4, 4, 3, 2, 1])], True],
            [[ListNode.createList([1, 2, 2, 1])], True],
            [[ListNode.createList([1])], True],
            [[ListNode.createList([1, 1, 1, 1, 1, 1])], True],
            [[ListNode.createList([1, 1, 1, 1, 1, 1, 1])], True],
            [[ListNode.createList([1, 2])], False],
        ],
    )
