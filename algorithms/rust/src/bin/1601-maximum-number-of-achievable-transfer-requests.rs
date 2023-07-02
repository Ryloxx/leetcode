/*
 * @lc app=leetcode id=1601 lang=rust
 *
 * [1601] Maximum Number of Achievable Transfer Requests
 *
 * https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/
 *
 * algorithms
 * Hard (51.18%)
 * Likes:    899
 * Dislikes: 54
 * Total Accepted:    31.7K
 * Total Submissions: 51.1K
 * Testcase Example:  '5\n[[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]'
 *
 * We have n buildings numbered from 0 to n - 1. Each building has a number
 * of employees. It's transfer season, and some employees want to change the
 * building they reside in.
 *
 * You are given an array requests where requests[i] = [fromi, toi]
 * represents an employee's request to transfer from building fromi to
 * building toi.
 *
 * All buildings are full, so a list of requests is achievable only if for
 * each building, the net change in employee transfers is zero. This means
 * the number of employees leaving is equal to the number of employees moving
 * in. For example if n = 3 and two employees are leaving building 0, one is
 * leaving building 1, and one is leaving building 2, there should be two
 * employees moving to building 0, one employee moving to building 1, and one
 * employee moving to building 2.
 *
 * Return the maximum number of achievable requests.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
 * Output: 5
 * Explantion: Let's see the requests:
 * From building 0 we have employees x and y and both want to move to
 * building 1.
 * From building 1 we have employees a and b and they want to move to
 * buildings 2 and 0 respectively.
 * From building 2 we have employee z and they want to move to building 0.
 * From building 3 we have employee c and they want to move to building 4.
 * From building 4 we don't have any requests.
 * We can achieve the requests of users x and b by swapping their places.
 * We can achieve the requests of users y, a and z by swapping the places in
 * the 3 buildings.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 3, requests = [[0,0],[1,2],[2,1]]
 * Output: 3
 * Explantion: Let's see the requests:
 * From building 0 we have employee x and they want to stay in the same
 * building 0.
 * From building 1 we have employee y and they want to move to building 2.
 * From building 2 we have employee z and they want to move to building 1.
 * We can achieve all the requests.
 *
 * Example 3:
 *
 *
 * Input: n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
 * Output: 4
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 20
 * 1 <= requests.length <= 16
 * requests[i].length == 2
 * 0 <= fromi, toi < n
 *
 *
 */
struct Solution;

// @lc code=start
impl Solution {
    pub fn maximum_requests(n: i32, requests: Vec<Vec<i32>>) -> i32 {
        let mut buildings = vec![0; n as usize];
        let mut res = 0i32;
        for state in 0i32..1 << requests.len() {
            let ones = state.count_ones() as i32;
            if ones <= res {
                continue;
            }
            for i in 0..requests.len() {
                if 1 << i & state != 0 {
                    let from = requests[i][0] as usize;
                    let to = requests[i][1] as usize;
                    buildings[from] -= 1;
                    buildings[to] += 1;
                }
            }
            let mut good = true;
            for i in buildings.iter_mut() {
                if *i != 0 {
                    good = false;
                }
                *i = 0;
            }
            if good {
                res = ones;
            }
        }
        res
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::maximum_requests(e.0, e.1),
        vec![
            (
                (
                    5,
                    vec![
                        vec![0, 1],
                        vec![1, 0],
                        vec![0, 1],
                        vec![1, 2],
                        vec![2, 0],
                        vec![3, 4],
                    ],
                ),
                5,
            ),
            ((3, vec![vec![0, 0], vec![1, 2], vec![2, 1]]), 3),
            ((4, vec![vec![0, 3], vec![3, 1], vec![1, 2], vec![2, 0]]), 4),
            (
                (
                    20,
                    vec![
                        vec![0, 3],
                        vec![3, 1],
                        vec![1, 2],
                        vec![2, 0],
                        vec![0, 3],
                        vec![3, 1],
                        vec![1, 2],
                        vec![2, 0],
                        vec![0, 3],
                        vec![3, 1],
                        vec![1, 2],
                        vec![2, 0],
                        vec![0, 3],
                        vec![3, 1],
                        vec![1, 2],
                        vec![2, 0],
                    ],
                ),
                16,
            ),
            (
                (
                    3,
                    vec![
                        vec![1, 2],
                        vec![2, 2],
                        vec![0, 0],
                        vec![1, 1],
                        vec![0, 2],
                        vec![0, 0],
                        vec![2, 1],
                        vec![0, 1],
                        vec![1, 0],
                        vec![2, 2],
                        vec![0, 1],
                        vec![2, 0],
                        vec![2, 2],
                    ],
                ),
                12,
            ),
        ],
        |a, b| a == b,
    );
}
