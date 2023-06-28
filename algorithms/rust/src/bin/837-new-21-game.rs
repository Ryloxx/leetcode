/*
 * @lc app=leetcode id=837 lang=rust
 *
 * [837] New 21 Game
 *
 * https://leetcode.com/problems/new-21-game/description/
 *
 * algorithms
 * Medium (36.09%)
 * Likes:    1650
 * Dislikes: 1443
 * Total Accepted:    57.7K
 * Total Submissions: 133.5K
 * Testcase Example:  '10\n1\n10'
 *
 * Alice plays the following game, loosely based on the card game "21".
 *
 * Alice starts with 0 points and draws numbers while she has less than k
 * points. During each draw, she gains an integer number of points randomly
 * from the range [1, maxPts], where maxPts is an integer. Each draw is
 * independent and the outcomes have equal probabilities.
 *
 * Alice stops drawing numbers when she gets k or more points.
 *
 * Return the probability that Alice has n or fewer points.
 *
 * Answers within 10^-5 of the actual answer are considered accepted.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 10, k = 1, maxPts = 10
 * Output: 1.00000
 * Explanation: Alice gets a single card, then stops.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 6, k = 1, maxPts = 10
 * Output: 0.60000
 * Explanation: Alice gets a single card, then stops.
 * In 6 out of 10 possibilities, she is at or below 6 points.
 *
 *
 * Example 3:
 *
 *
 * Input: n = 21, k = 17, maxPts = 10
 * Output: 0.73278
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= k <= n <= 10^4
 * 1 <= maxPts <= 10^4
 *
 *
 */

use std::collections::{HashMap, VecDeque};

struct Solution;
// @lc code=start
impl Solution {
    pub fn new21_game(n: i32, k: i32, max_pts: i32) -> f64 {
        if k == 0 || n >= k + max_pts {
            return 1.;
        }
        let n = n as usize;
        let k = k as usize;
        let max_pts = max_pts as usize;
        let mut dp = vec![0.0; n + 1];
        let p = 1.0 / max_pts as f64;
        dp[0] = 1.0;
        let mut s = 1.0;
        for i in 1..=n {
            dp[i] = s * p;
            if i < k {
                s += dp[i];
            }
            if i >= max_pts && i < k + max_pts {
                s -= dp[i - max_pts];
            }
        }
        return dp.iter().skip(k).sum::<f64>();
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |s| Solution::new21_game(s.0, s.1, s.2),
        vec![
            ((10, 1, 10), 1.00000),
            ((6, 1, 10), 0.60000),
            ((21, 17, 10), 0.73278),
            ((7, 5, 3), 1.00000),
            ((5, 4, 10), 0.26620),
            ((5, 4, 100), 0.02061),
        ],
        |a, b| (a - b).abs().lt(&1e-5),
    )
}
