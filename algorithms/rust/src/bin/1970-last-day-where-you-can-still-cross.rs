/*
 * @lc app=leetcode id=1970 lang=rust
 *
 * [1970] Last Day Where You Can Still Cross
 *
 * https://leetcode.com/problems/last-day-where-you-can-still-cross/description/
 *
 * algorithms
 * Hard (49.51%)
 * Likes:    1253
 * Dislikes: 23
 * Total Accepted:    30.1K
 * Total Submissions: 50.5K
 * Testcase Example:  '2\n2\n[[1,1],[2,1],[1,2],[2,2]]'
 *
 * There is a 1-based binary matrix where 0 represents land and 1 represents
 * water. You are given integers row and col representing the number of rows
 * and columns in the matrix, respectively.
 *
 * Initially on day 0, the entire matrix is land. However, each day a new
 * cell becomes flooded with water. You are given a 1-based 2D array cells,
 * where cells[i] = [ri, ci] represents that on the i^th day, the cell on the
 * ri^th row and ci^th column (1-based coordinates) will be covered with
 * water (i.e., changed to 1).
 *
 * You want to find the last day that it is possible to walk from the top to
 * the bottom by only walking on land cells. You can start from any cell in
 * the top row and end at any cell in the bottom row. You can only travel in
 * the four cardinal directions (left, right, up, and down).
 *
 * Return the last day where it is possible to walk from the top to the
 * bottom by only walking on land cells.
 *
 *
 * Example 1:
 *
 *
 * Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
 * Output: 2
 * Explanation: The above image depicts how the matrix changes each day
 * starting from day 0.
 * The last day where it is possible to cross from top to bottom is on day 2.
 *
 *
 * Example 2:
 *
 *
 * Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
 * Output: 1
 * Explanation: The above image depicts how the matrix changes each day
 * starting from day 0.
 * The last day where it is possible to cross from top to bottom is on day 1.
 *
 *
 * Example 3:
 *
 *
 * Input: row = 3, col = 3, cells =
 * [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
 * Output: 3
 * Explanation: The above image depicts how the matrix changes each day
 * starting from day 0.
 * The last day where it is possible to cross from top to bottom is on day
 * 3.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= row, col <= 2 * 10^4
 * 4 <= row * col <= 2 * 10^4
 * cells.length == row * col
 * 1 <= ri <= row
 * 1 <= ci <= col
 * All the values of cells are unique.
 *
 *
 */
struct Solution;
// @lc code=start
// use std::collections::{HashSet, VecDeque};
impl Solution {
    pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
        let row = row as usize;
        let col = col as usize;
        const DIRECTIONS: [(usize, usize); 4] = [(!0usize, 0usize), (0, !0), (1, 0), (0, 1)];
        // filled: 1b, parents 15b, ranks 15b, pos 2b = 33b
        const FILLED_SHIFT: u32 = 15 + 15 + 2;
        const PARENTS_SHIFT: u32 = 15 + 2;
        const RANKS_SHIFT: u32 = 2;
        const POS_SHIFT: u32 = 0;
        const FILLED_MASK: u64 = 0b1 << FILLED_SHIFT;
        const PARENTS_MASK: u64 = 0x7fff << PARENTS_SHIFT;
        const RANKS_MASK: u64 = 0x7fff << RANKS_SHIFT;
        const POS_MASK: u64 = 0b11 << POS_SHIFT;
        let mut all = vec![0u64; row * col];
        (0..row * col).for_each(|idx| {
            all[idx] |= (idx as u64) << PARENTS_SHIFT;
        });
        for x in 0..col {
            all[x] |= 1 << POS_SHIFT;
            all[(row - 1) * col + x] |= 2 << POS_SHIFT;
        }

        fn find(mut x: usize, all: &[u64]) -> usize {
            loop {
                let px = ((all[x] & PARENTS_MASK) >> PARENTS_SHIFT) as usize;
                if px == x {
                    break px;
                }
                x = px
            }
        }

