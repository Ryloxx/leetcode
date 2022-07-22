#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (47.99%)
# Likes:    3757
# Dislikes: 510
# Total Accepted:    356.8K
# Total Submissions: 733.1K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given the head of a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
#
# Example 1:
#
#
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
#
#
# Example 2:
#
#
# Input: head = [2,1], x = 2
# Output: [1,2]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200
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

    # O(N) time complexity
    # O(1) space complexity
    def partition(self, head: Optional[ListNode],
                  x: int) -> Optional[ListNode]:

        res = ListNode()
        res.next, head = head, res
        while head and head.next and head.next.val < x:
            head = head.next
        insert_point = head
        while head and head.next:
            if head.next.val < x:
                tail = head.next.next
                insert_point.next, head.next.next \
                    = head.next, insert_point.next
                head.next = tail
                insert_point = insert_point.next
            else:
                head = head.next
        return res.next


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.partition, Solution()), [
        [[ListNode.createList([1, 4, 3, 2, 5, 2]), 3],
         ListNode.createList([1, 2, 2, 4, 3, 5])],
        [[ListNode.createList([5, 4, 3, 2, 1]), 3],
         ListNode.createList([2, 1, 5, 4, 3])],
        [[ListNode.createList([3]), 3],
         ListNode.createList([3])],
        [[ListNode.createList([2]), 3],
         ListNode.createList([2])],
        [[ListNode.createList([4]), 3],
         ListNode.createList([4])],
        [[ListNode.createList([-5, -4, -3, -2, -1]), 3],
         ListNode.createList([-5, -4, -3, -2, -1])],
        [[ListNode.createList([-5, -4, -3, -2, -1]), -3],
         ListNode.createList([-5, -4, -3, -2, -1])],
        [[ListNode.createList([-1, -2, -3, -4, -5]), -3],
         ListNode.createList([-4, -5, -1, -2, -3])],
        [[ListNode.createList([-1, -2, -3, -4, -5]), 3],
         ListNode.createList([-1, -2, -3, -4, -5])],
    ],
        comparator=lambda a, b: ListNode.are_equal(a, b))
