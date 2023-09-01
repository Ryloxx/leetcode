/*
 * @lc app=leetcode id=2483 lang=rust
 *
 * [2483] Minimum Penalty for a Shop
 *
 * https://leetcode.com/problems/minimum-penalty-for-a-shop/description/
 *
 * algorithms
 * Medium (55.01%)
 * Likes:    967
 * Dislikes: 50
 * Total Accepted:    42.8K
 * Total Submissions: 64.5K
 * Testcase Example:  '"YYNY"'
 *
 * You are given the customer visit log of a shop represented by a 0-indexed
 * string customers consisting only of characters 'N' and 'Y':
 *
 *
 * if the i^th character is 'Y', it means that customers come at the i^th
 * hour
 * whereas 'N' indicates that no customers come at the i^th hour.
 *
 *
 * If the shop closes at the j^th hour (0 <= j <= n), the penalty is
 * calculated as follows:
 *
 *
 * For every hour when the shop is open and no customers come, the penalty
 * increases by 1.
 * For every hour when the shop is closed and customers come, the penalty
 * increases by 1.
 *
 *
 * Return the earliest hour at which the shop must be closed to incur a
 * minimum penalty.
 *
 * Note that if a shop closes at the j^th hour, it means the shop is closed
 * at the hour j.
 *
 *
 * Example 1:
 *
 *
 * Input: customers = "YYNY"
 * Output: 2
 * Explanation:
 * - Closing the shop at the 0^th hour incurs in 1+1+0+1 = 3 penalty.
 * - Closing the shop at the 1^st hour incurs in 0+1+0+1 = 2 penalty.
 * - Closing the shop at the 2^nd hour incurs in 0+0+0+1 = 1 penalty.
 * - Closing the shop at the 3^rd hour incurs in 0+0+1+1 = 2 penalty.
 * - Closing the shop at the 4^th hour incurs in 0+0+1+0 = 1 penalty.
 * Closing the shop at 2^nd or 4^th hour gives a minimum penalty. Since 2 is
 * earlier, the optimal closing time is 2.
 *
 *
 * Example 2:
 *
 *
 * Input: customers = "NNNNN"
 * Output: 0
 * Explanation: It is best to close the shop at the 0^th hour as no customers
 * arrive.
 *
 * Example 3:
 *
 *
 * Input: customers = "YYYY"
 * Output: 4
 * Explanation: It is best to close the shop at the 4^th hour as customers
 * arrive at each hour.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= customers.length <= 10^5
 * customers consists only of characters 'Y' and 'N'.
 *
 *
 */
struct Solution;

// @lc code=start
impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        let mut curr_p = 0;
        let mut min_p = 0;
        let mut res = 0;
        for i in 0..customers.len() {
            curr_p += -1 + 2 * ((customers.as_bytes()[i] == b'N') as i32);
            if curr_p < min_p {
                min_p = curr_p;
                res = i + 1;
            }
        }
        res as i32
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::best_closing_time(e),
        vec![
            (("YYNY".to_string()), 2),
            (("YYYY".to_string()), 4),
            (("N".to_string()), 0),
            (("Y".to_string()), 1),
        ],
        |a, b| a == b,
    );
}
