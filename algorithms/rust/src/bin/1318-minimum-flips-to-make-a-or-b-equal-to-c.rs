/*
 * @lc app=leetcode id=1318 lang=rust
 *
 * [1318] Minimum Flips to Make a OR b Equal to c
 *
 * https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/
 *
 * algorithms
 * Medium (66.08%)
 * Likes:    1364
 * Dislikes: 74
 * Total Accepted:    66.1K
 * Total Submissions: 94K
 * Testcase Example:  '2\n6\n5'
 *
 * Given 3 positives numbers a, b and c. Return the minimum flips required in
 * some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
 * Flip operation consists of change any single bit 1 to 0 or change the bit
 * 0 to 1 in their binary representation.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: a = 2, b = 6, c = 5
 * Output: 3
 * Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
 *
 * Example 2:
 *
 *
 * Input: a = 4, b = 2, c = 7
 * Output: 1
 *
 *
 * Example 3:
 *
 *
 * Input: a = 1, b = 2, c = 3
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= a <= 10^9
 * 1 <= b <= 10^9
 * 1 <= c <= 10^9
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn min_flips(a: i32, b: i32, c: i32) -> i32 {
        let r = (a | b) ^ c;
        (r.count_ones() + (r & a & b).count_ones()) as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::min_flips(e.0, e.1, e.2),
        vec![
            ((2, 6, 5), 3),
            ((4, 2, 7), 1),
            ((1, 2, 3), 0),
            ((7, 7, 7), 0),
        ],
        |a, b| a == b,
    );
}
