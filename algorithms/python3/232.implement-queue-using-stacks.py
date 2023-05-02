#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (62.54%)
# Likes:    5390
# Dislikes: 317
# Total Accepted:    590.3K
# Total Submissions: 943.8K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],
# [2],[],[],[]]'
#
# Implement a first in first out (FIFO) queue using only two stacks. The
# implemented queue should support all the functions of a normal queue (push,
# peek, pop, and empty).
#
# Implement the MyQueue class:
#
#
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
#
#
# Notes:
#
#
# You must use only standard operations of a stack, which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may
# simulate a stack using a list or deque (double-ended queue) as long as you
# use only a stack's standard operations.
#
#
#
# Example 1:
#
#
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
#
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
#
#
#
# Constraints:
#
#
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.
#
#
#
# Follow-up: Can you implement the queue such that each operation is amortized
# O(1) time complexity? In other words, performing n operations will take
# overall O(n) time even if one of those operations may take longer.
#
#
from algo_input import run, wrapp_class


# @lc code=start
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def swap(self):
        if not self.q2:
            while self.q1:
                self.q2.append(self.q1.pop())

    def pop(self) -> int:
        self.swap()
        return self.q2.pop()

    def peek(self) -> int:
        self.swap()
        return self.q2[-1]

    def empty(self) -> bool:
        self.swap()
        return not self.q2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
if __name__ == "__main__":
    run(wrapp_class(MyQueue), [([[],
                                 [
                                     ["push", [1]],
                                     ["push", [2]],
                                     ["peek", []],
                                     ["pop", []],
                                     ["empty", []],
                                 ]], [None, None, 1, 1, False])])
