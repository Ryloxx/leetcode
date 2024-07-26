/*
 * @lc app=leetcode id=1334 lang=rust
 *
 * [1334] Find the City With the Smallest Number of Neighbors at a Threshold
 * Distance
 *
 * https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
 *
 * algorithms
 * Medium (59.97%)
 * Likes:    2896
 * Dislikes: 117
 * Total Accepted:    141.2K
 * Total Submissions: 218.9K
 * Testcase Example:  '4\n[[0,1,3],[1,2,1],[1,3,4],[2,3,1]]\n4'
 *
 * There are n cities numbered from 0 to n-1. Given the array edges where
 * edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted
 * edge between cities fromi and toi, and given the integer
 * distanceThreshold.
 *
 * Return the city with the smallest number of cities that are reachable
 * through some path and whose distance is at most distanceThreshold, If
 * there are multiple such cities, return the city with the greatest number.
 *
 * Notice that the distance of a path connecting cities i and j is equal to
 * the sum of the edges' weights along that path.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold
 * = 4
 * Output: 3
 * Explanation: The figure above describes the graph.
 * The neighboring cities at a distanceThreshold = 4 for each city are:
 * City 0 -> [City 1, City 2]
 * City 1 -> [City 0, City 2, City 3]
 * City 2 -> [City 0, City 1, City 3]
 * City 3 -> [City 1, City 2]
 * Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but
 * we have to return city 3 since it has the greatest number.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],
 * distanceThreshold = 2
 * Output: 0
 * Explanation: The figure above describes the graph.
 * The neighboring cities at a distanceThreshold = 2 for each city are:
 * City 0 -> [City 1]
 * City 1 -> [City 0, City 4]
 * City 2 -> [City 3, City 4]
 * City 3 -> [City 2, City 4]
 * City 4 -> [City 1, City 2, City 3]
 * The city 0 has 1 neighboring city at a distanceThreshold = 2.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= n <= 100
 * 1 <= edges.length <= n * (n - 1) / 2
 * edges[i].length == 3
 * 0 <= fromi < toi < n
 * 1 <= weighti, distanceThreshold <= 10^4
 * All pairs (fromi, toi) are distinct.
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::{BinaryHeap, HashMap, HashSet};
impl Solution {
    pub fn find_the_city(n: i32, edges: Vec<Vec<i32>>, distance_threshold: i32) -> i32 {
        let mut graph: HashMap<u8, HashMap<u8, u16>> = HashMap::new();
        for uvw in edges {
            let u = uvw[0] as u8;
            let v = uvw[1] as u8;
            let w = uvw[2] as u16;
            *(graph.entry(u).or_default().entry(v).or_default()) = w;
            *(graph.entry(v).or_default().entry(u).or_default()) = w;
        }
        let mut h = BinaryHeap::new();
        let mut seen = HashSet::new();
        let mut res = 0;
        let mut best = u8::MAX;
        'outer: for i in (0..n as u8).rev() {
            h.clear();
            seen.clear();

            let mut count = 0;
            h.push((0i32, i));
            while let Some((weight, u)) = h.pop() {
                if seen.contains(&u) || -weight > distance_threshold {
                    continue;
                }
                count += 1;
                if count >= best {
                    continue 'outer;
                }
                seen.insert(u);
                if let Some(graph) = graph.get(&u) {
                    for (v, w) in graph.iter() {
                        h.push((weight - *w as i32, *v))
                    }
                }
            }

            best = count;
            res = i;
        }
        res as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::find_the_city(e.0, e.1, e.2),
        vec![
            (
                (
                    4,
                    vec![vec![0, 1, 3], vec![1, 2, 1], vec![1, 3, 4], vec![2, 3, 1]],
                    4,
                ),
                3,
            ),
            (
                (
                    5,
                    vec![
                        vec![0, 1, 2],
                        vec![0, 4, 8],
                        vec![1, 2, 3],
                        vec![1, 4, 2],
                        vec![2, 3, 1],
                        vec![3, 4, 1],
                    ],
                    2,
                ),
                0,
            ),
        ],
        |a, b| a == b,
    )
}
