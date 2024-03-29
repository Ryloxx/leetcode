/*
 * @lc app=leetcode id=2125 lang=rust
 *
 * [2125] Number of Laser Beams in a Bank
 *
 * https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
 *
 * algorithms
 * Medium (81.20%)
 * Likes:    1422
 * Dislikes: 138
 * Total Accepted:    134K
 * Total Submissions: 156.6K
 * Testcase Example:  '["011001","000000","010100","001000"]'
 *
 * Anti-theft security devices are activated inside a bank. You are given a
 * 0-indexed binary string array bank representing the floor plan of the
 * bank, which is an m x n 2D matrix. bank[i] represents the i^th row,
 * consisting of '0's and '1's. '0' means the cell is empty, while'1' means
 * the cell has a security device.
 *
 * There is one laser beam between any two security devices if both
 * conditions are met:
 *
 *
 * The two devices are located on two different rows: r1 and r2, where r1 <
 * r2.
 * For each row i where r1 < i < r2, there are no security devices in the
 * i^th row.
 *
 *
 * Laser beams are independent, i.e., one beam does not interfere nor join
 * with another.
 *
 * Return the total number of laser beams in the bank.
 *
 *
 * Example 1:
 *
 *
 * Input: bank = ["011001","000000","010100","001000"]
 * Output: 8
 * Explanation: Between each of the following device pairs, there is one
 * beam. In total, there are 8 beams:
 * ⁠* bank[0][1] -- bank[2][1]
 * ⁠* bank[0][1] -- bank[2][3]
 * ⁠* bank[0][2] -- bank[2][1]
 * ⁠* bank[0][2] -- bank[2][3]
 * ⁠* bank[0][5] -- bank[2][1]
 * ⁠* bank[0][5] -- bank[2][3]
 * ⁠* bank[2][1] -- bank[3][2]
 * ⁠* bank[2][3] -- bank[3][2]
 * Note that there is no beam between any device on the 0^th row with any on
 * the 3^rd row.
 * This is because the 2^nd row contains security devices, which breaks the
 * second condition.
 *
 *
 * Example 2:
 *
 *
 * Input: bank = ["000","111","000"]
 * Output: 0
 * Explanation: There does not exist two devices located on two different
 * rows.
 *
 *
 *
 * Constraints:
 *
 *
 * m == bank.length
 * n == bank[i].length
 * 1 <= m, n <= 500
 * bank[i][j] is either '0' or '1'.
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        let mut curr = 0;
        let mut res = 0;
        for line in bank {
            let cnt = line
                .into_bytes()
                .into_iter()
                .map(|c| (c - b'0') as i32)
                .sum();
            if cnt > 0 {
                res += curr * cnt;
                curr = cnt;
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::number_of_beams,
        vec![
            (
                vec!["011001", "000000", "010100", "001000"]
                    .into_iter()
                    .map(String::from)
                    .collect(),
                8,
            ),
            (
                vec!["000", "111", "000"]
                    .into_iter()
                    .map(String::from)
                    .collect(),
                0,
            ),
            (
                vec!["111", "111", "111"]
                    .into_iter()
                    .map(String::from)
                    .collect(),
                18,
            ),
            (vec!["000"].into_iter().map(String::from).collect(), 0),
            (vec!["111"].into_iter().map(String::from).collect(), 0),
            (vec!["1"].into_iter().map(String::from).collect(), 0),
            (vec!["0"].into_iter().map(String::from).collect(), 0),
        ],
        |a, b| a == b,
    );
}
