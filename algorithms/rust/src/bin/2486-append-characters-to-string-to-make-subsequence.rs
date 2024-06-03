/*
 * @lc app=leetcode id=2486 lang=rust
 *
 * [2486] Append Characters to String to Make Subsequence
 *
 * https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/
 *
 * algorithms
 * Medium (65.98%)
 * Likes:    856
 * Dislikes: 64
 * Total Accepted:    116.3K
 * Total Submissions: 160.6K
 * Testcase Example:  '"coaching"\n"coding"'
 *
 * You are given two strings s and t consisting of only lowercase English
 * letters.
 *
 * Return the minimum number of characters that need to be appended to the
 * end of s so that t becomes a subsequence of s.
 *
 * A subsequence is a string that can be derived from another string by
 * deleting some or no characters without changing the order of the remaining
 * characters.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "coaching", t = "coding"
 * Output: 4
 * Explanation: Append the characters "ding" to the end of s so that s =
 * "coachingding".
 * Now, t is a subsequence of s ("coachingding").
 * It can be shown that appending any 3 characters to the end of s will never
 * make t a subsequence.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "abcde", t = "a"
 * Output: 0
 * Explanation: t is already a subsequence of s ("abcde").
 *
 *
 * Example 3:
 *
 *
 * Input: s = "z", t = "abcde"
 * Output: 5
 * Explanation: Append the characters "abcde" to the end of s so that s =
 * "zabcde".
 * Now, t is a subsequence of s ("zabcde").
 * It can be shown that appending any 4 characters to the end of s will never
 * make t a subsequence.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length, t.length <= 10^5
 * s and t consist only of lowercase English letters.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn append_characters(s: String, t: String) -> i32 {
        let mut i = 0;
        let mut j = 0;
        while i < s.len() && j < t.len() {
            if s.as_bytes()[i] == t.as_bytes()[j] {
                j += 1;
            }
            i += 1;
        }
        (t.len() - j) as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::append_characters(e.0, e.1),
        vec![
            (("coaching".to_string(), "coding".to_string()), 4),
            (("abcde".to_string(), "a".to_string()), 0),
            (("z".to_string(), "abcde".to_string()), 5),
        ],
        |a, b| a == b,
    )
}
