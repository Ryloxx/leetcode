#
# @lc app=leetcode id=1354 lang=python3
#
# [1354] Construct Target Array With Multiple Sums
#
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/description/
#
# algorithms
# Hard (31.20%)
# Likes:    670
# Dislikes: 75
# Total Accepted:    25.8K
# Total Submissions: 82.4K
# Testcase Example:  '[9,3,5]'
#
# You are given an array target of n integers. From a starting array arr
# consisting of n 1's, you may perform the following procedure :
#
#
# let x be the sum of all elements currently in your array.
# choose index i, such that 0 <= i < n and set the value of arr at index i to
# x.
# You may repeat this procedure as many times as needed.
#
#
# Return true if it is possible to construct the target array from arr,
# otherwise, return false.
#
#
# Example 1:
#
#
# Input: target = [9,3,5]
# Output: true
# Explanation: Start with arr = [1, 1, 1]
# [1, 1, 1], sum = 3 choose index 1
# [1, 3, 1], sum = 5 choose index 2
# [1, 3, 5], sum = 9 choose index 0
# [9, 3, 5] Done
#
#
# Example 2:
#
#
# Input: target = [1,1,1,2]
# Output: false
# Explanation: Impossible to create target array from [1,1,1,1].
#
#
# Example 3:
#
#
# Input: target = [8,5]
# Output: true
#
#
#
# Constraints:
#
#
# n == target.length
# 1 <= n <= 5 * 10^4
# 1 <= target[i] <= 10^9
#
#
#
from heapq import heapify, heappop, heappush
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def isPossible(self, target: List[int]) -> bool:
        if len(target) < 2:
            return target and target[0] == 1
        s = 0
        for i in range(len(target)):
            target[i] = -target[i]
            s += target[i]
        heapify(target)
        while target[0] < -1:
            curr = heappop(target)
            s -= curr
            curr -= (s * max(1, ((curr - target[0]) // s)))
            s += curr
            if curr > -1:
                return False
            heappush(target, curr)
        return True


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isPossible, Solution()),
        [
            [[[1]], True],
            [[[1, 1000000000]], True],
            [[[2]], False],
            [[[8, 5]], True],
            [[[1, 9, 1]], True],
            [[[1, 1, 1, 2]], False],
            [[[1, 10, 1]], False],
            [[[9, 3, 5]], True],
            [[[5, 5]], False],
            [[list(range(2, 5 * 10**4 + 2))], False],
            [[[2, 900000002]], False],
            [[[1, 10**9]], True],
        ],
    )
