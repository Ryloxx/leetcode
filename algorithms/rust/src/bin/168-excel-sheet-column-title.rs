/*
 * @lc app=leetcode id=168 lang=rust
 *
 * [168] Excel Sheet Column Title
 *
 * https://leetcode.com/problems/excel-sheet-column-title/description/
 *
 * algorithms
 * Easy (34.93%)
 * Likes:    4013
 * Dislikes: 573
 * Total Accepted:    396.5K
 * Total Submissions: 1.1M
 * Testcase Example:  '1'
 *
 * Given an integer columnNumber, return its corresponding column title as it
 * appears in an Excel sheet.
 *
 * For example:
 *
 *
 * A -> 1
 * B -> 2
 * C -> 3
 * ...
 * Z -> 26
 * AA -> 27
 * AB -> 28
 * ...
 *
 *
 *
 * Example 1:
 *
 *
 * Input: columnNumber = 1
 * Output: "A"
 *
 *
 * Example 2:
 *
 *
 * Input: columnNumber = 28
 * Output: "AB"
 *
 *
 * Example 3:
 *
 *
 * Input: columnNumber = 701
 * Output: "ZY"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= columnNumber <= 2^31 - 1
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn convert_to_title(mut column_number: i32) -> String {
        let mut ret: Vec<char> = Vec::with_capacity(7);
        while column_number != 0 {
            column_number -= 1;
            ret.push((b'A' + (column_number % 26) as u8) as char);
            column_number = column_number / 26;
        }
        ret.into_iter().rev().collect()
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::convert_to_title(e),
        vec![
            ((1), "A".to_string()),
            ((28), "AB".to_string()),
            ((701), "ZY".to_string()),
            ((703), "AAA".to_string()),
        ],
        |a, b| a == b,
    );
}
