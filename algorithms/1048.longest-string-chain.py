#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (57.87%)
# Likes:    3546
# Dislikes: 167
# Total Accepted:    209.7K
# Total Submissions: 361.9K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# You are given an array of words where each word consists of lowercase English
# letters.
#
# wordA is a predecessor of wordB if and only if we can insert exactly one
# letter anywhere in wordA without changing the order of the other characters
# to make it equal to wordB.
#
#
# For example, "abc" is a predecessor of "abac", while "cba" is not a
# predecessor of "bcad".
#
#
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1,
# where word1 is a predecessor of word2, word2 is a predecessor of word3, and
# so on. A single word is trivially a word chain with k == 1.
#
# Return the length of the longest possible word chain with words chosen from
# the given list of words.
#
#
# Example 1:
#
#
# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
#
#
# Example 2:
#
#
# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
# Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc",
# "pcxbc", "pcxbcf"].
#
#
# Example 3:
#
#
# Input: words = ["abcd","dbqca"]
# Output: 1
# Explanation: The trivial word chain ["abcd"] is one of the longest word
# chains.
# ["abcd","dbqca"] is not a valid word chain because the ordering of the
# letters is changed.
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of lowercase English letters.
#
#
#
from itertools import chain
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    MAX_WORD_LENGTH = 16

    # N = len(words), M = max(len(words[i]))
    # O(N * M**2) time complexity
    # O(N * M) space complexity
    def longestStrChain(self, words: List[str]) -> int:
        if not words:
            return 0
        # Bucket sort the words using length of words
        buckets = [[] for _ in range(Solution.MAX_WORD_LENGTH + 1)]
        dp = {}
        res = 0
        for w in words:
            buckets[len(w)].append(w)
        for w in chain.from_iterable(buckets):
            value = max(
                dp.get(w[:idx] + w[idx + 1:], 0) for idx in range(len(w))) + 1
            dp[w] = value
            res = max(res, value)
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.longestStrChain, Solution()),
        [
            [[["a", "b", "ba", "bca", "bda", "bdca"]], 4],
            [[["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]], 5],
            [[["abcd", "dbqca"]], 1],
            [[["a"]], 1],
            [[[
                "uiykgmcc", "jrgbss", "mhkqodcpy", "lkj", "bwqktun", "s",
                "nrctyzifwytjblwy", "wrp", "scqlcwmxw", "irqvnxdcxoejuu",
                "gmlckvofwyifmrw", "wbzbyrcppaljigvo", "lk", "kfeouqyyrer",
                "efzzpvi", "ubkcitcmwxk", "txihn", "mdwdmbtx", "vuzvcoaif",
                "jwmboqvhpqodsj", "wscfvrfl", "pzye", "waxyoxftvrgqmkg",
                "wwdidopozinxxn", "dclpg", "xjsvlxktxs", "ajj", "pvsdastm",
                "tatjxhygidhn", "feafycxdxagn", "irqvnxxoeuu", "kwjo",
                "tztoovsyfwz", "prllrw", "sclmx", "bbmjnwaxcwaml", "gl",
                "wiax", "uzvcoaif", "ztovyfwz", "qxy", "zuexoxyp", "qxyyrl",
                "pvsdasvtm", "femafycxdxaagn", "rspvccjcm", "wvyiax", "vst",
                "efzi", "fjmdcc", "icsinrbpql", "ctybiizlcr", "ntyzfwytjblw",
                "tatjxhygidhpn", "e", "kykizdandafusu", "pnepuwcsxl",
                "kfeuqyyrer", "afplzhbqguu", "hvajtj", "prll", "ildzdimea",
                "zueoxp", "ezi", "lqr", "jkaagljikwamaqvf", "mlzwhkxsn",
                "rspvccbcjjtcm", "wscfvrl", "m", "msygukwlkrqboc",
                "pifojogoveub", "bkcmwx", "jercgybhss", "wrpi",
                "aicsinkgrbpqli", "aplzbuu", "sclcmxw", "atpepgsz",
                "govrcuuglaer", "bdxjpsvlxkytxs", "uikgm", "bm", "wvyhiqax",
                "znvaasgfvqi", "hatpepgsz", "hrzebpa", "bnfz", "lybtqrfzw",
                "taxhygihn", "bjnfzk", "mhqp", "ide", "znvcaasgfvqi", "ftv",
                "afplzhbqsguuu", "thn", "pdbccbe", "mxevopfoimgjww",
                "fjmdrcce", "rspvccjjcm", "jv", "motnfwohwule", "xjsvlxtxs",
                "bqeb", "eug", "jftavwgl", "rzebpa", "lybtqrfazw", "zuexoxp",
                "jercgybhsys", "hajtj", "bkcitcmwxk", "mbpvxsdastvtm",
                "mowlznwhkxsn", "dvenn", "rsacxe", "tatjxhygihn",
                "cotybiizlcr", "bbmnaxaml", "pkwrpsi", "nqpdbccbkxens",
                "mbpbovxsdastvtm", "mj", "pxpsvikwekuq", "qeug", "dmelddga",
                "aicsinkgrbpxqli", "bdxjpsvlxktytxs", "pkrllrxw",
                "jkgljikwmaqf", "iddie", "ctybiizcr", "nyzfwytjblw",
                "yvuhmiuehspi", "keuqre", "wzbypaigvo", "sck", "uzcoaf",
                "dlpg", "ubkcpitlscmwxk", "molzwhkxsn", "pepuwcsxl", "laplm",
                "dclpgc", "mahkxqodcpy", "sclcmx", "hvrzebpaz",
                "bgovrcuuglaer", "clazpulmw", "yvuyhmiuehspiq",
                "wzbycpaljigvo", "sceqalciwmxw", "hjytflmvsgv", "u",
                "hjyvxytfflhmvsgv", "jkgjikwmaqf", "fefycxdxagn", "ftvw",
                "ofncgxrkqvcr", "spvcjc", "pvsdastvtm", "kykzdandaus",
                "wbzbycppaljigvo", "haytpepgsz", "jmowlznwhkxsn", "aplzhbguu",
                "zvyz", "nfvqi", "jfvtavwsgl", "xejnllhfulns", "zhhvbiqiw",
                "jkgljikwmaqvf", "tyizc", "irqvnxcxoejuu", "clvazzpulmw",
                "oncgxrqvcr", "qlupvpdkhrm", "mtnfwohwule", "wwdidopzozinxxn",
                "auiykgmcc", "wscfvrfyl", "pfksmrullrxw", "jwmoqvhpqods",
                "ftavwg", "iddiea", "kcmw", "ykkwjwo", "pe", "aplzbguu", "eu",
                "bbmnaxal", "ntyswtnlab", "zhhhvbhbiqiw", "jwmoqvpqods",
                "kykzdndaus", "bbmjnaxcwaml", "zunvcaasgfvqi", "icsingrbpql",
                "sceqalciwmsxyw", "yvuhmiuehsp", "bxjsvlxktxs",
                "waxoxftvrgqmkg", "cogxxpaknks", "scllvazzpulmw",
                "tatjxhygeidhpn", "ftvwg", "tyz", "nafvqi", "oby", "pgzpkhqog",
                "irqvnxxoejuu", "oxwpkxlakcp", "bnf", "oxwnpkxlakcp", "bwqktu",
                "ufybbaozoqk", "ntydswtnlab", "zvyfz", "znaafvqi", "npdbccbke",
                "mhkqocpy", "kuq", "bjnfz", "taxhyihn", "kwrpsi",
                "qifepmcatbdjlf", "lzwhks", "kfeuqre", "mxevopfoimgww",
                "spvcjcm", "oncgxrkqvcr", "jftavwsgl", "soifcbya", "jpzyeg",
                "jwmboqvhpqods", "lapulm", "jrgbhss", "xejfnllhfulns",
                "zhhhvbbiqiw", "km", "kuqre", "scxlzlvazzpulmw", "ztvyfwz",
                "wbzbycpaljigvo", "rzbpa", "vsastm", "uybaooqk", "dn",
                "ykwjwo", "ufybmvbaozoqk", "nknm", "mbpvsdastvtm",
                "dpgzpxykhqog", "wzbypajigvo", "bnjnfzk", "eollbigtftpdrd",
                "zhbiqiw", "yvuhiuehp", "zhhhvbhbiqiwg", "pfksrullrxw",
                "pzyeg", "aplzhbqguu", "z", "hvrzecbpazw", "clvazpulmw",
                "tajxhygihn", "pgzpxykhqog", "fefyxdxagn", "wimomuvhn",
                "lqrzw", "xejnlhfulns", "jhrc", "xsxxs", "slmx", "jrgss",
                "uikgmc", "ncgqvcr", "womuhn", "aryouvtnmme", "uzco",
                "zhhhvbiqiw", "hjytflhmvsgv", "znvaasfvqi", "kuqr", "ojrpp",
                "ztoovyfwz", "zvz", "pxpsviweuq", "ufybaooqk", "xy",
                "jfvvtavwksvgl", "raiachv", "bmnaxl", "rspvccjjtcm",
                "pgzpxkhqog", "xhbtfnqebaj", "sceqalciwmsxw", "jssctk",
                "uzvcoaf", "fefydxagn", "jhrvc", "mbj", "raiahv",
                "nrtyzifwytjblwy", "mhqcp", "jkgjkwmaqf", "wscfvrfylhi",
                "lqrz", "ahabucermswyrvl", "wxoxftvrgqmkg", "ku", "uyaoq",
                "mhqocp", "ykwjo", "vstm", "ofncgxrkqvcwr", "dqvh", "taxyihn",
                "idie", "bwqtu", "tztoovyfwz", "rspvcccjjtcm", "uojrpp",
                "wmomuhn", "cotycbiizlxcr", "nrtyzfwytjblw", "ocbya",
                "sceqlciwmxw", "ajtj", "rspvccbcjjthcm", "kfeuqyyre",
                "dmelddg", "txyihn", "ubkcitlscmwxk", "ntyswtnla",
                "bdxjpstvlxktytxs", "odqdvbh", "pxpsvikeewekuq", "mdwdmbdtux",
                "vs", "bma", "wzbypigvo", "qxyy", "vsstm", "hbtnqeba",
                "hrzebpaz", "xhbtfnjsqebbaj", "ahaucermswyrv", "ddmbtx",
                "zhhbiqiw", "pxpsvikewekuq", "odqdvgbh", "bxjpsvlxktxs",
                "jsck", "fjmdc", "mdwdmbdtx", "jqxyyrl", "pxpsvikweuq",
                "ctybizcr", "dqvbh", "lpl", "lqrfzw", "ufybaozoqk",
                "znvaafvqi", "yvuhmiuehp", "hvrzebpazw", "pfksrllrxw", "alzuu",
                "xjsvxtxs", "afplzhbqguuu", "icsingrbpqli", "hjxytflhmvsgv",
                "femafycxdxagn", "uyaoqk", "gmlckvofwyifrw", "cinrbpql",
                "jrcgbhss", "oxwpkxlkcp", "jkagljikwamaqvf", "eollbigtftpdrdy",
                "rspvcjcm", "socbya", "clapulm", "qeb", "kwrpi", "efzpi",
                "hbtfnqebaj", "kykizdnandafusu", "sclvazzpulmw", "efzzpvvi",
                "jfvvtavwsvgl", "mhqocpy", "v", "mbpbvxsdastvtm", "irqvnxouu",
                "hvaajtj", "ofnlcgxrkqvcwr", "hbtqeba", "hbtqeb", "jwmqpds",
                "ntrnlhujdslco", "zv", "npdbccbken", "mhp", "ddb", "prllw",
                "mddmbtx", "clazpulm", "cogxxpaknkse", "bkitcmwxk",
                "oxwpklkcp", "tyiz", "jwmqvpqods", "waxyoxftvrgqmkgb",
                "afplzhbbqsgujuu", "bwtu", "jercgbhss", "rsacx", "mahkqodcpy",
                "cotycbiizlcr", "ahabucermswyrv", "lupvpkhr", "dvnn", "b",
                "atpepsz", "ncgxqvcr", "qe", "ubkcitlcmwxk", "lyqrfzw",
                "wimomuhn", "bbmnaxl", "motnfwohrwule", "yvuyhmiuehspi",
                "jfvvtavwsgl", "rac", "fefdxagn", "bwqkctun", "uotjrpp",
                "ddbtx", "afplzhbbqsguuu", "xss", "xsxs", "wvyiqax",
                "kykizdandaus", "npdbccbkens", "r", "oxwnpkxjlakcp",
                "tzmteoovsyfwz", "kykizdnandafuspu", "ahabulcermswyrvl",
                "xjsxxs", "qxyyr", "ck", "xhbtfnqebbaj", "nqpdbccbkens",
                "mpvsdastvtm", "zuexqoxyp", "gmlkvofwyifrw", "kmw", "txhn",
                "kykizdandausu", "molznwhkxsn", "lupvpdkhr", "jwmqvpds",
                "bktcmwx", "wyiax", "hzvaajtj", "ddbx", "pifojogveub",
                "naafvqi", "motnfwjohrwule", "odqvbh", "aicsingrbpqli",
                "jopzyeg", "lybtqrfazrw", "pijogveub", "xzejfnllhfulns",
                "scxllvazzpulmw", "irqyvnxdcxfoejuu", "cogxpaknks", "pdkwrpsi",
                "wzbycpajigvo", "xjsxtxs", "irqvnxdcxfoejuu", "xhbtfnjqebbaj",
                "uybaoqk", "oncgxqvcr", "aj", "pepuwsxl", "lytqrfzw", "nkm",
                "jrgs", "pkrllrw", "wscfvrfyli", "bbmjnaxcaml", "jftavwg",
                "vuzvcozaif", "pifjogveub", "cmogxxpaknkse", "cinrbql",
                "scqlciwmxw", "ztvyfz", "mxyevopfoimgjpww", "soicbya",
                "lupvpdkhrm", "ahaucermsyrv", "ufybmvbaouzoqk",
                "bdxjpsvlxktxs", "hjxytfflhmvsgv", "hjvxytfflhmvsgv",
                "nqpdbccbzkxens", "wr", "kykzdndus", "iddimea", "fjmdrcc",
                "efzzpi", "vsdastm", "btqeb", "pfkrllrxw", "ocby",
                "irqvnxxouu", "ildzpdimea", "lzwhkxsn", "ilddimea",
                "ufybvbaozoqk", "mxyevopfoimgjww", "jhr", "kcmwx", "dvn",
                "uzcof", "glw", "hbtnqebaj", "riahv", "w", "qeugv", "kfeuqyre",
                "ilrdzpdimea", "lplm", "icinrbpql", "scqlcmxw", "bbmjnaxaml",
                "e", "rsac", "bf", "jwmqvpqds", "tzteoovsyfwz", "rc",
                "lzwhkxs", "jkgljikwamaqvf", "tybizc", "aplzuu",
                "nrtyzifwytjblw", "pze", "bktcmwxk", "uiykgmc", "jsctk",
                "npdbccbe", "tybizcr"
            ]], 15],
            [[[
                "qyssedya", "pabouk", "mjwdrbqwp", "vylodpmwp", "nfyqeowa",
                "pu", "paboukc", "qssedya", "lopmw", "nfyqowa", "vlodpmw",
                "mwdrqwp", "opmw", "qsda", "neo", "qyssedhyac", "pmw",
                "lodpmw", "mjwdrqwp", "eo", "nfqwa", "pabuk", "nfyqwa",
                "qssdya", "qsdya", "qyssedhya", "pabu", "nqwa", "pabqoukc",
                "pbu", "mw", "vlodpmwp", "x", "xr"
            ]], 8],
            [[[
                "brwbne", "otixjfysmyjuwf", "yvnhnlbdeqcbazbj", "mezjcgr",
                "vhzfhpsnsea", "nlcj", "gzsgzput", "hqmhdrfqscasni", "wuepe",
                "dvqqabnobvhgqj", "ujrlukpvukgs", "pnxoagc", "oixjfysmuf",
                "vyrv", "qgxxbc", "ivfyrwvnipzj", "ebzrjz", "fzjq",
                "ijtrxgnkw", "cktgcqlfv", "utjrlukgpvukgs", "tclf", "sidvq",
                "npyolrgguid", "mdotbuot", "nrjaxkzsfek", "ujrkvuks", "whpj",
                "xfpfzjq", "rhjhdie", "qmhdss", "eamvlkwq", "invp",
                "njaxkzsfek", "mebvdidzaveyx", "hqmhdfqscsni", "ivyrwvnipzj",
                "zennejgi", "iwujepfes", "senzxcmjofsinag", "uafwwwhg",
                "tvgygpmscwc", "vaeyrhkcf", "ceskvurcmzb", "zenngi",
                "bwkpebmpgfhy", "ivfyrwvnipzjd", "ycofhg", "xyiacxzhnac",
                "dqxlsbfdmyn", "npyolrgqguiwd", "ultcahoyz", "ivyrvnizj",
                "pbshtsoeuo", "rjhdie", "hqmhdqscsi", "rrgdj", "yoggpjr",
                "pybbpn", "xacxzac", "irxkgpmpv", "xfazpfjkzjsgq",
                "bdidzaveyx", "eogdhhi", "pnoagc", "mybbrkwsbnuxje",
                "senzxmjofsinag", "ivyrviz", "bze", "epevejifzvkud", "rbe",
                "nirjaxkzswfek", "azsjb", "ceskvburcmzb", "pybshtsoetuot", "r",
                "rkmp", "ah", "xfyazpfjkzjsgqj", "npyolrgguiwd", "xiacxzhnac",
                "qxhvdxibyqjsnom", "pybbkkpnjd", "xxb", "cxrcyxuhlzcll",
                "iyejuejeqn", "mdotbuoqt", "cbwaxyv", "cf", "jgebzrjz",
                "ebzrz", "kcazotwzfalckzey", "kwujgyxnsactcov", "evq", "asjb",
                "hqmhdscsi", "senzxjfsiag", "arkhfjhfxduiee", "byzlqte",
                "pnaxoragc", "skfpnaxoragc", "yevq", "oijfymuf", "oixjfymuf",
                "yoggjpjrq", "ivyrvz", "skfpnwaxoragc", "rmp", "si", "xazac",
                "kfixgt", "mdtuot", "dvnqxlgsbfdmyn", "spnaxoragc",
                "mebvdidzacveyxf", "f", "xffzjq", "jqztcybler", "jtrgk",
                "ulahoyz", "epevejxifzvvkqud", "yoggjpjr", "bzlqte",
                "cqazysjb", "vyv", "srswyftkzn", "bz", "uawwhg", "meizjcgr",
                "vaeyrhykchf", "ohhi", "bwkpebmpgfuhy", "kfixggt", "imc",
                "brwbnue", "vaeyrhkchf", "xfazpfjkzjsgqj", "mdotbguoqt",
                "jebzrjz", "utjrlukgpmvukgs", "gzsgzpu", "tvgygpmqskcwc",
                "epy", "xaza", "cofg", "avhlkzneu", "ayrhkf", "ijtrxgxnkw",
                "yciofhg", "bgnkclvr", "eoghhi", "arkhfjhfxduigeve",
                "kfixggty", "tetmllxujt", "qgigwnrfatzcr", "hqmhdfqscasni",
                "tetmlnlxujt", "zeyhnvt", "uqdpolfskzamh", "ic", "cbx",
                "uqdpofskzamh", "bebmpgy", "aeyrhkcf", "xfapfjkzjsgq",
                "vqbnobvhqj", "ctetmlnlxujt", "siv", "mbbrwbnuxe",
                "arkhfjhduiee", "uawh", "ijmlc", "rhjhdiee", "ebz", "xaxzac",
                "cebwaxyv", "amdovftbguoqtp", "ijtrgk", "yevqzy",
                "kwujgyxnsctcov", "mybbrkwsjbnuxje", "avnhlkzneu",
                "dqxlbfdmyn", "pcebwaxyv", "ecqazyspjb", "oijfymf", "yolrggui",
                "fqnwxughwwrhq", "pbshtsoetuo", "wpj", "qgigwnrrfatzcr",
                "nlbcabj", "srsytkzn", "xgiwoujepfes", "mdotbguoqtp",
                "xfapfjzjsgq", "wvbvp", "ibtaj", "pybbkpnj", "zennegi",
                "eamvlwq", "nlcaj", "bzcdbh", "mebvdidzacveyixf", "nxkzsfe",
                "bebmpghy", "zehnt", "vysrv", "yggpr", "dqldmy", "nxkzsfek",
                "iwuepes", "ctgcqlfv", "bzlte", "cavnjhlkzneu", "zengi",
                "kskfpnwaxoragc", "cx", "ttjayafyp", "cskvurcmzb",
                "qxhvxibyqjsom", "vymlkrdihcvjqpaw", "rergtdjn",
                "qgigvwnrcrfatzcr", "arhjhdiee", "qazsjb", "tr", "srskzn",
                "ijtrgnk", "yolrgui", "rjhdi", "pnaxoagc", "giwujepfes",
                "pnoag", "wuepes", "irkmpv", "ycofg", "iwujepes", "ey",
                "ezmsorpmyhkbmy", "yrougjygjpjrq", "srsowyftkzn",
                "xsgiwoujepfes", "dvqabnobvhgqj", "arkhjhduiee", "engi",
                "arhjhduiee", "xgyiacxzhnac", "utjrlukpvukgs", "msjtvckwvnvsm",
                "yciofhgp", "epevejifzvvkqud", "jfdwhhndlxuq", "eq",
                "kskfpnwalxoragc", "mbvdidzaveyx", "mdtut", "vnlbecabj",
                "etmllxujt", "qgigvwnrrfatzcr", "byzlqtel", "ayrhf",
                "ecqazysjb", "brbe", "wujgyxnsctcov", "vnnlbecabj", "iemsb",
                "yrougjykgjpjryq", "ivv", "mjvcknsm", "ctzetmlnlxujt",
                "tztjayafyp", "mjvckwvnsm", "vysrvq", "hqmhdrfbqscasni",
                "yvnnlbdeqcabj", "knkxazq", "amdoftbguoqtp", "mtut",
                "msjtvckwvnsm", "mjvcknm", "cxcxuhlzcll", "mtt", "yrogjgjpjrq",
                "irxkmpv", "vnlbcabj", "ezmsorpmyhakbmy", "ivvz", "dqldmyn",
                "jvcknm", "srseowytfktkzn", "mdtbuot", "re", "ujrukvuks",
                "arkhfjhxduiee", "jvcnm", "mebvdidzacveyx", "cxcyxuhlzcll",
                "yogjgjpjrq", "ujrkvuk", "xfpfjzjq", "vnnlbdecabj",
                "dvqxlgsbfdmyn", "bzte", "pna", "cbwxy", "susidvq",
                "ujrukvukgs", "gkclv", "knkxoazq", "cavnjhlokzneu",
                "vzhpsnsea", "yvnnlbdeqcazbj", "pbshtsoetuot", "ctclfv",
                "gzsgpu", "iemb", "qxxb", "nlcabj", "epgy", "srswytkzn",
                "cbwxyv", "naxkzsfek", "wnqc", "egi", "ezmsorpmyhbmy",
                "oixjfysmyuwf", "ctcqlfv", "xb", "jgebzrjzf", "usidvq",
                "irkmp", "skpnaxoragc", "nyolrggui", "jfdwhuhndlxuuq", "v",
                "enzxjfsiag", "yvnhnlbdeqcazbj", "qnwxwrhq", "vnnlbdeqcabj",
                "yevqz", "mybbrkwbnuxje", "gxgyiatcxzhnsac", "dvqqabnobvhgqjw",
                "nyolrgguid", "kfixiggty", "pybbkpnjd", "oixjfysmyjuwf",
                "qmhdscs", "ayrh", "dvqbnobvhqj", "iyejuedjeqn", "yoggpr",
                "ujrlukvukgs", "qnwxghwrhq", "emb", "srsykzn", "fzq",
                "ayrhkcf", "pybpn", "mjvckvnsm", "whgpj", "jfdwhhndlxuuq",
                "kfixiaggty", "a", "amdosvftbguoqtp", "mybbrkwsjbhnuxje",
                "gxgyiacxzhnsac", "xfapfjzjgq", "pbshtsoeu", "iyejuedsjeqn",
                "cof", "mbbrkwbnuxje", "qgxxb", "jvcm", "kfixt", "mtr",
                "pybbpnj", "iyejuedssjeqn", "oixjfysmuwf", "bwkebmpghy", "arh",
                "dvqxlsbfdmyn", "lahoyz", "nirjaxkzsfek", "amdotbguoqtp",
                "cbwx", "hqmhdqscsni", "nqc", "mbbrwbnuxje", "mbrwbnue",
                "motr", "ebzz", "sivq", "msjvckwvnsm", "xslgiwoujepfes",
                "ivyrvniz", "b", "ujgyxnsctcov", "zehnvt", "ctclf", "ohh",
                "oghhi", "xgyiacxzhnsac", "wvbp", "cskvurczb", "bwkpebmpghy",
                "ultahoyz", "uafwwhg", "xfapfjzjq", "brbne", "ffllbydeziobquh",
                "ivyvz", "ivyrvnipzj", "rveguibaoc", "rhdi", "bepgy",
                "vhzhpsnsea", "dqlbdmyn", "mbbrwbnue", "ahlkzneu", "ei",
                "xiacxznac", "motrp", "cavnhlkzneu", "iv", "gnkclvr",
                "rvguibaoc", "ctzqetmlnlxujt", "bkgnkclvr", "dvqabnobvhqj",
                "epevejifzvkqud", "uawhg", "sj", "xfyazpfjnkzjsgqj",
                "ijtrxgnk", "meizcjcgr", "jloaw", "giwoujepfes",
                "qxhvdxibyqjsom", "jgyxnsctcov", "srsowytfktkzn", "ijmc",
                "dqxlbdmyn", "rbzcdbh", "irxkgmpv", "hh", "eamvwq",
                "bkebmpghy", "srsowyfktkzn", "fqnwxughwrhq", "nirjaxkzswifek",
                "ffzjq", "tvgygpmqscwc", "mbdidzaveyx", "gnkclv",
                "kskfpnwalxoragcy", "hqmhdscs", "fq", "pnag", "av",
                "yrougjgjpjrq", "qazysjb", "xacxznac", "jkwujgyxnsactcov",
                "qnwxughwrhq", "sskzn", "senzxjofsinag", "arkhfjhfxduieve",
                "qnwxgwrhq", "jqztccybler", "bebpgy", "tvgygpmqskcwcb",
                "iyejuejeq", "sjb", "rergtdj", "invcp", "rrgtdj", "j",
                "mezjcg", "senzxjfsinag", "yrougjygjpjryq"
            ]], 16],
        ],
    )
