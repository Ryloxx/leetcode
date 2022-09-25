#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#
# https://leetcode.com/problems/design-circular-queue/description/
#
# algorithms
# Medium (48.74%)
# Likes:    2630
# Dislikes: 217
# Total Accepted:    226.7K
# Total Submissions: 444K
# Testcase Example:  '["MyCircularQueue","enQueue","enQueue","enQueue",
# "enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n' +
#  '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# Design your implementation of the circular queue. The circular queue is a
# linear data structure in which the operations are performed based on FIFO
# (First In First Out) principle and the last position is connected back to the
# first position to make a circle. It is also called "Ring Buffer".
#
# One of the benefits of the circular queue is that we can make use of the
# spaces in front of the queue. In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the
# queue. But using the circular queue, we can use the space to store new
# values.
#
# Implementation the MyCircularQueue class:
#
#
# MyCircularQueue(k) Initializes the object with the size of the queue to be
# k.
# int Front() Gets the front item from the queue. If the queue is empty, return
# -1.
# int Rear() Gets the last item from the queue. If the queue is empty, return
# -1.
# boolean enQueue(int value) Inserts an element into the circular queue. Return
# true if the operation is successful.
# boolean deQueue() Deletes an element from the circular queue. Return true if
# the operation is successful.
# boolean isEmpty() Checks whether the circular queue is empty or not.
# boolean isFull() Checks whether the circular queue is full or not.
#
#
# You must solve the problem without using the built-in queue data structure in
# your programming language.
#
#
# Example 1:
#
#
# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear",
# "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]
#
# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4
#
#
#
# Constraints:
#
#
# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty,
# and isFull.
#
#
#
from algo_input import run, wrapp_class


# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.max_size = k
        self.curr_size = 0
        self.c_queue = [0] * self.max_size
        self.head = self.tail = k - 1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.c_queue[self.head] = value
        self.head = (self.head - 1) % self.max_size
        self.curr_size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % self.max_size
        self.curr_size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.isEmpty() else self.c_queue[self.tail]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.isEmpty() else self.c_queue[(self.head + 1) %
                                                      self.max_size]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.curr_size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.curr_size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end
if __name__ == "__main__":
    run(
        wrapp_class(MyCircularQueue),
        [
            [[[3],
              [
                  ["enQueue", [1]],
                  ["enQueue", [2]],
                  ["enQueue", [3]],
                  ["enQueue", [4]],
                  ["Rear", []],
                  ["isFull", []],
                  ["deQueue", []],
                  ["enQueue", [4]],
                  ["Rear", []],
              ]], [True, True, True, False, 3, True, True, True, 4]],
            [[[5],
              [
                  ["enQueue", [1]],
                  ["enQueue", [2]],
                  ["enQueue", [3]],
                  ["Rear", []],
                  ["Front", []],
                  ["isFull", []],
                  ["deQueue", []],
                  ["enQueue", [4]],
                  ["Rear", []],
              ]], [True, True, True, 3, 1, False, True, True, 4]],
        ],
    )
