/*
 * @lc app=leetcode id=2466 lang=rust
 *
 * [2466] Count Ways To Build Good Strings
 *
 * https://leetcode.com/problems/count-ways-to-build-good-strings/description/
 *
 * algorithms
 * Medium (42.09%)
 * Likes:    958
 * Dislikes: 82
 * Total Accepted:    33.8K
 * Total Submissions: 63.3K
 * Testcase Example:  '3\n3\n1\n1'
 *
 * Given the integers zero, one, low, and high, we can construct a string by
 * starting with an empty string, and then at each step perform either of the
 * following:
 *
 *
 * Append the character '0' zero times.
 * Append the character '1' one times.
 *
 *
 * This can be performed any number of times.
 *
 * A good string is a string constructed by the above process having a length
 * between low and high (inclusive).
 *
 * Return the number of different good strings that can be constructed
 * satisfying these properties. Since the answer can be large, return it modulo
 * 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: low = 3, high = 3, zero = 1, one = 1
 * Output: 8
 * Explanation:
 * One possible valid good string is "011".
 * It can be constructed as follows: "" -> "0" -> "01" -> "011".
 * All binary strings from "000" to "111" are good strings in this example.
 *
 *
 * Example 2:
 *
 *
 * Input: low = 2, high = 3, zero = 1, one = 2
 * Output: 5
 * Explanation: The good strings are "00", "11", "000", "110", and "011".
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= low <= high <= 10^5
 * 1 <= zero, one <= low
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn count_good_strings(low: i32, high: i32, zero: i32, one: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let zero = zero as usize;
        let one = one as usize;
        let low = low as usize;
        let high = high as usize;
        let n = std::cmp::min(std::cmp::max(zero, one), high) + 1;
        let mut dp = vec![0; n];
        let mut res: i32 = 0;
        dp[0] = 1;

        for i in 1..=high {
            dp[i % n] = (if i >= zero { dp[(i - zero) % n] } else { 0 }
                + if i >= one { dp[(i - one) % n] } else { 0 })
                % MOD;
            if i >= low && i <= high {
                res += dp[i % n];
                res %= MOD;
            }
        }
        res
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::count_good_strings(e.0, e.1, e.2, e.3),
        vec![
            ((3, 3, 1, 1), 8),
            ((2, 3, 1, 2), 5),
            ((200, 200, 10, 1), 764262396),
            ((1, 1, 1, 1), 2),
        ],
        |a, b| a == b,
    );
}
