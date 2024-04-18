/*
 * @lc app=leetcode id=463 lang=rust
 *
 * [463] Island Perimeter
 *
 * https://leetcode.com/problems/island-perimeter/description/
 *
 * algorithms
 * Easy (70.24%)
 * Likes:    6605
 * Dislikes: 362
 * Total Accepted:    571.7K
 * Total Submissions: 796.3K
 * Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
 *
 * You are given row x col grid representing a map where grid[i][j] = 1
 * represents land and grid[i][j] = 0 represents water.
 *
 * Grid cells are connected horizontally/vertically (not diagonally). The
 * grid is completely surrounded by water, and there is exactly one island
 * (i.e., one or more connected land cells).
 *
 * The island doesn't have "lakes", meaning the water inside isn't connected
 * to the water around the island. One cell is a square with side length 1.
 * The grid is rectangular, width and height don't exceed 100. Determine the
 * perimeter of the island.
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
 * Output: 16
 * Explanation: The perimeter is the 16 yellow stripes in the image above.
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [[1]]
 * Output: 4
 *
 *
 * Example 3:
 *
 *
 * Input: grid = [[1,0]]
 * Output: 4
 *
 *
 *
 * Constraints:
 *
 *
 * row == grid.length
 * col == grid[i].length
 * 1 <= row, col <= 100
 * grid[i][j] is 0 or 1.
 * There is exactly one island in grid.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let mut res = 0;
        fn get(i: usize, j: usize, m: usize, n: usize, arr: &[Vec<i32>]) -> i32 {
            if i >= m || j >= n {
                0
            } else {
                arr[i][j]
            }
        }
        for i in 0..m + 1 {
            let mut cell = 0;
            for j in 0..n + 1 {
                let right = get(i.wrapping_sub(1), j, m, n, &grid);
                let bottom = get(i, j.wrapping_sub(1), m, n, &grid);
                res += ((cell + right) & 1) + ((cell + bottom) & 1);
                cell = right;
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::island_perimeter,
        vec![
            (
                (vec![
                    vec![0, 1, 0, 0],
                    vec![1, 1, 1, 0],
                    vec![0, 1, 0, 0],
                    vec![1, 1, 0, 0],
                ]),
                16,
            ),
            ((vec![vec![1]]), 4),
            ((vec![vec![1, 0]]), 4),
            ((vec![vec![1, 1], vec![1, 1]]), 8),
        ],
        |a, b| a == b,
    )
}
