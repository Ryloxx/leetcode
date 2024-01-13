/*
 * @lc app=leetcode id=1347 lang=rust
 *
 * [1347] Minimum Number of Steps to Make Two Strings Anagram
 *
 * https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
 *
 * algorithms
 * Medium (78.20%)
 * Likes:    2155
 * Dislikes: 93
 * Total Accepted:    170.1K
 * Total Submissions: 213.6K
 * Testcase Example:  '"bab"\n"aba"'
 *
 * You are given two strings of the same length s and t. In one step you can
 * choose any character of t and replace it with another character.
 *
 * Return the minimum number of steps to make t an anagram of s.
 *
 * An Anagram of a string is a string that contains the same characters with
 * a different (or the same) ordering.
 *
 *
 * Example 1:
 *
 * Input: s = "bab", t = "aba" Output: 1
 * Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram
 * of s.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "leetcode", t = "practice"
 * Output: 5
 * Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper
 * characters to make t anagram of s.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "anagram", t = "mangaar"
 * Output: 0
 * Explanation: "anagram" and "mangaar" are anagrams.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 5 * 10^4
 * s.length == t.length
 * s and t consist of lowercase English letters only.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        let mut ret = [0i32; 26];
        for c in s.as_bytes() {
            ret[(c - b'a') as usize] += 1;
        }
        for c in t.as_bytes() {
            ret[(c - b'a') as usize] -= 1;
        }
        ret.into_iter().map(|value| value.abs()).sum::<i32>() / 2
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::min_steps(e.0, e.1),
        vec![
            //
            (("bab".to_string(), "aba".to_string()), 1),
            (("leetcode".to_string(), "practice".to_string()), 5),
            (("anagram".to_string(), "mangaar".to_string()), 0),
        ],
        |a, b| a == b,
    )
}
