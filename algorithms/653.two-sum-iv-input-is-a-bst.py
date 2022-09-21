#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (58.81%)
# Likes:    4414
# Dislikes: 213
# Total Accepted:    356.3K
# Total Submissions: 600.1K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given the root of a Binary Search Tree and a target number k, return true if
# there exist two elements in the BST such that their sum is equal to the given
# target.
#
#
# Example 1:
#
#
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
#
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
# root is guaranteed to be a valid binary search tree.
# -10^5 <= k <= 10^5
#
#
#
from collections import defaultdict
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
class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = defaultdict(int)

        def dfs(node):
            if not node:
                return False
            seen_count = seen[k - node.val]
            seen[node.val] += 1
            return seen_count or dfs(node.left) or dfs(node.right)

        return dfs(root)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findTarget, Solution()),
        [
            [[TreeNode.create_tree([5, 3, 6, 2, 4, None, 7]), 9], True],
            [[TreeNode.create_tree([5, 3, 6, 2, 4, None, 7]), 28], False],
        ],
    )
