#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#
# https://leetcode.com/problems/jump-game-iv/description/
#
# algorithms
# Hard (43.95%)
# Likes:    2664
# Dislikes: 101
# Total Accepted:    97.6K
# Total Submissions: 216.7K
# Testcase Example:  '[100,-23,-23,404,100,23,23,23,3,404]'
#
# Given an array of integers arr, you are initially positioned at the first
# index of the array.
#
# In one step you can jump from index i to index:
#
#
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
#
#
# Return the minimum number of steps to reach the last index of the array.
#
# Notice that you can not jump outside of the array at any time.
#
#
# Example 1:
#
#
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that
# index 9 is the last index of the array.
#
#
# Example 2:
#
#
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You do not need to jump.
#
#
# Example 3:
#
#
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last
# index of the array.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8
#
#
#
from collections import defaultdict
from typing import List
from itertools import chain
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minJumps(self, arr: List[int]) -> int:
        jumps = defaultdict(list)
        for current_idx, idx in enumerate(arr):
            jumps[idx].append(current_idx)
        seen = set()
        q = [0]
        res = 0
        while q:
            t = []
            for current_idx in q:
                if current_idx == len(arr) - 1:
                    return res
                for idx in chain([current_idx - 1, current_idx + 1],
                                 jumps[arr[current_idx]]):
                    if idx in seen or not (0 <= idx < len(arr)):
                        continue
                    seen.add(idx)
                    t.append(idx)
                jumps[arr[current_idx]].clear()
            q = t
            res += 1
        return -1


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minJumps, Solution()),
        [
            ([[100, -23, -23, 404, 100, 23, 22, 21, 3, 404]], 3),
            ([[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]], 3),
            ([[7]], 0),
            ([[7, 6, 9, 6, 9, 6, 9, 7]], 1),
            ([[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]], 3),
            ([([7] * 10**5) + [8]], 2),
        ],
    )
