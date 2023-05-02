#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (70.18%)
# Likes:    4954
# Dislikes: 528
# Total Accepted:    225.9K
# Total Submissions: 321.2K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# You are given an array of people, people, which are the attributes of some
# people in a queue (not necessarily in order). Each people[i] = [hi, ki]
# represents the i^th person of height hi with exactly ki other people in front
# who have a height greater than or equal to hi.
#
# Reconstruct and return the queue that is represented by the input array
# people. The returned queue should be formatted as an array queue, where
# queue[j] = [hj, kj] is the attributes of the j^th person in the queue
# (queue[0] is the person at the front of the queue).
#
#
# Example 1:
#
#
# Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# Explanation:
# Person 0 has height 5 with no other people taller or the same height in
# front.
# Person 1 has height 7 with no other people taller or the same height in
# front.
# Person 2 has height 5 with two persons taller or the same height in front,
# which is person 0 and 1.
# Person 3 has height 6 with one person taller or the same height in front,
# which is person 1.
# Person 4 has height 4 with four people taller or the same height in front,
# which are people 0, 1, 2, and 3.
# Person 5 has height 7 with one person taller or the same height in front,
# which is person 1.
# Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
#
#
# Example 2:
#
#
# Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
#
#
#
# Constraints:
#
#
# 1 <= people.length <= 2000
# 0 <= hi <= 10^6
# 0 <= ki < people.length
# It is guaranteed that the queue can be reconstructed.
#
#
#
# from collections import defaultdict
# from functools import reduce
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:

    # O(NlogN) time complexity
    # O(N) space complexity
    # Using Fenwick tree + optimized lower bound search
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        BIT = [0] + [1] * n

        def find_lo(val):
            idx = 0
            for i in range(n.bit_length(), -1, -1):
                mask = 1 << i
                next_idx = idx + mask
                if next_idx < n and BIT[next_idx] < val:
                    idx = next_idx
                    val -= BIT[next_idx]
            return idx

        def update(i, value):
            i += 1
            while i < len(BIT):
                BIT[i] += value
                i += i & -i

        people.sort(key=lambda x: [x[0], -x[1]])
        res = [0] * n

        for i in range(n):
            p = i + (i & -i)
            if p < n:
                BIT[p] += BIT[i]

        for h, k in people:
            lo = find_lo(k + 1)
            res[lo] = [h, k]
            update(lo, -1)

        return res

    # O(N**2) time complexity
    # O(N) space complexity
    # def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    #     n = len(people)
    #     people.sort(key=lambda x: [x[0], -x[1]])
    #     res = [0] * n
    #     for p in people:
    #         seen, k = 0, p[1]
    #         for j in range(n):
    #             if not res[j]:
    #                 if seen == k:
    #                     res[j] = p
    #                     break
    #                 seen += 1
    #     return res

    # O(N**2) time complexity
    # O(N) space complexity
    # I didn't come up with this one myself but it is quite an elegant one.
    #
    # def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    #     return reduce(
    #         lambda a, b: a.insert(b[1], b) or a,
    #         sorted(people, key=lambda x: [x[0], -x[1]], reverse=True), [])


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.reconstructQueue, Solution()),
        [[[[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]],
          [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]],
         [[[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]],
          [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]],
         [[[[0, 0]]], [[0, 0]]]],
    )
