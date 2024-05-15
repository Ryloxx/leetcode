/*
 * @lc app=leetcode id=2812 lang=rust
 *
 * [2812] Find the Safest Path in a Grid
 *
 * https://leetcode.com/problems/find-the-safest-path-in-a-grid/description/
 *
 * algorithms
 * Medium (31.31%)
 * Likes:    857
 * Dislikes: 120
 * Total Accepted:    24.5K
 * Total Submissions: 70.2K
 * Testcase Example:  '[[1,0,0],[0,0,0],[0,0,1]]'
 *
 * You are given a 0-indexed 2D matrix grid of size n x n, where (r, c)
 * represents:
 *
 *
 * A cell containing a thief if grid[r][c] = 1
 * An empty cell if grid[r][c] = 0
 *
 *
 * You are initially positioned at cell (0, 0). In one move, you can move to
 * any adjacent cell in the grid, including cells containing thieves.
 *
 * The safeness factor of a path on the grid is defined as the minimum
 * manhattan distance from any cell in the path to any thief in the grid.
 *
 * Return the maximum safeness factor of all paths leading to cell (n - 1, n
 * - 1).
 *
 * An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c -
 * 1), (r + 1, c) and (r - 1, c) if it exists.
 *
 * The Manhattan distance between two cells (a, b) and (x, y) is equal to |a
 * - x| + |b - y|, where |val| denotes the absolute value of val.
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
 * Output: 0
 * Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the
 * thieves in cells (0, 0) and (n - 1, n - 1).
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
 * Output: 2
 * Explanation: The path depicted in the picture above has a safeness factor
 * of 2 since:
 * - The closest cell of the path to the thief at cell (0, 2) is cell (0, 0).
 * The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
 * It can be shown that there are no other paths with a higher safeness
 * factor.
 *
 *
 * Example 3:
 *
 *
 * Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
 * Output: 2
 * Explanation: The path depicted in the picture above has a safeness factor
 * of 2 since:
 * - The closest cell of the path to the thief at cell (0, 3) is cell (1, 2).
 * The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
 * - The closest cell of the path to the thief at cell (3, 0) is cell (3, 2).
 * The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
 * It can be shown that there are no other paths with a higher safeness
 * factor.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= grid.length == n <= 400
 * grid[i].length == n
 * grid[i][j] is either 0 or 1.
 * There is at least one thief in the grid.
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::VecDeque;
impl Solution {
    pub fn maximum_safeness_factor(mut grid: Vec<Vec<i32>>) -> i32 {
        const DIRECTIONS: [(usize, usize); 4] = [(!0usize, 0usize), (0, !0), (1, 0), (0, 1)];
        let m = grid.len();
        let n = grid[0].len();
        let mut q = VecDeque::new();
        for (i, row) in grid.iter_mut().enumerate() {
            for (j, cell) in row.iter_mut().enumerate() {
                if *cell == 1 {
                    q.push_back((i, j, 1))
                }
            }
        }
        while let Some((i, j, mut dist)) = q.pop_front() {
            dist += 1;
            for (dy, dx) in DIRECTIONS {
                let i = i.wrapping_add(dy);
                let j = j.wrapping_add(dx);
                if i < m && j < n && grid[i][j] == 0 {
                    grid[i][j] = dist;
                    q.push_back((i, j, dist))
                }
            }
        }
        q.push_front((0, 0, grid[0][0]));
        let mut limit = grid[0][0];
        grid[0][0] = 0;
        while let Some((i, j, safeness_factor)) = q.pop_front() {
            if i == m - 1 && j == n - 1 {
                return safeness_factor - 1;
            }
            limit = limit.min(safeness_factor);
            for (dy, dx) in DIRECTIONS {
                let i = i.wrapping_add(dy);
                let j = j.wrapping_add(dx);
                if i < m && j < n && grid[i][j] > 0 {
                    let safeness_factor = safeness_factor.min(grid[i][j]);
                    if safeness_factor < limit {
                        q.push_back((i, j, safeness_factor));
                    } else {
                        q.push_front((i, j, safeness_factor));
                    }
                    grid[i][j] = 0;
                }
            }
        }
        0
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::maximum_safeness_factor,
        vec![
            ((vec![vec![1, 0, 0], vec![0, 0, 0], vec![0, 0, 1]]), 0),
            ((vec![vec![0, 0, 1], vec![0, 0, 0], vec![0, 0, 0]]), 2),
            (
                (vec![
                    vec![0, 0, 0, 1],
                    vec![0, 0, 0, 0],
                    vec![0, 0, 0, 0],
                    vec![1, 0, 0, 0],
                ]),
                2,
            ),
            (
                (vec![
                    vec![0, 0, 0, 0],
                    vec![0, 0, 0, 0],
                    vec![0, 0, 0, 0],
                    vec![0, 0, 1, 0],
                ]),
                1,
            ),
            (
                (vec![
                    vec![0, 0, 0, 0],
                    vec![0, 0, 0, 0],
                    vec![0, 0, 0, 0],
                    vec![0, 0, 0, 0],
                ]),
                0,
            ),
            (
                (vec![
                    vec![0, 1, 0, 0],
                    vec![0, 0, 0, 0],
                    vec![0, 0, 0, 0],
                    vec![0, 0, 1, 0],
                ]),
                1,
            ),
            ((vec![vec![1; 400]; 400]), 0),
        ],
        |a, b| a == b,
    )
}
