#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#
# https://leetcode.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (41.96%)
# Likes:    2788
# Dislikes: 32
# Total Accepted:    67K
# Total Submissions: 159K
# Testcase Example:  '[0,0,null,0,0]'
#
# You are given the root of a binary tree. We install cameras on the tree nodes
# where each camera at a node can monitor its parent, itself, and its immediate
# children.
#
# Return the minimum number of cameras needed to monitor all nodes of the
# tree.
#
#
# Example 1:
#
#
# Input: root = [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#
#
# Example 2:
#
#
# Input: root = [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the
# tree. The above image shows one of the valid configurations of camera
# placement.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# Node.val == 0
#
#
#
from typing import Optional
from algo_input import run, TreeNode
from types import MethodType


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        hasCamera = set()

        def dfs(parent, current):
            if not current:
                return
            dfs(current, current.left)
            dfs(current, current.right)
            if (not current.left and not current.right) or\
                (current not in hasCamera
                    and parent not in hasCamera
                    and current.left not in hasCamera
                    and current.right not in hasCamera):
                hasCamera.add(parent)

        dfs(None, root)
        return len(hasCamera)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minCameraCover, Solution()),
        [
            [[TreeNode.createTree([0, None, 0, None, 0, None, 0])], 2],
            [[TreeNode.createTree([0, 0, None, 0, 0])], 1],
            [[TreeNode.createTree([0])], 1],
            [[TreeNode.createTree([0, None, 0, 0, None, 0, 0, None, None, 0])],
             3],
            [[TreeNode.createTree([0, 0, None, 0, 0, 0, None, None, 0])], 3],
            [[TreeNode.createTree([0, 0, None, 0, None, 0, None, None, 0])], 2
             ],
            [[TreeNode.createTree([0, 0, None, None, 0, 0, None, None, 0, 0])],
             2],
        ],
    )
