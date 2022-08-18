#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (27.07%)
# Likes:    4534
# Dislikes: 563
# Total Accepted:    321.1K
# Total Submissions: 1.2M
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
#
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
# be in wordList.
# sk == endWord
#
#
# Given two words, beginWord and endWord, and a dictionary wordList, return all
# the shortest transformation sequences from beginWord to endWord, or an empty
# list if no such sequence exists. Each sequence should be returned as a list
# of the words [beginWord, s1, s2, ..., sk].
#
#
# Example 1:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
#
#
# Example 2:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
#
#
#
# Constraints:
#
#
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 500
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
#
#
#
from collections import defaultdict
from typing import List, Set
from algo_input import run, any_order
from types import MethodType


# @lc code=start
class Solution:

    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        wordList = set(wordList)
        graph = defaultdict(set)
        for w in wordList:
            w_l = list(w)
            for b in range(len(w)):
                prev = w_l[b]
                for c_offset in range(26):
                    c = chr(ord('a') + c_offset)
                    if c == prev:
                        continue
                    w_l[b] = c
                    t = "".join(w_l)
                    if t in wordList:
                        graph[w].add(t)
                        graph[t].add(w)
                w_l[b] = prev
        res = []

        def dfs(curr: str, path: List[List[str]], seen: Set[str]):
            nonlocal res
            if res and len(path) > len(res[-1]):
                return
            if curr == endWord:
                if not res or len(res[-1]) > len(path):
                    res = []
                res.append(list(path))
                return
            if curr in seen:
                return
            seen.add(curr)
            for e in graph[curr]:
                path.append(e)
                dfs(e, path, seen)
                path.pop()
            seen.discard(curr)

        dfs(beginWord, [beginWord], set())
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.findLadders, Solution()),
        [
            # [["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
            #  [["hit", "hot", "dot", "dog", "cog"],
            #   ["hit", "hot", "lot", "log", "cog"]]],
            # [["dog", "cog", ["cog"]], [["dog", "cog"]]],
            # [["hit", "cog", ["cog"]], []],
            # [[
            #     "leet", "code",
            #     ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
            # ], [["leet", "lest", "lost", "lose", "lode", "code"]]],
            # [["hit", "cog", ["hot", "dot", "dog", "lat", "log", "cog"]],
            #  [["hit", "hot", "dot", "dog", "cog"]]],
            # [["hit", "cog", ["hot", "dot", "dag", "lat", "log", "cog"]], []],
            # [["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], []],
            # [["hit", "cog", []], []],
            [[
                "cet", "ism",
                [
                    "kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz",
                    "brr", "gay", "sip", "kay", "per", "val", "mes", "ohs",
                    "now", "boa", "cet", "pal", "bar", "die", "war", "hay",
                    "eco", "pub", "lob", "rue", "fry", "lit", "rex", "jan",
                    "cot", "bid", "ali", "pay", "col", "gum", "ger", "row",
                    "won", "dan", "rum", "fad", "tut", "sag", "yip", "sui",
                    "ark", "has", "zip", "fez", "own", "ump", "dis", "ads",
                    "max", "jaw", "out", "btu", "ana", "gap", "cry", "led",
                    "abe", "box", "ore", "pig", "fie", "toy", "fat", "cal",
                    "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply",
                    "awe", "pry", "tit", "tie", "yet", "too", "tax", "jim",
                    "san", "pan", "map", "ski", "ova", "wed", "non", "wac",
                    "nut", "why", "bye", "lye", "oct", "old", "fin", "feb",
                    "chi", "sap", "owl", "log", "tod", "dot", "bow", "fob",
                    "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib",
                    "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag",
                    "jar", "arm", "lot", "tom", "sax", "tex", "yum", "pei",
                    "wen", "wry", "ire", "irk", "far", "mew", "wit", "doe",
                    "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy",
                    "nag", "ron", "soy", "gin", "don", "tug", "fay", "vic",
                    "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen",
                    "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod",
                    "yam", "pew", "web", "hod", "hun", "gyp", "wei", "wis",
                    "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere",
                    "dig", "era", "cat", "fox", "bee", "mod", "day", "apr",
                    "vie", "nev", "jam", "pam", "new", "aye", "ani", "and",
                    "ibm", "yap", "can", "pyx", "tar", "kin", "fog", "hum",
                    "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan",
                    "fey", "bus", "oak", "bad", "ats", "set", "qom", "vat",
                    "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao",
                    "mom", "mas", "pro", "few", "opt", "poe", "art", "ash",
                    "oar", "cap", "lop", "may", "shy", "rid", "bat", "sum",
                    "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava",
                    "rap", "den", "fla", "auk", "cox", "ibo", "hey", "saw",
                    "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva",
                    "tog", "ram", "let", "see", "zit", "maw", "nix", "ate",
                    "gig", "rep", "owe", "ind", "hog", "eve", "sam", "zoo",
                    "any", "dow", "cod", "bed", "vet", "ham", "sis", "hex",
                    "via", "fir", "nod", "mao", "aug", "mum", "hoe", "bah",
                    "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem",
                    "who", "bet", "gos", "son", "ear", "spy", "kit", "boy",
                    "due", "sen", "oaf", "mix", "hep", "fur", "ada", "bin",
                    "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye",
                    "hop", "haw", "wax", "mid", "tad", "ken", "wad", "rye",
                    "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin",
                    "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug",
                    "asp", "hui", "yak", "bay", "poi", "yep", "bun", "try",
                    "lad", "elm", "nat", "wyo", "gym", "dug", "toe", "dee",
                    "wig", "sly", "rip", "geo", "cog", "pas", "zen", "odd",
                    "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio",
                    "yon", "dec", "leg", "put", "sue", "dim", "pet", "yaw",
                    "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc",
                    "moe", "caw", "eel", "dix", "cub", "end", "gem", "off",
                    "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton",
                    "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil",
                    "jig", "hub", "low", "did", "tin", "get", "gte", "sox",
                    "lei", "mig", "fig", "lon", "use", "ban", "flo", "nov",
                    "jut", "bag", "mir", "sty", "lap", "two", "ins", "con",
                    "ant", "net", "tux", "ode", "stu", "mug", "cad", "nap",
                    "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot",
                    "del", "imp", "cob", "way", "ann", "tan", "mci", "job",
                    "wet", "ism", "err", "him", "all", "pad", "hah", "hie",
                    "aim"
                ]
            ],
             [[
                 "cet", "cat", "can", "ian", "inn", "ins", "its", "ito", "ibo",
                 "ibm", "ism"
             ],
              [
                  "cet", "cot", "con", "ion", "inn", "ins", "its", "ito",
                  "ibo", "ibm", "ism"
              ]]],
        ],
        comparator=any_order)
