/*
 * @lc app=leetcode id=54 lang=rust
 *
 * [54] Spiral Matrix
 *
 * https://leetcode.com/problems/spiral-matrix/description/
 *
 * algorithms
 * Medium (44.07%)
 * Likes:    11683
 * Dislikes: 1061
 * Total Accepted:    1M
 * Total Submissions: 2.3M
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * Given an m x n matrix, return all elements of the matrix in spiral order.
 *
 *
 * Example 1:
 *
 *
 * Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
 * Output: [1,2,3,6,9,8,7,4,5]
 *
 *
 * Example 2:
 *
 *
 * Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
 * Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 *
 *
 *
 * Constraints:
 *
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 10
 * -100 <= matrix[i][j] <= 100
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        if matrix.is_empty() || matrix[0].is_empty() {
            return vec![];
        }
        let mut matrix = matrix;
        let (m, n) = (matrix.len(), matrix[0].len());
        let directions = [(0, 1), (1, 0), (0, !0), (!0, 0)];
        let mut current_direction = 0;
        let (mut y, mut x) = (0, 0);
        let mut res = vec![];
        for _ in 0..(m * n) {
            res.push(matrix[y][x]);
            matrix[y][x] = i32::MAX;
            let yi = y.wrapping_add(directions[current_direction].0);
            let xi = x.wrapping_add(directions[current_direction].1);
            if yi >= m || xi >= n || matrix[yi][xi] == i32::MAX {
                current_direction = (current_direction + 1) % 4;
                y = y.wrapping_add(directions[current_direction].0);
                x = x.wrapping_add(directions[current_direction].1);
            } else {
                y = yi;
                x = xi;
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::spiral_order,
        vec![
            (
                vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]],
                vec![1, 2, 3, 6, 9, 8, 7, 4, 5],
            ),
            (
                vec![vec![1, 2, 3, 4], vec![5, 6, 7, 8], vec![9, 10, 11, 12]],
                vec![1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
            ),
            (
                vec![vec![2, 5], vec![8, 4], vec![0, -1]],
                vec![2, 5, 4, -1, 0, 8],
            ),
        ],
        |a, b| a == b,
    );
}
