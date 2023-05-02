#
# @lc app=leetcode id=587 lang=python3
#
# [587] Erect the Fence
#
# https://leetcode.com/problems/erect-the-fence/description/
#
# algorithms
# Hard (43.23%)
# Likes:    848
# Dislikes: 485
# Total Accepted:    32.5K
# Total Submissions: 69.8K
# Testcase Example:  '[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]'
#
# You are given an array trees where trees[i] = [xi, yi] represents the
# location of a tree in the garden.
#
# You are asked to fence the entire garden using the minimum length of rope as
# it is expensive. The garden is well fenced only if all the trees are
# enclosed.
#
# Return the coordinates of trees that are exactly located on the fence
# perimeter.
#
#
# Example 1:
#
#
# Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
#
#
# Example 2:
#
#
# Input: points = [[1,2],[2,2],[4,2]]
# Output: [[4,2],[2,2],[1,2]]
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 3000
# points[i].length == 2
# 0 <= xi, yi <= 100
# All the given points are unique.
#
#
#
from algo_input import run, any_order
from types import MethodType
from typing import List, Tuple
from operator import gt, lt


# @lc code=start
class Solution:

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:

        buckets = [[101, -1, []] for _ in range(101)]
        top = 0
        bottom = 100
        left_side = []
        right_side = []

        def slope(a, b):
            if a[1] == b[1]:
                return 0
            return (a[0] - b[0]) / (a[1] - b[1])

        def add(side: List[Tuple[int, int]], point: Tuple[int, int], cmp):
            while len(side) > 1 and cmp(slope(side[-2], side[-1]),
                                        slope(side[-2], point)):
                side.pop()
            side.append(point)

        for x, y in trees:
            top = max(top, y)
            bottom = min(bottom, y)
            buckets[y][0] = min(buckets[y][0], x)
            buckets[y][1] = max(buckets[y][1], x)
            buckets[y][2].append((x, y))
        for y in range(top, bottom - 1, -1):
            if buckets[y][1] < 0:
                continue
            add(left_side, (buckets[y][0], y), lt)
            add(right_side, (buckets[y][1], y), gt)

        return list(
            map(
                list,
                set(left_side) | set(right_side) | set(buckets[top][2])
                | set(buckets[bottom][2])))


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.outerTrees, Solution()), [
        ([[[3, 7], [6, 8], [7, 8], [11, 10], [4, 3], [8, 5], [7, 13], [4, 13]]
          ], [[3, 7], [4, 13], [11, 10], [4, 3], [8, 5], [7, 13]]),
        ([[[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]]
          ], [[1, 1], [2, 0], [3, 3], [2, 4], [4, 2]]),
        ([[[1, 2], [2, 2], [4, 2]]], [[1, 2], [2, 2], [4, 2]]),
        ([[]], []),
        ([[[3, 0], [4, 0], [5, 0], [6, 1], [7, 2], [7, 3], [7, 4], [6, 5],
           [5, 5], [4, 5], [3, 5], [2, 5], [1, 4], [1, 3], [1, 2], [2, 1],
           [4, 2], [0, 3]]], [[4, 5], [2, 5], [6, 1], [3, 5], [2, 1], [1, 4],
                              [1, 2], [7, 4], [7, 3], [7, 2], [3, 0], [0, 3],
                              [5, 0], [5, 5], [4, 0], [6, 5]]),
    ],
        comparator=any_order)
