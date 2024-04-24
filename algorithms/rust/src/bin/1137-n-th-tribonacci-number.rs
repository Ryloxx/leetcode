/*
 * @lc app=leetcode id=1137 lang=rust
 *
 * [1137] N-th Tribonacci Number
 *
 * https://leetcode.com/problems/n-th-tribonacci-number/description/
 *
 * algorithms
 * Easy (63.45%)
 * Likes:    4200
 * Dislikes: 184
 * Total Accepted:    680.2K
 * Total Submissions: 1.1M
 * Testcase Example:  '4'
 *
 * The Tribonacci sequence Tn is defined as follows:
 *
 * T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
 *
 * Given n, return the value of Tn.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 4
 * Output: 4
 * Explanation:
 * T_3 = 0 + 1 + 1 = 2
 * T_4 = 1 + 1 + 2 = 4
 *
 *
 * Example 2:
 *
 *
 * Input: n = 25
 * Output: 1389537
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= n <= 37
 * The answer is guaranteed to fit within a 32-bit integer, ie. answer <=
 * 2^31
 * - 1.
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        (0..n).fold((0, 1, 1), |(a, b, c), _| (b, c, a + b + c)).0
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::tribonacci,
        vec![(4, 4), (25, 1389537), (1, 1), (0, 0), (2, 1)],
        |a, b| a == b,
    )
}
