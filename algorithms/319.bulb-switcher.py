#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#
# https://leetcode.com/problems/bulb-switcher/description/
#
# algorithms
# Medium (48.13%)
# Likes:    1767
# Dislikes: 2413
# Total Accepted:    157.8K
# Total Submissions: 311.8K
# Testcase Example:  '3'
#
# There are n bulbs that are initially off. You first turn on all the bulbs,
# then you turn off every second bulb.
#
# On the third round, you toggle every third bulb (turning on if it's off or
# turning off if it's on). For the i^th round, you toggle every i bulb. For the
# n^th round, you only toggle the last bulb.
#
# Return the number of bulbs that are on after n rounds.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 1
# Explanation: At first, the three bulbs are [off, off, off].
# After the first round, the three bulbs are [on, on, on].
# After the second round, the three bulbs are [on, off, on].
# After the third round, the three bulbs are [on, off, off].
# So you should return 1 because there is only one bulb is on.
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^9
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def bulbSwitch(self, n: int) -> int:
        return int(n**(1 / 2))


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.bulbSwitch, Solution()),
        [
            ([3], 1),
            ([0], 0),
            ([1], 1),
        ],
    )
