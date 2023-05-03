#
# @lc app=leetcode id=1878 lang=python3
#
# [image.png] Get Biggest Three Rhombus Sums in a Grid
#
# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/description/
#
# algorithms
# Medium (45.70%)
# Likes:    131
# Dislikes: 375
# Total Accepted:    10K
# Total Submissions: 21.8K
# Testcase Example:  '[[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1]
# ,[4,3,2,2,5]]'
#
# You are given an m x n integer matrix grid​​​.
#
# A rhombus sum is the sum of the elements that form the border of a regular
# rhombus shape in grid​​​. The rhombus must have the shape of a square rotated
# 45 degrees with each of the corners centered in a grid cell. Below is an
# image of four valid rhombus shapes with the corresponding colored cells that
# should be included in each rhombus sum:
#
# Note that the rhombus can have an area of 0, which is depicted by the purple
# rhombus in the bottom right corner.
#
# Return the biggest three distinct rhombus sums in the grid in descending
# order. If there are less than three distinct values, return all of them.
#
#
# Example 1:
#
#
# Input: grid =
# [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
# Output: [228,216,211]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums
# are depicted above.
# - Blue: 20 + 3 + 200 + 5 = 228
# - Red: 200 + 2 + 10 + 4 = 216
# - Green: 5 + 200 + 4 + 2 = 211
#
#
# Example 2:
#
#
# Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [20,9,8]
# Explanation: The rhombus shapes for the three biggest distinct rhombus sums
# are depicted above.
# - Blue: 4 + 2 + 6 + 8 = 20
# - Red: 9 (area 0 rhombus in the bottom right corner)
# - Green: 8 (area 0 rhombus in the bottom middle)
#
#
# Example 3:
#
#
# Input: grid = [[7,7,7]]
# Output: [7]
# Explanation: All three possible rhombus sums are the same, so return [7].
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# 1 <= grid[i][j] <= 10^5
#
#
#
from functools import cache
from itertools import product
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = set()

        @cache
        def dp(y, x, direction):
            if not (0 <= y < m and 0 <= x < n):
                return 0
            return dp(y + direction, x + 1, direction) + grid[y][x]

        for y, x in product(range(m), range(n)):
            res.add(grid[y - 1][x - 1])
            for c in range(1, min(y, x, m - y - 1, n - x - 1) + 1):
                res.add(
                    dp(y - 1, x - c + 1, -1) - dp(y - c, x, -1) +
                    dp(y - c, x, 1) - dp(y, x + c, 1) +
                    dp(y + 1, x - c + 1, 1) - dp(y + c, x, 1) +
                    dp(y + c, x, -1) - dp(y, x + c, -1) + dp(y, x + c, -1) -
                    dp(y - 1, x + c + 1, -1) + dp(y, x - c, -1) -
                    dp(y - 1, x - c + 1, -1))

        return sorted(res, reverse=True)[:3]


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.getBiggestThree, Solution()),
        [
            [[[[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10],
               [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]], [228, 216, 211]],
            [[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], [20, 9, 8]],
            [[[[7, 7, 7]]], [7]],
            [[[[0]]], [0]],
            [[[[0], [1], [2]]], [2, 1, 0]],
            [[[[0, 1, 2]]], [2, 1, 0]],
            [[[[
                46988, 71126, 27148, 94144, 90345, 57050, 36898, 50813, 88540,
                14050, 33543, 93386, 28353, 79316, 54052, 20747, 68552, 90238,
                67854, 83011, 97316, 72477, 95715, 87762, 73409, 19863, 41544,
                21891, 3327, 88422, 3661, 5017, 73021, 78222, 20954, 48665,
                71656, 9548, 51168, 73518, 83665, 43186, 151, 83018, 51564,
                83860, 19063, 90971, 56961, 37726
            ],
               [
                   61169, 37764, 5590, 27982, 65627, 45174, 79919, 8250, 57246,
                   43958, 28855, 69176, 43493, 60385, 26737, 58631, 38281,
                   80933, 59134, 18380, 79537, 17545, 88631, 23570, 4552,
                   29312, 38765, 37481, 65037, 64848, 37114, 80993, 81376,
                   93869, 92441, 68324, 59616, 41842, 91263, 11947, 24617,
                   81377, 59463, 21183, 39416, 96861, 35278, 32605, 37753,
                   28268
               ],
               [
                   84785, 64889, 45074, 36145, 6213, 52384, 95736, 98868,
                   97000, 33378, 32756, 31689, 33098, 34419, 62299, 76672,
                   9445, 10292, 25746, 85870, 69578, 65465, 19225, 2777, 65681,
                   50775, 48911, 17469, 43681, 88236, 80028, 78489, 82444,
                   42995, 52152, 77504, 31630, 18467, 86223, 53759, 15508,
                   1838, 38718, 80082, 23051, 59052, 66699, 78850, 58663, 71198
               ],
               [
                   68028, 8255, 48649, 61132, 72533, 42549, 72642, 98640,
                   12922, 12552, 76966, 54034, 14431, 57109, 10489, 446, 91867,
                   2584, 54598, 76663, 5284, 60640, 81628, 19683, 44555, 59623,
                   88870, 25516, 8252, 96402, 38903, 51804, 20557, 62736,
                   62614, 4373, 14296, 40353, 26705, 82849, 56115, 73730,
                   46783, 19010, 24092, 33826, 70454, 99088, 80292, 64936
               ],
               [
                   96801, 17273, 62935, 1591, 11906, 77520, 70282, 75769,
                   62135, 15559, 13051, 58703, 73417, 38325, 41913, 63541,
                   48710, 66703, 19074, 14651, 37293, 92453, 80239, 57614,
                   46613, 50878, 54264, 59433, 53971, 41313, 13292, 57712,
                   93359, 49869, 85315, 43740, 29103, 70963, 11514, 33272,
                   16065, 62972, 26683, 44499, 18450, 80024, 31894, 98942,
                   27125, 76727
               ],
               [
                   26326, 95377, 77943, 76189, 83802, 51932, 69562, 52122,
                   20285, 88909, 26356, 73128, 42531, 66399, 25084, 24767,
                   67224, 57479, 27849, 12928, 12006, 48460, 82006, 95384,
                   86320, 36052, 35268, 16374, 16637, 12916, 7741, 17576,
                   32710, 44282, 21762, 36216, 49662, 18540, 7965, 17054,
                   65714, 36085, 24535, 69261, 38208, 40501, 42165, 76338,
                   29398, 67029
               ],
               [
                   63540, 97807, 20234, 65431, 17442, 83194, 86745, 86347,
                   54084, 45694, 98424, 7480, 13650, 96104, 24126, 79928,
                   63040, 11848, 67449, 24686, 20297, 35363, 88637, 57381,
                   24654, 37315, 75180, 14238, 11396, 97669, 67071, 55671,
                   29304, 3754, 59373, 93721, 83822, 97311, 10688, 87440,
                   23772, 68530, 4025, 69175, 73925, 84258, 22171, 80932,
                   40930, 27512
               ],
               [
                   10894, 94033, 24766, 67672, 37497, 58680, 75201, 42681,
                   92874, 32269, 38019, 32653, 70873, 68021, 25059, 73303,
                   11067, 97907, 89940, 42925, 3727, 99743, 69737, 46156,
                   98261, 14444, 27645, 94374, 46420, 42987, 41942, 90463,
                   23779, 92451, 13000, 26808, 83403, 24393, 51162, 53178,
                   86967, 78702, 36207, 96775, 12249, 22465, 13662, 76644,
                   66974, 59068
               ],
               [
                   8606, 42647, 85650, 91475, 27044, 21691, 97371, 77517,
                   80278, 84299, 40629, 96550, 33519, 16488, 3948, 63568,
                   70912, 63469, 76343, 36519, 89997, 74289, 97920, 53828,
                   67093, 15005, 80911, 25971, 36830, 55920, 19326, 29046,
                   13497, 31378, 92583, 98625, 9720, 53265, 62398, 70997,
                   51693, 73490, 96594, 98256, 90179, 53635, 18885, 51921,
                   74575, 39932
               ],
               [
                   77729, 37416, 28979, 16818, 78453, 91769, 59814, 98728,
                   49325, 57165, 890, 96966, 37534, 62476, 39512, 42418, 47390,
                   33603, 25419, 80830, 24421, 62888, 89475, 32964, 7623,
                   62104, 15465, 39484, 2768, 8202, 47281, 71554, 78646, 50665,
                   72237, 72600, 34112, 31834, 34547, 84232, 83483, 85855,
                   78699, 86824, 30537, 73628, 26798, 70760, 8082, 6984
               ],
               [
                   89437, 60390, 57532, 16052, 61675, 3378, 31206, 51991,
                   53900, 93855, 80376, 29552, 35765, 36968, 49550, 45252,
                   80412, 53552, 25846, 69013, 94376, 62989, 70037, 29113,
                   99704, 66646, 78563, 59414, 12537, 51134, 70732, 61001,
                   1586, 47823, 56432, 55800, 80205, 72606, 21897, 2781, 30613,
                   53388, 74134, 47406, 42409, 35458, 403, 49109, 97287, 74473
               ],
               [
                   62290, 70526, 96882, 53442, 48403, 30625, 37775, 7765,
                   12425, 40274, 78849, 37695, 45003, 94883, 3159, 24718,
                   96485, 20069, 54903, 8108, 1234, 6665, 61443, 25163, 14464,
                   66515, 81856, 62262, 88816, 10244, 14118, 51931, 83363,
                   77032, 1164, 48705, 975, 84910, 40319, 95923, 75759, 72444,
                   98416, 77793, 40044, 92227, 54707, 73858, 53289, 1530
               ],
               [
                   21118, 8231, 81962, 62269, 13691, 22492, 32677, 22465, 9231,
                   24036, 60275, 12376, 96467, 22416, 9239, 64748, 296, 14347,
                   45037, 49924, 34957, 49580, 74897, 46147, 30732, 9838,
                   64859, 20738, 15840, 7792, 32745, 76317, 42373, 99231, 5544,
                   29899, 64996, 88856, 22882, 4834, 29568, 61855, 45331,
                   32576, 88910, 28086, 34759, 35035, 41509, 62241
               ],
               [
                   29990, 32273, 4953, 75148, 37244, 63783, 50161, 6755, 8933,
                   99607, 81812, 87547, 77232, 98082, 8603, 98884, 4610, 38821,
                   64387, 21044, 64493, 70886, 22234, 80168, 92442, 5091,
                   68795, 41423, 40153, 32912, 15048, 34996, 76923, 61201,
                   85741, 94153, 96339, 56864, 19533, 62388, 49893, 39985,
                   12399, 14162, 88414, 85844, 85900, 41477, 22481, 33767
               ],
               [
                   52166, 74511, 84504, 89848, 64978, 49843, 49414, 72803,
                   87909, 88486, 95783, 61781, 83034, 33086, 28145, 90571,
                   66355, 406, 70497, 92538, 85784, 74457, 75617, 71465, 57825,
                   8969, 38949, 27265, 13071, 74847, 38954, 26818, 76381,
                   87375, 36686, 90752, 97227, 96632, 25072, 16749, 53034,
                   49206, 92324, 90595, 15005, 81899, 93937, 30506, 75337,
                   37782
               ],
               [
                   7361, 65616, 34725, 61978, 66485, 77602, 28376, 65587,
                   28010, 77200, 12944, 47495, 51264, 80828, 89658, 20348,
                   69203, 85517, 77101, 21099, 30203, 45235, 70821, 94292,
                   26943, 41705, 94761, 49484, 31691, 94390, 98166, 55492,
                   87330, 7955, 38630, 84237, 91446, 97486, 88864, 25509,
                   17793, 59034, 16125, 83086, 52060, 95801, 66620, 97730,
                   37821, 14272
               ],
               [
                   16034, 85568, 92979, 55679, 80952, 70248, 78039, 33332,
                   89329, 79423, 53815, 43048, 66888, 20759, 80326, 17887,
                   56107, 99313, 38138, 68859, 39163, 57086, 31952, 203, 65792,
                   39633, 11073, 88990, 43265, 61321, 16304, 99937, 63835,
                   67880, 88073, 32963, 73932, 52600, 87963, 35353, 20978,
                   22727, 11181, 31957, 28991, 7099, 21683, 47888, 21342, 43384
               ],
               [
                   54483, 94862, 4500, 64499, 40219, 37489, 15070, 45527,
                   34260, 24040, 6619, 58009, 85923, 11524, 93994, 45710,
                   56210, 34241, 43023, 37222, 30248, 27431, 36927, 59904,
                   66627, 10624, 35664, 22539, 48708, 58423, 2410, 34656,
                   78044, 69060, 44463, 24857, 79990, 17340, 67167, 62472,
                   21304, 94080, 97091, 3955, 52228, 29143, 42586, 64769,
                   11240, 12563
               ],
               [
                   80930, 96785, 30102, 51349, 78836, 4965, 4541, 11723, 82598,
                   93089, 31703, 70427, 98581, 12390, 53674, 45947, 49895,
                   30591, 22914, 34245, 94558, 19627, 77378, 68036, 58787,
                   45509, 72164, 21254, 46458, 20378, 57262, 8513, 74566,
                   94956, 54463, 1131, 89830, 32006, 20084, 96652, 37906,
                   67165, 86759, 18703, 91603, 59404, 75846, 94022, 49665,
                   99074
               ],
               [
                   78838, 48829, 99918, 62949, 67953, 79875, 3713, 89571, 9368,
                   22950, 99798, 15963, 3699, 90864, 80918, 18501, 36614,
                   99876, 44562, 64426, 45604, 81990, 70929, 27174, 950, 2195,
                   43586, 23431, 70656, 80994, 31910, 13484, 18194, 91468,
                   5024, 91331, 6019, 83685, 56423, 37050, 27801, 16026, 33674,
                   90351, 73060, 65543, 506, 72042, 65587, 95526
               ],
               [
                   29857, 24793, 91781, 91093, 43394, 15964, 2850, 83676,
                   36248, 99108, 88683, 70949, 42594, 67557, 41554, 34959,
                   83828, 7787, 88340, 7485, 47719, 17682, 15956, 35896, 55959,
                   88209, 80377, 34467, 40412, 78528, 59551, 39194, 3696,
                   99202, 34521, 50898, 50507, 46415, 26893, 56894, 85178,
                   92800, 38736, 30813, 65879, 26382, 14696, 63767, 52871,
                   82696
               ],
               [
                   45442, 78402, 5826, 23309, 61475, 38766, 94577, 18388,
                   31875, 66086, 81837, 25318, 75312, 56333, 32726, 60880,
                   26956, 79639, 43274, 33609, 28514, 89960, 42909, 83524,
                   15949, 44179, 61049, 16360, 85251, 54091, 10728, 86818,
                   42997, 11909, 65769, 19606, 83166, 2568, 16257, 94109,
                   17267, 99101, 97859, 85140, 10183, 11178, 23163, 93316,
                   38119, 30503
               ],
               [
                   71867, 73207, 72816, 5866, 43482, 57754, 55935, 67537,
                   21968, 33647, 22684, 78553, 66998, 64820, 11322, 60779,
                   28985, 62120, 82972, 14753, 26910, 50714, 34690, 86904,
                   45514, 41979, 88261, 51516, 28811, 55038, 87672, 73353,
                   77537, 78564, 9144, 79023, 90692, 37421, 90545, 85341, 3529,
                   32109, 29790, 45553, 38181, 68135, 6249, 23527, 67727, 68826
               ],
               [
                   81250, 86078, 86659, 9153, 10908, 39360, 46138, 46098,
                   42780, 63976, 93928, 20185, 99097, 89927, 26276, 70561,
                   12198, 45914, 6996, 30379, 44210, 98956, 92367, 56523, 2253,
                   99559, 35109, 13939, 23143, 98251, 81759, 71780, 64906,
                   92467, 89484, 40586, 92343, 29173, 5597, 23594, 93527, 9509,
                   75988, 38946, 35132, 22047, 58083, 40611, 94393, 10325
               ],
               [
                   80513, 56701, 94772, 40373, 62343, 49160, 70938, 68516,
                   77271, 73708, 72379, 36665, 2753, 23793, 19045, 37975,
                   74961, 56075, 74689, 24024, 5620, 28261, 54281, 73440,
                   64256, 29392, 46806, 79592, 5440, 81367, 36633, 25402,
                   54022, 39525, 75240, 56803, 73352, 87086, 71377, 81069,
                   2562, 70318, 81034, 58094, 61356, 11720, 89625, 19557,
                   70408, 49098
               ],
               [
                   31213, 46388, 44620, 40323, 73796, 6153, 86069, 43578,
                   88519, 83593, 40992, 77942, 30456, 63736, 28599, 75154,
                   86762, 33749, 53494, 41723, 30302, 81383, 3965, 18944,
                   16860, 61904, 16636, 93724, 37792, 95106, 61098, 31145,
                   24037, 77226, 41227, 75085, 13475, 38918, 48595, 49538,
                   12013, 12274, 77, 35446, 45122, 25145, 38988, 28574, 5819,
                   59328
               ],
               [
                   27988, 76495, 49092, 71547, 67403, 92701, 44431, 55117,
                   43122, 74584, 38086, 9537, 49853, 62841, 77588, 44793, 3991,
                   37001, 20225, 20292, 13272, 68837, 43865, 67531, 62762,
                   16208, 51485, 29783, 9337, 77299, 77901, 35057, 37707,
                   45291, 59781, 36422, 22731, 49919, 14926, 1368, 30687, 2232,
                   79929, 27347, 99981, 50358, 55012, 55205, 75241, 89694
               ],
               [
                   78523, 63103, 37562, 39707, 10101, 42593, 54601, 20969,
                   77775, 67996, 17952, 3321, 73566, 94105, 2552, 37161, 10039,
                   79861, 5443, 4006, 85575, 2931, 56475, 75993, 10267, 34156,
                   65694, 27224, 69158, 41807, 43112, 33378, 32920, 62443,
                   55526, 42165, 96844, 51791, 2350, 44030, 55360, 31022,
                   31959, 40510, 68679, 35092, 29839, 47286, 65086, 11840
               ],
               [
                   1508, 10101, 23929, 65646, 1289, 58826, 17240, 58713, 18471,
                   73463, 7556, 14432, 10942, 14161, 28996, 32609, 82662,
                   44900, 24753, 28267, 68368, 14774, 53553, 69917, 6328,
                   57075, 37126, 12662, 88057, 13822, 80054, 84744, 3803,
                   23728, 82925, 28680, 41414, 44219, 54958, 49757, 33660,
                   65727, 22514, 52518, 15474, 52076, 40006, 58477, 3204, 71378
               ],
               [
                   48342, 78975, 65797, 38755, 28821, 38311, 50443, 11984,
                   83967, 58011, 90289, 36883, 15248, 51356, 16997, 78502,
                   37909, 81196, 1119, 75617, 7888, 87359, 50036, 60377, 28871,
                   18712, 4544, 98822, 44079, 18032, 70775, 94442, 18396, 7905,
                   4511, 76496, 78415, 34873, 53627, 52779, 66913, 44224,
                   84104, 75038, 90707, 8184, 16477, 81643, 30328, 90264
               ],
               [
                   33984, 5576, 43807, 33981, 39903, 79310, 44256, 73369,
                   51391, 46915, 40051, 83819, 72797, 28913, 58033, 68315,
                   42446, 35364, 40397, 77920, 16584, 48725, 77498, 49185,
                   33189, 7467, 21721, 83409, 43416, 56522, 14759, 66766,
                   43029, 30518, 92524, 77479, 66882, 91159, 10714, 82991,
                   60429, 42851, 36507, 8408, 6981, 77684, 62437, 82219, 71564,
                   59644
               ],
               [
                   93382, 80535, 73726, 74957, 53886, 73562, 70377, 36530,
                   70067, 74035, 62034, 51563, 26086, 48245, 46462, 68099,
                   94371, 4451, 52822, 62959, 6521, 6070, 37791, 79116, 7349,
                   83688, 88393, 28524, 90594, 35550, 74997, 32260, 96429,
                   77307, 12027, 53858, 83534, 34978, 92405, 34935, 80471,
                   83404, 67905, 92591, 79015, 2859, 36453, 63554, 80353, 43151
               ],
               [
                   85569, 64257, 4581, 61378, 79187, 21, 20649, 38682, 22921,
                   60510, 63699, 72648, 69208, 40481, 24394, 58988, 77225,
                   26642, 41232, 13091, 5924, 29632, 80171, 86527, 75140,
                   13587, 20314, 17159, 90272, 18677, 77316, 46282, 21247,
                   37427, 43904, 65427, 27413, 32295, 29741, 4968, 15173,
                   13102, 77471, 48690, 74799, 16440, 4064, 64967, 8866, 23950
               ],
               [
                   31466, 20467, 71311, 46930, 26832, 8820, 86034, 12906,
                   79507, 94973, 52994, 87711, 96697, 41051, 79716, 93043,
                   95942, 17329, 49828, 3400, 57885, 58208, 25889, 12313,
                   96030, 82527, 51067, 98496, 10386, 20257, 43125, 63575,
                   55628, 6665, 77575, 10981, 95736, 65847, 92090, 96774,
                   30911, 28674, 20972, 88419, 61581, 92308, 30584, 43155,
                   27780, 6299
               ],
               [
                   38840, 14903, 73243, 21279, 71774, 6052, 5417, 49879, 26335,
                   45938, 55155, 20349, 37363, 51390, 38895, 53719, 24421,
                   38167, 78571, 38413, 73489, 50006, 2425, 32185, 36468,
                   46614, 40401, 36553, 12943, 17782, 76058, 34681, 51175,
                   87045, 19611, 20969, 35604, 3311, 10573, 16034, 56763,
                   52838, 13878, 9340, 67446, 91884, 98990, 96760, 82117, 97199
               ],
               [
                   23488, 20470, 74391, 78068, 28153, 91101, 25667, 32715,
                   8375, 4958, 79583, 59155, 48657, 35244, 73341, 31219, 99927,
                   97780, 27763, 71379, 23332, 55922, 17759, 4441, 60204,
                   39440, 51897, 45346, 75901, 5238, 26291, 44271, 80320,
                   92608, 56610, 29654, 33031, 64270, 20826, 35373, 52236,
                   42744, 77589, 45131, 43225, 82103, 10246, 62881, 4650, 86643
               ],
               [
                   82702, 52198, 6583, 70848, 46994, 45777, 99978, 24959,
                   81182, 27268, 69524, 90352, 68571, 60913, 97648, 19406,
                   48931, 78296, 27810, 89957, 62726, 8584, 88635, 58194, 4573,
                   71200, 80132, 96334, 52687, 58693, 17110, 41875, 12320,
                   3891, 73679, 65612, 28772, 37085, 80149, 11655, 40666,
                   79910, 63377, 29597, 34608, 19463, 98906, 731, 93547, 29245
               ],
               [
                   53370, 93850, 60696, 47433, 82999, 67321, 80921, 26101,
                   18369, 49009, 4487, 10522, 27959, 47814, 60360, 88494,
                   99542, 57112, 11983, 54641, 71541, 760, 5340, 82030, 3332,
                   8231, 31779, 93848, 8943, 73887, 5057, 95384, 66541, 89739,
                   1119, 26031, 49483, 10671, 78822, 13450, 87786, 4141, 55847,
                   74020, 25211, 82470, 63595, 26047, 45482, 90379
               ],
               [
                   16021, 8478, 91340, 88759, 43336, 26377, 28408, 67621,
                   48452, 86949, 22392, 99066, 44324, 42504, 93344, 31414,
                   59196, 46035, 40503, 47370, 3135, 30749, 70011, 41770,
                   76171, 22400, 43952, 94, 57879, 25034, 52088, 63791, 96029,
                   30495, 43605, 48919, 99012, 72745, 2204, 24846, 72564,
                   98086, 47433, 64199, 53430, 22641, 26181, 9184, 14840, 28057
               ],
               [
                   85149, 21804, 7019, 81808, 9337, 30167, 61963, 64810, 52875,
                   46132, 70608, 8218, 72009, 61938, 3519, 65111, 84255, 55614,
                   39527, 74636, 32972, 48839, 71648, 59702, 37192, 53682,
                   43026, 45541, 74094, 23952, 5453, 41594, 93467, 92622,
                   21254, 87520, 21431, 65386, 42223, 22805, 40786, 97355,
                   18793, 69751, 71965, 18015, 49016, 769, 62659, 8078
               ],
               [
                   53347, 53087, 20475, 23493, 89501, 5930, 87442, 46110,
                   53221, 68451, 80924, 75610, 98630, 38484, 27560, 59902,
                   81371, 85750, 10070, 65665, 88280, 93381, 23011, 56985,
                   35340, 66100, 75048, 60872, 96937, 90327, 68544, 42687,
                   64056, 9968, 11442, 56419, 99395, 75804, 56598, 99967,
                   63134, 97448, 58621, 58509, 51238, 9956, 93948, 93818,
                   15792, 89650
               ],
               [
                   3690, 55037, 13706, 82100, 94617, 12742, 97894, 66497,
                   68224, 25697, 11379, 12746, 63936, 11746, 59429, 46331,
                   46174, 24519, 16377, 92219, 1387, 93916, 98439, 43335,
                   50562, 22970, 91826, 15913, 72604, 54962, 37802, 90551,
                   35716, 75316, 5391, 33759, 96785, 95430, 81686, 87352,
                   51125, 22605, 12693, 14197, 90440, 58740, 79388, 31385,
                   87149, 46829
               ],
               [
                   1846, 15131, 55064, 29368, 46026, 52292, 71603, 30289,
                   58860, 67172, 91696, 67630, 49632, 70830, 58088, 93096,
                   42037, 26642, 6346, 30992, 63087, 71926, 78410, 59657,
                   55762, 68551, 46208, 27485, 72814, 35074, 37091, 55452,
                   39488, 44655, 53155, 92791, 47913, 95118, 77867, 14558,
                   97793, 43163, 9762, 24674, 60028, 62815, 92507, 28187,
                   29689, 74575
               ],
               [
                   43626, 28619, 64269, 21841, 12089, 46892, 86052, 69904,
                   79896, 16612, 88298, 23031, 16235, 13099, 66353, 45079,
                   89291, 1770, 99859, 43870, 12265, 81554, 91362, 90677, 3134,
                   40082, 38407, 18074, 55849, 85456, 50825, 6025, 14359,
                   61130, 95337, 1596, 72821, 62409, 29349, 53041, 52731,
                   70279, 55814, 39882, 28205, 96634, 21240, 43440, 42006,
                   68669
               ],
               [
                   76722, 24476, 83025, 16000, 97872, 97591, 38908, 72236,
                   68911, 52079, 33481, 61702, 66850, 95515, 69370, 4649,
                   46679, 583, 46152, 24463, 21845, 20424, 4573, 24680, 15081,
                   83593, 28942, 18931, 95545, 86166, 55091, 67252, 79694,
                   55711, 63561, 47696, 52276, 77718, 44868, 43587, 96583,
                   4031, 56956, 97830, 74997, 49155, 19999, 71011, 48850, 18852
               ],
               [
                   88063, 87584, 75617, 83415, 7531, 74557, 67691, 24758,
                   49889, 49079, 83234, 87706, 77858, 94912, 34828, 86634,
                   56205, 97480, 78957, 76417, 83874, 736, 19692, 75025, 25427,
                   13521, 47313, 5475, 40447, 56025, 82076, 42964, 27617,
                   88129, 37679, 50039, 20150, 13949, 22575, 21471, 61038,
                   93920, 75794, 71939, 78359, 12338, 78762, 17540, 92873,
                   10613
               ],
               [
                   46831, 42328, 10031, 21195, 9961, 78976, 855, 11537, 19951,
                   86697, 93849, 75861, 32844, 5866, 57946, 75145, 36376,
                   35920, 58672, 44313, 39345, 26345, 58364, 3646, 34658,
                   12481, 17881, 24069, 60995, 99461, 12800, 61188, 66073,
                   77845, 71948, 59937, 49171, 6077, 91639, 46070, 61676,
                   94806, 38066, 68822, 68446, 56306, 4766, 68198, 32988, 31252
               ],
               [
                   7213, 20113, 21066, 45677, 17623, 70214, 82767, 32528,
                   81015, 66278, 33259, 15305, 2963, 48420, 49718, 18227,
                   42484, 59905, 47772, 41006, 48460, 16888, 93041, 67826,
                   5846, 37929, 70743, 77945, 10884, 48093, 42697, 87619,
                   43884, 79048, 88980, 14786, 13340, 39899, 97073, 34718,
                   17081, 40630, 25973, 5246, 32214, 83733, 27977, 72370,
                   74315, 61500
               ],
               [
                   4661, 63558, 14213, 43899, 33563, 15456, 14211, 60185, 1358,
                   62429, 20851, 44819, 80784, 3815, 75161, 79722, 54121,
                   37232, 10030, 36722, 39421, 55520, 55974, 7609, 13240,
                   30900, 15070, 85256, 35219, 60432, 1441, 67364, 97079,
                   46663, 5946, 87444, 34743, 59478, 84561, 28419, 14775,
                   57953, 21830, 3263, 25547, 97035, 84491, 39317, 48642, 98728
               ],
               [
                   1618, 35381, 82987, 29644, 12130, 97883, 88048, 37323,
                   29417, 31152, 7074, 42053, 97120, 89562, 6331, 35797, 72816,
                   25776, 20070, 34165, 52632, 84753, 18900, 22320, 6443,
                   73142, 89754, 29041, 14658, 14472, 28711, 47747, 1254, 1494,
                   62692, 73135, 60242, 56433, 84618, 898, 78145, 5971, 73100,
                   87340, 78780, 44300, 48235, 48836, 76435, 29313
               ]]], [4960038, 4910595, 4891267]],
        ],
    )