/*
 * @lc app=leetcode id=1359 lang=rust
 *
 * [1359] Count All Valid Pickup and Delivery Options
 *
 * https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
 *
 * algorithms
 * Hard (64.57%)
 * Likes:    2565
 * Dislikes: 196
 * Total Accepted:    94.1K
 * Total Submissions: 145.7K
 * Testcase Example:  '1'
 *
 * Given n orders, each order consist in pickup and delivery services.
 *
 * Count all valid pickup/delivery possible sequences such that delivery(i)
 * is always after of pickup(i).
 *
 * Since the answer may be too large, return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 1
 * Output: 1
 * Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup
 * 1.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 2
 * Output: 6
 * Explanation: All possible orders:
 * (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1)
 * and (P2,D2,P1,D1).
 * This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of
 * Delivery 2.
 *
 *
 * Example 3:
 *
 *
 * Input: n = 3
 * Output: 90
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 500
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn count_orders(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut res: i64 = 1;
        for i in 1..n as i64 + 1 {
            res *= (i * 2 - 1) * i;
            res %= MOD;
        }
        res as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |s| Solution::count_orders(s),
        vec![
            ///
            (1, 1),
            (2, 6),
            (3, 90),
            (500, 764678010),
        ],
        |a, b| a == b,
    )
}
