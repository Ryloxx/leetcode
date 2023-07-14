/*
 * @lc app=leetcode id=1218 lang=rust
 *
 * [1218] Longest Arithmetic Subsequence of Given Difference
 *
 * https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
 *
 * algorithms
 * Medium (51.86%)
 * Likes:    1975
 * Dislikes: 56
 * Total Accepted:    81.5K
 * Total Submissions: 152.6K
 * Testcase Example:  '[1,2,3,4]\n1'
 *
 * Given an integer array arr and an integer difference, return the length of
 * the longest subsequence in arr which is an arithmetic sequence such that
 * the difference between adjacent elements in the subsequence equals
 * difference.
 *
 * A subsequence is a sequence that can be derived from arr by deleting some
 * or no elements without changing the order of the remaining elements.
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [1,2,3,4], difference = 1
 * Output: 4
 * Explanation: The longest arithmetic subsequence is [1,2,3,4].
 *
 * Example 2:
 *
 *
 * Input: arr = [1,3,5,7], difference = 1
 * Output: 1
 * Explanation: The longest arithmetic subsequence is any single element.
 *
 *
 * Example 3:
 *
 *
 * Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
 * Output: 4
 * Explanation: The longest arithmetic subsequence is [7,5,3,1].
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= arr.length <= 10^5
 * -10^4 <= arr[i], difference <= 10^4
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn longest_subsequence(arr: Vec<i32>, difference: i32) -> i32 {
        let mut seen = HashMap::<i32, i32>::new();
        let mut res = 0;
        for &curr in arr.iter() {
            let prev = curr - difference;
            let length = if let Some(prev) = seen.get(&prev) {
                prev + 1
            } else {
                1
            };
            seen.insert(curr, length);
            res = res.max(length);
        }
        res
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::longest_subsequence(e.0, e.1),
        vec![
            ((vec![1, 2, 3, 4], 1), 4),
            ((vec![1, 3, 5, 7], 1), 1),
            ((vec![1, 5, 7, 8, 5, 3, 4, 2, 1], -2), 4),
            ((vec![3, 0, -3, 4, -4, 7, 6], 3), 2),
        ],
        |a, b| a == b,
    );
}
