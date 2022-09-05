#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (68.92%)
# Likes:    2283
# Dislikes: 101
# Total Accepted:    206.5K
# Total Submissions: 296.5K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).
#
#
# Example 1:
#
#
#
#
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]
#
#
# Example 2:
#
#
#
#
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
#
#
#
# Constraints:
#
#
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]
#
#
#
from typing import List
from algo_input import run, NTreeNode as Node
from types import MethodType
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res, left, level = [], 0, [root]
        while left < len(level):
            res.append([])
            for idx in range(left, len(level)):
                node = level[idx]
                res[-1].append(node.val)
                node.children and level.extend(node.children)
                left += 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.levelOrder, Solution()),
        [
            [[Node.create_tree([1, None, 3, 2, 4, None, 5, 6])],
             [[1], [3, 2, 4], [5, 6]]],
            [[
                Node.create_tree([
                    1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9,
                    10, None, None, 11, None, 12, None, 13, None, None, 14
                ])
            ], [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]],
            [[Node.create_tree([1])], [[1]]],
            [[Node.create_tree([])], []],
            [[Node.create_tree([1, None, 2, 3, None, 4, 5, None, 6, 7])],
             [[1], [2, 3], [4, 5, 6, 7]]],
        ],
    )
