/*
 * @lc app=leetcode id=1514 lang=rust
 *
 * [1514] Path with Maximum Probability
 *
 * https://leetcode.com/problems/path-with-maximum-probability/description/
 *
 * algorithms
 * Medium (48.43%)
 * Likes:    2480
 * Dislikes: 48
 * Total Accepted:    93.6K
 * Total Submissions: 178K
 * Testcase Example:  '3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.2]\n0\n2'
 *
 * You are given an undirected weighted graph of n nodes (0-indexed),
 * represented by an edge list where edges[i] = [a, b] is an undirected edge
 * connecting the nodes a and b with a probability of success of traversing
 * that edge succProb[i].
 *
 * Given two nodes start and end, find the path with the maximum probability
 * of success to go from start to end and return its success probability.
 *
 * If there is no path from start to end, return 0. Your answer will be
 * accepted if it differs from the correct answer by at most 1e-5.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start
 * = 0, end = 2
 * Output: 0.25000
 * Explanation: There are two paths from start to end, one having a
 * probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
 *
 *
 * Example 2:
 *
 *
 *
 *
 * Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start
 * = 0, end = 2
 * Output: 0.30000
 *
 *
 * Example 3:
 *
 *
 *
 *
 * Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
 * Output: 0.00000
 * Explanation: There is no path between 0 and 2.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= n <= 10^4
 * 0 <= start, end < n
 * start != end
 * 0 <= a, b < n
 * a != b
 * 0 <= succProb.length == edges.length <= 2*10^4
 * 0 <= succProb[i] <= 1
 * There is at most one edge between every two nodes.
 *
 *
 */

struct Solution;

// @lc code=start

use std::{
    cmp::Ordering,
    collections::{BinaryHeap, HashMap},
};
#[derive(PartialEq)]
struct OrderedF64(f64);

impl Eq for OrderedF64 {}

impl PartialOrd for OrderedF64 {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        self.0.partial_cmp(&other.0)
    }
}

impl Ord for OrderedF64 {
    fn cmp(&self, other: &OrderedF64) -> Ordering {
        self.partial_cmp(other).unwrap()
    }
}

impl Solution {
    pub fn max_probability(
        n: i32,
        edges: Vec<Vec<i32>>,
        succ_prob: Vec<f64>,
        start: i32,
        end: i32,
    ) -> f64 {
        let n = n as usize;
        let start = start as usize;
        let end = end as usize;
        let mut graph = HashMap::new();
        let mut visited = vec![false; n];
        let mut q: BinaryHeap<(OrderedF64, usize)> = BinaryHeap::new();
        for (edge, prob) in edges.iter().zip(succ_prob) {
            graph
                .entry(edge[0] as usize)
                .or_insert(HashMap::new())
                .insert(edge[1] as usize, prob);
            graph
                .entry(edge[1] as usize)
                .or_insert(HashMap::new())
                .insert(edge[0] as usize, prob);
        }
        q.push((OrderedF64(1.), start as usize));
        while !q.is_empty() {
            let (curr_prob, u) = q.pop().unwrap();
            if u == end {
                return curr_prob.0;
            }
            if visited[u] {
                continue;
            }
            visited[u] = true;
            if let Some(adj_u) = graph.get(&u) {
                for &v in adj_u.keys().filter(|&&v| !visited[v]) {
                    let prob = adj_u.get(&v).unwrap();
                    q.push((OrderedF64(curr_prob.0 * prob), v));
                }
            }
        }
        0.
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::max_probability(e.0, e.1, e.2, e.3, e.4),
        vec![
            //
            (
                (
                    3,
                    vec![vec![0, 1], vec![1, 2], vec![0, 2]],
                    vec![0.5, 0.5, 0.2],
                    0,
                    2,
                ),
                0.25000,
            ),
            (
                (
                    3,
                    vec![vec![0, 1], vec![1, 2], vec![0, 2]],
                    vec![0.5, 0.5, 0.3],
                    0,
                    2,
                ),
                0.30000,
            ),
            ((3, vec![vec![0, 1]], vec![0.5], 0, 2), 0.00000),
        ],
        |a, b| (a - b).abs().lt(&1e-5),
    )
}
