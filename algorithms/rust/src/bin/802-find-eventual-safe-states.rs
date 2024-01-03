/*
 * @lc app=leetcode id=802 lang=rust
 *
 * [802] Find Eventual Safe States
 *
 * https://leetcode.com/problems/find-eventual-safe-states/description/
 *
 * algorithms
 * Medium (55.56%)
 * Likes:    4746
 * Dislikes: 414
 * Total Accepted:    175.9K
 * Total Submissions: 291K
 * Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
 *
 * There is a directed graph of n nodes with each node labeled from 0 to n -
 * 1. The graph is represented by a 0-indexed 2D integer array graph where
 * graph[i] is an integer array of nodes adjacent to node i, meaning there is
 * an edge from node i to each node in graph[i].
 *
 * A node is a terminal node if there are no outgoing edges. A node is a safe
 * node if every possible path starting from that node leads to a terminal
 * node (or another safe node).
 *
 * Return an array containing all the safe nodes of the graph. The answer
 * should be sorted in ascending order.
 *
 *
 * Example 1:
 *
 *
 * Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
 * Output: [2,4,5,6]
 * Explanation: The given graph is shown above.
 * Nodes 5 and 6 are terminal nodes as there are no outgoing edges from
 * either of them.
 * Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or
 * 6.
 *
 * Example 2:
 *
 *
 * Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
 * Output: [4]
 * Explanation:
 * Only node 4 is a terminal node, and every path starting at node 4 leads to
 * node 4.
 *
 *
 *
 * Constraints:
 *
 *
 * n == graph.length
 * 1 <= n <= 10^4
 * 0 <= graph[i].length <= n
 * 0 <= graph[i][j] <= n - 1
 * graph[i] is sorted in a strictly increasing order.
 * The graph may contain self-loops.
 * The number of edges in the graph will be in the range [1, 4 * 10^4].
 *
 *
 */

struct Solution;
// @lc code=start

impl Solution {
    pub fn eventual_safe_nodes(graph: Vec<Vec<i32>>) -> Vec<i32> {
        let mut memo: Vec<i32> = vec![-1; graph.len()];
        let mut path = vec![false; graph.len()];

        fn dfs(
            curr: usize,
            graph: &Vec<Vec<i32>>,
            memo: &mut Vec<i32>,
            path: &mut Vec<bool>,
        ) -> i32 {
            if memo[curr] >= 0 {
                return memo[curr];
            }
            if path[curr] {
                return 0;
            }
            path[curr] = true;
            memo[curr] = graph[curr]
                .iter()
                .all(|&neigh| dfs(neigh as usize, graph, memo, path) == 1)
                as i32;
            path[curr] = false;
            memo[curr]
        }
        (0..graph.len() as i32)
            .filter(|&start| dfs(start as usize, &graph, &mut memo, &mut path) == 1)
            .collect()
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        Solution::eventual_safe_nodes,
        vec![
            (
                (vec![
                    vec![1, 2],
                    vec![2, 3],
                    vec![5],
                    vec![0],
                    vec![5],
                    vec![],
                    vec![],
                ]),
                vec![2, 4, 5, 6],
            ),
            (
                (vec![vec![1, 2, 3, 4], vec![1, 2], vec![3, 4], vec![0, 4], vec![]]),
                vec![4],
            ),
            (
                (vec![vec![], vec![0, 2, 3, 4], vec![3], vec![4], vec![]]),
                vec![0, 1, 2, 3, 4],
            ),
        ],
        |a, b| a == b,
    )
}
