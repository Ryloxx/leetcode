/*
 * @lc app=leetcode id=1582 lang=rust
 *
 * [1582] Special Positions in a Binary Matrix
 *
 * https://leetcode.com/problems/special-positions-in-a-binary-matrix/description/
 *
 * algorithms
 * Easy (65.15%)
 * Likes:    1346
 * Dislikes: 62
 * Total Accepted:    125.9K
 * Total Submissions: 182.3K
 * Testcase Example:  '[[1,0,0],[0,0,1],[1,0,0]]'
 *
 * Given an m x n binary matrix mat, return the number of special positions
 * in mat.
 *
 * A position (i, j) is called special if mat[i][j] == 1 and all other
 * elements in row i and column j are 0 (rows and columns are 0-indexed).
 *
 *
 * Example 1:
 *
 *
 * Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
 * Output: 1
 * Explanation: (1, 2) is a special position because mat[1][2] == 1 and all
 * other elements in row 1 and column 2 are 0.
 *
 *
 * Example 2:
 *
 *
 * Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
 * Output: 3
 * Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 *
 *
 *
 * Constraints:
 *
 *
 * m == mat.length
 * n == mat[i].length
 * 1 <= m, n <= 100
 * mat[i][j] is either 0 or 1.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn num_special(mat: Vec<Vec<i32>>) -> i32 {
        let m = mat.len();
        let n = mat[0].len();
        let mut p = vec![0; m + n];
        let mut res = 0;
        for i in 0..m {
            for j in 0..n {
                if mat[i][j] == 1 {
                    p[i] += 1;
                    p[m + j] += 1;
                }
            }
        }
        for i in 0..m {
            if p[i] != 1 {
                continue;
            }
            for j in 0..n {
                if mat[i][j] == 1 && p[m + j] == 1 {
                    res += 1;
                    break;
                }
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::num_special,
        vec![
            ((vec![vec![1, 0, 0], vec![0, 0, 1], vec![1, 0, 0]]), 1),
            ((vec![vec![1, 0, 0], vec![0, 1, 0], vec![0, 0, 1]]), 3),
        ],
        |a, b| a == b,
    );
}
