#
# @lc app=leetcode id=894 lang=python3
#
# [894] All Possible Full Binary Trees
#
# https://leetcode.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (80.00%)
# Likes:    3938
# Dislikes: 274
# Total Accepted:    122.3K
# Total Submissions: 151.3K
# Testcase Example:  '7'
#
# Given an integer n, return a list of all possible full binary trees with n
# nodes. Each node of each tree in the answer must have Node.val == 0.
#
# Each element of the answer is the root node of one possible tree. You may
# return the final list of trees in any order.
#
# A full binary tree is a binary tree where each node has exactly 0 or 2
# children.
#
#
# Example 1:
#
#
# Input: n = 7
# Output:
# [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
#
#
# Example 2:
#
#
# Input: n = 3
# Output: [[0,0,0]]
#
#
#
# Constraints:
#
#
# 1 <= n <= 20
#
#
#
from typing import List, Optional
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

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n % 2:
            return []
        dp = [[] for _ in range(n + 2)]
        dp[1].append(TreeNode(0))
        for x in range(2, n + 1, 2):
            for i in range(1, x):
                for left in dp[i]:
                    for right in dp[x - i]:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        dp[x + 1].append(root)
        return dp[n]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.allPossibleFBT, Solution()),
        [
            (
                [7],
                [
                    TreeNode.create_tree(
                        [0, 0, 0, None, None, 0, 0, None, None, 0, 0]),
                    TreeNode.create_tree([0, 0, 0, None, None, 0, 0, 0, 0]),
                    ##
                    TreeNode.create_tree([0, 0, 0, 0, 0, 0, 0]),
                    TreeNode.create_tree(
                        [0, 0, 0, 0, 0, None, None, None, None, 0, 0]),
                    TreeNode.create_tree([0, 0, 0, 0, 0, None, None, 0, 0])
                ]),
            ([3], [
                TreeNode.create_tree([0, 0, 0]),
            ]),
            ([20], []),
        ],
        comparator=lambda x, y: len(x) == len(y) and all(
            any(TreeNode.are_equal(a, b) for b in y) for a in x))
