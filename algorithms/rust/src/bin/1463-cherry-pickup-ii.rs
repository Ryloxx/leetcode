#![feature(test)]
/*
 * @lc app=leetcode id=1463 lang=rust
 *
 * [1463] Cherry Pickup II
 *
 * https://leetcode.com/problems/cherry-pickup-ii/description/
 *
 * algorithms
 * Hard (69.50%)
 * Likes:    3683
 * Dislikes: 40
 * Total Accepted:    121.2K
 * Total Submissions: 171.1K
 * Testcase Example:  '[[3,1,1],[2,5,1],[1,5,5],[2,1,1]]'
 *
 * You are given a rows x cols matrix grid representing a field of cherries
 * where grid[i][j] represents the number of cherries that you can collect
 * from the (i, j) cell.
 *
 * You have two robots that can collect cherries for you:
 *
 *
 * Robot #1 is located at the top-left corner (0, 0), and
 * Robot #2 is located at the top-right corner (0, cols - 1).
 *
 *
 * Return the maximum number of cherries collection using both robots by
 * following the rules below:
 *
 *
 * From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or
 * (i + 1, j + 1).
 * When any robot passes through a cell, It picks up all cherries, and the
 * cell becomes an empty cell.
 * When both robots stay in the same cell, only one takes the cherries.
 * Both robots cannot move outside of the grid at any moment.
 * Both robots should reach the bottom row in grid.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
 * Output: 24
 * Explanation: Path of robot #1 and #2 are described in color green and blue
 * respectively.
 * Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
 * Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
 * Total of cherries: 12 + 12 = 24.
 *
 *
 * Example 2:
 *
 *
 * Input: grid =
 * [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,
 * 0,0,6]] Output: 28
 * Explanation: Path of robot #1 and #2 are described in color green and blue
 * respectively.
 * Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
 * Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
 * Total of cherries: 17 + 11 = 28.
 *
 *
 *
 * Constraints:
 *
 *
 * rows == grid.length
 * cols == grid[i].length
 * 2 <= rows, cols <= 70
 * 0 <= grid[i][j] <= 100
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    // Using vector memo + iteration + space optimization
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let n = grid[0].len();
        let pn = n + 2;
        let mut dp = vec![0; 2 * pn * pn];
        #[inline(always)]
        fn get(i: usize, robot_a: usize, robot_b: usize, pn: usize) -> usize {
            i * pn * pn + robot_a * pn + robot_b
        }
        for i in (0..m).rev() {
            let upper_bound = n.min(i + 1);
            for robot_a in 1..=upper_bound {
                for robot_b in (1 + (n - upper_bound))..=n {
                    let curr = get(i % 2, robot_a, robot_b, pn);
                    for a in 0..3 {
                        for b in 0..3 {
                            dp[curr] = dp[curr]
                                .max(dp[get((i + 1) % 2, robot_a + a - 1, robot_b + b - 1, pn)]);
                        }
                    }

                    dp[curr] += grid[i][robot_a - 1];
                    if robot_a != robot_b {
                        dp[curr] += grid[i][robot_b - 1];
                    }
                }
            }
        }
        dp[get(0, 1, n, pn)]
    }

    // Using hashmap memo + recursion
    // pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
    //     use std::collections::HashMap;
    //     fn dp(
    //         robot_a: usize,
    //         robot_b: usize,
    //         i: usize,
    //         grid: &Vec<Vec<i32>>,
    //         memo: &mut HashMap<u32, i32>,
    //     ) -> i32 {
    //         if i >= grid.len() || robot_a >= grid[0].len() || robot_b >=
    // grid[0].len() {             return 0;
    //         }
    //         let key = (robot_a as u32) << 14 | (robot_b as u32) << 7 | i as u32;
    //         if let Some(memo) = memo.get(&key) {
    //             return *memo;
    //         }
    //         let ret = (if robot_a == robot_b {
    //             grid[i][robot_a]
    //         } else {
    //             grid[i][robot_a] + grid[i][robot_b]
    //         } + (0..3)
    //             .flat_map(|y| (0..3).map(move |x| (x, y)))
    //             .map(|(a, b)| {
    //                 dp(
    //                     (robot_a + a).wrapping_sub(1),
    //                     (robot_b + b).wrapping_sub(1),
    //                     i + 1,
    //                     grid,
    //                     memo,
    //                 )
    //             })
    //             .max()
    //             .unwrap_or_default());

    //         memo.insert(key, ret);
    //         ret
    //     }
    //     dp(0, grid[0].len() - 1, 0, &grid, &mut HashMap::new())
    // }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::cherry_pickup,
        vec![
            (
                vec![vec![3, 1, 1], vec![2, 5, 1], vec![1, 5, 5], vec![2, 1, 1]],
                24,
            ),
            (
                vec![
                    vec![1, 0, 0, 0, 0, 0, 1],
                    vec![2, 0, 0, 0, 0, 3, 0],
                    vec![2, 0, 9, 0, 0, 0, 0],
                    vec![0, 3, 0, 5, 4, 0, 0],
                    vec![1, 0, 2, 3, 0, 0, 6],
                ],
                28,
            ),
        ],
        |a, b| a == b,
    )
}

#[cfg(test)]
mod test {
    use test::Bencher;

    use crate::Solution;

    extern crate test;

    #[bench]
    fn tempz(b: &mut Bencher) {
        b.iter(|| {
            Solution::cherry_pickup(vec![
                vec![3, 1, 1],
                vec![2, 5, 1],
                vec![1, 5, 5],
                vec![2, 1, 1],
            ]);
            Solution::cherry_pickup(vec![
                vec![1, 0, 0, 0, 0, 0, 1],
                vec![2, 0, 0, 0, 0, 3, 0],
                vec![2, 0, 9, 0, 0, 0, 0],
                vec![0, 3, 0, 5, 4, 0, 0],
                vec![1, 0, 2, 3, 0, 0, 6],
            ]);
        });
    }
}
