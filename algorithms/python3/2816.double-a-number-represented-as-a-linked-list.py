#
# @lc app=leetcode id=2816 lang=python3
#
# [2816] Double a Number Represented as a Linked List
#
# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/
#
# algorithms
# Medium (49.77%)
# Likes:    541
# Dislikes: 10
# Total Accepted:    51.7K
# Total Submissions: 98.3K
# Testcase Example:  '[1,8,9]'
#
# You are given the head of a non-empty linked list representing a non-negative
# integer without leading zeroes.
#
# Return the head of the linked list after doubling it.
#
#
# Example 1:
#
#
# Input: head = [1,8,9]
# Output: [3,7,8]
# Explanation: The figure above corresponds to the given linked list which
# represents the number 189. Hence, the returned linked list represents the
# number 189 * 2 = 378.
#
#
# Example 2:
#
#
# Input: head = [9,9,9]
# Output: [1,9,9,8]
# Explanation: The figure above corresponds to the given linked list which
# represents the number 999. Hence, the returned linked list reprersents the
# number 999 * 2 = 1998.
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^4]
# 0 <= Node.val <= 9
# The input is generated such that the list represents a number that does not
# have leading zeros, except the number 0 itself.
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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(curr):
            if not curr:
                return 0
            val = curr.val * 2 + dfs(curr.next)
            curr.val = val % 10
            return val // 10

        if dfs(head):
            return ListNode(1, head)
        return head


# @lc code=end

if __name__ == "__main__":
    run(
        MethodType(Solution.doubleIt, Solution()),
        [
            ([ListNode.create_list([1, 8, 9])], ListNode.create_list([3, 7, 8])),
            ([ListNode.create_list([9, 9, 9])], ListNode.create_list([1, 9, 9, 8])),
            ([ListNode.create_list([0])], ListNode.create_list([0])),
        ],
        comparator=ListNode.are_equal,
    )
