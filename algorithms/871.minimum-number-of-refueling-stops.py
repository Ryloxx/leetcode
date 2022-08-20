#
# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#
# https://leetcode.com/problems/minimum-number-of-refueling-stops/description/
#
# algorithms
# Hard (35.74%)
# Likes:    3816
# Dislikes: 75
# Total Accepted:    108.7K
# Total Submissions: 273.2K
# Testcase Example:  '1\n1\n[]'
#
# A car travels from a starting position to a destination which is target miles
# east of the starting position.
#
# There are gas stations along the way. The gas stations are represented as an
# array stations where stations[i] = [positioni, fueli] indicates that the i^th
# gas station is positioni miles east of the starting position and has fueli
# liters of gas.
#
# The car starts with an infinite tank of gas, which initially has startFuel
# liters of fuel in it. It uses one liter of gas per one mile that it drives.
# When the car reaches a gas station, it may stop and refuel, transferring all
# the gas from the station into the car.
#
# Return the minimum number of refueling stops the car must make in order to
# reach its destination. If it cannot reach the destination, return -1.
#
# Note that if the car reaches a gas station with 0 fuel left, the car can
# still refuel there. If the car reaches the destination with 0 fuel left, it
# is still considered to have arrived.
#
#
# Example 1:
#
#
# Input: target = 1, startFuel = 1, stations = []
# Output: 0
# Explanation: We can reach the target without refueling.
#
#
# Example 2:
#
#
# Input: target = 100, startFuel = 1, stations = [[10,100]]
# Output: -1
# Explanation: We can not reach the target (or even the first gas station).
#
#
# Example 3:
#
#
# Input: target = 100, startFuel = 10, stations =
# [[10,60],[20,30],[30,30],[60,40]]
# Output: 2
# Explanation: We start with 10 liters of fuel.
# We drive to position 10, expending 10 liters of fuel.  We refuel from 0
# liters to 60 liters of gas.
# Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
# and refuel from 10 liters to 50 liters of gas.  We then drive to and reach
# the target.
# We made 2 refueling stops along the way, so we return 2.
#
#
#
# Constraints:
#
#
# 1 <= target, startFuel <= 10^9
# 0 <= stations.length <= 500
# 0 <= positioni <= positioni+1 < target
# 1 <= fueli < 10^9
#
#
#
from heapq import heappop, heappush
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    def minRefuelStops(self, target: int, startFuel: int,
                       stations: List[List[int]]) -> int:
        stations.append([target, 0])
        bank, res, current_dist = [], 0, 0
        for dist, refill in stations:
            diff = dist - current_dist
            current_dist += diff
            startFuel -= diff
            while startFuel < 0:
                if not bank:
                    return -1
                startFuel -= heappop(bank)
                res += 1
            heappush(bank, -refill)
        return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.minRefuelStops, Solution()),
        [
            [[100, 50, [[25, 25], [50, 50]]], 1],
            [[1, 1, []], 0],
            [[100, 1, [[10, 100]]], -1],
            [[100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]], 2],
            [[100, 10, [[10, 100], [20, 30], [30, 30], [60, 40]]], 1],
        ],
    )
