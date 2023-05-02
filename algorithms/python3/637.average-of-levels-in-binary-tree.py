#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (68.77%)
# Likes:    3086
# Dislikes: 242
# Total Accepted:    278.4K
# Total Submissions: 403.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the average value of the nodes on
# each level in the form of an array. Answers within 10^-5 of the actual answer
# will be accepted.
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
# and on level 2 is 11.
# Hence return [3, 14.5, 11].
#
#
# Example 2:
#
#
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
#
#
#
from statistics import mean
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

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        curr = [root]
        while curr:
            res.append(mean(map(lambda x: x.val, curr)))
            temp = []
            for node in curr:
                node.left and temp.append(node.left)
                node.right and temp.append(node.right)
            curr = temp
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.averageOfLevels, Solution()),
        [
            [[TreeNode.create_tree([3, 9, 20, None, None, 15, 7])],
             [3.00000, 14.50000, 11.00000]],
            [[TreeNode.create_tree([3, 9, 20, 15, 7])],
             [3.00000, 14.50000, 11.00000]],
        ],
    )
