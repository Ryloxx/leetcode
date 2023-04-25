#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#
# https://leetcode.com/problems/smallest-number-in-infinite-set/description/
#
# algorithms
# Medium (71.60%)
# Likes:    714
# Dislikes: 71
# Total Accepted:    47.6K
# Total Submissions: 64.5K
# Testcase Example:  '["SmallestInfiniteSet",
# "addBack","popSmallest","popSmallest","popSmallest",
# "addBack","popSmallest","popSmallest","popSmallest"]\n' +
# '[[],[2],[],[],[],[1],[],[],[]]'
#
# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
#
# Implement the SmallestInfiniteSet class:
#
#
# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain
# all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the
# infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set,
# if it is not already in the infinite set.
#
#
#
# Example 1:
#
#
# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest",
# "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]
#
# Explanation
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change
# is made.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest
# number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
# smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the
# set and
# ⁠                                  // is the smallest number, and remove it
# from the set.
# smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 5, and remove it from the
# set.
#
#
#
# Constraints:
#
#
# 1 <= num <= 1000
# At most 1000 calls will be made in total to popSmallest and addBack.
#
#
#
from heapq import heappop, heappush
from algo_input import run, wrapp_class


# @lc code=start
class SmallestInfiniteSet:

    def __init__(self):
        self.next = 1
        self.h = []
        self.borrowed = set()

    def popSmallest(self) -> int:
        res = 0
        if self.h:
            res = heappop(self.h)
        else:
            res = self.next
            self.next += 1
        self.borrowed.add(res)
        return res

    def addBack(self, num: int) -> None:
        if self.next <= num or num not in self.borrowed:
            return
        self.borrowed.remove(num)
        heappush(self.h, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end
if __name__ == "__main__":
    run(
        wrapp_class(SmallestInfiniteSet),
        [
            ([[],
              list(
                  zip([
                      "addBack", "popSmallest", "popSmallest", "popSmallest",
                      "addBack", "popSmallest", "popSmallest", "popSmallest"
                  ], [[2], [], [], [], [1], [], [], []]))
              ], [None, 1, 2, 3, None, 1, 4, 5]),
            ([
                [],
                list(
                    zip([
                        "addBack", "addBack", "addBack", "popSmallest",
                        "popSmallest", "addBack", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "addBack", "addBack", "addBack", "popSmallest",
                        "addBack", "addBack", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "addBack", "addBack", "addBack", "addBack", "addBack",
                        "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "addBack", "addBack", "addBack", "popSmallest",
                        "addBack", "addBack", "addBack", "addBack", "addBack",
                        "addBack", "addBack", "addBack", "addBack", "addBack",
                        "addBack", "addBack", "popSmallest", "addBack",
                        "popSmallest", "addBack", "popSmallest", "addBack",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "addBack", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "addBack", "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "popSmallest", "addBack",
                        "addBack", "addBack", "popSmallest", "popSmallest",
                        "addBack", "popSmallest", "addBack", "popSmallest",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "addBack", "popSmallest", "addBack", "popSmallest",
                        "addBack", "addBack", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "addBack", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "addBack", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "addBack", "popSmallest",
                        "addBack", "addBack", "popSmallest", "popSmallest",
                        "addBack", "popSmallest", "addBack", "popSmallest",
                        "addBack", "addBack", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "addBack", "popSmallest", "addBack", "addBack",
                        "addBack", "popSmallest", "addBack", "popSmallest",
                        "addBack", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "addBack", "addBack", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "addBack", "addBack", "addBack", "popSmallest",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "addBack", "popSmallest", "addBack", "addBack",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "addBack", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "addBack", "addBack", "popSmallest", "addBack",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "addBack", "popSmallest", "popSmallest", "popSmallest",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "addBack", "addBack", "popSmallest",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "addBack", "popSmallest", "addBack", "addBack",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "addBack", "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "addBack", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "addBack", "addBack", "addBack", "popSmallest",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "addBack", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "popSmallest", "addBack",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "addBack", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "addBack", "popSmallest",
                        "addBack", "popSmallest", "addBack", "popSmallest",
                        "addBack", "addBack", "popSmallest", "popSmallest",
                        "addBack", "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "addBack", "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "addBack", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "addBack", "popSmallest", "addBack",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "addBack", "addBack", "popSmallest", "popSmallest",
                        "addBack", "addBack", "popSmallest", "addBack",
                        "addBack", "popSmallest", "addBack", "popSmallest",
                        "addBack", "addBack", "addBack", "addBack", "addBack",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "addBack", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "popSmallest", "addBack",
                        "addBack", "addBack", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "addBack", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "addBack", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "addBack", "addBack", "popSmallest",
                        "addBack", "popSmallest", "addBack", "addBack",
                        "addBack", "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "popSmallest", "addBack", "addBack", "popSmallest",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "addBack", "addBack", "popSmallest",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "addBack", "popSmallest",
                        "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "addBack", "popSmallest", "addBack", "addBack",
                        "addBack", "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "addBack", "addBack", "addBack",
                        "addBack", "popSmallest", "addBack", "addBack",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "addBack", "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest", "addBack",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "addBack", "addBack", "popSmallest", "addBack",
                        "popSmallest", "addBack", "popSmallest", "popSmallest",
                        "addBack", "addBack", "popSmallest", "popSmallest",
                        "addBack", "popSmallest", "addBack", "addBack",
                        "popSmallest", "popSmallest", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "addBack", "addBack", "addBack", "popSmallest",
                        "popSmallest", "popSmallest", "addBack", "addBack",
                        "addBack", "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "addBack", "popSmallest", "addBack",
                        "addBack", "popSmallest", "popSmallest", "addBack",
                        "addBack", "addBack", "addBack", "addBack", "addBack",
                        "popSmallest", "addBack", "addBack", "addBack"
                    ], [[84], [550], [88], [], [], [152], [], [413], [], [],
                        [359], [33], [], [321], [], [], [], [], [], [], [], [],
                        [827], [839], [618], [165], [], [89], [783], [708], [],
                        [], [], [], [], [], [816], [], [], [], [], [], [],
                        [869], [34], [707], [841], [957], [485], [527], [109],
                        [254], [799], [442], [], [], [], [318], [], [], [980],
                        [], [202], [], [], [993], [119], [], [], [188], [], [],
                        [], [855], [], [], [], [], [], [630], [], [], [], [],
                        [435], [67], [681], [396], [73], [], [218], [179],
                        [868], [157], [435], [334], [], [514], [883], [641],
                        [325], [60], [926], [67], [667], [709], [134], [763],
                        [534], [], [899], [], [389], [], [24], [], [769],
                        [473], [51], [], [], [479], [], [471], [991], [787],
                        [288], [], [599], [455], [], [], [], [], [785], [991],
                        [], [], [], [], [663], [], [990], [484], [246], [], [],
                        [356], [], [618], [], [90], [], [], [27], [466], [],
                        [493], [], [579], [170], [], [42], [], [], [], [645],
                        [710], [], [], [458], [464], [], [], [418], [], [753],
                        [], [441], [], [], [820], [395], [], [731], [19], [],
                        [], [], [], [], [], [], [], [941], [917], [], [865],
                        [537], [], [], [52], [], [604], [], [963], [862], [],
                        [162], [], [], [89], [], [], [], [], [], [], [115],
                        [691], [], [807], [], [], [], [529], [846],
                        [529], [255], [], [799], [395], [759], [], [717], [],
                        [728], [483], [], [], [], [], [], [], [], [], [140],
                        [462], [537], [287], [], [], [], [180], [], [], [],
                        [305], [856], [636], [561], [178], [], [660], [], [],
                        [703], [578], [], [902], [99], [], [477], [259], [768],
                        [], [726], [], [], [], [], [68], [463], [], [984], [],
                        [511], [], [], [], [401], [106], [91], [], [671], [],
                        [233], [], [], [94], [], [], [777], [451], [], [], [],
                        [868], [], [], [133], [], [249], [128], [], [], [942],
                        [991], [406], [886], [], [55], [470], [247], [], [],
                        [943], [68], [], [], [], [], [], [], [], [], [108],
                        [488], [685], [315], [832], [952],
                        [], [], [208], [], [], [], [460], [], [], [], [189],
                        [437], [], [642], [], [316], [], [], [356], [], [138],
                        [628], [520], [], [], [771], [42], [549], [751], [17],
                        [], [], [], [], [], [], [13], [], [], [], [270], [],
                        [210], [], [764], [27], [419], [], [], [], [957], [],
                        [996], [546], [32], [], [], [], [], [], [10],
                        [412], [], [], [690], [220], [], [], [873], [], [219],
                        [296], [647], [936], [], [], [56], [946], [897], [],
                        [579], [], [], [], [], [333], [], [], [], [], [92],
                        [212], [], [80], [], [289], [], [494], [907], [], [],
                        [512], [], [], [], [], [552], [745], [874], [633], [],
                        [], [], [], [], [656], [], [989], [479], [797], [807],
                        [], [], [509], [280], [591], [], [3], [], [], [16], [],
                        [796], [726], [], [], [125], [], [], [], [217], [908],
                        [58], [], [], [432], [692], [], [23], [512], [], [554],
                        [], [249], [953], [662], [143], [808], [627], [], [],
                        [255], [], [952], [], [], [], [], [467], [], [], [852],
                        [41], [302], [730], [644],
                        [], [], [], [383], [], [510], [540], [194], [], [558],
                        [], [], [676], [662], [], [940], [], [], [], [312], [],
                        [], [93], [], [434], [], [], [], [], [150], [], [338],
                        [575], [731], [710], [610], [], [], [], [], [], [], [],
                        [938], [563], [], [], [], [734], [], [], [245], [], [],
                        [], [], [], [173], [], [], [], [], [439], [], [], [],
                        [451], [], [], [], [], [924], [], [], [], [], [], [33],
                        [498], [], [80], [296], [], [391], [], [39], [522],
                        [487], [119], [940], [999], [337], [],
                        [], [406], [696], [], [493], [642], [], [841], [], [],
                        [369], [], [], [], [], [], [396], [], [], [20], [328],
                        [], [], [158], [751], [686], [], [233], [], [], [],
                        [595], [984], [], [676], [101], [75], [397], [], [],
                        [128], [], [242], [], [76], [526], [956], [377], [477],
                        [957], [335], [], [], [], [], [622], [815],
                        [381], [490], [], [908], [231], [], [], [504], [767],
                        [419], [], [], [], [], [], [], [], [], [], [23], [],
                        [408], [], [], [760], [730], [], [319], [], [605], [],
                        [], [939], [638], [], [], [250], [], [513], [903], [],
                        [], [251], [], [], [], [], [], [], [649], [5], [152],
                        [], [], [716], [873], [120], [153], [], [], [], [312],
                        [747], [533], [168], [289], [44], [168], [], [778], [],
                        [971], [883], [], [], [901], [886], [931], [529], [71],
                        [186], [], [805], [919], [670]]))
            ], [
                None, None, None,
                1, 2, None, 3, None, 4, 5, None, None, 6, None, 7, 8, 9, 10,
                11, 12, 13, 14, None, None, None, None, 15, None, None, None,
                16, 17, 18, 19, 20, 21, None, 22, 23, 24, 25, 26, 27, None,
                None, None, None, None, None, None, None, None, None, None, 28,
                29, 30, None, 31, 32, None, 33, None, 34, 35, None, None,
                36, 37, None, 38, 39, 40, None, 41, 42, 43, 44, 45, None, 46,
                47, 48, 49, None, None, None, None, None, 50, None, None, None,
                None, None, None, 51, None, None, None, None, None, None, None,
                None, None, None, None, None, 52, None, 53, None, 54, None, 24,
                None, None, None, 51, 55, None, 56, None, None, None, None, 57,
                None, None, 58, 59, 60, 61, None, None, 62, 63, 64, 65, None,
                66, None, None, None, 67, 68, None, 69, None, 70, None, 71, 72,
                None, None, 27, None, 73, None, None, 74, None, 42, 75, 76,
                None, None, 77, 78, None, None, 79, 80, None, 81, None, 82,
                None, 83, 84, None, None, 85, None, None, 19, 86, 87, 88, 89,
                90, 91, 92, None, None, 93, None, None, 94, 95, None, 52, None,
                96, None, None, 97, None, 98, 99, None, 89, 100, 101, 102, 103,
                104, None, None, 105, None, 106, 107, 108, None, None, None,
                None, 109, None, None, None, 110, None, 111, None, None, 112,
                113, 114, 115, 116, 117, 118, 119, None, None, None, None, 120,
                121, 122, None, 123, 124, 125, None, None, None, None, None,
                126, None, 127, 128, None, None, 129, None, None, 99, None,
                None, None, 130, None, 131, 132, 133, 134, None, None, 68,
                None, 135, None, 136, 137, 138, None, None, None, 91, None,
                106, None, 139, 140, None, 94, 141, None, None, 142, 143, 144,
                None, 145, 146, None, 133, None, None, 128, 147, None, None,
                None, None, 148, None, None, None, 55, 149, None, None, 68,
                150, 151, 152, 153, 154, 155, 156, None, None, None, None,
                None, None, 108, 157, None, 158, 159, 160, None, 161, 162, 163,
                None, None, 164, None, 165, None, 166, 167, None, 168, None,
                None, None, 138, 169, None, None, None, None, None, 17, 42,
                170, 171, 172, 173, None, 13, 174, 175, None, 176, None, 177,
                None, None, None, 27, 178, 179, None, 180, None, None, None,
                32, 181, 182, 183, 184, None, None, 10, 185, None, None, 186,
                187, None, 188, None, None, None, None, 189, 190, None, None,
                None, 56, None, 191, 192, 193, 194, None, 195, 196, 197, 198,
                None, None, 92, None, 80, None, 199, None, None, 200, 201,
                None, 202, 203, 204, 205, None, None, None, None, 206, 207,
                208, 209, 210, None, 211, None, None, None, None, 212, 213,
                None, None, None, 214, None, 3, 215, None, 16, None, None, 216,
                217, None, 125, 218, 219, None, None, None, 58, 217, None,
                None, 220, None, None, 23, None, 221, None, None, None, None,
                None, None, 143, 222, None, 223, None, 224, 225, 226, 227,
                None, 228, 229, None, None, None, None, None, 41, 230, 231,
                None, 232, None, None, None, 194, None, 233, 234, None, None,
                235, None, 236, 237, 238, None, 239, 240, None, 93, None, 241,
                242, 243, 244, None, 150, None, None, None, None, None, 245,
                246, 247, 248, 249, 250, 251, None, None, 252, 253, 254, None,
                255, 256, None, 245, 257, 258, 259, 260, None, 173, 261, 262,
                263, None, 264, 265, 266, None, 267, 268, 269, 270, None, 271,
                272, 273, 274, 275, None, None, 33, None, None, 80, None, 276,
                None, None, None, None, None, None, None, 39, 119, None, None,
                277, None, None, 278, None, 279, 280, None, 281, 282, 283, 284,
                285, None, 286, 287, None, None, 20, 288, None, None, None,
                158, None, 233, 289, 290, None, None, 291, None, None, None,
                None, 75, 101, None, 128, None, 242, None, None, None, None,
                None, None, None, 76, 292, 293, 294, None, None, None, None,
                295, None, None, 231, 296, None, None, None, 297, 298, 299,
                300, 301, 302, 303, 304, 305, None, 23, None, 306, 307, None,
                None, 308, None, 309, None, 310, 311, None, None, 312, 313,
                None, 250, None, None, 314, 315, None, 251, 316, 317, 318, 319,
                320, None, None, None, 5, 152, None, None, None, None, 120,
                153, 321, None, None, None, None, None, None, None, 44, None,
                168, None, None, 289, 312, None, None, None, None, None, None,
                71, None, None, None
            ]),
        ],
    )
