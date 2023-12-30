/*
 * @lc app=leetcode id=2482 lang=rust
 *
 * [2482] Difference Between Ones and Zeros in Row and Column
 *
 * https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/
 *
 * algorithms
 * Medium (79.88%)
 * Likes:    1001
 * Dislikes: 69
 * Total Accepted:    97.8K
 * Total Submissions: 115.1K
 * Testcase Example:  '[[0,1,1],[1,0,1],[0,0,1]]'
 *
 * You are given a 0-indexed m x n binary matrix grid.
 *
 * A 0-indexed m x n difference matrix diff is created with the following
 * procedure:
 *
 *
 * Let the number of ones in the i^th row be onesRowi.
 * Let the number of ones in the j^th column be onesColj.
 * Let the number of zeros in the i^th row be zerosRowi.
 * Let the number of zeros in the j^th column be zerosColj.
 * diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
 *
 *
 * Return the difference matrix diff.
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
 * Output: [[0,0,4],[0,0,4],[-2,-2,2]]
 * Explanation:
 * - diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2
 *   =
 * 0
 * - diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2
 *   =
 * 0
 * - diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0
 *   =
 * 4
 * - diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2
 *   =
 * 0
 * - diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2
 *   =
 * 0
 * - diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0
 *   =
 * 4
 * - diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2
 *   =
 * -2
 * - diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2
 *   =
 * -2
 * - diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0
 *   =
 * 2
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [[1,1,1],[1,1,1]]
 * Output: [[5,5,5],[5,5,5]]
 * Explanation:
 * - diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0
 *   =
 * 5
 * - diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0
 *   =
 * 5
 * - diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0
 *   =
 * 5
 * - diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0
 *   =
 * 5
 * - diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0
 *   =
 * 5
 * - diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0
 *   =
 * 5
 *
 *
 *
 * Constraints:
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 10^5
 * 1 <= m * n <= 10^5
 * grid[i][j] is either 0 or 1.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn ones_minus_zeros(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = grid.len();
        let n = grid[0].len();
        let mut cnts = vec![0; m + n];
        let mut res = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == 1 {
                    cnts[i] += 1;
                    cnts[m + j] += 1;
                }
            }
        }
        for i in 0..m {
            for j in 0..n {
                res[i][j] = cnts[i] * 2 + cnts[m + j] * 2 - (n + m) as i32;
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::ones_minus_zeros,
        vec![
            (
                (vec![vec![0, 1, 1], vec![1, 0, 1], vec![0, 0, 1]]),
                vec![vec![0, 0, 4], vec![0, 0, 4], vec![-2, -2, 2]],
            ),
            (
                (vec![vec![1, 1, 1], vec![1, 1, 1]]),
                vec![vec![5, 5, 5], vec![5, 5, 5]],
            ),
        ],
        |a, b| a == b,
    );
}
