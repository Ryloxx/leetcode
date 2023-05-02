#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#
# https://leetcode.com/problems/path-crossing/description/
#
# algorithms
# Easy (55.78%)
# Likes:    496
# Dislikes: 10
# Total Accepted:    37K
# Total Submissions: 66.4K
# Testcase Example:  '"NES"'
#
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing
# moving one unit north, south, east, or west, respectively. You start at the
# origin (0, 0) on a 2D plane and walk on the path specified by path.
#
# Return true if the path crosses itself at any point, that is, if at any time
# you are on a location you have previously visited. Return false otherwise.
#
#
# Example 1:
#
#
# Input: path = "NES"
# Output: false
# Explanation: Notice that the path doesn't cross any point more than once.
#
#
# Example 2:
#
#
# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
#
#
# Constraints:
#
#
# 1 <= path.length <= 10^4
# path[i] is either 'N', 'S', 'E', or 'W'.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        seen = set()
        for p in path:
            if (x, y) in seen:
                return True
            seen.add((x, y))
            if p == "N":
                y -= 1
            elif p == "S":
                y += 1
            elif p == "E":
                x += 1
            else:
                x -= 1
        return (x, y) in seen


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.isPathCrossing, Solution()),
        [
            [["SN"], True],
            [["NES"], False],
            [["NESWW"], True],
        ],
    )
