/*
 * @lc app=leetcode id=2328 lang=rust
 *
 * [2328] Number of Increasing Paths in a Grid
 *
 * https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/description/
 *
 * algorithms
 * Hard (47.71%)
 * Likes:    1223
 * Dislikes: 28
 * Total Accepted:    34.4K
 * Total Submissions: 61.6K
 * Testcase Example:  '[[1,1],[3,4]]'
 *
 * You are given an m x n integer matrix grid, where you can move from a cell
 * to any adjacent cell in all 4 directions.
 *
 * Return the number of strictly increasing paths in the grid such that you
 * can start from any cell and end at any cell. Since the answer may be very
 * large, return it modulo 10^9 + 7.
 *
 * Two paths are considered different if they do not have exactly the same
 * sequence of visited cells.
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [[1,1],[3,4]]
 * Output: 8
 * Explanation: The strictly increasing paths are:
 * - Paths with length 1: [1], [1], [3], [4].
 * - Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
 * - Paths with length 3: [1 -> 3 -> 4].
 * The total number of paths is 4 + 3 + 1 = 8.
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [[1],[2]]
 * Output: 3
 * Explanation: The strictly increasing paths are:
 * - Paths with length 1: [1], [2].
 * - Paths with length 2: [1 -> 2].
 * The total number of paths is 2 + 1 = 3.
 *
 *
 *
 * Constraints:
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 1000
 * 1 <= m * n <= 10^5
 * 1 <= grid[i][j] <= 10^5
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn count_paths(grid: Vec<Vec<i32>>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let (m, n) = (grid.len(), grid[0].len());
        let directions = [(0, 1), (1, 0), (!0, 0), (0, !0)];
        fn dfs(
            y: usize,
            x: usize,
            m: usize,
            n: usize,
            grid: &Vec<Vec<i32>>,
            directions: &[(usize, usize)],
            memo: &mut HashMap<(usize, usize), i32>,
        ) -> i32 {
            if let Some(memo) = memo.get(&(y, x)) {
                return *memo;
            }
            let mut res = 1;
            for (dy, dx) in directions {
                let ny = y.wrapping_add(*dy);
                let nx = x.wrapping_add(*dx);
                if ny < m && nx < n && grid[ny][nx] < grid[y][x] {
                    res += dfs(ny, nx, m, n, grid, directions, memo);
                    res %= MOD;
                }
            }
            memo.insert((y, x), res);
            res
        }
        let mut memo = HashMap::new();
        let mut res = 0;
        for y in 0..m {
            for x in 0..n {
                res += dfs(y, x, m, n, &grid, &directions, &mut memo);
                res %= MOD;
            }
        }
        res
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        Solution::count_paths,
        vec![
            //
            (vec![vec![1, 1], vec![3, 4]], 8),
            (vec![vec![1], vec![2]], 3),
        ],
        |a, b| a == b,
    );
}
