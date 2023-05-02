#
# @lc app=leetcode id=1996 lang=python3
#
# [1996] The Number of Weak Characters in the Game
#
# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/description/
#
# algorithms
# Medium (33.77%)
# Likes:    1608
# Dislikes: 55
# Total Accepted:    46.9K
# Total Submissions: 113.7K
# Testcase Example:  '[[5,5],[6,3],[3,6]]'
#
# You are playing a game that contains multiple characters, and each of the
# characters has two main properties: attack and defense. You are given a 2D
# integer array properties where properties[i] = [attacki, defensei] represents
# the properties of the i^th character in the game.
#
# A character is said to be weak if any other character has both attack and
# defense levels strictly greater than this character's attack and defense
# levels. More formally, a character i is said to be weak if there exists
# another character j where attackj > attacki and defensej > defensei.
#
# Return the number of weak characters.
#
#
# Example 1:
#
#
# Input: properties = [[5,5],[6,3],[3,6]]
# Output: 0
# Explanation: No character has strictly greater attack and defense than the
# other.
#
#
# Example 2:
#
#
# Input: properties = [[2,2],[3,3]]
# Output: 1
# Explanation: The first character is weak because the second character has a
# strictly greater attack and defense.
#
#
# Example 3:
#
#
# Input: properties = [[1,5],[10,4],[4,3]]
# Output: 1
# Explanation: The third character is weak because the second character has a
# strictly greater attack and defense.
#
#
#
# Constraints:
#
#
# 2 <= properties.length <= 10^5
# properties[i].length == 2
# 1 <= attacki, defensei <= 10^5
#
#
#
from collections import defaultdict
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        max_attack = max(properties)[0]
        max_defence = defaultdict(lambda: -float('inf'))
        for attack, defence in properties:
            max_defence[attack] = max(max_defence[attack], defence)
        for x in range(max_attack, 0, -1):
            max_defence[x - 1] = max(max_defence[x], max_defence[x - 1])
        return sum(
            int(max_defence[attack + 1] > defence)
            for attack, defence in properties)


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.numberOfWeakCharacters, Solution()),
        [
            [[[[1, 5], [10, 4], [4, 3]]], 1],
            [[[[5, 5], [6, 3], [3, 6]]], 0],
            [[[[2, 2], [3, 3]]], 1],
            [[[[18, 12], [33, 3], [47, 18], [27, 27], [26, 50], [43, 35],
               [41, 29], [11, 8], [34, 16], [40, 9], [38, 31], [15, 44],
               [40, 41], [26, 33], [14, 6], [48, 26], [14, 22], [38, 50],
               [45, 28], [40, 41]]], 13],
            [[[[16, 11], [28, 27], [33, 15], [49, 8], [14, 12], [42, 11],
               [36, 9], [7, 5], [16, 20], [46, 15], [34, 24],
               [29, 46], [21, 26], [39, 1], [28, 31], [29, 11], [49, 13],
               [14, 46], [29, 49], [49, 49], [16, 1], [14, 9], [39, 24],
               [11, 27], [18, 5], [30, 40], [31, 15], [11, 24], [48, 30],
               [26, 37], [41, 47], [44, 39], [6, 39], [2, 33], [1, 2],
               [28, 10], [50, 25], [23, 22], [40, 28], [32, 15], [25, 8],
               [9, 41], [43, 43], [23, 50], [40, 30], [22, 40], [45, 29],
               [4, 24], [20, 13], [21, 40], [36, 16], [38, 42], [19, 16],
               [34, 15], [23, 37], [41, 2], [36, 19], [26, 17], [41, 11],
               [3, 26], [15, 39], [24, 17], [4, 29], [22, 36], [37, 28],
               [26, 32], [2, 33], [11, 40], [12, 37], [38, 41], [18, 37],
               [5, 21], [24, 3], [4, 35], [17, 4], [29, 29], [13, 42],
               [10, 11], [7, 14], [34, 39], [23, 34], [45, 41], [42, 42],
               [27, 22], [26, 46], [6, 47], [21, 15], [50, 42], [31, 35],
               [28, 25], [20, 30], [4, 40], [16, 4], [15, 39], [7, 28],
               [49, 31], [15, 46], [47, 11], [48, 44], [34, 3]]], 95],
        ],
    )
