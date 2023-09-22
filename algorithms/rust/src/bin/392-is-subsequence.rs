/*
 * @lc app=leetcode id=392 lang=rust
 *
 * [392] Is Subsequence
 *
 * https://leetcode.com/problems/is-subsequence/description/
 *
 * algorithms
 * Easy (47.21%)
 * Likes:    8802
 * Dislikes: 468
 * Total Accepted:    1.1M
 * Total Submissions: 2.3M
 * Testcase Example:  '"abc"\n"ahbgdc"'
 *
 * Given two strings s and t, return true if s is a subsequence of t, or
 * false otherwise.
 *
 * A subsequence of a string is a new string that is formed from the original
 * string by deleting some (can be none) of the characters without disturbing
 * the relative positions of the remaining characters. (i.e., "ace" is a
 * subsequence of "abcde" while "aec" is not).
 *
 *
 * Example 1:
 * Input: s = "abc", t = "ahbgdc"
 * Output: true
 * Example 2:
 * Input: s = "axc", t = "ahbgdc"
 * Output: false
 *
 *
 * Constraints:
 *
 *
 * 0 <= s.length <= 100
 * 0 <= t.length <= 10^4
 * s and t consist only of lowercase English letters.
 *
 *
 *
 * Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where
 * k >= 10^9, and you want to check one by one to see if t has its
 * subsequence. In this scenario, how would you change your code?
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        let s = s.as_bytes();
        let t = t.as_bytes();
        let mut i = 0;
        let mut j = 0;
        while i < s.len() && j < t.len() {
            if s[i] == t[j] {
                i += 1;
            }
            j += 1;
        }
        i == s.len()
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::is_subsequence(e.0, e.1),
        vec![
            (("abc".to_string(), "ahbgdc".to_string()), true),
            (("axc".to_string(), "ahbgdc".to_string()), false),
            (("".to_string(), "".to_string()), true),
            (("".to_string(), "ahbgdc".to_string()), true),
        ],
        |a, b| a == b,
    )
}
