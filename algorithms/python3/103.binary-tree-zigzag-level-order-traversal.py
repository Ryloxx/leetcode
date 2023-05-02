#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (55.34%)
# Likes:    8827
# Dislikes: 235
# Total Accepted:    924.2K
# Total Submissions: 1.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values. (i.e., from left to right, then right to left for the next
# level and alternate between).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
#
#
#
from collections import deque
from typing import Deque, List, Optional, Tuple
from algo_input import run, TreeNode
from types import MethodType


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d: List[Deque[int]] = []
        q: Deque[Tuple[TreeNode, int]] = deque()
        q.append((root, 0))
        while q:
            curr, r = q.popleft()
            r == len(d) and d.append(deque())
            r % 2 and d[-1].appendleft(curr.val)
            not r % 2 and d[-1].append(curr.val)
            curr.left and q.append((curr.left, r + 1))
            curr.right and q.append((curr.right, r + 1))
        return list(map(list, d))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.zigzagLevelOrder, Solution()),
        [
            ([TreeNode.create_tree([3, 9, 20, None, None, 15, 7])
              ], [[3], [20, 9], [15, 7]]),
            ([TreeNode.create_tree([1])], [[1]]),
            ([TreeNode.create_tree([])], []),
        ],
    )
