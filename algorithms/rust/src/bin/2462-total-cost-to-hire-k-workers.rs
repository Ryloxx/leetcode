/*
 * @lc app=leetcode id=2462 lang=rust
 *
 * [2462] Total Cost to Hire K Workers
 *
 * https://leetcode.com/problems/total-cost-to-hire-k-workers/description/
 *
 * algorithms
 * Medium (37.43%)
 * Likes:    1087
 * Dislikes: 257
 * Total Accepted:    40.4K
 * Total Submissions: 93.1K
 * Testcase Example:  '[17,12,10,2,7,2,11,20,8]\n3\n4'
 *
 * You are given a 0-indexed integer array costs where costs[i] is the cost
 * of hiring the i^th worker.
 *
 * You are also given two integers k and candidates. We want to hire exactly
 * k workers according to the following rules:
 *
 *
 * You will run k sessions and hire exactly one worker in each session.
 * In each hiring session, choose the worker with the lowest cost from either
 * the first candidates workers or the last candidates workers. Break the tie
 * by the smallest index.
 *
 * For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the
 * first hiring session, we will choose the 4^th worker because they have the
 * lowest cost [3,2,7,7,1,2].
 * In the second hiring session, we will choose 1^st worker because they have
 * the same lowest cost as 4^th worker but they have the smallest index
 * [3,2,7,7,2]. Please note that the indexing may be changed in the
 * process.
 *
 *
 * If there are fewer than candidates workers remaining, choose the worker
 * with the lowest cost among them. Break the tie by the smallest index.
 * A worker can only be chosen once.
 *
 *
 * Return the total cost to hire exactly k workers.
 *
 *
 * Example 1:
 *
 *
 * Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
 * Output: 11
 * Explanation: We hire 3 workers in total. The total cost is initially 0.
 * - In the first hiring round we choose the worker from
 * [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by
 * the smallest index, which is 3. The total cost = 0 + 2 = 2.
 * - In the second hiring round we choose the worker from
 * [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2
 * + 2 = 4.
 * - In the third hiring round we choose the worker from
 *   [17,12,10,7,11,20,8].
 * The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that
 * the worker with index 3 was common in the first and last four workers.
 * The total hiring cost is 11.
 *
 *
 * Example 2:
 *
 *
 * Input: costs = [1,2,4,1], k = 3, candidates = 3
 * Output: 4
 * Explanation: We hire 3 workers in total. The total cost is initially 0.
 * - In the first hiring round we choose the worker from [1,2,4,1]. The
 *   lowest
 * cost is 1, and we break the tie by the smallest index, which is 0. The
 * total cost = 0 + 1 = 1. Notice that workers with index 1 and 2 are common
 * in the first and last 3 workers.
 * - In the second hiring round we choose the worker from [2,4,1]. The lowest
 * cost is 1 (index 2). The total cost = 1 + 1 = 2.
 * - In the third hiring round there are less than three candidates. We
 *   choose
 * the worker from the remaining workers [2,4]. The lowest cost is 2 (index
 * 0). The total cost = 2 + 2 = 4.
 * The total hiring cost is 4.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= costs.length <= 10^5
 * 1 <= costs[i] <= 10^5
 * 1 <= k, candidates <= costs.length
 *
 *
 */

struct Solution;
// @lc code=start
use std::collections::BinaryHeap;
impl Solution {
    pub fn total_cost(costs: Vec<i32>, k: i32, candidates: i32) -> i64 {
        let candidates = candidates as usize;
        let mut left_idx = candidates.min(costs.len());
        let mut right_idx = candidates.max(costs.len() - candidates) - 1;
        let mut q: BinaryHeap<(i64, i32)> = costs
            .iter()
            .take(left_idx)
            .map(|x| (-x as i64, 1))
            .chain(
                costs
                    .iter()
                    .rev()
                    .take(costs.len() - right_idx - 1)
                    .map(|x| (-x as i64, 0)),
            )
            .collect();
        (0..k)
            .into_iter()
            .scan(&mut q, |q, _| {
                if let Some((x, y)) = q.pop() {
                    if y == 0 {
                        if right_idx >= left_idx {
                            q.push((-costs[right_idx] as i64, 0));
                            right_idx -= 1;
                        }
                    } else {
                        if left_idx <= right_idx {
                            q.push((-costs[left_idx] as i64, 1));
                            left_idx += 1;
                        }
                    }
                    Some(-x)
                } else {
                    None
                }
            })
            .sum()
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::total_cost(e.0, e.1, e.2),
        vec![
            ((vec![17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4), 11),
            ((vec![1, 2, 4, 1], 3, 3), 4),
            ((vec![1, 1, 1], 2, 1), 2),
            (
                (
                    vec![
                        7, 31, 45, 82, 17, 41, 87, 63, 96, 75, 73, 82, 99, 27, 10, 4, 97,
                    ],
                    7,
                    1,
                ),
                310,
            ),
            (
                (vec![67, 13, 54, 96, 58, 81, 29, 72, 97, 67, 85], 9, 10),
                526,
            ),
            (
                (vec![79, 85, 37, 79, 93, 73, 49, 97, 45, 35, 55, 88], 6, 4),
                294,
            ),
            (
                (
                    vec![84, 8, 6, 85, 4, 63, 49, 96, 18, 69, 6, 24, 25, 21, 19, 69],
                    3,
                    3,
                ),
                18,
            ),
            ((vec![59, 94, 43, 27, 57, 53, 5, 71, 89, 8, 86], 3, 5), 40),
            (
                (
                    vec![
                        85, 5, 47, 59, 75, 83, 59, 30, 28, 78, 84, 41, 25, 61, 50, 87,
                    ],
                    6,
                    11,
                ),
                176,
            ),
            (
                (
                    vec![
                        19, 52, 99, 99, 1, 75, 1, 36, 54, 13, 12, 17, 38, 23, 21, 77, 10, 8, 46,
                        85, 38, 85,
                    ],
                    6,
                    7,
                ),
                52,
            ),
            (
                (
                    vec![
                        6, 43, 91, 22, 9, 41, 53, 36, 77, 96, 88, 8, 98, 31, 50, 39, 76,
                    ],
                    12,
                    12,
                ),
                414,
            ),
            (
                (
                    vec![
                        31, 96, 53, 75, 56, 44, 15, 43, 41, 43, 92, 82, 3, 23, 18, 2, 33, 90, 86,
                        38, 8, 62, 55, 17,
                    ],
                    4,
                    6,
                ),
                71,
            ),
            (
                (
                    vec![
                        38, 75, 37, 96, 64, 96, 78, 100, 68, 67, 79, 48, 51, 99, 32, 16, 39, 66, 10,
                    ],
                    12,
                    15,
                ),
                536,
            ),
            (
                (
                    vec![
                        45, 61, 1, 87, 21, 66, 53, 55, 71, 26, 44, 46, 100, 85, 97, 36, 24, 26, 21,
                        49, 84, 58,
                    ],
                    4,
                    6,
                ),
                67,
            ),
            (
                (
                    vec![
                        98, 74, 100, 79, 49, 2, 96, 50, 24, 32, 66, 45, 35, 47, 89, 21, 27, 62, 66,
                    ],
                    11,
                    10,
                ),
                394,
            ),
            (
                (
                    vec![
                        4, 60, 71, 99, 27, 64, 87, 59, 32, 47, 64, 40, 33, 74, 30, 62, 37, 97, 21,
                        37, 12, 18, 8, 18,
                    ],
                    9,
                    14,
                ),
                170,
            ),
        ],
        |a, b| a == b,
    )
}
