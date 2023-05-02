#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#
# https://leetcode.com/problems/count-vowels-permutation/description/
#
# algorithms
# Hard (56.20%)
# Likes:    2008
# Dislikes: 138
# Total Accepted:    81.6K
# Total Submissions: 135.6K
# Testcase Example:  '1'
#
# Given an integer n, your task is to count how many strings of length n can be
# formed under the following rules:
#
#
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
#
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
#
#
# Example 2:
#
#
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io",
# "iu", "oi", "ou" and "ua".
#
#
# Example 3:
#
#
# Input: n = 5
# Output: 68
#
#
# Constraints:
#
#
# 1 <= n <= 2 * 10^4
#
#
#
# from functools import cache
# from typing import List
from types import MethodType
from algo_input import run

# @lc code=start
import numpy as np


class Solution:

    # O(N) precompute time complexity precompute
    # O(1) query time complexity
    # O(N) space complexity
    # @staticmethod
    # @cache
    # def pre_computed() -> List[int]:

    #     def itemgetter(*items):
    #         indexes = list(items)

    #         def getter(arr):
    #             return tuple(arr[idx] for idx in indexes)

    #         return getter

    #     MOD, curr, res = 7 + 10**9, [1, 1, 1, 1, 1], []
    #     temp = [
    #         itemgetter(1, 2, 4),
    #         itemgetter(0, 2),
    #         itemgetter(1, 3),
    #         itemgetter(2),
    #         itemgetter(2, 3),
    #     ]
    #     for _ in range(2 * 10**4):
    #         res.append(sum(curr) % MOD)
    #         curr = list(map(lambda x: sum(x(curr)), temp))
    #         pass
    #     return res

    # def countVowelPermutation(self, n: int) -> int:
    #     return Solution.pre_computed()[n - 1]

    # O(logN) time complexity
    # O(1) space complexity
    def countVowelPermutation(self, n: int) -> int:
        res = np.array([1, 1, 1, 1, 1], dtype=np.ulonglong)
        m = np.array([[0, 1, 1, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0], [0, 0, 1, 1, 0]],
                     dtype=np.ulonglong)
        MOD = 7 + 10**9
        n -= 1
        while n:
            if n & 1:
                res = np.mod(m.dot(res), MOD)
            m = np.mod(m.dot(m), MOD)
            n >>= 1
        return int(np.mod(res.sum(), MOD))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.countVowelPermutation, Solution()),
        [
            [[1], 5],
            [[1305], 985362357],
            [[15061], 682798046],
            [[5], 68],
            [[2], 10],
            [[2 * 10**4], 759959057],
        ],
    )
