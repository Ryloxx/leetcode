#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#
# https://leetcode.com/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (42.58%)
# Likes:    2638
# Dislikes: 200
# Total Accepted:    278.3K
# Total Submissions: 645.9K
# Testcase Example:  '[1,2,1]'
#
# You are visiting a farm that has a single row of fruit trees arranged from
# left to right. The trees are represented by an integer array fruits where
# fruits[i] is the type of fruit the i^th tree produces.
#
# You want to collect as much fruit as possible. However, the owner has some
# strict rules that you must follow:
#
#
# You only have two baskets, and each basket can only hold a single type of
# fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from
# every tree (including the start tree) while moving to the right. The picked
# fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must
# stop.
#
#
# Given the integer array fruits, return the maximum number of fruits you can
# pick.
#
#
# Example 1:
#
#
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
#
#
# Example 2:
#
#
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
#
#
# Example 3:
#
#
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
#
#
#
# Constraints:
#
#
# 1 <= fruits.length <= 10^5
# 0 <= fruits[i] < fruits.length
#
#
#
from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        d = defaultdict(int)
        left = 0
        ans = 0
        for i in tree:
            d[i] += 1
            while len(d) > 2:
                d[tree[left]] -= 1
                if not d[tree[left]]:
                    del d[tree[left]]
                left += 1
            ans = max(ans, sum(d.values()))
        return ans


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.totalFruit, Solution()),
        [
            ([[1, 2, 1]], 3),
            ([[0, 1, 2, 2]], 3),
            ([[1, 2, 3, 2, 2]], 4),
        ],
    )
