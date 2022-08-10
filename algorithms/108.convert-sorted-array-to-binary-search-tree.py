#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (66.19%)
# Likes:    7482
# Dislikes: 389
# Total Accepted:    815.7K
# Total Submissions: 1.2M
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an integer array nums where the elements are sorted in ascending order,
# convert it to a height-balanced binary search tree.
#
# A height-balanced binary tree is a binary tree in which the depth of the two
# subtrees of every node never differs by more than one.
#
#
# Example 1:
#
#
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
#
#
#
# Example 2:
#
#
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.
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

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def f(i, j):
            if i > j:
                return
            m = (i + j) // 2
            return TreeNode(nums[m], f(i, m - 1), f(m + 1, j))

        return f(0, len(nums) - 1)


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.sortedArrayToBST, Solution()), [
        [[[-10, -3, 0, 5, 9]],
         TreeNode.createTree([0, -3, 9, -10, None, 5])],
        [[[1, 3]], TreeNode.createTree([3, 1])],
    ],
        comparator=lambda tree_1, tree_2: TreeNode.is_valid_binary_tree(tree_1)
        and TreeNode.getHeightDiff(tree_1) <= 1 and list(
            TreeNode.in_order(tree_1)) == list(TreeNode.in_order(tree_2)))
