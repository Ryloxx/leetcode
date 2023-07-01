/*
 * @lc app=leetcode id=2305 lang=rust
 *
 * [2305] Fair Distribution of Cookies
 *
 * https://leetcode.com/problems/fair-distribution-of-cookies/description/
 *
 * algorithms
 * Medium (62.43%)
 * Likes:    1781
 * Dislikes: 73
 * Total Accepted:    55.6K
 * Total Submissions: 80.9K
 * Testcase Example:  '[8,15,10,20,8]\n2'
 *
 * You are given an integer array cookies, where cookies[i] denotes the
 * number of cookies in the i^th bag. You are also given an integer k that
 * denotes the number of children to distribute all the bags of cookies to.
 * All the cookies in the same bag must go to the same child and cannot be
 * split up.
 *
 * The unfairness of a distribution is defined as the maximum total cookies
 * obtained by a single child in the distribution.
 *
 * Return the minimum unfairness of all distributions.
 *
 *
 * Example 1:
 *
 *
 * Input: cookies = [8,15,10,20,8], k = 2
 * Output: 31
 * Explanation: One optimal distribution is [8,15,8] and [10,20]
 * - The 1^st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31
 * cookies.
 * - The 2^nd child receives [10,20] which has a total of 10 + 20 = 30
 *   cookies.
 * The unfairness of the distribution is max(31,30) = 31.
 * It can be shown that there is no distribution with an unfairness less than
 * 31.
 *
 *
 * Example 2:
 *
 *
 * Input: cookies = [6,1,3,2,2,4,1,2], k = 3
 * Output: 7
 * Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
 * - The 1^st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
 * - The 2^nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7
 * cookies.
 * - The 3^rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7
 * cookies.
 * The unfairness of the distribution is max(7,7,7) = 7.
 * It can be shown that there is no distribution with an unfairness less than
 * 7.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= cookies.length <= 8
 * 1 <= cookies[i] <= 10^5
 * 2 <= k <= cookies.length
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn distribute_cookies(cookies: Vec<i32>, k: i32) -> i32 {
        let res = &mut i32::MAX.clone();
        fn distribute(
            current_bag: usize,
            distribution: &mut Vec<i32>,
            served_children: u32,
            curr_max: i32,
            avg: i32,
            cookies: &Vec<i32>,
            res: &mut i32,
        ) {
            if current_bag == cookies.len() {
                *res = (*res).min(curr_max);
                return;
            }
            if distribution.len() - served_children.count_ones() as usize
                > cookies.len() - current_bag
                || curr_max >= *res
            {
                return;
            }
            for j in 0..distribution.len() {
                if distribution[j] <= avg {
                    distribution[j] += cookies[current_bag];
                    distribute(
                        current_bag + 1,
                        distribution,
                        served_children | 1 << j,
                        curr_max.max(distribution[j]),
                        avg,
                        cookies,
                        res,
                    );
                    distribution[j] -= cookies[current_bag];
                }
            }
        }
        distribute(
            0,
            &mut vec![0; k as usize],
            0,
            0,
            (cookies.iter().sum::<i32>() + 1) / k,
            &cookies,
            res,
        );
        *res
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::distribute_cookies(e.0, e.1),
        vec![
            //
            ((vec![8, 15, 10, 20, 8], 2), 31),
            ((vec![6, 1, 3, 2, 2, 4, 1, 2], 3), 7),
            (
                (
                    vec![76265, 7826, 16834, 63341, 68901, 58882, 50651, 75609],
                    8,
                ),
                76265,
            ),
        ],
        |a, b| a == b,
    );
}
