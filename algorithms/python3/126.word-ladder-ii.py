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
from collections import defaultdict, deque
from string import ascii_lowercase
from typing import List
from algo_input import run, any_order
from types import MethodType


# @lc code=start
class Solution:

    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        lookup = {x: idx for idx, x in enumerate(wordList)}
        if endWord not in lookup:
            return []
        graph = defaultdict(set)
        for w in wordList:
            for i in range(len(w)):
                for c in ascii_lowercase:
                    bridge_word = w[:i] + c + w[i + 1:]
                    if bridge_word in lookup:
                        x, y = lookup[bridge_word], lookup[w]
                        graph[x].add(y)
                        graph[y].add(x)
        start = lookup[beginWord]
        q, res, seen, end, max_depth, tree = deque(
            [[start,
              1]]), [], set(), lookup[endWord], float('inf'), defaultdict(set)
        while q:
            curr, depth = q.popleft()
            if depth > max_depth:
                break
            if curr == end:
                max_depth = depth
                continue
            if curr in seen:
                continue
            seen.add(curr)
            for e in graph[curr]:
                if e in seen:
                    continue
                tree[e].add(curr)
                q.append([e, depth + 1])

        def build(path: List[int]):
            if len(path) > max_depth:
                return
            if path[-1] == start:
                res.append(
                    list(wordList[path[x]]
                         for x in range(len(path) - 1, -1, -1)))
                return
            edge = path[-1]
            for next_edge in tree[edge]:
                path.append(next_edge)
                build(path)
                path.pop()

        build([end])
        return res


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.findLadders, Solution()), [
        [[
            "aaaaa", "ggggg",
            [
                "aaaaa", "caaaa", "cbaaa", "daaaa", "dbaaa", "eaaaa", "ebaaa",
                "faaaa", "fbaaa", "gaaaa", "gbaaa", "haaaa", "hbaaa", "iaaaa",
                "ibaaa", "jaaaa", "jbaaa", "kaaaa", "kbaaa", "laaaa", "lbaaa",
                "maaaa", "mbaaa", "naaaa", "nbaaa", "oaaaa", "obaaa", "paaaa",
                "pbaaa", "bbaaa", "bbcaa", "bbcba", "bbdaa", "bbdba", "bbeaa",
                "bbeba", "bbfaa", "bbfba", "bbgaa", "bbgba", "bbhaa", "bbhba",
                "bbiaa", "bbiba", "bbjaa", "bbjba", "bbkaa", "bbkba", "bblaa",
                "bblba", "bbmaa", "bbmba", "bbnaa", "bbnba", "bboaa", "bboba",
                "bbpaa", "bbpba", "bbbba", "abbba", "acbba", "dbbba", "dcbba",
                "ebbba", "ecbba", "fbbba", "fcbba", "gbbba", "gcbba", "hbbba",
                "hcbba", "ibbba", "icbba", "jbbba", "jcbba", "kbbba", "kcbba",
                "lbbba", "lcbba", "mbbba", "mcbba", "nbbba", "ncbba", "obbba",
                "ocbba", "pbbba", "pcbba", "ccbba", "ccaba", "ccaca", "ccdba",
                "ccdca", "cceba", "cceca", "ccfba", "ccfca", "ccgba", "ccgca",
                "cchba", "cchca", "cciba", "ccica", "ccjba", "ccjca", "cckba",
                "cckca", "cclba", "cclca", "ccmba", "ccmca", "ccnba", "ccnca",
                "ccoba", "ccoca", "ccpba", "ccpca", "cccca", "accca", "adcca",
                "bccca", "bdcca", "eccca", "edcca", "fccca", "fdcca", "gccca",
                "gdcca", "hccca", "hdcca", "iccca", "idcca", "jccca", "jdcca",
                "kccca", "kdcca", "lccca", "ldcca", "mccca", "mdcca", "nccca",
                "ndcca", "occca", "odcca", "pccca", "pdcca", "ddcca", "ddaca",
                "ddada", "ddbca", "ddbda", "ddeca", "ddeda", "ddfca", "ddfda",
                "ddgca", "ddgda", "ddhca", "ddhda", "ddica", "ddida", "ddjca",
                "ddjda", "ddkca", "ddkda", "ddlca", "ddlda", "ddmca", "ddmda",
                "ddnca", "ddnda", "ddoca", "ddoda", "ddpca", "ddpda", "dddda",
                "addda", "aedda", "bddda", "bedda", "cddda", "cedda", "fddda",
                "fedda", "gddda", "gedda", "hddda", "hedda", "iddda", "iedda",
                "jddda", "jedda", "kddda", "kedda", "lddda", "ledda", "mddda",
                "medda", "nddda", "nedda", "oddda", "oedda", "pddda", "pedda",
                "eedda", "eeada", "eeaea", "eebda", "eebea", "eecda", "eecea",
                "eefda", "eefea", "eegda", "eegea", "eehda", "eehea", "eeida",
                "eeiea", "eejda", "eejea", "eekda", "eekea", "eelda", "eelea",
                "eemda", "eemea", "eenda", "eenea", "eeoda", "eeoea", "eepda",
                "eepea", "eeeea", "ggggg", "agggg", "ahggg", "bgggg", "bhggg",
                "cgggg", "chggg", "dgggg", "dhggg", "egggg", "ehggg", "fgggg",
                "fhggg", "igggg", "ihggg", "jgggg", "jhggg", "kgggg", "khggg",
                "lgggg", "lhggg", "mgggg", "mhggg", "ngggg", "nhggg", "ogggg",
                "ohggg", "pgggg", "phggg", "hhggg", "hhagg", "hhahg", "hhbgg",
                "hhbhg", "hhcgg", "hhchg", "hhdgg", "hhdhg", "hhegg", "hhehg",
                "hhfgg", "hhfhg", "hhigg", "hhihg", "hhjgg", "hhjhg", "hhkgg",
                "hhkhg", "hhlgg", "hhlhg", "hhmgg", "hhmhg", "hhngg", "hhnhg",
                "hhogg", "hhohg", "hhpgg", "hhphg", "hhhhg", "ahhhg", "aihhg",
                "bhhhg", "bihhg", "chhhg", "cihhg", "dhhhg", "dihhg", "ehhhg",
                "eihhg", "fhhhg", "fihhg", "ghhhg", "gihhg", "jhhhg", "jihhg",
                "khhhg", "kihhg", "lhhhg", "lihhg", "mhhhg", "mihhg", "nhhhg",
                "nihhg", "ohhhg", "oihhg", "phhhg", "pihhg", "iihhg", "iiahg",
                "iiaig", "iibhg", "iibig", "iichg", "iicig", "iidhg", "iidig",
                "iiehg", "iieig", "iifhg", "iifig", "iighg", "iigig", "iijhg",
                "iijig", "iikhg", "iikig", "iilhg", "iilig", "iimhg", "iimig",
                "iinhg", "iinig", "iiohg", "iioig", "iiphg", "iipig", "iiiig",
                "aiiig", "ajiig", "biiig", "bjiig", "ciiig", "cjiig", "diiig",
                "djiig", "eiiig", "ejiig", "fiiig", "fjiig", "giiig", "gjiig",
                "hiiig", "hjiig", "kiiig", "kjiig", "liiig", "ljiig", "miiig",
                "mjiig", "niiig", "njiig", "oiiig", "ojiig", "piiig", "pjiig",
                "jjiig", "jjaig", "jjajg", "jjbig", "jjbjg", "jjcig", "jjcjg",
                "jjdig", "jjdjg", "jjeig", "jjejg", "jjfig", "jjfjg", "jjgig",
                "jjgjg", "jjhig", "jjhjg", "jjkig", "jjkjg", "jjlig", "jjljg",
                "jjmig", "jjmjg", "jjnig", "jjnjg", "jjoig", "jjojg", "jjpig",
                "jjpjg", "jjjjg", "ajjjg", "akjjg", "bjjjg", "bkjjg", "cjjjg",
                "ckjjg", "djjjg", "dkjjg", "ejjjg", "ekjjg", "fjjjg", "fkjjg",
                "gjjjg", "gkjjg", "hjjjg", "hkjjg", "ijjjg", "ikjjg", "ljjjg",
                "lkjjg", "mjjjg", "mkjjg", "njjjg", "nkjjg", "ojjjg", "okjjg",
                "pjjjg", "pkjjg", "kkjjg", "kkajg", "kkakg", "kkbjg", "kkbkg",
                "kkcjg", "kkckg", "kkdjg", "kkdkg", "kkejg", "kkekg", "kkfjg",
                "kkfkg", "kkgjg", "kkgkg", "kkhjg", "kkhkg", "kkijg", "kkikg",
                "kkljg", "kklkg", "kkmjg", "kkmkg", "kknjg", "kknkg", "kkojg",
                "kkokg", "kkpjg", "kkpkg", "kkkkg", "ggggx", "gggxx", "ggxxx",
                "gxxxx", "xxxxx", "xxxxy", "xxxyy", "xxyyy", "xyyyy", "yyyyy",
                "yyyyw", "yyyww", "yywww", "ywwww", "wwwww", "wwvww", "wvvww",
                "vvvww", "vvvwz", "avvwz", "aavwz", "aaawz", "aaaaz"
            ]
        ],
         [[
             "aaaaa", "aaaaz", "aaawz", "aavwz", "avvwz", "vvvwz", "vvvww",
             "wvvww", "wwvww", "wwwww", "ywwww", "yywww", "yyyww", "yyyyw",
             "yyyyy", "xyyyy", "xxyyy", "xxxyy", "xxxxy", "xxxxx", "gxxxx",
             "ggxxx", "gggxx", "ggggx", "ggggg"
         ]]],
        [["dog", "cog", ["cog"]], [["dog", "cog"]]],
        [["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]],
         [["hit", "hot", "dot", "dog", "cog"],
          ["hit", "hot", "lot", "log", "cog"]]],
        [["hit", "cog", ["cog"]], []],
        [[
            "leet", "code",
            ["lest", "leet", "lose", "code", "lode", "robe", "lost"]
        ], [["leet", "lest", "lost", "lose", "lode", "code"]]],
        [["hit", "cog", ["hot", "dot", "dog", "lat", "log", "cog"]],
         [["hit", "hot", "dot", "dog", "cog"]]],
        [["hit", "cog", ["hot", "dot", "dag", "lat", "log", "cog"]], []],
        [["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], []],
        [["hit", "cog", []], []],
        [[
            "cet", "ism",
            [
                "kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr",
                "gay", "sip", "kay", "per", "val", "mes", "ohs", "now", "boa",
                "cet", "pal", "bar", "die", "war", "hay", "eco", "pub", "lob",
                "rue", "fry", "lit", "rex", "jan", "cot", "bid", "ali", "pay",
                "col", "gum", "ger", "row", "won", "dan", "rum", "fad", "tut",
                "sag", "yip", "sui", "ark", "has", "zip", "fez", "own", "ump",
                "dis", "ads", "max", "jaw", "out", "btu", "ana", "gap", "cry",
                "led", "abe", "box", "ore", "pig", "fie", "toy", "fat", "cal",
                "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply", "awe",
                "pry", "tit", "tie", "yet", "too", "tax", "jim", "san", "pan",
                "map", "ski", "ova", "wed", "non", "wac", "nut", "why", "bye",
                "lye", "oct", "old", "fin", "feb", "chi", "sap", "owl", "log",
                "tod", "dot", "bow", "fob", "for", "joe", "ivy", "fan", "age",
                "fax", "hip", "jib", "mel", "hus", "sob", "ifs", "tab", "ara",
                "dab", "jag", "jar", "arm", "lot", "tom", "sax", "tex", "yum",
                "pei", "wen", "wry", "ire", "irk", "far", "mew", "wit", "doe",
                "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy", "nag",
                "ron", "soy", "gin", "don", "tug", "fay", "vic", "boo", "nam",
                "ave", "buy", "sop", "but", "orb", "fen", "paw", "his", "sub",
                "bob", "yea", "oft", "inn", "rod", "yam", "pew", "web", "hod",
                "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog",
                "bib", "rub", "ere", "dig", "era", "cat", "fox", "bee", "mod",
                "day", "apr", "vie", "nev", "jam", "pam", "new", "aye", "ani",
                "and", "ibm", "yap", "can", "pyx", "tar", "kin", "fog", "hum",
                "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan", "fey",
                "bus", "oak", "bad", "ats", "set", "qom", "vat", "eat", "pus",
                "rev", "axe", "ion", "six", "ila", "lao", "mom", "mas", "pro",
                "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may",
                "shy", "rid", "bat", "sum", "rim", "fee", "bmw", "sky", "maj",
                "hue", "thy", "ava", "rap", "den", "fla", "auk", "cox", "ibo",
                "hey", "saw", "vim", "sec", "ltd", "you", "its", "tat", "dew",
                "eva", "tog", "ram", "let", "see", "zit", "maw", "nix", "ate",
                "gig", "rep", "owe", "ind", "hog", "eve", "sam", "zoo", "any",
                "dow", "cod", "bed", "vet", "ham", "sis", "hex", "via", "fir",
                "nod", "mao", "aug", "mum", "hoe", "bah", "hal", "keg", "hew",
                "zed", "tow", "gog", "ass", "dem", "who", "bet", "gos", "son",
                "ear", "spy", "kit", "boy", "due", "sen", "oaf", "mix", "hep",
                "fur", "ada", "bin", "nil", "mia", "ewe", "hit", "fix", "sad",
                "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken", "wad",
                "rye", "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin",
                "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug", "asp",
                "hui", "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm",
                "nat", "wyo", "gym", "dug", "toe", "dee", "wig", "sly", "rip",
                "geo", "cog", "pas", "zen", "odd", "nan", "lay", "pod", "fit",
                "hem", "joy", "bum", "rio", "yon", "dec", "leg", "put", "sue",
                "dim", "pet", "yaw", "nub", "bit", "bur", "sid", "sun", "oil",
                "red", "doc", "moe", "caw", "eel", "dix", "cub", "end", "gem",
                "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton",
                "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil", "jig",
                "hub", "low", "did", "tin", "get", "gte", "sox", "lei", "mig",
                "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir",
                "sty", "lap", "two", "ins", "con", "ant", "net", "tux", "ode",
                "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow", "sal",
                "sic", "ted", "wot", "del", "imp", "cob", "way", "ann", "tan",
                "mci", "job", "wet", "ism", "err", "him", "all", "pad", "hah",
                "hie", "aim"
            ]
        ],
         [[
             "cet", "cat", "can", "ian", "inn", "ins", "its", "ito", "ibo",
             "ibm", "ism"
         ],
          [
              "cet", "cot", "con", "ion", "inn", "ins", "its", "ito", "ibo",
              "ibm", "ism"
          ]]],
    ],
        comparator=any_order)
