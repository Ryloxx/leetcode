/*
 * [1289] Minimum Falling Path Sum II
 *
 *
 * https:leetcode.com/problems/minimum-falling-path-sum-ii/description/
 *
 * algorithms
 * Hard (57.80%)
 * Total Accepted:    78.3K
 * Total Submissions: 128.4K
 * Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
 *
 * Given an n x n integer matrix grid, return the minimum sum of a falling path
 * with non-zero shifts.

 * A falling path with non-zero shifts is a choice of exactly one element from
 * each row of grid such that no two elements chosen in adjacent rows are in the
 * same column.
 *
 *
 * Example 1:
 *
 * Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
 * Output: 13
 * Explanation:
 * The possible falling paths are:
 * [1,5,9], [1,5,7], [1,6,7], [1,6,8],
 * [2,4,8], [2,4,9], [2,6,7], [2,6,8],
 * [3,4,8], [3,4,9], [3,5,7], [3,5,9]
 * The falling path with the smallest sum is [1,5,7], so the answer is 13.
 *
 * Example 2:
 *
 * Input: grid = [[7]]
 * Output: 7
 *
 *
 * Constraints:
 *
 * n == grid.length == grid[i].length
 * 1 <= n <= 200
 * -99 <= grid[i][j] <= 99
*/

struct Solution;
// @lc code=start
impl Solution {
    // DP
    // O(N^2) time complexity
    // O(N) space complexity
    pub fn min_falling_path_sum(mut grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut dp = std::mem::take(&mut grid[m - 1]);
        for i in (0..m - 1).rev() {
            let minimum_idx = (0..n).min_by_key(|x| dp[*x]).unwrap();
            let minimum = dp[minimum_idx];
            let second_minimum = dp[(0..n)
                .filter(|x| *x != minimum_idx)
                .min_by_key(|x| dp[*x])
                .unwrap()];
            (0..n).for_each(|j| dp[j] = minimum + grid[i][j]);
            dp[minimum_idx] += -minimum + second_minimum;
        }
        dp.into_iter().min().unwrap()
    }

    // Dijkstra
    // O(N^2 * log(N^2)) time complexity
    // O(N^2) space complexity
    //
    // Note that Dijkstra can work here because the number of edges for every path
    // connecting a node A to a node B is constant. Therefore, we can just remove
    // negative weight by adding a constant to it, and the answer will still be
    // correct.
    // pub fn min_falling_path_sum(grid: Vec<Vec<i32>>) -> i32 {
    //     use std::collections::BinaryHeap;
    //     const CONSTANT: i32 = 99;
    //     let m = grid.len();
    //     let n = grid[0].len();
    //     let mut h = BinaryHeap::new();
    //     h.push((0, 0, 0));
    //     let mut seen = vec![false; m * (n + 1)];
    //     while let Some((d, i, j)) = h.pop() {
    //         if i == m {
    //             return (-d) - (CONSTANT * m as i32);
    //         }
    //         for k in 0..n {
    //             let idx = (i + 1) * n + k;
    //             if (k == j && i > 0) || seen[idx] {
    //                 continue;
    //             }
    //             seen[idx] = true;
    //             h.push((d - (grid[i][k] + CONSTANT), i + 1, k));
    //         }
    //     }
    //     -1
    // }

    // Brute force by llama 3
    // O(N^3) time complexity
    // O(N^2) space complexity
    // pub fn min_falling_path_sum(grid: Vec<Vec<i32>>) -> i32 {
    //     let n = grid.len();
    //     let mut dp = grid.clone();

    //     for i in 1..n {
    //         for j in 0..n {
    //             let mut min_val = i32::MAX;
    //             for k in 0..n {
    //                 if k != j {
    //                     min_val = min_val.min(dp[i - 1][k]);
    //                 }
    //             }
    //             dp[i][j] += min_val;
    //         }
    //     }

    //     *dp.last().unwrap().iter().min().unwrap()
    // }
}
// @lc code=end
fn main() {
    rust::test_algo(
        Solution::min_falling_path_sum,
        vec![
            (vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]], 13),
            (vec![vec![7]], 7),
            (
                vec![
                    vec![-37, 51, -36, 34, -22],
                    vec![82, 4, 30, 14, 38],
                    vec![-68, -52, -92, 65, -85],
                    vec![-49, -3, -77, 8, -19],
                    vec![-60, -71, -21, -62, -73],
                ],
                -268,
            ),
            (
                vec![
                    vec![73, 3, 75, -98, -9, 94, -18],
                    vec![88, -81, 86, 23, -72, -24, -78],
                    vec![-89, 73, 97, -46, -18, -14, -54],
                    vec![24, -34, 78, 81, -29, 24, -99],
                    vec![86, 26, 14, 40, -28, -47, 61],
                    vec![-13, -53, -77, 45, -90, 31, -19],
                    vec![71, 60, -1, -53, -69, 8, -76],
                ],
                -580,
            ),
            (
                vec![
                    vec![18, -97, 57, -42, -7, 13, 7],
                    vec![99, 78, -20, 77, -55, 77, 81],
                    vec![16, -32, -35, -13, 77, 89, 81],
                    vec![-17, -3, 91, 74, -82, -5, -59],
                    vec![0, -90, -58, -54, -29, 88, -2],
                    vec![70, 94, 22, -10, -13, 45, -52],
                    vec![-20, -54, -8, 14, 80, 24, -72],
                ],
                -465,
            ),
            (
                vec![
                    vec![-24, 94, 9, -84, -38],
                    vec![-41, 83, -48, -70, -96],
                    vec![-54, -76, 15, 89, 37],
                    vec![-63, -53, 87, -34, 26],
                    vec![-76, 32, -86, 16, 57],
                ],
                -405,
            ),
            (
                vec![
                    vec![20, -17, 5, 60, -75, -30, -87, 47, 39, 71],
                    vec![27, -66, 6, -82, -5, -23, 35, 22, 30, -59],
                    vec![-16, -10, 47, 70, 79, 0, 96, -27, -25, 26],
                    vec![61, 15, 10, -82, -24, 1, 39, -44, 56, -34],
                    vec![-40, 85, -43, 94, 71, 33, -33, -77, 70, 22],
                    vec![-8, -95, 1, 40, -26, 20, 82, 49, 23, -42],
                    vec![58, 13, 38, 31, 13, -42, -53, -86, 66, -72],
                    vec![76, 89, 66, 52, 46, 38, 98, 0, -47, 7],
                    vec![95, -89, -70, 58, -27, 73, 13, 4, 59, -38],
                    vec![-84, -1, 59, 42, -81, 21, 45, 84, -61, -69],
                ],
                -756,
            ),
            (
                vec![
                    vec![-96, 92, -3, -77],
                    vec![17, 25, -94, -91],
                    vec![30, 75, 51, -95],
                    vec![57, -58, 80, 22],
                ],
                -343,
            ),
            (vec![vec![1; 200]; 200], 200),
            (
                Vec::from_iter(
                    (0..200).map(|_| Vec::from_iter((0..200).map(|y| ((y & 1) * 2) - 1))),
                ),
                -200,
            ),
        ],
        |a, b| a == b,
    )
}
