#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (50.11%)
# Likes:    9414
# Dislikes: 912
# Total Accepted:    982.7K
# Total Submissions: 1.9M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# Given the heads of two singly linked-lists headA and headB, return the node
# at which the two lists intersect. If the two linked lists have no
# intersection at all, return null.
#
# For example, the following two linked lists begin to intersect at node c1:
#
# The test cases are generated such that there are no cycles anywhere in the
# entire linked structure.
#
# Note that the linked lists must retain their original structure after the
# function returns.
#
# Custom Judge:
#
# The inputs to the judge are given as follows (your program is not given these
# inputs):
#
#
# intersectVal - The value of the node where the intersection occurs. This is 0
# if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head)
# to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head)
# to get to the intersected node.
#
#
# The judge will then create the linked structure based on these inputs and
# pass the two heads, headA and headB to your program. If you correctly return
# the intersected node, then your solution will be accepted.
#
#
# Example 1:
#
#
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA =
# 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as
# [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are
# 3 nodes before the intersected node in B.
#
#
# Example 2:
#
#
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3,
# skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0
# if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as
# [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node
# before the intersected node in B.
#
#
# Example 3:
#
#
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: No intersection
# Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it
# reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0,
# while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
#
#
#
# Constraints:
#
#
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 10^4
# 1 <= Node.val <= 10^5
# 0 <= skipA < m
# 0 <= skipB < n
# intersectVal is 0 if listA and listB do not intersect.
# intersectVal == listA[skipA] == listB[skipB] if listA and listB
# intersect.
#
#
#
# Follow up: Could you write a solution that runs in O(m + n) time and use only
# O(1) memory?
#
from typing import Optional


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def length(self, head: ListNode):
        res = 0
        while head:
            res += 1
            head = head.next
        return res

    def skip(self, head: ListNode, count: int):
        for i in range(count):
            if not head:
                break
            head = head.next
        return head

    # Two pass constant space version
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> Optional[ListNode]:
        la, lb = self.length(headA), self.length(headB)
        headA, headB = self.skip(headA, max(0, la - lb)), self.skip(
            headB, max(0, lb - la))
        while headA != headB and headA:
            headA = headA.next
            headB = headB.next
        return headA

    # One pass constant space version
    # def getIntersectionNode(self, headA: ListNode,
    #                         headB: ListNode) -> Optional[ListNode]:
    #     a, b = headA, headB
    #     while a != b:
    #         a = headB if a is None else a.next
    #         b = headA if b is None else b.next
    #     return a

    # O(m + n) space version
    # def getIntersectionNode(self, headA: ListNode,
    #                         headB: ListNode) -> Optional[ListNode]:
    #     seen = set()
    #     while headA or headB:
    #         if headA and headA in seen:
    #             return headA
    #         seen.add(headA)
    #         if headB and headB in seen:
    #             return headB
    #         seen.add(headB)
    #         headA = headA.next if headA else headA
    #         headB = headB.next if headB else headB


# @lc code=end
