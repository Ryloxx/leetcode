/*
 * @lc app=leetcode id=1219 lang=rust
 *
 * [1219] Path with Maximum Gold
 *
 * https://leetcode.com/problems/path-with-maximum-gold/description/
 *
 * algorithms
 * Medium (63.57%)
 * Likes:    2740
 * Dislikes: 72
 * Total Accepted:    122.4K
 * Total Submissions: 190.6K
 * Testcase Example:  '[[0,6,0],[5,8,7],[0,9,0]]'
 *
 * In a gold mine grid of size m x n, each cell in this mine has an integer
 * representing the amount of gold in that cell, 0 if it is empty.
 *
 * Return the maximum amount of gold you can collect under the
 * conditions:
 *
 *
 * Every time you are located in a cell you will collect all the gold in that
 * cell.
 * From your position, you can walk one step to the left, right, up, or
 * down.
 * You can't visit the same cell more than once.
 * Never visit a cell with 0 gold.
 * You can start and stop collecting gold from any position in the grid that
 * has some gold.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
 * Output: 24
 * Explanation:
 * [[0,6,0],
 * [5,8,7],
 * [0,9,0]]
 * Path to get the maximum gold, 9 -> 8 -> 7.
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
 * Output: 28
 * Explanation:
 * [[1,0,7],
 * [2,0,6],
 * [3,4,5],
 * [0,3,0],
 * [9,0,20]]
 * Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 *
 *
 *
 * Constraints:
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 15
 * 0 <= grid[i][j] <= 100
 * There are at most 25 cells containing gold.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn get_maximum_gold(mut grid: Vec<Vec<i32>>) -> i32 {
        fn backtrack(i: usize, j: usize, grid: &mut [Vec<i32>]) -> i32 {
            if i >= grid.len() || j >= grid[0].len() || grid[i][j] == 0 {
                return 0;
            }
            let prev = grid[i][j];
            grid[i][j] = 0;
            let ret = DIRECTIONS
                .iter()
                .map(|&(dy, dx)| backtrack(i.wrapping_add(dy), j.wrapping_add(dx), grid))
                .max()
                .unwrap();
            grid[i][j] = prev;
            ret + prev
        }
        const DIRECTIONS: [(usize, usize); 4] = [(!0usize, 0usize), (0, !0), (1, 0), (0, 1)];
        let m = grid.len();
        let n = grid[0].len();
        let golds = grid.iter().map(|row| row.iter().sum::<i32>()).sum::<i32>();
        let mut res = 0;
        for i in 0..m {
            for j in 0..n {
                res = backtrack(i, j, &mut grid).max(res);
                if res == golds {
                    return res;
                }
            }
        }
        res
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        Solution::get_maximum_gold,
        vec![
            ((vec![vec![0, 6, 0], vec![5, 8, 7], vec![0, 9, 0]]), 24),
            (
                (vec![
                    vec![1, 0, 7],
                    vec![2, 0, 6],
                    vec![3, 4, 5],
                    vec![0, 3, 0],
                    vec![9, 0, 20],
                ]),
                28,
            ),
            ((vec![vec![1; 5]; 5]), 25),
        ],
        |a, b| a == b,
    )
}
