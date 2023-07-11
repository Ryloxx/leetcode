#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (62.17%)
# Likes:    9615
# Dislikes: 185
# Total Accepted:    349K
# Total Submissions: 549.6K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# Given the root of a binary tree, the value of a target node target, and an
# integer k, return an array of the values of all nodes that have a distance k
# from the target node.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value
# 5) have values 7, 4, and 1.
#
#
# Example 2:
#
#
# Input: root = [1], target = 1, k = 3
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500
# All the values Node.val are unique.
# target is the value of one of the nodes in the tree.
# 0 <= k <= 1000
#
#
#
from collections import defaultdict
from typing import List
from algo_input import run, TreeNode, any_order
from types import MethodType

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        graph = defaultdict(set)

        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].add(parent.val)
            if node.right:
                graph[node.val].add(node.right.val)
                build_graph(node.right, node)
            if node.left:
                graph[node.val].add(node.left.val)
                build_graph(node.left, node)

        def fill(node, k, parent):
            if k <= 0:
                res.append(node)
            else:
                for neigh in graph[node]:
                    if neigh != parent:
                        fill(neigh, k - 1, node)

        build_graph(root, None)
        fill(target.val, k, None)
        return res


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.distanceK, Solution()), [
        ([
            TreeNode.create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
            TreeNode(5), 2
        ], [7, 4, 1]),
        ([TreeNode.create_tree([1]), TreeNode(1), 3], []),
    ],
        comparator=any_order)