        fn union(x: usize, y: usize, all: &mut [u64]) -> u64 {
            let px = find(x, all);
            let py = find(y, all);
            let rank_x = (all[px] & (RANKS_MASK)) >> RANKS_SHIFT;
            let rank_y = (all[py] & (RANKS_MASK)) >> RANKS_SHIFT;
            let parent = if px == py {
                px
            } else if rank_x >= rank_y {
                all[py] = (all[py] & !PARENTS_MASK) | (px as u64) << PARENTS_SHIFT;
                all[px] = (all[px] & !RANKS_MASK) | rank_x.max(rank_y + 1) << RANKS_SHIFT;
                px
            } else {
                all[px] = (all[px] & !PARENTS_MASK) | (py as u64) << PARENTS_SHIFT;
                py
            };
            all[parent] |= (all[px] | all[py]) & POS_MASK;
            all[parent] & POS_MASK
        }

        for (day, cell) in cells.into_iter().enumerate().rev() {
            let y = (cell[0] - 1) as usize;
            let x = (cell[1] - 1) as usize;
            let curr = y * col + x;
            all[curr] |= FILLED_MASK;
            for (dy, dx) in DIRECTIONS {
                let ny = y.wrapping_add(dy);
                let nx = x.wrapping_add(dx);
                if ny < row && nx < col {
                    let other = ny * col + nx;
                    if all[other] & FILLED_MASK != 0 && union(curr, other, &mut all) == 3 {
                        return day as i32;
                    }
                }
            }
        }
        -1
    }
    // BFS + Binary Search
    // pub fn latest_day_to_cross(row: i32, col: i32, cells: Vec<Vec<i32>>) -> i32 {
    //     let row = row as usize;
    //     let col = col as usize;
    //     const DIRECTIONS: [(usize, usize); 4] = [(!0usize, 0usize), (0, !0), (1,
    // 0), (0, 1)];     let mut filled = vec![vec![0; col]; row];
    //     for (day, cell) in cells.into_iter().enumerate() {
    //         filled[(cell[0] - 1) as usize][(cell[1] - 1) as usize] = day;
    //     }
    //     fn can_reach_bottom(day: usize, row: usize, col: usize, filled:
    // &Vec<Vec<usize>>) -> bool {         let mut q = VecDeque::new();
    //         let mut visited = HashSet::new();
    //         let mut i = 0usize;
    //         while i < col || !q.is_empty() {
    //             let (y, x) = if i < col {
    //                 let ret = (0, i);
    //                 i += 1;
    //                 ret
    //             } else {
    //                 q.pop_front().unwrap()
    //             };
    //             let key: u64 = ((y as u64) << 32) | (x as u64);
    //             if visited.contains(&key) {
    //                 continue;
    //             }
    //             visited.insert(key);
    //             if filled[y][x] < day {
    //                 continue;
    //             }
    //             if y == row - 1 {
    //                 return true;
    //             }
    //             for (dy, dx) in DIRECTIONS {
    //                 let ny = y.wrapping_add(dy);
    //                 let nx = x.wrapping_add(dx);
    //                 if ny < row && nx < col {
    //                     q.push_back((ny, nx));
    //                 }
    //             }
    //         }
    //         false
    //     }
    //     let mut lo = 0;
    //     let mut hi = row * (col - 1);
    //     while lo < hi {
    //         let mid = (lo + hi + 1) / 2;
    //         if can_reach_bottom(mid, row, col, &filled) {
    //             lo = mid;
    //         } else {
    //             hi = mid - 1;
    //         }
    //     }
    //     lo as i32
    // }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::latest_day_to_cross(e.0, e.1, e.2),
        vec![
            (
                (2, 2, vec![vec![1, 1], vec![2, 1], vec![1, 2], vec![2, 2]]),
                2,
            ),
            (
                (2, 2, vec![vec![1, 1], vec![1, 2], vec![2, 1], vec![2, 2]]),
                1,
            ),
            (
                (
                    3,
                    3,
                    vec![
                        vec![1, 2],
                        vec![2, 1],
                        vec![3, 3],
                        vec![2, 2],
                        vec![1, 1],
                        vec![1, 3],
                        vec![2, 3],
                        vec![3, 2],
                        vec![3, 1],
                    ],
                ),
                3,
            ),
            (
                (
                    6,
                    2,
                    vec![
                        vec![4, 2],
                        vec![6, 2],
                        vec![2, 1],
                        vec![4, 1],
                        vec![6, 1],
                        vec![3, 1],
                        vec![2, 2],
                        vec![3, 2],
                        vec![1, 1],
                        vec![5, 1],
                        vec![5, 2],
                        vec![1, 2],
                    ],
                ),
                3,
            ),
            (
                (
                    55,
                    2,
                    vec![
                        vec![53, 1],
                        vec![25, 1],
                        vec![9, 2],
                        vec![3, 1],
                        vec![54, 1],
                        vec![14, 2],
                        vec![28, 1],
                        vec![4, 1],
                        vec![44, 1],
                        vec![20, 2],
                        vec![28, 2],
                        vec![24, 2],
                        vec![50, 1],
                        vec![47, 2],
                        vec![21, 1],
                        vec![47, 1],
                        vec![22, 2],
                        vec![10, 1],
                        vec![17, 1],
                        vec![13, 1],
                        vec![12, 1],
                        vec![37, 2],
                        vec![46, 2],
                        vec![51, 1],
                        vec![32, 1],
                        vec![51, 2],
                        vec![6, 2],
                        vec![49, 2],
                        vec![13, 2],
                        vec![34, 1],
                        vec![33, 1],
                        vec![38, 2],
                        vec![52, 2],
                        vec![26, 2],
                        vec![46, 1],
                        vec![20, 1],
                        vec![33, 2],
                        vec![23, 2],
                        vec![17, 2],
                        vec![1, 2],
                        vec![3, 2],
                        vec![50, 2],
                        vec![25, 2],
                        vec![19, 1],
                        vec![21, 2],
                        vec![49, 1],
                        vec![29, 1],
                        vec![30, 2],
                        vec![41, 1],
                        vec![16, 1],
                        vec![39, 2],
                        vec![9, 1],
                        vec![48, 2],
                        vec![23, 1],
                        vec![27, 1],
                        vec![43, 1],
                        vec![45, 1],
                        vec![31, 1],
                        vec![40, 1],
                        vec![6, 1],
                        vec![42, 1],
                        vec![8, 2],
                        vec![12, 2],
                        vec![29, 2],
                        vec![36, 2],
                        vec![39, 1],
                        vec![41, 2],
                        vec![10, 2],
                        vec![44, 2],
                        vec![14, 1],
                        vec![35, 1],
                        vec![30, 1],
                        vec![2, 2],
                        vec![34, 2],
                        vec![55, 1],
                        vec![18, 1],
                        vec![32, 2],
                        vec![27, 2],
                        vec![4, 2],
                        vec![37, 1],
                        vec![38, 1],
                        vec![16, 2],
                        vec![26, 1],
                        vec![15, 2],
                        vec![19, 2],
                        vec![5, 1],
                        vec![45, 2],
                        vec![43, 2],
                        vec![55, 2],
                        vec![35, 2],
                        vec![54, 2],
                        vec![42, 2],
                        vec![22, 1],
                        vec![11, 1],
                        vec![48, 1],
                        vec![1, 1],
                        vec![36, 1],
                        vec![24, 1],
                        vec![8, 1],
                        vec![2, 1],
                        vec![7, 1],
                        vec![15, 1],
                        vec![31, 2],
                        vec![18, 2],
                        vec![7, 2],
                        vec![52, 1],
                        vec![40, 2],
                        vec![53, 2],
                        vec![11, 2],
                        vec![5, 2],
                    ],
                ),
                10,
            ),
        ],
        |a, b| a == b,
    )
}
