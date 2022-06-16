#
# @lc app=leetcode id=1044 lang=python3
#
# [1044] Longest Duplicate Substring
#
# https://leetcode.com/problems/longest-duplicate-substring/description/
#
# algorithms
# Hard (31.10%)
# Likes:    1717
# Dislikes: 336
# Total Accepted:    54.2K
# Total Submissions: 175K
# Testcase Example:  '"banana"'
#
# Given a string s, consider all duplicated substrings: (contiguous) substrings
# of s that occur 2 or more times. The occurrences may overlap.
#
# Return any duplicated substring that has the longest possible length. If s
# does not have a duplicated substring, the answer is "".
#
#
# Example 1:
# Input: s = "banana"
# Output: "ana"
# Example 2:
# Input: s = "abcd"
# Output: ""
#
#
# Constraints:
#
#
# 2 <= s.length <= 3 * 10^4
# s consists of lowercase English letters.
#
#
#
from algo_input import run
from types import MethodType
# @lc code=start


class Solution:

    def longestDupSubstring(self, s: str) -> str:

        def checkForLength(length):
            seen = set()
            for x in range(len(s)):
                sub = s[x:x + length]
                if sub in seen:
                    return sub
                seen.add(sub)
            return ""

        lo, hi, res = 0, len(s), ""
        while lo < hi:
            mid = (lo + hi) // 2
            isValidLength = checkForLength(mid)
            if isValidLength:
                res = isValidLength
                lo = mid + 1
            else:
                hi = mid
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestDupSubstring, Solution()),
        [
            [["kbanakba"], "kba"],
            [["aa"], "a"],
            [["banana"], "ana"],
            [["sfsvkvthtddxsvtdd"], "tdd"],
            [["abcd"], ""],
            [[
                "nyvzwttxsshphczjjklqniaztccdrawueylaelk"
                "qtjtxdvutsewhghcmoxlvqjktgawwgpytuvoepn"
                "yfbdywpmmfukoslqvdrkuokxcexwugogcwvsuhc"
                "ziwuwzfktjlhbiuhkxcreqrdbj"
            ], "hcz"],
            [[
                "pmyiaxmicpmvqywlkisfzzutlxxjipitwcfxgqq"
                "fnxizowkqfmzsvkxryknasyvthozahbmapwqocu"
                "pxcktmmtddxgatzftamrsvtddjpbnrojcqonmzx"
                "mknashplmykdbadiiccdkbyyzifqxvqfwgwihxg"
                "nrhqlmqprnjawuzcotutbkgnykuuwtzzzppmoyf"
                "mplhpznpnlwwbndekakpsmehzmbcfoyudgwsveh"
                "zgsfwqdkihiiwxfskicrbmoevxvpmmymihlkmgn"
                "uyohcofzfkehccwxezxypnnvqzrilr"
            ], "knas"],
            [["nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy"], "ma"],
            [[
                "bevcduddeblkojppqffscovgumdefmmoecxauhp"
                "yennopqbrfzrvrawhlncggqlgafamkashszwnog"
                "eutmfxhpfoetzxbzvqmsjb"
            ], "de"],
        ],
    )
