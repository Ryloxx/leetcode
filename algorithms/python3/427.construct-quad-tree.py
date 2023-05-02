#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#
# https://leetcode.com/problems/construct-quad-tree/description/
#
# algorithms
# Medium (66.48%)
# Likes:    634
# Dislikes: 875
# Total Accepted:    55.3K
# Total Submissions: 81.8K
# Testcase Example:  '[[0,1],[1,0]]'
#
# Given a n * n matrix grid of 0's and 1's only. We want to represent the grid
# with a Quad-Tree.
#
# Return the root of the Quad-Tree representing the grid.
#
# Notice that you can assign the value of a node to True or False when isLeaf
# is False, and both are accepted in the answer.
#
# A Quad-Tree is a tree data structure in which each internal node has exactly
# four children. Besides, each node has two attributes:
#
#
# val: True if the node represents a grid of 1's or False if the node
# represents a grid of 0's.
# isLeaf: True if the node is leaf node on the tree or False if the node has
# the four children.
#
#
#
# class Node {
# ⁠   public boolean val;
# ⁠   public boolean isLeaf;
# ⁠   public Node topLeft;
# ⁠   public Node topRight;
# ⁠   public Node bottomLeft;
# ⁠   public Node bottomRight;
# }
#
# We can construct a Quad-Tree from a two-dimensional area using the following
# steps:
#
#
# If the current grid has the same value (i.e all 1's or all 0's) set isLeaf
# True and set val to the value of the grid and set the four children to Null
# and stop.
# If the current grid has different values, set isLeaf to False and set val to
# any value and divide the current grid into four sub-grids as shown in the
# photo.
# Recurse for each of the children with the proper sub-grid.
#
#
# If you want to know more about the Quad-Tree, you can refer to the wiki.
#
# Quad-Tree format:
#
# The output represents the serialized format of a Quad-Tree using level order
# traversal, where null signifies a path terminator where no node exists
# below.
#
# It is very similar to the serialization of the binary tree. The only
# difference is that the node is represented as a list [isLeaf, val].
#
# If the value of isLeaf or val is True we represent it as 1 in the list
# [isLeaf, val] and if the value of isLeaf or val is False we represent it as
# 0.
#
#
# Example 1:
#
#
# Input: grid = [[0,1],[1,0]]
# Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
# Explanation: The explanation of this example is shown below:
# Notice that 0 represnts False and 1 represents True in the photo representing
# the Quad-Tree.
#
#
#
# Example 2:
#
#
#
#
# Input: grid =
# [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
# Output:
# [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# Explanation: All values in the grid are not the same. We divide the grid into
# four sub-grids.
# The topLeft, bottomLeft and bottomRight each has the same value.
# The topRight have different values so we divide it into 4 sub-grids where
# each has the same value.
# Explanation is shown in the photo below:
#
#
#
#
# Constraints:
#
#
# n == grid.length == grid[i].length
# n == 2^x where 0 <= x <= 6
#
#
#
from typing import List, Optional, Tuple
from algo_input import run
from types import MethodType

# @lc code=start


# Definition for a QuadTree node.
class Node:

    def __init__(self, val: int, isLeaf: bool, topLeft: Optional['Node'],
                 topRight: Optional['Node'], bottomLeft: Optional['Node'],
                 bottomRight: Optional['Node']):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:

    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(topLeftCorner: Tuple[int, int], n) -> Node:
            n >>= 1
            node = Node(grid[topLeftCorner[0]][topLeftCorner[1]], True, None,
                        None, None, None)
            if n:
                topLeft = dfs(topLeftCorner, n)
                bottomLeft = dfs((topLeftCorner[0] + n, topLeftCorner[1]), n)
                topRight = dfs((topLeftCorner[0], topLeftCorner[1] + n), n)
                bottomRight = dfs((topLeftCorner[0] + n, topLeftCorner[1] + n),
                                  n)
                node.isLeaf = (
                    bottomLeft.isLeaf and topLeft.isLeaf and bottomRight.isLeaf
                    and topRight.isLeaf) and (bottomLeft.val == topLeft.val ==
                                              bottomRight.val == topRight.val)
                if not node.isLeaf:
                    node.bottomLeft = bottomLeft
                    node.bottomRight = bottomRight
                    node.topLeft = topLeft
                    node.topRight = topRight
            return node

        return dfs((0, 0), len(grid))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.construct, Solution()),
        [
            # TODO: Implement judge for QuadTreeNode
            #
            # ([[[0, 1], [1, 0]]], [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]),
            # ([[[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
            #    [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
            #    [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
            #    [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]
            #   ], [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None,
            #       None, [1, 0], [1, 0], [1, 1], [1, 1]]),
            # ([[[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
            #    [1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0],
            #    [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
            #    [0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1]]],
            #  [[0, 1], [1, 1], [0, 1], [0, 1], [1, 1], None, None, None, None,
            # [1, 1], [1, 1], [1, 1], [1, 0], [1, 1], [1, 1], [1, 0], [1, 0]]),
        ],
    )
