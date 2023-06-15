#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
#
# algorithms
# Medium (66.08%)
# Likes:    2502
# Dislikes: 80
# Total Accepted:    160.2K
# Total Submissions: 238.1K
# Testcase Example:  '[1,7,0,7,-8,null,null]'
#
# Given the root of a binary tree, the level of its root is 1, the level of its
# children is 2, and so on.
#
# Return the smallest level x such that the sum of all the values of nodes at
# level x is maximal.
#
#
# Example 1:
#
#
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
#
#
# Example 2:
#
#
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#
from sys import maxsize
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

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        s1, s2 = [root], []
        i = 1
        res = (-maxsize, 0)
        while s1:
            s = 0
            while s1:
                node = s1.pop()
                if node.left:
                    s2.append(node.left)
                if node.right:
                    s2.append(node.right)
                s += node.val
            res = max(res, (s, -i))
            s1, s2 = s2, s1
            i += 1
        return -res[1]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.maxLevelSum, Solution()),
        [
            ([TreeNode.create_tree([1, 7, 0, 7, -8, None, None])], 2),
            ([
                TreeNode.create_tree([
                    989, None, 10250, 98693, -89388, None, None, None, -32127
                ])
            ], 2),
        ],
    )
