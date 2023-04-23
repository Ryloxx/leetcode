#
# @lc app=leetcode id=1416 lang=python3
#
# [1416] Restore The Array
#
# https://leetcode.com/problems/restore-the-array/description/
#
# algorithms
# Hard (38.77%)
# Likes:    798
# Dislikes: 31
# Total Accepted:    25.7K
# Total Submissions: 58.2K
# Testcase Example:  '"1000"\n10000'
#
# A program was supposed to print an array of integers. The program forgot to
# print whitespaces and the array is printed as a string of digits s and all we
# know is that all integers in the array were in the range [1, k] and there are
# no leading zeros in the array.
#
# Given the string s and the integer k, return the number of the possible
# arrays that can be printed as s using the mentioned program. Since the answer
# may be very large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: s = "1000", k = 10000
# Output: 1
# Explanation: The only possible array is [1000]
#
#
# Example 2:
#
#
# Input: s = "1000", k = 10
# Output: 0
# Explanation: There cannot be an array that was printed this way and has all
# integer >= 1 and <= 10.
#
#
# Example 3:
#
#
# Input: s = "1317", k = 2000
# Output: 8
# Explanation: Possible arrays are
# [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only digits and does not contain leading zeros.
# 1 <= k <= 10^9
#
#
#
from functools import cache
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = (10**9 + 7)

        @cache
        def dp(idx):
            if idx == len(s):
                return 1
            if s[idx] == "0":
                return 0
            res = n = 0
            for right in range(idx, len(s)):
                n *= 10
                n += int(s[right])
                if n > k:
                    break
                res += dp(right + 1)
                res %= MOD
            return res

        return dp(0)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numberOfArrays, Solution()),
        [
            (["1000", 10000], 1),
            (["1000", 10], 0),
            (["1317", 2000], 8),
            (["1234567890", 90], 34),
            (["2020", 30], 1),
        ],
    )
