#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (54.41%)
# Likes:    5688
# Dislikes: 284
# Total Accepted:    456.1K
# Total Submissions: 817.3K
# Testcase Example:  '["i","love","leetcode","i","love","coding"]\n2'
#
# Given an array of strings words and an integer k, return the k most frequent
# strings.
#
# Return the answer sorted by the frequency from highest to lowest. Sort the
# words with the same frequency by their lexicographical order.
#
#
# Example 1:
#
#
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
#
#
# Example 2:
#
#
# Input: words =
# ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# with the number of occurrence being 4, 3, 2 and 1 respectively.
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]
#
#
#
# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
#
#
from collections import Counter
# from heapq import heappop, heappush
from heapq import nsmallest
from typing import List
from algo_input import run
from types import MethodType


# @lc code=start
class Solution:
    # Using built-in
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        w_count = Counter(words)
        return nsmallest(k, w_count, key=lambda x: (-w_count[x], x))

    # Custom
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:

    #     class Node:

    #         def __init__(self, freq: int, w: str):
    #             self.freq = freq
    #             self.w = w

    #         def __lt__(self, other):
    #             return (self.freq < other.freq
    #                     or self.freq == other.freq and self.w > other.w)

    #     if k <= 0:
    #         return []
    #     w_count, h = Counter(words), []
    #     for w in w_count:
    #         n = Node(w_count[w], w)
    #         heappush(h, n)
    #         if len(h) > k:
    #             heappop(h)
    #     res = [""] * len(h)
    #     while h:
    #         res[len(h)] = heappop(h).w
    #     return res


# @lc code=end
if __name__ == "__main__":
    run(
        MethodType(Solution.topKFrequent, Solution()),
        [
            ([["i", "love", "leetcode", "i", "love", "coding"], 3
              ], ["i", "love", "coding"]),
            ([["i", "love", "leetcode", "i", "love", "coding"], 2
              ], ["i", "love"]),
            ([[
                "the", "day", "is", "sunny", "the", "the", "the", "sunny",
                "is", "is"
            ], 4], ["the", "is", "sunny", "day"]),
            ([["i", "love", "leetcode", "i", "love", "coding"], 0], []),
            ([["i", "love", "leetcode", "i", "love", "coding"], 4
              ], ["i", "love", "coding", "leetcode"]),
            ([["i", "love", "leetcode", "i", "love", "coding"], 1], ["i"]),
            ([["aaa", "aa", "a"], 2], ["a", "aa"]),
        ],
    )
