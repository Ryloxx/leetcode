/*
 * @lc app=leetcode id=2370 lang=rust
 *
 * [2370] Longest Ideal Subsequence
 *
 * https://leetcode.com/problems/longest-ideal-subsequence/description/
 *
 * algorithms
 * Medium (37.50%)
 * Likes:    1011
 * Dislikes: 41
 * Total Accepted:    45.3K
 * Total Submissions: 106.7K
 * Testcase Example:  '"acfgbd"\n2'
 *
 * You are given a string s consisting of lowercase letters and an integer k.
 * We call a string t ideal if the following conditions are satisfied:
 *
 *
 * t is a subsequence of the string s.
 * The absolute difference in the alphabet order of every two adjacent
 * letters in t is less than or equal to k.
 *
 *
 * Return the length of the longest ideal string.
 *
 * A subsequence is a string that can be derived from another string by
 * deleting some or no characters without changing the order of the remaining
 * characters.
 *
 * Note that the alphabet order is not cyclic. For example, the absolute
 * difference in the alphabet order of 'a' and 'z' is 25, not 1.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "acfgbd", k = 2
 * Output: 4
 * Explanation: The longest ideal string is "acbd". The length of this string
 * is 4, so 4 is returned.
 * Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3
 * in alphabet order.
 *
 * Example 2:
 *
 *
 * Input: s = "abcd", k = 3
 * Output: 4
 * Explanation: The longest ideal string is "abcd". The length of this string
 * is 4, so 4 is returned.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * 0 <= k <= 25
 * s consists of lowercase English letters.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn longest_ideal_string(s: String, k: i32) -> i32 {
        let k = k as usize;
        let mut dp = [0; 256];
        let mut res = 0;
        for i in s.as_bytes().iter().copied() {
            let u = i as usize;
            let best = unsafe {
                dp.iter()
                    .take(u + k + 1)
                    .skip(u - k)
                    .max()
                    .unwrap_unchecked()
            };
            dp[u] = dp[u].max(best + 1);
            res = res.max(dp[u]);
        }
        res
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::longest_ideal_string(e.0, e.1),
        vec![
            (("acfgbd".to_string(), 2), 4),
            (("abcd".to_string(), 3), 4),
            (("aaaaaa".to_string(), 3), 6),
            (("aaaaaa".to_string(), 1), 6),
            (("azaza".to_string(), 25), 5),
            (("azaza".to_string(), 0), 3),
        ],
        |a, b| a == b,
    )
}
