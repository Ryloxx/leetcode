/*
 * @lc app=leetcode id=201 lang=rust
 *
 * [201] Bitwise AND of Numbers Range
 *
 * https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
 *
 * algorithms
 * Medium (44.21%)
 * Likes:    3462
 * Dislikes: 254
 * Total Accepted:    304.1K
 * Total Submissions: 687.8K
 * Testcase Example:  '5\n7'
 *
 * Given two integers left and right that represent the range [left, right],
 * return the bitwise AND of all numbers in this range, inclusive.
 *
 *
 * Example 1:
 *
 *
 * Input: left = 5, right = 7
 * Output: 4
 *
 *
 * Example 2:
 *
 *
 * Input: left = 0, right = 0
 * Output: 0
 *
 *
 * Example 3:
 *
 *
 * Input: left = 1, right = 2147483647
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= left <= right <= 2^31 - 1
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn range_bitwise_and(left: i32, right: i32) -> i32 {
        left & right & !(((right - left) as u32).next_power_of_two() - 1) as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::range_bitwise_and(e.0, e.1),
        vec![
            ((5, 7), 4),
            ((0, 0), 0),
            ((1, 2147483647), 0),
            ((700000000, 2147483641), 0),
            ((10681, 32767), 0),
            ((0, 127), 0),
            ((1, 127), 0),
            ((127, 127), 127),
            ((20, 21), 20),
            ((10, 10), 10),
        ],
        |a, b| a == b,
    )
}
