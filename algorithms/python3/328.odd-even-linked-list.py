#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (59.58%)
# Likes:    7249
# Dislikes: 419
# Total Accepted:    649.5K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered
# list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should
# remain as it was in the input.
#
# You must solve the problem in O(1) extra space complexity and O(n) time
# complexity.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
#
#
# Example 2:
#
#
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]
#
#
#
# Constraints:
#
#
# The number of nodes in the linked list is in the range [0, 10^4].
# -10^6 <= Node.val <= 10^6
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

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = ListNode("dummy")
        mid = even
        odd = ListNode("dummy")
        n_head = odd
        cnt = 0
        while head:
            if not cnt % 2:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            cnt += 1
        odd.next = mid.next
        even.next = None
        return n_head.next


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.oddEvenList, Solution()), [
        ([ListNode.create_list([1, 2, 3, 4, 5])
          ], ListNode.create_list([1, 3, 5, 2, 4])),
        ([ListNode.create_list([2, 1, 3, 5, 6, 4, 7])
          ], ListNode.create_list([2, 3, 6, 7, 1, 5, 4])),
    ],
        comparator=ListNode.are_equal)
