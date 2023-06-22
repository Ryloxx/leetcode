/*
 * @lc app=leetcode id=714 lang=rust
 *
 * [714] Best Time to Buy and Sell Stock with Transaction Fee
 *
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
 *
 * algorithms
 * Medium (64.56%)
 * Likes:    5894
 * Dislikes: 153
 * Total Accepted:    258.7K
 * Total Submissions: 388.8K
 * Testcase Example:  '[1,3,2,8,4,9]\n2'
 *
 * You are given an array prices where prices[i] is the price of a given
 * stock on the i^th day, and an integer fee representing a transaction fee.
 *
 * Find the maximum profit you can achieve. You may complete as many
 * transactions as you like, but you need to pay the transaction fee for each
 * transaction.
 *
 * Note: You may not engage in multiple transactions simultaneously (i.e.,
 * you must sell the stock before you buy again).
 *
 *
 * Example 1:
 *
 *
 * Input: prices = [1,3,2,8,4,9], fee = 2
 * Output: 8
 * Explanation: The maximum profit can be achieved by:
 * - Buying at prices[0] = 1
 * - Selling at prices[3] = 8
 * - Buying at prices[4] = 4
 * - Selling at prices[5] = 9
 * The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
 *
 *
 * Example 2:
 *
 *
 * Input: prices = [1,3,7,5,10,3], fee = 3
 * Output: 6
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= prices.length <= 5 * 10^4
 * 1 <= prices[i] < 5 * 10^4
 * 0 <= fee < 5 * 10^4
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 {
        let mut free = 0;
        let mut hold = -prices[0];
        for i in 1..prices.len() {
            let tmp_free = free.max(hold + prices[i] - fee);
            let tmp_hold = hold.max(free - prices[i]);
            free = tmp_free;
            hold = tmp_hold;
        }
        free
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::max_profit(e.0, e.1),
        vec![
            //
            ((vec![1, 3, 2, 8, 4, 9], 2), 8),
            ((vec![1, 3, 7, 5, 10, 3], 3), 6),
        ],
        |a, b| a == b,
    )
}
