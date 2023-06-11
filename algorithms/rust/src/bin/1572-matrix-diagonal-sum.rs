/*
 * @lc app=leetcode id=1572 lang=rust
 *
 * [1572] Matrix Diagonal Sum
 *
 * https://leetcode.com/problems/matrix-diagonal-sum/description/
 *
 * algorithms
 * Easy (79.85%)
 * Likes:    2477
 * Dislikes: 31
 * Total Accepted:    218.8K
 * Total Submissions: 266.8K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * Given a square matrix mat, return the sum of the matrix diagonals.
 *
 * Only include the sum of all the elements on the primary diagonal and all
 * the elements on the secondary diagonal that are not part of the primary
 * diagonal.
 *
 *
 * Example 1:
 *
 *
 * Input: mat = [[1,2,3],
 * [4,5,6],
 * [7,8,9]]
 * Output: 25
 * Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
 * Notice that element mat[1][1] = 5 is counted only once.
 *
 *
 * Example 2:
 *
 *
 * Input: mat = [[1,1,1,1],
 * [1,1,1,1],
 * [1,1,1,1],
 * [1,1,1,1]]
 * Output: 8
 *
 *
 * Example 3:
 *
 *
 * Input: mat = [[5]]
 * Output: 5
 *
 *
 *
 * Constraints:
 *
 *
 * n == mat.length == mat[i].length
 * 1 <= n <= 100
 * 1 <= mat[i][j] <= 100
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 {
        let n = mat.len();
        (0..n).map(|x| mat[x][x] + mat[x][n - x - 1]).sum::<i32>()
            - if n % 2 == 1 { mat[n / 2][n / 2] } else { 0 }
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::diagonal_sum(e),
        vec![
            (vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]], 25),
            (
                vec![
                    vec![1, 1, 1, 1],
                    vec![1, 1, 1, 1],
                    vec![1, 1, 1, 1],
                    vec![1, 1, 1, 1],
                ],
                8,
            ),
            (vec![vec![5]], 5),
        ],
        |a, b| a == b,
    );
}
