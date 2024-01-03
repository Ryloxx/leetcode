/*
 * @lc app=leetcode id=815 lang=rust
 *
 * [815] Bus Routes
 *
 * https://leetcode.com/problems/bus-routes/description/
 *
 * algorithms
 * Hard (45.51%)
 * Likes:    3334
 * Dislikes: 82
 * Total Accepted:    140.7K
 * Total Submissions: 308K
 * Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
 *
 * You are given an array routes representing bus routes where routes[i] is a
 * bus route that the i^th bus repeats forever.
 *
 *
 * For example, if routes[0] = [1, 5, 7], this means that the 0^th bus
 * travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
 *
 *
 * You will start at the bus stop source (You are not on any bus initially),
 * and you want to go to the bus stop target. You can travel between bus
 * stops by buses only.
 *
 * Return the least number of buses you must take to travel from source to
 * target. Return -1 if it is not possible.
 *
 *
 * Example 1:
 *
 *
 * Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
 * Output: 2
 * Explanation: The best strategy is take the first bus to the bus stop 7,
 * then take the second bus to the bus stop 6.
 *
 *
 * Example 2:
 *
 *
 * Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15,
 * target = 12
 * Output: -1
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= routes.length <= 500.
 * 1 <= routes[i].length <= 10^5
 * All the values of routes[i] are unique.
 * sum(routes[i].length) <= 10^5
 * 0 <= routes[i][j] < 10^6
 * 0 <= source, target < 10^6
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::{HashMap, HashSet};
impl Solution {
    pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
        if source == target {
            return 0;
        }
        let mut graph = HashMap::<i32, Vec<i32>>::new();
        for (idx, route) in routes.iter().enumerate() {
            for stop in route {
                graph.entry(*stop).or_default().push(idx as i32);
            }
        }

        let mut q1 = std::mem::take(graph.get_mut(&source).unwrap());
        let mut q2 = vec![];
        let mut seen = HashSet::new();
        let mut res = 0;
        while !q1.is_empty() {
            res += 1;
            for idx in q1.iter() {
                let k_idx = (*idx) << 20;
                if seen.contains(&k_idx) {
                    continue;
                }
                seen.insert(k_idx);
                for stop in routes[*idx as usize].iter() {
                    if *stop == target {
                        return res;
                    }
                    if seen.contains(stop) {
                        continue;
                    }
                    seen.insert(*stop);
                    q2.extend(graph[stop].iter())
                }
            }
            q1.clear();
            std::mem::swap(&mut q1, &mut q2);
        }
        -1
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::num_buses_to_destination(e.0, e.1, e.2),
        vec![
            ((vec![vec![1, 2, 7], vec![3, 6, 7]], 1, 6), 2),
            (
                (
                    vec![
                        vec![7, 12],
                        vec![4, 5, 15],
                        vec![6],
                        vec![15, 19],
                        vec![9, 12, 13],
                    ],
                    15,
                    12,
                ),
                -1,
            ),
            ((vec![vec![1, 2, 7], vec![3, 6, 7]], 1, 2), 1),
            ((vec![vec![1, 7], vec![3, 5]], 5, 5), 0),
        ],
        |a, b| a == b,
    );
}
