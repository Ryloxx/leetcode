#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#
# https://leetcode.com/problems/linked-list-random-node/description/
#
# algorithms
# Medium (59.60%)
# Likes:    2201
# Dislikes: 517
# Total Accepted:    176.5K
# Total Submissions: 291.9K
# Testcase Example:  '["Solution","getRandom","getRandom","getRandom"
# ,"getRandom","getRandom"]\n' +
# '[[[1,2,3]],[],[],[],[],[]]'
#
# Given a singly linked list, return a random node's value from the linked
# list. Each node must have the same probability of being chosen.
#
# Implement the Solution class:
#
#
# Solution(ListNode head) Initializes the object with the head of the
# singly-linked list head.
# int getRandom() Chooses a node randomly from the list and returns its value.
# All the nodes of the list should be equally likely to be chosen.
#
#
#
# Example 1:
#
#
# Input
# ["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 3, 2, 2, 3]
#
# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.getRandom(); // return 1
# solution.getRandom(); // return 3
# solution.getRandom(); // return 2
# solution.getRandom(); // return 2
# solution.getRandom(); // return 3
# // getRandom() should return either 1, 2, or 3 randomly. Each element should
# have equal probability of returning.
#
#
#
# Constraints:
#
#
# The number of nodes in the linked list will be in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
# At most 10^4 calls will be made to getRandom.
#
#
#
# Follow up:
#
#
# What if the linked list is extremely large and its length is unknown to
# you?
# Could you solve this efficiently without using extra space?
#
#
#
from random import randint
from typing import Counter, Optional
from algo_input import run, ListNode


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = -1

    def getRandom(self) -> int:
        if self.length < 0:
            dummy = self.head
            while dummy:
                dummy = dummy.next
                self.length += 1
        if self.length < 0:
            return -1
        idx = randint(0, self.length)
        dummy = self.head
        while idx and dummy:
            idx -= 1
            dummy = dummy.next
        return dummy.val  # type: ignore


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
if __name__ == "__main__":

    def judge(head: Optional[ListNode]):
        iteration_count = 10**5
        sol = Solution(head)
        freqs = Counter(sol.getRandom() for _ in range(iteration_count))
        dummy = head
        length = 0
        while dummy:
            dummy = dummy.next
            length += 1
        if not length:
            return True
        target_freq = 1 / length
        return all(
            abs(target_freq - (_ / iteration_count)) <= 0.02
            for _ in freqs.values())

    run(
        judge,
        [
            ([ListNode.create_list([1, 2, 3])], True),
            ([ListNode.create_list([0])], True),
        ],
    )
