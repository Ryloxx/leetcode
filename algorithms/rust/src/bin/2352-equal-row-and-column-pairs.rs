/*
 * @lc app=leetcode id=2352 lang=rust
 *
 * [2352] Equal Row and Column Pairs
 *
 * https://leetcode.com/problems/equal-row-and-column-pairs/description/
 *
 * algorithms
 * Medium (71.02%)
 * Likes:    1119
 * Dislikes: 61
 * Total Accepted:    72.3K
 * Total Submissions: 97.5K
 * Testcase Example:  '[[3,2,1],[1,7,6],[2,7,7]]'
 *
 * Given a 0-indexed n x n integer matrix grid, return the number of pairs
 * (ri, cj) such that row ri and column cj are equal.
 *
 * A row and column pair is considered equal if they contain the same
 * elements in the same order (i.e., an equal array).
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
 * Output: 1
 * Explanation: There is 1 equal row and column pair:
 * - (Row 2, Column 1): [2,7,7]
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
 * Output: 3
 * Explanation: There are 3 equal row and column pairs:
 * - (Row 0, Column 0): [3,1,2,2]
 * - (Row 2, Column 2): [2,4,2,2]
 * - (Row 3, Column 2): [2,4,2,2]
 *
 *
 *
 * Constraints:
 *
 *
 * n == grid.length == grid[i].length
 * 1 <= n <= 200
 * 1 <= grid[i][j] <= 10^5
 *
 *
 */
struct Solution;
// @lc code=start
use std::{
    collections::{hash_map::DefaultHasher, HashMap},
    hash::Hasher,
};

struct TrieNode {
    value: i32,
    children: Option<Box<HashMap<i32, TrieNode>>>,
}

impl TrieNode {
    fn insert(&mut self, num: i32) -> &mut Self {
        if let None = self.children {
            self.children = Some(Box::new(HashMap::new()));
        }
        return self.children.as_mut().unwrap().entry(num).or_default();
    }
    fn get(&self, num: i32) -> Option<&Self> {
        return self.children.as_ref().unwrap().get(&num);
    }
}

impl Default for TrieNode {
    fn default() -> Self {
        Self {
            children: None,
            value: 0,
        }
    }
}

impl Solution {
    // Hash based
    pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut seen = HashMap::<u64, (usize, usize)>::new();
        for i in 0..n {
            let mut hasher_row = DefaultHasher::new();
            let mut hasher_col = DefaultHasher::new();
            for j in 0..n {
                hasher_col.write_i32(grid[i][j]);
                hasher_row.write_i32(grid[j][i]);
            }
            let hash_row = hasher_row.finish();
            let hash_col = hasher_col.finish();
            seen.entry(hash_row).or_default().0 += 1;
            seen.entry(hash_col).or_default().1 += 1;
        }

        seen.values().into_iter().map(|(r, c)| (r * c) as i32).sum()
    }

    // Trie based
    // pub fn equal_pairs(grid: Vec<Vec<i32>>) -> i32 {
    //     let n = grid.len();
    //     let mut trie = TrieNode::default();
    //     let mut res = 0;
    //     for i in 0..n {
    //         let mut current = &mut trie;
    //         for j in 0..n {
    //             current = current.insert(grid[i][j]);
    //         }
    //         current.value += 1;
    //     }
    //     'outer: for i in 0..n {
    //         let mut current = Some(&trie);
    //         for j in 0..n {
    //             current = current.unwrap().get(grid[j][i]);
    //             if current.is_none() {
    //                 continue 'outer;
    //             }
    //         }
    //         res += current.unwrap().value;
    //     }
    //     res
    // }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::equal_pairs(e),
        vec![
            (vec![vec![3, 2, 1], vec![1, 7, 6], vec![2, 7, 7]], 1),
            (
                vec![
                    vec![3, 1, 2, 2],
                    vec![1, 4, 4, 5],
                    vec![2, 4, 2, 2],
                    vec![2, 4, 2, 2],
                ],
                3,
            ),
            //
        ],
        |a, b| a == b,
    );
}
