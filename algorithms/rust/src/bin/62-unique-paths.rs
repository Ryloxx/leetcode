/*
 * @lc app=leetcode id=62 lang=rust
 *
 * [62] Unique Paths
 *
 * https://leetcode.com/problems/unique-paths/description/
 *
 * algorithms
 * Medium (62.43%)
 * Likes:    15435
 * Dislikes: 410
 * Total Accepted:    1.6M
 * Total Submissions: 2.5M
 * Testcase Example:  '3\n7'
 *
 * There is a robot on an m x n grid. The robot is initially located at the
 * top-left corner (i.e., grid[0][0]). The robot tries to move to the
 * bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
 * either down or right at any point in time.
 *
 * Given the two integers m and n, return the number of possible unique paths
 * that the robot can take to reach the bottom-right corner.
 *
 * The test cases are generated so that the answer will be less than or equal
 * to 2 * 10^9.
 *
 *
 * Example 1:
 *
 *
 * Input: m = 3, n = 7
 * Output: 28
 *
 *
 * Example 2:
 *
 *
 * Input: m = 3, n = 2
 * Output: 3
 * Explanation: From the top-left corner, there are a total of 3 ways to
 * reach the bottom-right corner:
 * 1. Right -> Down -> Down
 * 2. Down -> Down -> Right
 * 3. Down -> Right -> Down
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= m, n <= 100
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn unique_paths(mut m: i32, mut n: i32) -> i32 {
        if m < n {
            std::mem::swap(&mut m, &mut n);
        }
        let mut res: i64 = 1;
        let mut i = n as i64;
        for j in 1..m as i64 {
            res *= i;
            res /= j;
            i += 1;
        }
        res as i32
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::unique_paths(e.0, e.1),
        vec![
            ((3, 7), 28),
            ((3, 2), 3),
            ((1, 1), 1),
            ((100, 7), 1609344100),
        ],
        |a, b| a == b,
    )
}
