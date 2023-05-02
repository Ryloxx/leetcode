#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#
# https://leetcode.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (61.25%)
# Likes:    975
# Dislikes: 254
# Total Accepted:    57.9K
# Total Submissions: 92.7K
# Testcase Example:  '1'
#
# You are given an integer n. We reorder the digits in any order (including the
# original order) such that the leading digit is not zero.
#
# Return true if and only if we can do this so that the resulting number is a
# power of two.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: true
#
#
# Example 2:
#
#
# Input: n = 10
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
#
#
#
# from collections import Counter
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # O(logN * logN) time complexity
    # O(logN) space complexity
    # No string manipulation
    def reorderedPowerOf2(self, n: int) -> bool:

        def countDigits(x):
            res = [0] * 10
            if x:
                while x:
                    res[x % 10] += 1
                    x //= 10
            else:
                res[0] += 1
            return res

        baseCount = countDigits(n)
        return any(baseCount == countDigits(1 << x) for x in range(30))

    # O(logN * logN) time complexity
    # O(logN) space complexity
    # def reorderedPowerOf2(self, n: int) -> bool:
    #     baseCount = Counter(str(n))
    #     return any(baseCount == Counter(str(1 << x)) for x in range(30))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.reorderedPowerOf2, Solution()),
        [
            [[46], True],
            [[0], False],
            [[1], True],
            [[10], False],
            [[211703], True],
            [[624214], True],
            [[4493140], True],
            [[4493141], False],
            [[6244], False],
        ],
    )
