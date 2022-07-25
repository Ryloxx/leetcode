#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
# https://leetcode.com/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (36.10%)
# Likes:    1175
# Dislikes: 139
# Total Accepted:    62.1K
# Total Submissions: 170.2K
# Testcase Example:  '["AllOne","inc","inc","getMaxKey","getMinKey",
# "inc","getMaxKey","getMinKey"]\n' +
# '[[],["hello"],["hello"],[],[],["leet"],[],[]]'
#
# Design a data structure to store the strings' count with the ability to
# return the strings with minimum and maximum counts.
#
# Implement the AllOne class:
#
#
# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not
# exist in the data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of
# key is 0 after the decrement, remove it from the data structure. It is
# guaranteed that key exists in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element
# exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element
# exists, return an empty string "".
#
#
# Note that each function must run in O(1) average time complexity.
#
#
# Example 1:
#
#
# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey",
# "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]
#
# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"
#
#
#
# Constraints:
#
#
# 1 <= key.length <= 10
# key consists of lowercase English letters.
# It is guaranteed that for each call to dec, key is existing in the data
# structure.
# At most 5 * 10^4 calls will be made to inc, dec, getMaxKey, and getMinKey.
#
#
#
from typing import Any, List, Tuple
from algo_input import run

# @lc code=start


class AllOne:

    class Node:

        def __init__(self, val) -> None:
            self.val = val
            self.keys = set()
            self.next = None
            self.prev = None

        def insert_after(self, other: "AllOne.Node") -> None:
            temp = self.next
            self.next = other
            if other:
                other.prev = self
                other.next = temp
            if temp:
                temp.prev = other

        def insert_before(self, other: "AllOne.Node") -> None:
            if self.prev:
                self.prev.insert_after(other)
            else:
                other.insert_after(self)

        def cut(self) -> None:
            if self.prev:
                self.prev.next = self.next
            if self.next:
                self.next.prev = self.prev
            self.prev = None
            self.next = None

    def __init__(self):
        self.tail = self.head = AllOne.Node(1)
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            if self.head.val != 1:
                n = AllOne.Node(1)
                n.insert_after(self.head)
                self.head = n
            self.head.keys.add(key)
            self.nodes[key] = self.head
            return
        node = self.nodes[key]
        node.keys.discard(key)
        if node.next and node.next.val == node.val + 1:
            node.next.keys.add(key)
        else:
            node.insert_after(AllOne.Node(node.val + 1))
            node.next.keys.add(key)
        self.nodes[key] = node.next
        if node == self.tail:
            self.tail = self.tail.next
        if not node.keys:
            if node == self.head:
                self.head = self.head.next
            node.cut()

    def dec(self, key: str) -> None:
        node = self.nodes[key]
        node.keys.discard(key)
        if node.val - 1 >= 1:
            if node.prev and node.prev.val == node.val - 1:
                node.prev.keys.add(key)
            else:
                node.insert_before(AllOne.Node(node.val - 1))
                node.prev.keys.add(key)
            self.nodes[key] = node.prev
            if node == self.head:
                self.head = self.head.prev
            if not node.keys:
                if node == self.tail:
                    self.tail = self.tail.prev
                node.cut()
        else:
            del self.nodes[key]

    def getMaxKey(self) -> str:
        return next(iter(self.tail.keys), None) or ""

    def getMinKey(self) -> str:
        temp = (self.head if self.head.val != 1 or self.head.keys
                or not self.head.next else self.head.next)
        return next(iter(temp.keys), None) or ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

obj = AllOne()


def process(steps: List[Tuple[str, List[Any]]]):
    return list(map(lambda step: getattr(obj, step[0])(*step[1]), steps))


if __name__ == "__main__":
    run(
        process,
        [
            [[[
                ["getMinKey", []],
                ["getMaxKey", []],
                ["inc", ["hello"]],
                ["getMinKey", []],
                ["getMaxKey", []],
                ["dec", ["hello"]],
                ["getMinKey", []],
                ["getMaxKey", []],
                ["inc", ["goodbye"]],
                ["inc", ["goodbye"]],
                ["inc", ["goodbye"]],
                ["inc", ["hello"]],
                ["inc", ["hello"]],
                ["getMinKey", []],
                ["getMaxKey", []],
                ["dec", ["goodbye"]],
                ["dec", ["goodbye"]],
                ["getMinKey", []],
                ["getMaxKey", []],
                ["dec", ["goodbye"]],
                ["getMinKey", []],
                ["getMaxKey", []],
                ["dec", ["hello"]],
                ["dec", ["hello"]],
                ["getMinKey", []],
                ["getMaxKey", []],
            ]],
             [
                 "", "", None, "hello", "hello", None, "", "", None, None,
                 None, None, None, "hello", "goodbye", None, None, "goodbye",
                 "hello", None, "hello", "hello", None, None, "", ""
             ]],
        ],
    )
