#
# @lc app=leetcode id=336 lang=python3
#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (35.73%)
# Likes:    3714
# Dislikes: 371
# Total Accepted:    174K
# Total Submissions: 494.4K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# Given a list of unique words, return all the pairs of the distinct indices
# (i, j) in the given list, so that the concatenation of the two words words[i]
# + words[j] is a palindrome.
#
#
# Example 1:
#
#
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
#
#
# Example 2:
#
#
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
#
#
# Example 3:
#
#
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.
#
#
#
from itertools import chain
from typing import List
from algo_input import run, any_order
from types import MethodType


# @lc code=start
class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        trie = {}
        res = []

        def dfs(path, curr):
            if "#" in curr and isPalindrome(path, 0, len(path) - 1):
                yield from curr["#"]
            for k in curr:
                if k == "#":
                    continue
                yield from dfs(path + k, curr[k])

        for idx, w in enumerate(words):
            curr = trie
            for c in w:
                curr = curr.setdefault(c, {})
            curr.setdefault('#', []).append(idx)

        for idx_1, w in enumerate(words):
            curr = trie
            left = len(w) - 1
            iters = []
            while left >= 0:
                if '#' in curr and isPalindrome(w, 0, left):
                    iters.append(iter(curr['#']))
                if w[left] not in curr:
                    break
                curr = curr[w[left]]
                left -= 1
            if left < 0:
                iters.append(dfs('', curr))
            for idx_2 in chain.from_iterable(iters):
                if idx_1 == idx_2:
                    continue
                res.append([idx_2, idx_1])
        return res


