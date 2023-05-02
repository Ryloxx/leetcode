#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (28.19%)
# Likes:    2880
# Dislikes: 2122
# Total Accepted:    295.1K
# Total Submissions: 984.8K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of
# each word in words exactly once, in any order, and without any intervening
# characters.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
#
#
# Example 3:
#
#
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.
#
#
#
from collections import Counter
from functools import reduce
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # N = len(s), M = len(words), P = len(words[i])

    # Using a rolling hash
    # O(M * P + N) time complexity
    # O(M + N) space complexity
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        words_len, w_len, res, p = len(words), len(words[0]), [], 31

        # This mod is good enough for this Leetcode problem but a higher one
        # should be safer like 7 + 10**9
        mod = 389

        words = Counter(
            reduce(lambda acc, curr: (acc * p + ord(curr)) % mod, w, 0)
            for w in words)
        rolling_hash, p_limit = 0, pow(p, w_len, mod)
        hashes = [
            rolling_hash :=  # noqa: F841
            (rolling_hash * p + ord(s[idx]) -
             (ord(s[idx - w_len]) * p_limit if idx >= w_len else 0)) % mod
            for idx in range(len(s))
        ]

        for i in range(w_len):
            word_count, start, w_count = Counter(), i + w_len - 1, 0
            for idx in range(start, len(s), w_len):
                w_hash = hashes[idx]
                if w_hash not in words:
                    word_count, start, w_count = Counter(), idx + w_len, 0
                    continue
                while word_count[w_hash] == words[w_hash]:
                    word_count[hashes[start]] -= 1
                    start += w_len
                    w_count -= 1
                word_count[w_hash] += 1
                w_count += 1
                if w_count == words_len:
                    res.append(idx - w_count * w_len + 1)
                    word_count[hashes[start]] -= 1
                    start += w_len
                    w_count -= 1

        return res

    # Using string slicing
    # O(M + P * N) time complexity
    # O(M * P) space complexity
    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     if not words:
    #         return []
    #     res = []
    #     len_s, len_words, len_w = len(s), len(words), len(words[0])
    #     wds = Counter(words)
    #     for i in range(len_w):
    #         window, start, c = Counter(), i, 0
    #         while i < len_s:
    #             w = s[i:i + len_w]
    #             if w not in wds:
    #                 window, start, c = Counter(), i + len_w, 0
    #             else:
    #                 window[w] += 1
    #                 c += 1
    #                 while window[w] > wds[w]:
    #                     window[s[start:start + len_w]] -= 1
    #                     c -= 1
    #                     start += len_w
    #                 if c == len_words:
    #                     res.append(start)
    #             i += len_w
    #     return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findSubstring, Solution()),
        [
            [["barfoothefoobarman", ["foo", "bar"]], [0, 9]],
            [["barfoofoobarthefoobarman", ["bar", "foo", "the"]], [6, 9, 12]],
            [["ababababab", ["ababa", "babab"]], [0]],
            [["wordgoodgoodgoodbestword", ["word", "good", "best", "good"]],
             [8]],
            [[
                "pjzkrkevzztxductzzxmxsvwjkxpvukmf"
                "jywwetvfnujhweiybwvvsrfequzkhossm"
                "ootkmyxgjgfordrpapjuunmqnxxdrqrfg"
                "krsjqbszgiqlcfnrpjlcwdrvbumtotzyl"
                "shdvccdmsqoadfrpsvnwpizlwszrtyclh"
                "gilklydbmfhuywotjmktnwrfvizvnmfvv"
                "qfiokkdprznnnjycttprkxpuykhmpchik"
                "syucbmtabiqkisgbhxngmhezrrqvayfsx"
                "auampdpxtafniiwfvdufhtwajrbkxtjzq"
                "jnfocdhekumttuqwovfjrgulhekcpjszy"
                "ynadxhnttgmnxkduqmmyhzfnjhducesct"
                "ufqbumxbamalqudeibljgbspeotkgvddc"
                "wgxidaiqcvgwykhbysjzlzfbupkqunuqt"
                "raxrlptivshhbihtsigtpipguhbhctcvu"
                "bnhqipncyxfjebdnjyetnlnvmuxhzsdah"
                "krscewabejifmxombiamxvauuitoltyym"
                "sarqcuuoezcbqpdaprxmsrickwpgwpsop"
                "lhugbikbkotzrtqkscekkgwjycfnvwfgd"
                "zogjzjvpcvixnsqsxacfwndzvrwrycwxr"
                "cismdhqapoojegggkocyrdtkzmiekhxop"
                "pctytvphjynrhtcvxcobxbcjjivtfjiwm"
                "duhzjokkbctweqtigwfhzorjlkpuuliai"
                "pbtfldinyetoybvugevwvhhhweejogrgh"
                "llsouipabfafcxnhukcbtmxzshoyyufjh"
                "zadhrelweszbfgwpkzlwxkogyogutscvu"
                "hcllphshivnoteztpxsaoaacgxyaztuix"
                "hunrowzljqfqrahosheukhahhbiaxqzfm"
                "mwcjxountkevsvpbzjnilwpoermxrtlfr"
                "oqoclexxisrdhvfsindffslyekrzwzqkp"
                "eocilatftymodgztjgybtyheqgcpwogdc"
                "jlnlesefgvimwbxcbzvaibspdjnrpqtye"
                "ilkcspknyylbwndvkffmzuriilxagyerj"
                "ptbgeqgebiaqnvdubrtxibhvakcyotkfo"
                "nmseszhczapxdlauexehhaireihxsplgd"
                "gmxfvaevrbadbwjbdrkfbbjjkgcztkcbw"
                "agtcnrtqryuqixtzhaakjlurnumzyovaw"
                "rcjiwabuwretmdamfkxrgqgcdgbrdbnug"
                "zecbgyxxdqmisaqcyjkqrntxqmdrczxbe"
                "bemcblftxplafnyoxqimkhcykwamvdsxj"
                "ezkpgdpvopddptdfbprjustquhlazkjfl"
                "uxrzopqdstulybnqvyknrchbphcarknnh"
                "hovweaqawdyxsqsqahkepluypwrzjegqt"
                "doxfgzdkydeoxvrfhxusrujnmjzqrrlxg"
                "lcmkiykldbiasnhrjbjekystzilrwkzho"
                "ntwmehrfsrzfaqrbbxncphbzuuxeteshy"
                "rveamjsfiaharkcqxefghgceeixkdgkub"
                "oupxnwhnfigpkwnqdvzlydpidcljmflbc"
                "carbiegsmweklwngvygbqpescpeichmfi"
                "dgsjmkvkofvkuehsmkkbocgejoiqcnafv"
                "uokelwuqsgkyoekaroptuvekfvmtxtqsh"
                "cwsztkrzwrpabqrrhnlerxjojemcxel",
                [
                    "dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila",
                    "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj",
                    "lnle", "sefg", "vimw", "bxcb"
                ]
            ], [935]],
            [["aaa", ["a", "b"]], []],
            [["", []], []],
            [["aaa", ["aa", "aa"]], []],
            [["mississippi", ["mississippis"]], []],
        ],
    )
