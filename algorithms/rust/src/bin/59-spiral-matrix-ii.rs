/*
 * @lc app=leetcode id=59 lang=rust
 *
 * [59] Spiral Matrix II
 *
 * https://leetcode.com/problems/spiral-matrix-ii/description/
 *
 * algorithms
 * Medium (66.84%)
 * Likes:    5387
 * Dislikes: 227
 * Total Accepted:    469.4K
 * Total Submissions: 682K
 * Testcase Example:  '3'
 *
 * Given a positive integer n, generate an n x n matrix filled with elements
 * from 1 to n^2 in spiral order.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 3
 * Output: [[1,2,3],[8,9,4],[7,6,5]]
 *
 *
 * Example 2:
 *
 *
 * Input: n = 1
 * Output: [[1]]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 20
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
        if n < 0 {
            return vec![vec![]];
        }
        let n = n as usize;
        let mut matrix = vec![vec![0; n]; n];
        let directions = [(0, 1), (1, 0), (0, !0), (!0, 0)];
        let mut current_direction = 0;
        let (mut y, mut x) = (0, 0);
        for i in 1..=(n * n) as i32 {
            matrix[y][x] = i;
            let yi = y.wrapping_add(directions[current_direction].0);
            let xi = x.wrapping_add(directions[current_direction].1);
            if yi >= n || xi >= n || matrix[yi][xi] != 0 {
                current_direction = (current_direction + 1) % 4;
                y = y.wrapping_add(directions[current_direction].0);
                x = x.wrapping_add(directions[current_direction].1);
            } else {
                y = yi;
                x = xi;
            }
        }
        matrix
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::generate_matrix,
        vec![
            (3, vec![vec![1, 2, 3], vec![8, 9, 4], vec![7, 6, 5]]),
            (1, vec![vec![1]]),
        ],
        |a, b| a == b,
    );
}
