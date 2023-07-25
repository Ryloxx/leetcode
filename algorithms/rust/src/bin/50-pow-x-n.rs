/*
 * @lc app=leetcode id=50 lang=rust
 *
 * [50] Pow(x, n)
 *
 * https://leetcode.com/problems/powx-n/description/
 *
 * algorithms
 * Medium (32.86%)
 * Likes:    7841
 * Dislikes: 7921
 * Total Accepted:    1.3M
 * Total Submissions: 3.8M
 * Testcase Example:  '2.00000\n10'
 *
 * Implement pow(x, n), which calculates x raised to the power n (i.e.,
 * x^n).
 *
 *
 * Example 1:
 *
 *
 * Input: x = 2.00000, n = 10
 * Output: 1024.00000
 *
 *
 * Example 2:
 *
 *
 * Input: x = 2.10000, n = 3
 * Output: 9.26100
 *
 *
 * Example 3:
 *
 *
 * Input: x = 2.00000, n = -2
 * Output: 0.25000
 * Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
 *
 *
 *
 * Constraints:
 *
 *
 * -100.0 < x < 100.0
 * -2^31 <= n <= 2^31-1
 * n is an integer.
 * Either x is not zero or n > 0.
 * -10^4 <= x^n <= 10^4
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        let mut n = n as i64;
        let mut res = 1.;
        let mut p = if n > 0 { x } else { 1. / x };
        n = n.abs();
        while n != 0 {
            if n & 1 == 1 {
                res *= p;
            }
            p *= p;
            n >>= 1;
        }
        res
    }
    // Lazy
    // pub fn my_pow(x: f64, n: i32) -> f64 {
    //     x.powi(n)
    // }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::my_pow(e.0, e.1),
        vec![
            ((2., 10), 1024.),
            ((2.1, 3), 9.26100),
            ((2., -2), 0.25000),
            ((1., -2147483648), 1.),
        ],
        |a, b| (a - b).abs() < 1e-5,
    )
}
