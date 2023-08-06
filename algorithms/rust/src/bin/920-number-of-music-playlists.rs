/*
 * @lc app=leetcode id=920 lang=rust
 *
 * [920] Number of Music Playlists
 *
 * https://leetcode.com/problems/number-of-music-playlists/description/
 *
 * algorithms
 * Hard (50.65%)
 * Likes:    1974
 * Dislikes: 171
 * Total Accepted:    57.4K
 * Total Submissions: 94K
 * Testcase Example:  '3\n3\n1'
 *
 * Your music player contains n different songs. You want to listen to goal
 * songs (not necessarily different) during your trip. To avoid boredom, you
 * will create a playlist so that:
 *
 *
 * Every song is played at least once.
 * A song can only be played again only if k other songs have been played.
 *
 *
 * Given n, goal, and k, return the number of possible playlists that you can
 * create. Since the answer can be very large, return it modulo 10^9 + 7.
 *
 * Example 1:
 *
 *
 * Input: n = 3, goal = 3, k = 1
 * Output: 6
 * Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1,
 * 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
 *
 *
 * Example 2:
 *
 *
 * Input: n = 2, goal = 3, k = 0
 * Output: 6
 * Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1,
 * 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
 *
 *
 * Example 3:
 *
 *
 * Input: n = 2, goal = 3, k = 1
 * Output: 2
 * Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= k < n <= goal <= 100
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn num_music_playlists(n: i32, goal: i32, k: i32) -> i32 {
        let goal = goal as usize;
        let n = n as usize;
        let k = k as usize;
        const MOD: i64 = 1_000_000_007;
        let mut dp = vec![vec![0i64; n + 1]; goal + 1];
        dp[0][0] = 1;
        for i in 1..(goal + 1) {
            for j in 1..(i.min(n) + 1) {
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) as i64;
                if k < j {
                    dp[i][j] += dp[i - 1][j] * (j - k) as i64;
                }
                dp[i][j] %= MOD;
            }
        }
        dp[goal][n] as i32
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::num_music_playlists(e.0, e.1, e.2),
        vec![
            ((3, 3, 1), 6),
            ((2, 3, 0), 6),
            ((2, 3, 1), 2),
            ((3, 4, 2), 6),
        ],
        |a, b| a == b,
    )
}
