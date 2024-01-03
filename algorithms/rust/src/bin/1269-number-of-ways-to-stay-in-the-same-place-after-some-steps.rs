/*
 * @lc app=leetcode id=1269 lang=rust
 *
 * [1269] Number of Ways to Stay in the Same Place After Some Steps
 *
 * https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/description/
 *
 * algorithms
 * Hard (43.48%)
 * Likes:    1011
 * Dislikes: 50
 * Total Accepted:    51.6K
 * Total Submissions: 109.6K
 * Testcase Example:  '3\n2'
 *
 * You have a pointer at index 0 in an array of size arrLen. At each step,
 * you can move 1 position to the left, 1 position to the right in the array,
 * or stay in the same place (The pointer should not be placed outside the
 * array at any time).
 *
 * Given two integers steps and arrLen, return the number of ways such that
 * your pointer is still at index 0 after exactly steps steps. Since the
 * answer may be too large, return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: steps = 3, arrLen = 2
 * Output: 4
 * Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
 * Right, Left, Stay
 * Stay, Right, Left
 * Right, Stay, Left
 * Stay, Stay, Stay
 *
 *
 * Example 2:
 *
 *
 * Input: steps = 2, arrLen = 4
 * Output: 2
 * Explanation: There are 2 differents ways to stay at index 0 after 2 steps
 * Right, Left
 * Stay, Stay
 *
 *
 * Example 3:
 *
 *
 * Input: steps = 4, arrLen = 2
 * Output: 8
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= steps <= 500
 * 1 <= arrLen <= 10^6
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn num_ways(steps: i32, arr_len: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut dp = vec![0; arr_len.min(steps / 2 + 1) as usize];
        dp[0] = 1;
        for step in 1..steps as usize + 1 {
            let mut prev = 0;
            for i in 0..dp.len() {
                if i > step {
                    break;
                }
                let next_prev = dp[i];
                dp[i] += prev;
                dp[i] %= MOD;
                if i < dp.len() - 1 {
                    dp[i] += dp[i + 1];
                    dp[i] %= MOD;
                }
                prev = next_prev;
            }
        }
        dp[0]
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::num_ways(e.0, e.1),
        vec![((3, 2), 4), ((2, 4), 2), ((4, 2), 8)],
        |a, b| a == b,
    );
}
