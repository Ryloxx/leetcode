/*
 * @lc app=leetcode id=1513 lang=rust
 *
 * [1513] Number of Substrings With Only 1s
 *
 * https://leetcode.com/problems/number-of-substrings-with-only-1s/description/
 *
 * algorithms
 * Medium (46.76%)
 * Likes:    900
 * Dislikes: 34
 * Total Accepted:    52.4K
 * Total Submissions: 109.6K
 * Testcase Example:  '"0110111"'
 *
 * Given a binary string s, return the number of substrings with all
 * characters 1's. Since the answer may be too large, return it modulo 10^9 +
 * 7.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "0110111"
 * Output: 9
 * Explanation: There are 9 substring in total with only 1's characters.
 * "1" -> 5 times.
 * "11" -> 3 times.
 * "111" -> 1 time.
 *
 * Example 2:
 *
 *
 * Input: s = "101"
 * Output: 2
 * Explanation: Substring "1" is shown 2 times in s.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "111111"
 * Output: 21
 * Explanation: Each substring contains only 1's characters.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s[i] is either '0' or '1'.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn num_sub(s: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut res = 0;
        let mut l = 0;
        for c in s.as_bytes() {
            l = (c - b'0') as i32 * (l + 1);
            res = (res + l) % MOD;
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::num_sub,
        vec![
            ("0110111".to_string(), 9),
            ("101".to_string(), 2),
            ("111111".to_string(), 21),
            ("1".to_string(), 1),
            ("0".to_string(), 0),
        ],
        |a, b| a == b,
    );
}
