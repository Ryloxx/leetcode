#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (53.52%)
# Likes:    12671
# Dislikes: 1282
# Total Accepted:    1.1M
# Total Submissions: 2M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or null.
#
# Construct a deep copy of the list. The deep copy should consist of exactly n
# brand new nodes, where each new node has its value set to the value of its
# corresponding original node. Both the next and random pointer of the new
# nodes should point to new nodes in the copied list such that the pointers in
# the original list and copied list represent the same list state. None of the
# pointers in the new list should point to nodes in the original list.
#
# For example, if there are two nodes X and Y in the original list, where
# X.random --> Y, then for the corresponding two nodes x and y in the copied
# list, x.random --> y.
#
# Return the head of the copied linked list.
#
# The linked list is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
#
#
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random
# pointer points to, or null if it does not point to any node.
#
#
# Your code will only be given the head of the original linked list.
#
#
# Example 1:
#
#
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# Example 2:
#
#
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
#
#
# Example 3:
#
#
#
#
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#
#
#
# Constraints:
#
#
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random is null or is pointing to some node in the linked list.
#
#
#
from typing import List, Optional
from algo_input import run


# @lc code=start
# Definition for a Node.
class Node:

    def __init__(self,
                 x: int,
                 next: Optional['Node'] = None,
                 random: Optional['Node'] = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lookup = {}
        dummy = Node(0)
        dest = dummy
        cp_dest = dest
        cp_head = head
        while cp_head:
            cp_dest.next = cp_dest = lookup[cp_head] = Node(cp_head.val)
            cp_head = cp_head.next
        cp_dest = dest.next
        cp_head = head

        while cp_head and cp_dest:
            if cp_head.random:
                cp_dest.random = lookup[cp_head.random]
            cp_head = cp_head.next
            cp_dest = cp_dest.next

        return dest.next


# @lc code=end
if __name__ == "__main__":

    def build_list(list: List[List[int | Optional[int]]]):
        dummy = Node(0)
        head = dummy
        a_list = []
        for val, _ in list:
            dummy.next = dummy = Node(val, None, None)  # type: ignore
            a_list.append(dummy)
        dummy = head.next
        for _, random in list:
            if dummy and random is not None:
                dummy.random = a_list[random]
                dummy = dummy.next
        return head.next

    def judge(list):
        return Solution().copyRandomList(build_list(list))

    def equal(list_a: Optional[None], list_b: Optional[None]) -> bool:
        while list_a and list_b:
            if list_a.val != list_b.val:
                return False
            if (list_a.random and
                    list_b.random) and list_a.random.val != list_b.random.val:
                return False
            list_a = list_a.next
            list_b = list_b.next
        return list_a is None and list_b is None

    run(judge,
        [([[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
           ], build_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])),
         ([[[3, None], [3, 0], [3, None]]
           ], build_list([[3, None], [3, 0], [3, None]])),
         ([[[1, 1], [2, 1]]], build_list([[1, 1], [2, 1]]))],
        comparator=lambda x, y: equal(x, y))
