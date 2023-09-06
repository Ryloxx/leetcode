#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#
# https://leetcode.com/problems/split-linked-list-in-parts/description/
#
# algorithms
# Medium (57.59%)
# Likes:    3140
# Dislikes: 270
# Total Accepted:    145.9K
# Total Submissions: 239.9K
# Testcase Example:  '[1,2,3]\n5'
#
# Given the head of a singly linked list and an integer k, split the linked
# list into k consecutive linked list parts.
#
# The length of each part should be as equal as possible: no two parts should
# have a size differing by more than one. This may lead to some parts being
# null.
#
# The parts should be in the order of occurrence in the input list, and parts
# occurring earlier should always have a size greater than or equal to parts
# occurring later.
#
# Return an array of the k parts.
#
#
# Example 1:
#
#
# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a
# ListNode is [].
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most
# 1, and earlier parts are a larger size than the later parts.
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50
#
#
#
from typing import List, Optional
from algo_input import run, ListNode
from types import MethodType


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def splitListToParts(self, head: Optional[ListNode],
                         k: int) -> List[Optional[ListNode]]:
        n = 0
        cp_head = head
        while cp_head:
            cp_head = cp_head.next
            n += 1
        res = []
        t, over, r = n // k, n % k, 0
        current, prev = head, None
        for _ in range(n):
            if r == 0:
                r = t + (over > 0)
                over -= 1
                if prev:
                    prev.next = None
                res.append(current)
            prev = current
            current = current.next  # type: ignore
            r -= 1

        while len(res) < k:
            res.append(None)
        return res


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.splitListToParts, Solution()),
        [([
            ListNode.create_list([1, 2, 3]),
            5,
        ], [
            ListNode.create_list([1]),
            ListNode.create_list([2]),
            ListNode.create_list([3]),
            None,
            None,
        ]),
         ([
             ListNode.create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
             3,
         ], [
             ListNode.create_list([1, 2, 3, 4]),
             ListNode.create_list([5, 6, 7]),
             ListNode.create_list([8, 9, 10])
         ]),
         ([
             ListNode.create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
             3,
         ], [
             ListNode.create_list([1, 2, 3, 4]),
             ListNode.create_list([5, 6, 7, 8]),
             ListNode.create_list([9, 10, 11])
         ]),
         ([
             ListNode.create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
             3,
         ], [
             ListNode.create_list([1, 2, 3, 4]),
             ListNode.create_list([5, 6, 7, 8]),
             ListNode.create_list([9, 10, 11, 12])
         ]), ([
             ListNode.create_list([]),
             10,
         ], [None] * 10)],
        comparator=lambda x, y: len(x) == len(y) and all(
            ListNode.are_equal(a, b) for a, b in zip(x, y)))
