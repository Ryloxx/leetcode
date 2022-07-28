#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
#
# algorithms
# Medium (79.62%)
# Likes:    2361
# Dislikes: 69
# Total Accepted:    169.7K
# Total Submissions: 212.9K
# Testcase Example:  '[2,1,4]\n[1,0,3]'
#
# Given two binary search trees root1 and root2, return a list containing all
# the integers from both trees sorted in ascending order.
#
#
# Example 1:
#
#
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
#
#
# Example 2:
#
#
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
#
#
#
# Constraints:
#
#
# The number of nodes in each tree is in the range [0, 5000].
# -10^5 <= Node.val <= 10^5
#
#
#
from typing import List
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

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack_1, stack_2 = [], []
        res = []
        while root1 or root2 or stack_1 or stack_2:
            while root1:
                stack_1.append(root1)
                root1 = root1.left
            while root2:
                stack_2.append(root2)
                root2 = root2.left
            if not stack_1:
                res.append(stack_2.pop())
                root2 = res[-1].right
            elif not stack_2:
                res.append(stack_1.pop())
                root1 = res[-1].right
            else:
                if stack_1[-1].val < stack_2[-1].val:
                    res.append(stack_1.pop())
                    root1 = res[-1].right
                else:
                    res.append(stack_2.pop())
                    root2 = res[-1].right

        return list(x.val for x in res)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.getAllElements, Solution()),
        [
            [[TreeNode.createTree([2, 1, 4]),
              TreeNode.createTree([1, 0, 3])], [0, 1, 1, 2, 3, 4]],
            [[TreeNode.createTree([1, None, 8]),
              TreeNode.createTree([8, 1])], [1, 1, 8, 8]],
        ],
    )
