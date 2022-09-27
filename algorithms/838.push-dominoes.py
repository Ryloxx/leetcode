#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#
# https://leetcode.com/problems/push-dominoes/description/
#
# algorithms
# Medium (52.36%)
# Likes:    2836
# Dislikes: 173
# Total Accepted:    100.2K
# Total Submissions: 175.7K
# Testcase Example:  '"RR.L"'
#
# There are n dominoes in a line, and we place each domino vertically upright.
# In the beginning, we simultaneously push some of the dominoes either to the
# left or to the right.
#
# After each second, each domino that is falling to the left pushes the
# adjacent domino on the left. Similarly, the dominoes falling to the right
# push their adjacent dominoes standing on the right.
#
# When a vertical domino has dominoes falling on it from both sides, it stays
# still due to the balance of the forces.
#
# For the purposes of this question, we will consider that a falling domino
# expends no additional force to a falling or already fallen domino.
#
# You are given a string dominoes representing the initial state where:
#
#
# dominoes[i] = 'L', if the i^th domino has been pushed to the left,
# dominoes[i] = 'R', if the i^th domino has been pushed to the right, and
# dominoes[i] = '.', if the i^th domino has not been pushed.
#
#
# Return a string representing the final state.
#
#
# Example 1:
#
#
# Input: dominoes = "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second
# domino.
#
#
# Example 2:
#
#
# Input: dominoes = ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
#
#
#
# Constraints:
#
#
# n == dominoes.length
# 1 <= n <= 10^5
# dominoes[i] is either 'L', 'R', or '.'.
#
#
#
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def pushDominoes(self, dominoes: str) -> str:
        dominoes = "L" + dominoes + "R"
        res = ""
        i = 0
        for j in range(1, len(dominoes)):
            if dominoes[j] == ".":
                continue
            length = j - i - 1
            if i:
                res += dominoes[i]
            if dominoes[i] == dominoes[j]:
                res += dominoes[i] * length
            elif dominoes[i] == "R":
                res += (length // 2) * dominoes[i] + "." * (length % 2) + (
                    length // 2) * dominoes[j]
            else:
                res += "." * length
            i = j
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.pushDominoes, Solution()),
        [
            [["RR.L"], "RR.L"],
            [[".L.R...LR..L.."], "LL.RR.LLRRLL.."],
            [[""], ""],
        ],
    )
