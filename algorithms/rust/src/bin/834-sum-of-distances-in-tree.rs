/*
 * @lc app=leetcode id=834 lang=rust
 *
 * [834] Sum of Distances in Tree
 *
 * https://leetcode.com/problems/sum-of-distances-in-tree/description/
 *
 * algorithms
 * Hard (59.48%)
 * Likes:    5003
 * Dislikes: 111
 * Total Accepted:    93.2K
 * Total Submissions: 157K
 * Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
 *
 * There is an undirected connected tree with n nodes labeled from 0 to n - 1
 * and n - 1 edges.
 *
 * You are given the integer n and the array edges where edges[i] = [ai, bi]
 * indicates that there is an edge between nodes ai and bi in the tree.
 *
 * Return an array answer of length n where answer[i] is the sum of the
 * distances between the i^th node in the tree and all other nodes.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
 * Output: [8,12,6,10,10,10]
 * Explanation: The tree is shown above.
 * We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
 * equals 1 + 1 + 2 + 2 + 2 = 8.
 * Hence, answer[0] = 8, and so on.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 1, edges = []
 * Output: [0]
 *
 *
 * Example 3:
 *
 *
 * Input: n = 2, edges = [[1,0]]
 * Output: [1,1]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 3 * 10^4
 * edges.length == n - 1
 * edges[i].length == 2
 * 0 <= ai, bi < n
 * ai != bi
 * The given input represents a valid tree.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn sum_of_distances_in_tree(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        fn dfs(
            node: usize,
            parent: usize,
            graph: &Vec<Vec<usize>>,
            count: &mut Vec<i32>,
            res: &mut Vec<i32>,
        ) {
            for &child in &graph[node] {
                if child == parent {
                    continue;
                }
                dfs(child, node, graph, count, res);
                count[node] += count[child];
                res[node] += res[child] + count[child];
            }
        }

        fn dfs2(
            node: usize,
            parent: usize,
            graph: &Vec<Vec<usize>>,
            count: &mut Vec<i32>,
            res: &mut Vec<i32>,
        ) {
            for &child in &graph[node] {
                if child == parent {
                    continue;
                }
                res[child] = res[node] + (count.len() as i32) - 2 * count[child];
                dfs2(child, node, graph, count, res);
            }
        }

        let mut graph: Vec<Vec<usize>> = vec![vec![]; n as usize];
        for edge in edges {
            let u = edge[0];
            let v = edge[1];
            graph[u as usize].push(v as usize);
            graph[v as usize].push(u as usize);
        }

        let mut count = vec![1; n as usize];
        let mut res = vec![0; n as usize];

        dfs(0, 0, &graph, &mut count, &mut res);
        dfs2(0, 0, &graph, &mut count, &mut res);

        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::sum_of_distances_in_tree(e.0, e.1),
        vec![
            (
                (
                    6,
                    vec![vec![0, 1], vec![0, 2], vec![2, 3], vec![2, 4], vec![2, 5]],
                ),
                vec![8, 12, 6, 10, 10, 10],
            ),
            // ((1, vec![]), vec![0]),
            // ((2, vec![vec![1, 0]]), vec![1, 1]),
        ],
        |a, b| a == b,
    )
}
