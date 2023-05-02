#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (59.68%)
# Likes:    7397
# Dislikes: 409
# Total Accepted:    740.1K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to
# bottom.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
#
# Example 2:
#
#
# Input: root = [1,null,3]
# Output: [1,3]
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
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
#
from collections import deque
from typing import List
from algo_input import run, TreeNode
from types import MethodType
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        res = []
        while q:
            node, depth = q.popleft()
            if depth == len(res):
                res.append(node.val)
            if node.right:
                q.append((node.right, depth + 1))
            if node.left:
                q.append((node.left, depth + 1))
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.rightSideView, Solution()),
        [
            [[TreeNode.create_tree([1, 2, 3, None, 5, None, 4])], [1, 3, 4]],
            [[TreeNode.create_tree([1, None, 3])], [1, 3]],
            [[TreeNode.create_tree([])], []],
        ],
    )
