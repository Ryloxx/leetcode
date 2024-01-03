/*
 * @lc app=leetcode id=864 lang=rust
 *
 * [864] Shortest Path to Get All Keys
 *
 * https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
 *
 * algorithms
 * Hard (45.50%)
 * Likes:    1899
 * Dislikes: 87
 * Total Accepted:    59.4K
 * Total Submissions: 110.6K
 * Testcase Example:  '["@.a..","###.#","b.A.B"]'
 *
 * You are given an m x n grid grid where:
 *
 *
 * '.' is an empty cell.
 * '#' is a wall.
 * '@' is the starting point.
 * Lowercase letters represent keys.
 * Uppercase letters represent locks.
 *
 *
 * You start at the starting point and one move consists of walking one space
 * in one of the four cardinal directions. You cannot walk outside the grid,
 * or walk into a wall.
 *
 * If you walk over a key, you can pick it up and you cannot walk over a lock
 * unless you have its corresponding key.
 *
 * For some 1 <= k <= 6, there is exactly one lowercase and one uppercase
 * letter of the first k letters of the English alphabet in the grid. This
 * means that there is exactly one key for each lock, and one lock for each
 * key; and also that the letters used to represent the keys and locks were
 * chosen in the same order as the English alphabet.
 *
 * Return the lowest number of moves to acquire all keys. If it is
 * impossible, return -1.
 *
 *
 * Example 1:
 *
 *
 * Input: grid = ["@.a..","###.#","b.A.B"]
 * Output: 8
 * Explanation: Note that the goal is to obtain all the keys not to open all
 * the locks.
 *
 *
 * Example 2:
 *
 *
 * Input: grid = ["@..aA","..B#.","....b"]
 * Output: 6
 *
 *
 * Example 3:
 *
 *
 * Input: grid = ["@Aa"]
 * Output: -1
 *
 *
 *
 * Constraints:
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 30
 * grid[i][j] is either an English letter, '.', '#', or '@'.
 * The number of keys in the grid is in the range [1, 6].
 * Each key in the grid is unique.
 * Each key in the grid has a matching lock.
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::VecDeque;
impl Solution {
    pub fn shortest_path_all_keys(grid: Vec<String>) -> i32 {
        const DIRECTIONS: [(usize, usize); 4] = [(!0usize, 0usize), (0, !0), (1, 0), (0, 1)];
        let mut all_keys = 0u32;
        let mut visited = [[[false; 64]; 30]; 30];
        let mut q = VecDeque::new();
        for (y, row) in grid.iter().enumerate() {
            for (x, cell) in row.chars().enumerate() {
                if cell as u8 == b'@' {
                    q.push_back((0i32, 0u32, y, x));
                }
                if cell.is_ascii_lowercase() {
                    all_keys <<= 1;
                    all_keys += 1;
                }
            }
        }
        while !q.is_empty() {
            let (mut dist, mut curr_keys, y, x) = q.pop_front().unwrap();
            let has_been_visited = &mut visited[y][x][curr_keys as usize];
            if *has_been_visited {
                continue;
            }
            *has_been_visited = true;
            let ch = grid[y].as_bytes()[x];
            match ch {
                b'#' => {
                    continue;
                }
                b'a'..=b'z' => {
                    curr_keys |= 1 << (ch - b'a');
                }
                b'A'..=b'Z' => {
                    if (1 << (ch - b'A') & curr_keys) == 0 {
                        continue;
                    }
                }
                _ => {}
            };
            if curr_keys == all_keys {
                return dist;
            }
            dist += 1;
            for (dy, dx) in DIRECTIONS {
                let ny = y.wrapping_add(dy);
                let nx = x.wrapping_add(dx);
                if ny < grid.len() && nx < grid[ny].len() {
                    q.push_back((dist, curr_keys, ny, nx));
                }
            }
        }
        -1
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::shortest_path_all_keys,
        vec![
            (
                ["@.a..", "###.#", "b.A.B"]
                    .into_iter()
                    .map(String::from)
                    .collect(),
                8,
            ),
            (
                ["@..aA", "..B#.", "....b"]
                    .into_iter()
                    .map(String::from)
                    .collect(),
                6,
            ),
            (["@Aa"].into_iter().map(String::from).collect(), -1),
            (
                [
                    ".##..##..B",
                    "##...#...#",
                    "..##..#...",
                    ".#..#b...#",
                    "#.##.a.###",
                    ".#....#...",
                    ".##..#.#..",
                    ".....###@.",
                    "..........",
                    ".........A",
                ]
                .into_iter()
                .map(String::from)
                .collect(),
                11,
            ),
            (
                ["@#b#", "..#.", "aAB."]
                    .into_iter()
                    .map(String::from)
                    .collect(),
                -1,
            ),
            (
                [".#.b.", "A.#aB", "#d...", "@.cC.", "D...#"]
                    .into_iter()
                    .map(String::from)
                    .collect(),
                8,
            ),
        ],
        |a, b| a == b,
    )
}
