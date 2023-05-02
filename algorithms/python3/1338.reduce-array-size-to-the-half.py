#
# @lc app=leetcode id=1338 lang=python3
#
# [1338] Reduce Array Size to The Half
#
# https://leetcode.com/problems/reduce-array-size-to-the-half/description/
#
# algorithms
# Medium (68.38%)
# Likes:    2599
# Dislikes: 131
# Total Accepted:    148.1K
# Total Submissions: 211.2K
# Testcase Example:  '[3,3,3,3,5,5,5,2,2,7]'
#
# You are given an integer array arr. You can choose a set of integers and
# remove all the occurrences of these integers in the array.
#
# Return the minimum size of the set so that at least half of the integers of
# the array are removed.
#
#
# Example 1:
#
#
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has
# size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array
# [3,3,3,3,5,5,5] which has a size greater than half of the size of the old
# array.
#
#
# Example 2:
#
#
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the
# new array empty.
#
#
#
# Constraints:
#
#
# 2 <= arr.length <= 10^5
# arr.length is even.
# 1 <= arr[i] <= 10^5
#
#
#
from collections import Counter
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        current = res = 0
        limit, freqs = (n + 1) // 2, [0] * (n + 1)
        for i in Counter(arr).values():
            freqs[i] += 1
        for i in range(n, -1, -1):
            while freqs[i]:
                if current >= limit:
                    return res
                res += 1
                current += i
                freqs[i] -= 1
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minSetSize, Solution()),
        [
            [[[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]], 2],
            [[[7, 7, 7, 7, 7, 7]], 1],
            [[[]], 0],
        ],
    )
