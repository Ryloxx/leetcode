/*
 * @lc app=leetcode id=1743 lang=rust
 *
 * [1743] Restore the Array From Adjacent Pairs
 *
 * https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/
 *
 * algorithms
 * Medium (69.01%)
 * Likes:    1331
 * Dislikes: 49
 * Total Accepted:    57.8K
 * Total Submissions: 79.7K
 * Testcase Example:  '[[2,1],[3,4],[3,2]]'
 *
 * There is an integer array nums that consists of n unique elements, but you
 * have forgotten it. However, you do remember every pair of adjacent
 * elements in nums.
 *
 * You are given a 2D integer array adjacentPairs of size n - 1 where each
 * adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are
 * adjacent in nums.
 *
 * It is guaranteed that every adjacent pair of elements nums[i] and
 * nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or
 * [nums[i+1], nums[i]]. The pairs can appear in any order.
 *
 * Return the original array nums. If there are multiple solutions, return
 * any of them.
 *
 *
 * Example 1:
 *
 *
 * Input: adjacentPairs = [[2,1],[3,4],[3,2]]
 * Output: [1,2,3,4]
 * Explanation: This array has all its adjacent pairs in adjacentPairs.
 * Notice that adjacentPairs[i] may not be in left-to-right order.
 *
 *
 * Example 2:
 *
 *
 * Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
 * Output: [-2,4,1,-3]
 * Explanation: There can be negative numbers.
 * Another solution is [-3,1,4,-2], which would also be accepted.
 *
 *
 * Example 3:
 *
 *
 * Input: adjacentPairs = [[100000,-100000]]
 * Output: [100000,-100000]
 *
 *
 *
 * Constraints:
 *
 *
 * nums.length == n
 * adjacentPairs.length == n - 1
 * adjacentPairs[i].length == 2
 * 2 <= n <= 10^5
 * -10^5 <= nums[i], ui, vi <= 10^5
 * There exists some nums that has adjacentPairs as its pairs.
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn restore_array(adjacent_pairs: Vec<Vec<i32>>) -> Vec<i32> {
        let n = adjacent_pairs.len() + 1;
        let mut m = HashMap::<i32, Vec<i32>>::new();
        for pairs in adjacent_pairs {
            (*m.entry(pairs[0]).or_default()).push(pairs[1]);
            (*m.entry(pairs[1]).or_default()).push(pairs[0]);
        }
        let (start, mut curr) = m.iter().find(|(_, idxs)| idxs.len() == 1).unwrap();
        let mut res = vec![*start];
        while res.len() < n {
            let next = curr
                .iter()
                .find(|x| res.len() == 1 || res[res.len() - 2] != **x)
                .unwrap();
            res.push(*next);
            curr = &m[next];
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::restore_array,
        vec![
            ((vec![vec![2, 1], vec![3, 4], vec![3, 2]]), vec![1, 2, 3, 4]),
            (
                (vec![vec![4, -2], vec![1, 4], vec![-3, 1]]),
                vec![-2, 4, 1, -3],
            ),
            ((vec![vec![100000, -100000]]), vec![100000, -100000]),
        ],
        |a, b| {
            a == b || {
                let mut b = b.clone();
                b.reverse();
                *a == b
            }
        },
    );
}
