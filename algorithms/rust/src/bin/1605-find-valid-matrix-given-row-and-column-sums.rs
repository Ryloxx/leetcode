/*
 * @lc app=leetcode id=1605 lang=rust
 *
 * [1605] Find Valid Matrix Given Row and Column Sums
 *
 * https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description/
 *
 * algorithms
 * Medium (77.27%)
 * Likes:    1929
 * Dislikes: 77
 * Total Accepted:    109.6K
 * Total Submissions: 132.9K
 * Testcase Example:  '[3,8]\n[4,7]'
 *
 * You are given two arrays rowSum and colSum of non-negative integers where
 * rowSum[i] is the sum of the elements in the i^th row and colSum[j] is the
 * sum of the elements of the j^th column of a 2D matrix. In other words, you
 * do not know the elements of the matrix, but you do know the sums of each
 * row and column.
 *
 * Find any matrix of non-negative integers of size rowSum.length x
 * colSum.length that satisfies the rowSum and colSum requirements.
 *
 * Return a 2D array representing any matrix that fulfills the requirements.
 * It's guaranteed that at least one matrix that fulfills the requirements
 * exists.
 *
 *
 * Example 1:
 *
 *
 * Input: rowSum = [3,8], colSum = [4,7]
 * Output: [[3,0],
 * ⁠        [1,7]]
 * Explanation:
 * 0^th row: 3 + 0 = 3 == rowSum[0]
 * 1^st row: 1 + 7 = 8 == rowSum[1]
 * 0^th column: 3 + 1 = 4 == colSum[0]
 * 1^st column: 0 + 7 = 7 == colSum[1]
 * The row and column sums match, and all matrix elements are non-negative.
 * Another possible matrix is: [[1,2],
 * ⁠                            [3,5]]
 *
 *
 * Example 2:
 *
 *
 * Input: rowSum = [5,7,10], colSum = [8,6,8]
 * Output: [[0,5,0],
 * ⁠        [6,1,0],
 * ⁠        [2,0,8]]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= rowSum.length, colSum.length <= 500
 * 0 <= rowSum[i], colSum[i] <= 10^8
 * sum(rowSum) == sum(colSum)
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn restore_matrix(mut row_sum: Vec<i32>, mut col_sum: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res = vec![vec![0; col_sum.len()]; row_sum.len()];
        for (i, row_sum) in row_sum.iter_mut().enumerate() {
            for (j, col_sum) in col_sum.iter_mut().enumerate() {
                let min = (*row_sum).min(*col_sum);
                *row_sum -= min;
                *col_sum -= min;
                res[i][j] = min;
            }
        }
        res
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::restore_matrix(e.0, e.1),
        vec![
            ((vec![3, 8], vec![4, 7]), vec![vec![3, 8], vec![4, 7]]),
            (
                (vec![5, 7, 10], vec![8, 6, 8]),
                vec![vec![5, 7, 10], vec![8, 6, 8]],
            ),
        ],
        |expected, returned| {
            let m = expected[0].len();
            let n = expected[1].len();
            returned
                .iter()
                .enumerate()
                .all(|(i, row)| expected[0][i] == row.iter().sum())
                && (0..n).all(|j| expected[1][j] == (0..m).map(|i| returned[i][j]).sum())
        },
    )
}
