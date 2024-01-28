/*
 * @lc app=leetcode id=1074 lang=rust
 *
 * [1074] Number of Submatrices That Sum to Target
 *
 * https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/
 *
 * algorithms
 * Hard (69.61%)
 * Likes:    3141
 * Dislikes: 66
 * Total Accepted:    96.9K
 * Total Submissions: 137.7K
 * Testcase Example:  '[[0,1,0],[1,1,1],[0,1,0]]\n0'
 *
 * Given a matrix and a target, return the number of non-empty submatrices
 * that sum to target.
 *
 * A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <=
 * x <= x2 and y1 <= y <= y2.
 *
 * Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if
 * they have some coordinate that is different: for example, if x1 != x1'.
 *
 *
 * Example 1:
 *
 *
 * Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
 * Output: 4
 * Explanation: The four 1x1 submatrices that only contain 0.
 *
 *
 * Example 2:
 *
 *
 * Input: matrix = [[1,-1],[-1,1]], target = 0
 * Output: 5
 * Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus
 * the 2x2 submatrix.
 *
 *
 * Example 3:
 *
 *
 * Input: matrix = [[904]], target = 0
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= matrix.length <= 100
 * 1 <= matrix[0].length <= 100
 * -1000 <= matrix[i] <= 1000
 * -10^8 <= target <= 10^8
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn num_submatrix_sum_target(matrix: Vec<Vec<i32>>, target: i32) -> i32 {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut prefix_matrix = vec![0; m * n];
        prefix_matrix[0] = matrix[0][0];
        for i in 1..n {
            prefix_matrix[i] = matrix[0][i] + prefix_matrix[i - 1];
        }
        for i in 1..m {
            prefix_matrix[i * n] = matrix[i][0] + prefix_matrix[(i - 1) * n];
        }
        for i in 1..m {
            for j in 1..n {
                prefix_matrix[i * n + j] =
                    matrix[i][j] + prefix_matrix[i * n + j - 1] + prefix_matrix[(i - 1) * n + j]
                        - prefix_matrix[(i - 1) * n + j - 1];
            }
        }
        let mut seen = HashMap::new();
        let mut res = 0;
        for top in 0..m {
            seen.insert(0, 1);
            for slice_end in 0..n {
                let slice = prefix_matrix[top * n + slice_end];
                res += seen.get(&(slice - target)).unwrap_or(&0);
                *(seen.entry(slice).or_insert(0)) += 1;
            }
            seen.clear();
        }
        for bottom in 1..m {
            for top in bottom..m {
                seen.insert(0, 1);
                for slice_end in 0..n {
                    let slice = prefix_matrix[top * n + slice_end]
                        - prefix_matrix[(bottom - 1) * n + slice_end];
                    res += seen.get(&(slice - target)).unwrap_or(&0);
                    *(seen.entry(slice).or_insert(0)) += 1;
                }
                seen.clear();
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::num_submatrix_sum_target(e.0, e.1),
        vec![
            ((vec![vec![0, 1, 0], vec![1, 1, 1], vec![0, 1, 0]], 0), 4),
            ((vec![vec![1, -1], vec![-1, 1]], 0), 5),
            ((vec![vec![904]], 0), 0),
            ((vec![vec![0, 0, 0, 0, 0]], 0), 15),
            ((vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]], 10), 0),
            (
                (vec![vec![3, 4], vec![5, 6], vec![7, 8], vec![9, 10]], 7),
                2,
            ),
        ],
        |a, b| a == b,
    );
}
