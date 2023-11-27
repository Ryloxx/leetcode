/*
 * @lc app=leetcode id=1727 lang=rust
 *
 * [1727] Largest Submatrix With Rearrangements
 *
 * https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/
 *
 * algorithms
 * Medium (75.57%)
 * Likes:    1746
 * Dislikes: 86
 * Total Accepted:    62.7K
 * Total Submissions: 83K
 * Testcase Example:  '[[0,0,1],[1,1,1],[1,0,1]]'
 *
 * You are given a binary matrix matrix of size m x n, and you are allowed to
 * rearrange the columns of the matrix in any order.
 *
 * Return the area of the largest submatrix within matrix where every element
 * of the submatrix is 1 after reordering the columns optimally.
 *
 *
 * Example 1:
 *
 *
 * Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
 * Output: 4
 * Explanation: You can rearrange the columns as shown above.
 * The largest submatrix of 1s, in bold, has an area of 4.
 *
 *
 * Example 2:
 *
 *
 * Input: matrix = [[1,0,1,0,1]]
 * Output: 3
 * Explanation: You can rearrange the columns as shown above.
 * The largest submatrix of 1s, in bold, has an area of 3.
 *
 *
 * Example 3:
 *
 *
 * Input: matrix = [[1,1,0],[1,0,1]]
 * Output: 2
 * Explanation: Notice that you must rearrange entire columns, and there is
 * no way to make a submatrix of 1s larger than an area of 2.
 *
 *
 *
 * Constraints:
 *
 *
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m * n <= 10^5
 * matrix[i][j] is either 0 or 1.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn largest_submatrix(matrix: Vec<Vec<i32>>) -> i32 {
        let n = matrix[0].len();
        let mut res = 0;
        let mut heights = vec![0];
        let mut idx = vec![0; n];
        let n = n as i32;
        for row in matrix.iter() {
            heights.push(0);
            for (j, num) in row.iter().enumerate() {
                if *num == 1 {
                    heights[idx[j]] -= 1;
                    idx[j] += 1;
                    heights[idx[j]] += 1;
                } else {
                    heights[idx[j]] -= 1;
                    idx[j] = 0;
                }
            }
            while !heights.is_empty() && *heights.last().unwrap() == 0 {
                heights.pop().unwrap();
            }
            let mut width = 0;
            let mut seen = 0;
            for (height, count) in heights.iter().enumerate().rev() {
                width += count;
                seen += count;
                res = res.max(width * height as i32);
                let max_possible = (height as i32 - 1) * (width + n - seen);
                if max_possible <= res {
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
        Solution::largest_submatrix,
        vec![
            ((vec![vec![0, 0, 1], vec![1, 1, 1], vec![1, 0, 1]]), 4),
            ((vec![vec![1, 0, 1, 0, 1]]), 3),
            ((vec![vec![1, 1, 0], vec![1, 0, 1]]), 2),
            ((vec![vec![1]; 10_000]), 10_000),
        ],
        |a, b| a == b,
    );
}