# @lc code=end
if __name__ == "__main__":
    run(MethodType(Solution.palindromePairs, Solution()), [
        [[["abcd", "dcba", "lls", "s", "sssll"]],
         [[0, 1], [1, 0], [3, 2], [2, 4]]],
        [[["ab", "ba", "abc", "cba"]],
         [[0, 1], [1, 0], [2, 1], [2, 3], [0, 3], [3, 2]]],
        [[["a", ""]], [[0, 1], [1, 0]]],
        [[["aaa", "a", "aa"]], [[0, 1], [1, 0], [0, 2], [2, 0], [1, 2], [2, 1]]
         ],
        [[["bat", "tab", "cat"]], [[0, 1], [1, 0]]],
        [[["a", "b", "c", "d"]], []],
        [[["a", "b", "c", "d", ""]],
         [[0, 4], [4, 0], [1, 4], [4, 1], [2, 4], [4, 2], [3, 4], [4, 3]]],
        [[["aba", "a"]], []],
        [[["abaa", "a"]], [[1, 0]]],
        [[[
            "ebdiaaeheghdbcibceea", "jcgghfbhgcifh", "jfhadidij",
            "cghbaiejdaa", "edeiij", "gbijai", "behj", "eejbcfibbgfgddhi",
            "ac", "efdcbigigddfjb", "chdcjgieihafci", "jc", "aafigjddggcg",
            "gaced", "idbdjfa", "fhafjjgifdbjcbe", "cddcda", "aegfjee", "fd",
            "h", "hachfjehbh", "ghihdahcficgagdjcgi", "iieeihecbicefjhgaa",
            "dbjaicha", "ga", "cdceegdcaicifgfd", "ibeaaibfjhja", "ecf",
            "heibhichiidbghea", "gbjebeecgde", "gabcbaecjfjidddb",
            "igcbhgagddibj", "dgeicgbaicdbdgfijifh", "ecbhgbhgifhc",
            "gbaehhgcdeecdfiggj", "fjbeff", "cibafb", "bcdgiaf",
            "bjhbdbgcgjgediabgdce", "agibifiddaechhbfeaf", "bbechbeeiafbb",
            "hedddideegfdjb", "ibiebabcegbeadad", "ihfddccicfejbjcdbb",
            "cdcfcffhcfagceef", "fgfgcbhdjeha", "bhcgjbcbbag", "di",
            "dfagbiefcfhb", "agaibbacdcddabafbb", "ffhigceehhb", "efhefeagid",
            "igjjbcijdfd", "ehgfachaagb", "jeicadidhcadggf",
            "diagfigdgdjfajfdji", "hieag", "dbajceejibhfjjbbjfcf",
            "hidhhegiihafafh", "dgdf", "acijhgdhcfijg", "c",
            "jaahbieefgahaegjada", "gdb", "jghijdch", "aafbd",
            "fbdggahijcefdhjcdai", "iiddadjjfhhccgeeif", "fbjdfigfgffccifefc",
            "hfibjajhefhh", "icheacba", "bjajcdhfgcgibjbf", "heeije",
            "bidgdeh", "dfijiahc", "cbfg", "eifhhaidedcdebhdgg", "eece",
            "jaagdab", "ffbf", "hdfgfccaiecgg", "eecgdiahbeadbcj", "cbc",
            "fahajjbadeahhfef", "cddgjee", "gfhehdgdgeihhgcghh", "ifjgcch",
            "iccejahjai", "ijeehci", "fhefgiach", "hifeiifahjeccahd",
            "cadcbbjhehjciahchaf", "ijdiadfbge", "cbdbidfb",
            "aefbchjijdccbjeejj", "jeijjfhfgeahhhajjgci", "ie", "giicc",
            "aijgdbeehjaifacbicd", "geibidjhcecf", "jbhbbf",
            "bbejaeffbhjfhgfbac", "cbihfdaf", "cjajgicahfcejcbccdeg",
            "hfbfbgb", "ffdaeiajfabacgacaga", "fhahdadefgbjhbdgib", "ehbii",
            "ahdffaefgciacbfadedb", "fdceggb", "dadfcfaehcfg", "gjcb",
            "iajefachgebghijd", "i", "jhibiah", "fgabeddejahe",
            "jhihhgdbgaggb", "fjaaifhheg", "af", "chaehehjijffha",
            "abjhcgedibb", "dejhgeac", "ahgebaacjccgefja", "hhjad",
            "dejhbfacegi", "edbacijhi", "dgecadieafjhcc", "eigjheeieebhaeaf",
            "aebebhdieahb", "aj", "iaghehgjbibc", "dgfhagiahfbhifiebb", "adae",
            "jcegdggbe", "ibgjaeihdiggiaabjbih", "hchgejbfdiijdcacc",
            "echieiab", "iicbfgdgbjhidcabhd", "bgegfbcgfaihicdaj", "ijiaag",
            "iddcfcccibjiifh", "d", "dcbdahaceegijhbdhc", "ed",
            "fcidfajdjcfhgeab", "diiaejbcfiaabeej", "fbdbcaheiifad", "jda",
            "if", "hhdejigfeijgaaefiji", "afgiddhehcjaebi", "hjhff", "afcfb",
            "cg", "hciddafbebj", "eddjgdibgbcdcfdhhfhh", "hbi",
            "fbaijjbedbabiih", "fjibbdhaifdeeejfj", "idigbefbbgh", "daghg",
            "hdhdghffdj", "acaadgigghf", "ghbjhjagcej", "dchfjceecbfdjgadcg",
            "hjj", "abfcgacfbjjiahadh", "baiffi", "he", "jaeiicbaiaabcebjhg",
            "cded", "bafaf", "adechg", "bgjgdhfbha", "jfgbi", "hgcbecdhbe",
            "fgfai", "ghchdjbbcebbcggdgcdf", "djji", "jbbbfb", "dgaefec",
            "ebejigbcf", "hcajjjbfgaecbjj", "bjhcdahidj", "dgegffddheedbge",
            "dfcibbaghfjadjgejdhf", "efjedifhjdda", "faj", "cedfgbhafidcdghai",
            "diajajigdhfdfafjicae", "eei", "eiaebbhjiad",
            "ceddgfcidbdheebjijhe", "fjedg", "acdhibdhheigg", "fgcajgaifb",
            "id", "bjghceh", "hiiabiedf", "dbgdgefi", "jcdjihihbbbbe",
            "jfjbiegcaagiigdhdb", "eci", "iffjfe", "dcbefijfacae",
            "ehgbedbigcijdaeia", "edceedb", "ijd", "faicacj", "caefcda",
            "abdjhegdfi", "jhjfhfagf", "ffgicedibiehf", "jegfabgdjiacaabbech",
            "bgfcbdbicbhbjhdfe", "gfdbafhihacdggihfe", "hgegjecieggi",
            "cegagjjaadfegge", "bbhjcaijhbgdh", "ddeecbabdegaihhd",
            "bdfbjgdhhdeijebhgegd", "jihfihdfhbdhifif", "bhcbajgbaidje",
            "cfjbfaggheh", "iaaahbadhiahhddffcaa", "cjijgefdeeice", "fjhcahh",
            "igacfjaafabefgjhide", "ahbdgchfgiadjhdbiida", "ggfadajbjfbdaeba",
            "bifbibfji", "hbigheajidgajb", "gcgiifjidcfhbe", "jeddfbic",
            "geeii", "dcicdjahhcgcje", "jdacffbjc", "eahecjb", "fgjcbfcb",
            "fjcejehegg", "igjieccace", "faiaff", "fcgdbb", "ghdccbcdbaabhig",
            "aceid", "a", "gifhdjaifbedcjjec", "degcge", "gefjbddcbed",
            "ghjeibbbba", "dcgbggeehc", "fejfdjaejjf", "jajafj", "ch",
            "gfgdhfcjidbididfb", "dhdaddffcebbagc", "giddicgagi", "cadebdchfa",
            "gf", "gafaigjce", "cfacccjefbhfaiceea", "cgfdbahbegfb", "gbcg",
            "aafj", "jhbfjdjecbajbh", "bbigbcbcgjfaddi", "jaifibddbaif",
            "djhdg", "hdgggcjfcfbbdfa", "fif", "dajijagefbhdbaaheee", "dj",
            "gaggaeigaehahhhhchf", "bijhhj", "dfgdahgdechcihafcjef", "hdebda",
            "jhjedeibdgege", "gijbgdhaadidi", "bdebfhhjafejghgi", "egeedhifce",
            "ciiffibb", "adjeaddhadfebbfghdga", "jbfegiehhadag", "aji",
            "ffbcbidhiihhiihhbcfc", "cfaefichfigccfd", "aabccdhfgiei",
            "ahdbagd", "jfh", "gcgg", "fccehgjbbfdbeb", "ehbigbebihcb",
            "hicgfei", "bccfgfjbbd", "jjif", "fagfdhb", "fihhcb",
            "gceicfgefbbbe", "ajihcgejg", "jejjadghjcd", "bfiabgbhchegcibcg",
            "fhdgiecdfaeijidbdj", "aaefei", "hcabgiigc", "ffabcf",
            "ajaeefdbhji", "aeafdedfedjde", "jdcdehfihdhgdedd", "eagji",
            "hcjehba", "ghddigfdhcfbdjgj", "hijadceehd", "egjbihhfehabjb",
            "dffddjfdahj", "bcagadghb", "ffjjhigdc", "dacgdbafcebbeaid",
            "diadjjbh", "dhccijibfefg", "eceecgjbaghdegibd", "je",
            "cbheihbfbghjbhe", "ffdeidgjaibjjf", "hejaiifcdbjh",
            "cfbgebicaeddifbh", "ahdjechdfdbeeccag", "fcdheedfbegdbecf",
            "dabbagfga", "jgdifdefcaadjabd", "eaeafhjddhhiedbjcg",
            "iabfaiebhiigc", "jhcfifbjebejedgajc", "hih", "jehecchahbaf",
            "jjiddbfegaii", "dffgbbaeibjeebiiifb", "fajcgfbgab",
            "hjgahgbhghcebi", "acd", "cjhh", "eheie", "ihgbiiiiagidbbc",
            "bhbiehgh", "fccddbiehhi", "hbhijedb", "afcjdabcbbbj", "ggjfc",
            "bagebhchcjjd", "gebjaeeahb", "cfaihdafjdc", "iegacaefhheijehje",
            "dajg", "eajfj", "ihbgfdjahdaiibfhjfi", "aaabdfcacdhdb",
            "jfbgdjhhbagciidjhha", "aefbjehdjbicfbhjeje", "ccij", "ccce",
            "chaecgbjhdebbde", "ihc", "fjbdaiecjhehe", "ajdbedbbfgbea",
            "dciaccf", "bcd", "cbajjfhfabcbceghigd", "hbiceaja", "agcejabfcg",
            "gajcfhfc", "agajdffddhdeaefj", "agh", "bcbdbc", "cbjf", "ghgeac",
            "fachhbjgahcdigiddj", "hedjeigidaddagf", "ejjadcih",
            "fgiabedhddiheaah", "e", "efabbgfaa", "ifegaf", "fce",
            "jbjaeechhhebdfba", "degegbjb", "ibgeeabedgdebijhbgii",
            "fhhfjibjijagd", "hegadgghiigbe", "ajabfhb", "b", "gcaedifdbjf",
            "igi", "ecchhbighiheeged", "jgchjhaabg", "ehafcabb", "hhhhfbcj",
            "cadadcajfgga", "hagefe", "dgidcgagdfhhgfa", "gjahbcbjaiha",
            "dafjbbggdiabbai", "bebcjijedeeaibd", "bagjdfceeeg", "haeabdabab",
            "jjachaccbjfggic", "ajjf", "cebecejfjcj", "iaebdeidgcige",
            "ecaegahajbbcbefgea", "ffgcfgddhddgcibeje", "jbfddcifeacc",
            "afjfhfiegfbjchbab", "jhfbjidch", "bfafd", "acdhdbfhhcjffaejia",
            "ij", "caccccdcijdiaa", "jffdecbdeeibfjcaahbj", "diaef",
            "badigdhjdfaegdfha", "efbdghbicddghgi", "ebhcccdegchhi", "djbed",
            "aibgjjcdahiecdfb", "jdabaaedhgicicce", "fdbbedh", "abhbgcghfd",
            "fcbcdaghgggdh", "idddciedcbdefddhha", "hj", "f", "eiajjfff",
            "bdhfc", "igjchfccaegjgj", "bfge", "jhaafcacgbdgb", "cfgddi",
            "dehfgdgbj", "bgahe", "adhbbjchddcjhddgd", "deiaagfhfeibjiidejd",
            "ihdeb", "be", "badadajaiiiigiihjghf", "eabiedbbjbhgaae",
            "ceaifdeehdccciifbgg", "fhaiih", "fhffabcabgehgjfi",
            "efdgaficcajaj", "jadbf", "egejjdfcjgaeba", "eihaehjiaei",
            "cdeifacceecfhig", "jfjghh", "bhbbjehcbbjcbeidi", "jhedf",
            "hghhhfbhj", "iiedhd", "gbcfggaedfaaf", "ddgi", "decfgfcifb",
            "facjhahjh", "aejbadcbefb", "geffhhbhjjgggj", "bf",
            "daiacdgahgjhfbf", "fehbedhhdebfihe", "iahieaibfcj",
            "habfgeabhjjdge", "hceijgiddj", "ihbjecebicjihhd", "bifacjde",
            "djdigb", "cghgjigcdihg", "bbgb", "ifibbdhgdicfa", "fgejibjf",
            "chechdgdedhdhia", "hjfghedff", "fdihbjj", "efidhiceidcee", "hb",
            "habjcceigdf", "dbbfdbbjhee", "fajgdhgahiijffefgchc",
            "dgeeidjejicafcie", "dfgiahhe", "hiiag", "iejecfh", "ajfagfhiddi",
            "ebjaehcgjgbegbhag", "dcihchhdii", "bcaaeiejjaed", "ffgeihdaa",
            "cbjcabcheiaj", "egadeadhijahihjd", "dacfbhajcagfd",
            "fdedeceghiaihbigceig", "iijheadihbggibjhha", "fgdedcicecjcfe",
            "ghhhigb", "hbbehjiagfdbcifeee", "gjjedi", "ihejefbg", "gebj",
            "fdi", "giacdibifa", "bcjheia", "bcjcfcdcgbejfaii", "eicaahibe",
            "ajbjchhebighdhich", "cdadeccbfjbhjfjfbdbc", "egbef",
            "gijajjbhdggcja", "cecefjbaiejcie", "jbdchehcbjcfgbgc", "ibjfeigg",
            "dif", "cbaieibegiigfjfehi", "gjfdgifbfejcec", "jjjebabc", "ccei",
            "cbdj", "fhdjgdiia", "ghacgbfdhjdbghccb", "jbdbchdajfbfffdcjjie",
            "iah", "gj", "bcehecadbbaghdfeaiae", "jhcbjgcacega",
            "ggicgfeacjghffjj", "cdfaefefcjhjd", "ffgad",
            "agbfhfjgbjcgejgghihd", "fehfbc", "jcgcgihfhaaadhbibaaj",
            "bebggejcahcddgd", "bbjdbgfbabebaedgg", "jdfhdibibjbhfjaf",
            "jbegibchedbaheb", "acabhjhaichd", "jaeeghefiehd",
            "dgdbgggcecigifia", "jhgahaffeabdiiiaddg", "dihb",
            "ddejfbiejfhffc", "jfg", "ghge", "dadgbdifichffacdbjfa",
            "eafjdebejfhdff", "cgghgcea", "hidfifebffijfjbcfdj",
            "bbcgagiffjie", "fbh", "fdfcj", "fibicdcedgddf", "gbhdgdf",
            "jfbbbcbibafaijfbfdag", "bjhfidhce", "gfeagg", "cifjfdba",
            "fbhcfadajcfb", "ggagjeiaafggdddchf", "bbhhc", "agaeegfbidd",
            "hgjabejiedfceff", "cgfedihaficjh", "afdefjchbadj", "fjdaahhcddgh",
            "bcc", "cafcdc", "achihccgdh", "gfcigfefacecaff",
            "gabaiafhfgdghge", "ihdgjgdddfeeeb", "egchaebcajabbiff", "acab",
            "ihbij", "dhafdaiajgacghfje", "jhgdifdjaeg", "bfjee",
            "ibbjhfcdggafdc", "ef", "ig", "hcegdeacj", "biadejhgcdc", "figebh",
            "afgihiagiehicedffh", "jdaifi", "ccbgif", "hebhbhgjhidffibcfbj",
            "dfggcbagidcc", "bhcfc", "chd", "cebgb", "gjfbfdb", "fegcfhci",
            "ijhjbjegdhjbhg", "ejijfabgfeccijjbiega", "eaccaj",
            "fbaabfdadcihfgdijj", "cidaijgbedcahf", "dffhh", "eja", "hhih",
            "eeihbhfjcegbge", "hhjfiihghhgihefjid", "ccagb", "gbgbebicib",
            "fhajjfcdffjhdeeagajc", "jjfbbddgjjhdhcib", "dbhfadhdfjddge",
            "egedeebgfgf", "ceebhg", "ibjhfedfiiahi", "adfahhiggd", "daj",
            "afhdjc", "fiadeaacdajbg", "fecej", "bbjbfhecd", "eibgiccbgddhdg",
            "igjcdeadagfcgf", "aigaaefgb", "hhfbgajajjaibcccje", "jhd",
            "jeajaiaijeedjhhbhfdb", "cejefgfhghdaf", "cjaabgbjjbcgbhfg",
            "fedhdhbdeiag", "gdabhajcdi", "ggfabdbejh", "eejgacceefdffe", "ff",
            "bcjadhhafbeg", "dfhajjiijijd", "db", "eahfjhebcjddd", "ahaf",
            "ddajggbgdbfjd", "hci", "hfbifjddjebedgc", "dcfe",
            "bdeifaegeibfadc", "chcfjigdj", "ghggfabaabjcgfebjj",
            "gdhefhdfhfbccde", "bfihfi", "bigffagdbhjeejabed",
            "hfibdjjehgfaad", "hd", "geijfbegeb", "icea", "daehec", "che",
            "cadaeadabbhjjjjjj", "eihjecdebfdjghgde", "ffhgceigcibddda",
            "jciiecicegh", "gahdiigeig", "dfihehhei", "ghhghcfeichhfic",
            "gfgiafibheijdfci", "hgigdceacahfgfe", "bgjdfhbeae", "ej",
            "cabbbbbigccf", "cdcccbddidbegcbc", "fahbccbhfjhdbd", "fafdhjc",
            "edbfbhjcf", "dgajadcdeihhdhcchbia", "jighjeifbfd", "ijf",
            "adcbfhhgaedjfhihh", "bbfbaefgfdaibi", "ajieciggjhbbc",
            "bhciihebebcbhhhdji", "ccffecd", "bdfeidbedbijaigb", "eiehabicc",
            "fiebedaiiedbceaegb", "gdjjd", "hhfgbjejaabi", "dddaaccefeeidfjca",
            "chiegabfijjbhgagaf", "geiahbeffcfgjigaab", "jbebcfaefj",
            "bdchdggdeecajcdib", "ecjbacbgac", "bhihgcajeafjbie",
            "iebacghajafgf", "ahbabajgfefjiafj", "fjeedheaagbbefjjdhah",
            "ecadhaab", "hhdgijh", "beibhjdfcjbebhcabf", "bhacihdhbibb",
            "bjcij", "dhafbigddbaa", "ifhjaffcijebafgai", "bgehfjdhbehhbfi",
            "gegcgacdjf", "fiaggijbh", "jdj", "bbgfejhge", "aaa", "dgeedhg",
            "aigbheaaifd", "dijgicdajjb", "higieibci", "bhjbaeaag",
            "gdighfbbcbbfdbf", "abj", "bjgi", "dba", "aafcbdcddegdi",
            "efbfefidi", "idhggcjdfha", "gbgidehigjhgdceh", "aebdhhfeic",
            "ijhgjcggdedbdgah", "igabcdhach", "hhbhgcadh", "jfcicgji", "jjdcf",
            "abbghhbfhgech", "acficfgcg", "eiaageddc", "icfeaaijaaic",
            "ababeacei", "gdj", "ggiiihgjfb", "bbgfj", "iheciibfdahaegcfdg",
            "acbja", "fdgcajdabghbbfif", "ghefjfifjbgigg",
            "cigfbgbafcdbiahiaeh", "bbifihgageh", "iabffgifadbibifff",
            "ccihhbebi", "hibibhbeh", "gfagiaididfgahjda", "fedabefa",
            "hbcajcdf", "jddjdahg", "fdj", "gihafjcjdihhdbbjbc",
            "bejaejhecfgiefgebj", "faceihhjcj"
        ]],
         [[8, 245], [61, 8], [61, 11], [18, 429], [141, 18], [245, 24],
          [27, 381], [47, 141], [113, 47], [47, 196], [429, 59], [77, 378],
          [79, 429], [96, 113], [378, 96], [118, 245], [429, 118], [615, 123],
          [129, 245], [378, 132], [143, 378], [141, 143], [147, 271],
          [148, 113], [429, 148], [632, 151], [153, 61], [165, 19], [168, 19],
          [378, 168], [170, 61], [187, 118], [96, 190], [113, 190], [196, 113],
          [141, 196], [196, 47], [271, 207], [429, 241], [247, 141], [253, 61],
          [19, 253], [429, 258], [269, 148], [271, 141], [414, 283],
          [289, 153], [378, 320], [320, 664],
          [339, 11], [340, 168], [378, 358], [253, 360], [370, 24], [371, 388],
          [381, 27], [582, 390], [414, 113], [428, 19], [441, 388], [378, 441],
          [582, 458], [463, 388], [429, 463], [473, 388],
          [480, 19], [388, 480], [196, 504], [516, 196], [96, 520], [258, 545],
          [378, 546], [480, 552], [552, 463], [11, 553], [568, 388], [
              388, 575
          ], [581, 378], [429, 581], [582, 113], [591, 480], [129, 602],
          [602, 320], [603, 19], [332, 603], [624, 428], [632, 429],
          [429, 632], [635, 141], [388, 635], [429, 637], [639, 253],
          [649, 19], [141, 649], [651, 202], [664, 378], [664, 320],
          [703, 271], [705, 245], [245, 705], [545, 732]]],
        [[[
            "gbagiejccfefdja", "ecghjehhabihjjdg", "ij", "diecfdcggfbih", "a",
            "bbaggbheggidcjaffdeg", "ffeegjf", "hicghibjhdggegac", "ibfeggda",
            "fjdgdhfie", "hadefcabdfgcaagb", "hjadfehbahcfbhjjieca",
            "gihhcgdgedhffe", "bbcjfccjceejajj", "djdj", "eebbeafci",
            "icgeahffcedef", "ichbc", "dffbjhihegghgbff",
            "gdajicijabibcggacch", "fecidebdechdaf", "ha", "ebj", "dheeaiihhg",
            "bb", "cc", "eiehdebiaicedibji", "hjeij", "c", "bi", "fdb",
            "aeigac", "adgibhegfffdjacfdc", "geiieheddbahjdga", "hgjjibafjc",
            "fdjbd", "ecaigajddbcfhif", "dhcdcdhfgbfidfabacei",
            "edegdfcahbhidgchf", "aiecebg", "dihdebafjhgbagbjdh",
            "dcighgdajdagbb", "gaiaag", "idghfcfcffehbggdaeb", "bdi",
            "dbifhgj", "cedeiaiidcdjjjbgeh", "bhfhbbbe", "ecacidgddggifajidfa",
            "jd", "hhbgbcddehbdc", "gbgeieb", "hgcdfbbfbdbcgb", "ijfifbe",
            "bjjhgehihdhahd", "dacjcgdabba", "ebcdeaediahjifdbgee", "degbiice",
            "chjbdbgjjhgiidcehehe", "iegdjdgihhhccafdedi", "bjj", "gcdee",
            "dbcaeiaceaedjbcehjea", "fdbjfjdedaceajjjbhf", "j",
            "gdcbjhdbiehejidc", "ajgib", "jheheccjadiedcib", "eagejbehjahaj",
            "jgdji", "bh", "g", "abchcebhdhjfjgcc", "djihjbfjadjibfjbgcfa",
            "egcjibgjb", "bfebabjahgaii", "hjecacdd", "ahacejicaggccaaaeb",
            "cfggdc", "gagheffcghicgia", "aggghigfhbgfeh", "head", "cbggaidah",
            "dgbajfhihediajjb", "cihhhgdjij", "cdadhjeehiejch", "gfdae",
            "ajhcheibijabagej", "becdggd", "idagidgffic", "fdibaaeihaefeagbid",
            "chjiaec", "hcjbfdbhbajbcai", "egbjhbegjigdicgdjdab", "igecajb",
            "ajafhd", "efbhghaaieae", "dfiacgijif", "efdjf", "cgfiehjiggafhd",
            "ajahigiijd", "eddfechgceifjc", "hig", "ijcgfbbefcabefbbheca",
            "ahgdhaefaihgbiaf", "aicacifajigfhidgfac", "ibghfihjbgcd",
            "ecdacaiid", "jifihdjehcdedhaebjig", "dfgch", "ddfdadjddgejjcfefd",
            "aciieececcdf", "fgcdjjcigb", "hgc", "dhcidegafifjgje",
            "ebhbfecfdihbba", "bc", "fhibbhbhji", "gfbh", "jhji", "dbhgfibgdh",
            "iffgdddefc", "jigegibbjiga", "iicfiiiiiifcdj", "ihdaaf",
            "eggijdb", "ggcidccbcgcdjdjhbj", "aib", "chbiaeaacgehddia",
            "hadehejfgach", "icghjhjagheeecafee", "ibifdihbjccjac", "jjjihbjb",
            "hhhffi", "geccedfbghcg", "ae", "hcgf", "acbfcghchahcbjaii",
            "bcgcdifbigcfhfefga", "cecihdghfffddjcecidd", "hhiicchdbi",
            "fdahfdjbdhceabac", "eidihihaddbcc", "hcaahghgijdgfcbibhc",
            "eiggdcdch", "fifgejbihgcajdffh", "bhjjib", "fgcejhaehbdbhdgdhib",
            "bgjfhccidbibabf", "ijeeaeeeebcfceeif", "gahidiehdfgdi",
            "fgigdfgjbhahehaed", "iafffcdb", "d", "cdgh",
            "cchafjghfdaecdffdcgf", "aecacedfeigcfghcfdef", "jbeidacgh",
            "eacecd", "afhbihecce", "acfbahfjdgdchijcaai", "biig",
            "ehdbhifaiaagi", "jdecb", "hdjfhggjgcfjdjcd", "icahcjbad", "e",
            "bifjbifbghdciaidg", "jjcbdichegeiejaga", "aehhb",
            "caabaejjcfjdhafba", "ehfiec", "gcjbjfeacccbegedefa", "fchggc",
            "jbefahijhhgagcjgdcfe", "ifacehcjiaacba", "gfae",
            "gjbbagdgbhhddibe", "cfjfdga", "iafagghbjda", "bjeb", "gbijeecedf",
            "bgbcfhi", "jicac", "gded", "efgedfbb", "idbdajdfcfeijf",
            "gfeiafhae", "digbajejb", "ihjib", "biefdigdidgh", "fedecff",
            "iebjigi", "ebaijieebhiigbd", "hjaciabbhfc", "edgbh", "gaejdc",
            "gd", "aebbcbfehgdc", "cbjjigjgia", "dchjjicjghdfagdha",
            "aghaggebjbbdj", "afhdhj", "ecajjbigfgeiejdfgjf", "bfcfjhje",
            "ejd", "becbccdffhjiha", "ahcd", "hjgfedcda", "acdd", "chfiec",
            "fajhfdfhcgj", "ac", "i", "jcbeghfbgjiib", "jechhf", "idcgadh",
            "dijgdgejigjgjbife", "bajcdfjgifcf", "ehcccbifhbbci",
            "gggbdfafcjaa", "fiijfiffbeeafhidgdh", "fjhijj", "bifghffcha",
            "cfjd", "ibhgf", "ifiggeedafjcgbdfbe", "bjhagccefjahchdjidh",
            "gchdjdacih", "jcgdad", "ecegiahjb", "dgf", "hhejeejjfgd",
            "igiedc", "faffaae", "hhhdagegjjhadcfdb", "djdedaibedhhhad",
            "agjcdbgciadghfg", "jhgiachghef", "ib", "jhaaidgiajbfc",
            "jegcdbhecb", "eiabgbieiahegjfdfcha", "dgcae", "jgdcaehgeffjdhdhd",
            "gjjc", "jbbgagji", "cdfgbjeeihhejcabih", "ahdhahadadje",
            "eeegecddajiiadahbhe", "baffhiihfgifhca", "cbjgfbbbe",
            "bihgfhfadjgfde", "jahhbfdijbfffh", "igcgj", "cghdcabgehjcie",
            "cghgaiajdj", "if", "fjbdgidbibhdif", "hhbcaa", "aabfgeic", "ahd",
            "ggfhahfgbjbhhii", "abaiiegibg", "abajjhadbfgg",
            "fibcgafjibacaegfbhaa", "jaagdjaciefgjjdfje", "bgeah", "diei",
            "gifcfffedcejdhgid", "dbi", "ahbicbaded", "iegdccicigfeajagibj",
            "afg", "dgh", "cjijdcccaebici", "afge", "eciih", "bfgcdjdfegac",
            "cbfhcbhfbcfiajd", "feibbfceedecadaiabb", "ccafdfcag", "bbbei",
            "jbbhff", "fhg", "cibcfhejhbhhjhfhbadh", "jgadaibddggajjegh",
            "ghahacag", "jbjcbbigdjh", "dfihbj", "cieieciffbdgef",
            "adcgifdcjdejbebi", "ccichece", "hhaej", "ijidfjajjgaeigiea", "fd",
            "df", "jjfebghacicgadeec", "chjdj", "jdabejje",
            "cadadjchbbehgfgiecaa", "hcddhecbeb", "ijjbhai", "ggjfdijhfh",
            "ageggjfibgeda", "bcgdceggbebbfd", "bjbbcbihfj", "eeaf", "iaic",
            "hhiibebjdbgheihaigff", "eeiedaibajgjcfga", "gchgfdjiaedfgacdjgad",
            "hjhbiehiig", "b", "geajijdebcajgfe", "ei", "idjaefi", "id",
            "bhdfdbcd", "hggd", "ghiigj", "aihfdggfadaeiihbb", "jbegid",
            "cfigdibdgidg", "bajfgbjadadhefgbjh", "afac", "ff",
            "aideabecjcchbcfhhc", "bdcafbaehafhahfde", "cgfiheejaidj",
            "bigeejbjgec", "dag", "giifhbgdgjbhcaaeiife", "ijgfcffgadechijj",
            "ieigcdc", "egagfdfabihe", "fiifbcd", "jcccjjfciea", "dge",
            "dgeff", "dfecjhciahh", "cjbdjiegjfcbcfhbfhg", "dcecedaeeebegf",
            "hjbhgecb", "cjbdefegfebchgc", "jeiaefjbicgbdihi", "hhcfbiefbbcj",
            "eg", "igeghceahe", "hh", "iighhghicbigaji", "ihcadidcbcfgaajahj",
            "igdjd", "iebijhjdieffd", "cfjdiiaaeichciie", "bidigjaebbcacigh",
            "eeahciab", "edhjchcdc", "gieifhhjejgdajgdigcd",
            "ibehahbigijgcbbehcaj", "gde", "cccijcadiadbcfccj",
            "hdfbejfefcaeigdehdhj", "hbchgdjjd", "ihhba", "ffjbjeajcfha",
            "adbadbediddah", "gcfadicdjdfjddhgjd", "chjjajcgfjefh",
            "egchcdeffbbjjhbfgjgj", "aahfjd", "hdhjaieeidj", "iechgceeiah",
            "bichjfbigeha", "jjibfgfcejfhjef", "hhajabbihdif", "fjcbjbbhja",
            "cjejddjbdjfffdga", "biaeiehc", "edihagfihjdbefhihg", "afj",
            "bdhhjjhfjjbdd", "bighfgcig", "fhbjfaadgdhfibcahi",
            "fidhdiicigchdgcajbc", "ibccefcfbccdbebaifb", "cdii",
            "feibajadhijfheifbaj", "babjhchg", "ibhjajjgh", "ajfbh",
            "bachehagcgadbichcic", "bjgiedhcahaifg", "ijahacfe", "jcghdcgdjjh",
            "bfhagjcidehgahehbd", "egegajidchfdjdgdfcc", "f", "cd", "hijd",
            "eideajaaecb", "hjiaefdaeabiehdjede", "jdgfcbehibieehdc", "jfb",
            "aeiiaifhedgccegbabg", "ijihcejf", "aejadfbedae", "fdjfbcfafjcbf",
            "bejjjcfd", "aicabca", "fa", "ihbef", "hjej", "gfihebacjfdaei",
            "dcbjcighgjgh", "fefhhihcb", "dbfgjcabfa", "cadhjhhgiffghffgajd",
            "dibhdbbcbah", "cidhgegcabfbdibjhef", "gb", "bificfaeghfcjfg",
            "faadefidbdjcebhg", "behfe", "ghgdhgjeid", "ghjhihdcadffaege",
            "acigfegdcjhgj", "dfajaecjdajiihjdc", "ajefgebgefahbjbffej",
            "fceia", "jihifjchehec", "ifcghhhhchcfdad", "eegagcjbdhc",
            "jfdijjahefdcihfaf", "chdbbfaedhh", "cg", "cfijhhcbijaacdbi", "hc",
            "ceddhbg", "ahehcdehdbbciee", "geeiaeibfjceajh", "jhbefdjgj",
            "cbgb", "bgd", "bd", "bjaafbacedf", "jfjcbg", "ihjaedfcadbi",
            "ghhaidbghhba", "aegdgcj", "afeccafcfcaifcf", "icheehijijc",
            "cadabegjjj", "ddfciaajcabefda", "cb", "ihgeeh",
            "ajiadfhcacjfdifcib", "dchahahcdegcc", "hi", "aihjfddibcihdh",
            "gdacjbfgde", "cfeeidaf", "ejehdic", "bbcfgighcb", "giieiicfcfaa",
            "aai", "fgahai", "efjiiaiehbjhjafhdhb", "edghhjiddecieec", "ej",
            "he", "hb", "ead", "hidjghcijb", "ibcbf", "ifdehfhcajfiebbaj",
            "ace", "gbhf", "bbihdhhc", "hbbafdhcbef", "jfcbe",
            "cjebbhaifdbbib", "ieeeejjacicjhddcch", "chihgddjfga", "hfhii",
            "ce", "bhi", "aidejahh", "jahfdehgbagddfjc", "ijicebfeeeja",
            "gfffadhedihdaecfbde", "efffibiifhbffh", "agchjcghjffjceaa",
            "eehafabifjicfb", "dgfigibd", "bjibgdhiedhgdbgjhce",
            "eijacdjadaigchchfeee", "gfdhfchgiedcadcjajih", "gjiej",
            "iaibcaebeabddaciba", "dbibcegdggihfhfcef", "jiffdecbdjejjcgh",
            "cffdbjceabbgfi", "gifha", "ghiieajjai", "cghijdicbjed",
            "adddggafj", "iiafejjcggdeeef", "beicaaicdhfdhbjj",
            "dccjfaaiiefhh", "heihghdgaafhjfac", "behidid", "jjbhbdeabbagdfcb",
            "ebgaiggafciebaea", "bagj", "hhdefjdaiiigieaed",
            "dhebhefbhciciecihee", "dg", "bcbcgagjaijbbdb", "ahdajhhcedb",
            "ii", "fjgbhjhccjgecjgh", "cgdjehhedec", "hjdfaaadfbaggd", "dfd",
            "cfaeeegiihi", "jahegibjabf", "icbii", "iibj", "hdjfbgd",
            "hfaichbdfjhcbfjabc", "ibaghgciec", "abgjcafbbbg",
            "idjehihcbfhihbdgbi", "begachciadfdadbhb", "biiaghdigaab", "egjfg",
            "bdji", "bfdebfba", "jdfhfcdjjgdfjahefgij", "hfbiedicieccbdjhjdj",
            "jeecejjiijgjdcifd", "gibbhicheadcg", "bfhjhhfcdcgbhjhbhgef",
            "hadfbgdih", "eehhcdej", "hchae", "eggd", "dicg",
            "aafgfhffdedghjajfdh", "gcfjhgfcdhgieiibff", "hjchbbdgdedfechebge",
            "jceii", "bdggccdhhdb", "cfehhdcbj", "hcbfdfcbdiiaah",
            "bjhgeeccjib", "hdaiedigd", "eahjifhjd", "fcgega", "jcbcehcgeebe",
            "ggbgaebfibdejafbaeeb", "fcigbhdddbg", "eecfhghc",
            "jdbehehjfdijejahbfdf", "cja", "eiaaagcbjec", "cbhcch",
            "jhhagfjji", "hgcbbhfgedfaiehgj", "hceigehdejdd", "cgdhdbiejihic",
            "cgbihcdhgecjjaec", "fdahfa", "h", "ijagaceheie", "hbeifcfibffcgj",
            "edfddjb", "aaffahhajdeaafajed", "jfdfbjiifjeabcjbhj", "egcaba",
            "ijie", "giaaibag", "iabhh", "cjeheeafg", "fccijfdgdcfhdc", "hhhj",
            "bccbhdgejhaggfhgccce", "gbj", "giffhifehhj", "afacd", "gchgbidjb",
            "fbjbfdicha", "jgh", "ibiihciggjd", "aaijjgfajifgadbd", "cje",
            "jhggafbhehbdhfedia", "gcjijhfgfigjhc", "igihhdificbj", "ef",
            "aeaighghbafjei", "jbbehagfcc", "jdgbhgbag", "jhj",
            "fhibchdcgijfbhabejcc", "eiaghab", "hggcbechfii",
            "gcjfjfddgehjhehe", "efbcaiidaejgccbij", "fdecchgedgf",
            "ebhdeifbedffaib", "fadeiddecchhejibfhje", "gjhfc", "cdijhcab",
            "geedadifhchhdibgbech", "jjjchdi", "hbgecedhjcecic",
            "difffebbhiihihedj", "cjgfbjchhceddbbgd", "eacgf",
            "gcafbdbibbchbhijcbi", "iagjiigdfibccjg", "gcaffeeejcbiefjaga",
            "dfjcg", "jcaf", "cjgce", "jj", "abegabdeffbj", "badfj",
            "jggijgicidbbddhd", "adc", "bgeajdjbaeja", "cabi",
            "ehbagjgebjhhehhjbf", "jaabgcbfei", "acgehebbc", "bgjagc",
            "hjahgeedhieehdjbcjd", "ijeabhici", "ehgiejdefhdehi",
            "gdedeegfdhdbd", "cjjceib", "gajfdaigdjdgi", "bfdaegbeaehadefg",
            "digaai", "jgicbadgebdjifjghg", "heaadfghjjadce",
            "bahbedgbjifcechc", "hfgag", "eeaegca", "bacechahejggagfibcia",
            "gdiif", "dbhhe", "dfehgeaiafbf", "dhahcc", "chh",
            "ejfbeiggdcaigidhdbdb", "agfjcfbeejgibefeaeh",
            "jgghgedceegcbhfagh", "efdjdffaiehijfbi", "cafggjaedcf",
            "adbihiggjjeeebg", "fajicbf", "hjjahdbjfggdf", "gfdgabhficb",
            "bgejhidib", "dihc", "ghagdddjbdaegdbihcf", "efg",
            "gedfhcgcafcfhajei", "dfdchhgfebfjcbdi", "fehajg", "ajafecgea",
            "gifdfia", "ad", "ceficegbgaabd", "dbbgdjhjdjehae",
            "djbhjiaejbdgaadcbjgi", "ifjacjgdedheeb", "afcdagacg",
            "gjfbdjbgeaejj", "jjdeaca", "cgccafhgiegag", "edhgbjjffcadhjhc",
            "hfcgeaibabaeedc", "bhjaheageef", "ggcadhdjbceicji", "gbebic",
            "fdjcadcei", "eadcc", "jgefihheiajfjegebcb", "bfijdaeijiebiihj",
            "bgfbfggaebghidbaeij", "hbfijfcechdib", "jcacf", "fbecigeedcbehib",
            "hdeeaafahj", "eciiehedaffajeeehgcc", "bidiafidhhiehejfg",
            "djadbeaciigehgahachc", "gbh", "feiegfc", "habfaeaibhdbf",
            "hbcgfaecde", "faabcidhegi", "giafjfbahjca", "fefifjcadfji",
            "gaicb", "fhcgabjidj", "hcdibbdcgfhggi", "dfjghdffjejfehccddc",
            "hhhgfaibbj", "ediejhggcgadfbifbce", "gdbgjhdhdbeggc", "gj",
            "jddjadfhh", "jhigbbdiej", "ageddiiic", "jchidcbijcaiaa",
            "biaaijffgdfhhfdcfgb", "ejhgb", "eabfhbb", "jggcacagaafcd",
            "iaedgbgbfccjejhe", "gggcj", "baahcfbfgcbadecci",
            "acdehbehgdiahecbigjg", "cjcdabedjajc", "jbfgi", "eedejcf",
            "ejciaaib", "ifidhaac", "habgebdefibhfi", "daacbgieijajefaafbh",
            "ffffaeac", "cjhdbfghfhefecichac", "iiegeghedejbifbbjbaj",
            "cijaajbfff", "eb"
        ]],
         [[2, 213], [64, 2], [14, 153], [64, 14],
          [21, 574], [4, 21], [24, 313], [313, 24], [25, 28], [28, 25],
          [29, 313], [213, 29], [29, 239], [444, 30], [30, 296], [317, 44],
          [49, 64], [153, 49], [60, 313], [627, 60], [70, 313], [574, 70],
          [70, 471], [136, 109], [435, 113], [116, 313], [28, 116], [116, 454],
          [119, 604], [213, 119], [29, 127], [135, 4], [166, 135], [176, 273],
          [183, 2], [184, 71], [197, 71], [153, 197], [197, 517], [212, 4],
          [28, 212], [231, 197], [239, 213], [313, 239], [239, 29], [257, 213],
          [397, 257], [261, 21], [268, 153], [239, 270], [270, 444],
          [273, 410], [274, 197], [295, 397], [153, 295], [295, 296],
          [296, 153], [397, 296], [296, 295], [298, 437], [410, 307],
          [28, 308], [315, 166], [213, 315], [317, 213], [153, 317], [28, 325],
          [326, 397], [397, 326], [331, 675], [347, 338], [338, 197],
          [347, 166], [71, 347], [349, 574], [574, 349], [360, 517],
          [380, 410], [398, 28], [153, 398], [410, 397], [4, 410], [412, 574],
          [420, 71], [313, 420], [435, 28], [71, 435], [437, 574], [28, 437],
          [442, 28], [517, 443], [443, 420], [444, 313], [153, 444], [454, 28],
          [313, 454], [454, 116], [458, 574], [213, 458], [213, 465], [
              469, 166
          ], [64, 469], [470, 574], [166, 470], [471, 574], [313, 471],
          [471, 70], [472, 135], [520, 484], [485, 28], [166, 485], [486, 471],
          [517, 153], [71, 517], [517, 197], [520, 213], [213, 520],
          [296, 524], [524, 295], [567, 116], [166, 581], [64, 586],
          [593, 715], [469, 596], [600, 166], [397, 600], [627, 64], [64, 627],
          [398, 631], [656, 28], [349, 656], [656, 437], [675, 4], [153, 675],
          [471, 701], [715, 71], [64, 715], [739, 166], [313, 739]]],
    ],
        comparator=any_order)
