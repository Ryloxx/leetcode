/*
 * @lc app=leetcode id=861 lang=rust
 *
 * [861] Score After Flipping Matrix
 *
 * https://leetcode.com/problems/score-after-flipping-matrix/description/
 *
 * algorithms
 * Medium (74.95%)
 * Likes:    1612
 * Dislikes: 180
 * Total Accepted:    52.3K
 * Total Submissions: 69.3K
 * Testcase Example:  '[[0,0,1,1],[1,0,1,0],[1,1,0,0]]'
 *
 * You are given an m x n binary matrix grid.
 *
 * A move consists of choosing any row or column and toggling each value in
 * that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
 *
 * Every row of the matrix is interpreted as a binary number, and the score
 * of the matrix is the sum of these numbers.
 *
 * Return the highest possible score after making any number of moves
 * (including zero moves).
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
 * Output: 39
 * Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [[0]]
 * Output: 1
 *
 *
 *
 * Constraints:
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 20
 * grid[i][j] is either 0 or 1.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn matrix_score(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut res = 0;
        for j in 0..n {
            let cnt = (0..m)
                .map(|i| (grid[i][j] == grid[i][0]) as u32)
                .sum::<u32>();
            res += (cnt.max(m as u32 - cnt)) * (1 << (n - j - 1));
        }
        res as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::matrix_score,
        vec![
            (
                (vec![vec![0, 0, 1, 1], vec![1, 0, 1, 0], vec![1, 1, 0, 0]]),
                39,
            ),
            ((vec![vec![0]]), 1),
            ((vec![vec![1]]), 1),
        ],
        |a, b| a == b,
    )
}
