#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (56.50%)
# Likes:    4992
# Dislikes: 404
# Total Accepted:    217.3K
# Total Submissions: 371K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
#
# Two trees are duplicate if they have the same structure with the same node
# values.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
#
#
# Example 2:
#
#
# Input: root = [2,1,1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
#
#
#
# Constraints:
#
#
# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200
#
#
#
from typing import Counter, List, Optional
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

    def findDuplicateSubtrees(
            self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = {}
        h_s = {}
        cnt = Counter()

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            h = (node.val, dfs(node.left), dfs(node.right))

            if h not in h_s:
                h_s[h] = len(h_s) + 1
            id = h_s[h]
            cnt[id] += 1
            if cnt[id] >= 2:
                res[id] = node
            return id

        dfs(root)
        return list(res.values())


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.findDuplicateSubtrees, Solution()), [
        ([TreeNode.create_tree([1, 2, 3, 4, None, 2, 4, None, None, 4])
          ], [TreeNode.create_tree([2, 4]),
              TreeNode.create_tree([4])]),
        ([TreeNode.create_tree([2, 1, 1])], [TreeNode.create_tree([1])]),
        ([TreeNode.create_tree([2, 2, 2, 3, None, 3, None])
          ], [TreeNode.create_tree([2, 3]),
              TreeNode.create_tree([3])]),
    ],
        comparator=lambda a, b: len(a) == len(b) and all(
            any(TreeNode.are_equal(x, y) for y in b) for x in a))
