/*
 * @lc app=leetcode id=1481 lang=rust
 *
 * [1481] Least Number of Unique Integers after K Removals
 *
 * https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/
 *
 * algorithms
 * Medium (55.99%)
 * Likes:    1971
 * Dislikes: 199
 * Total Accepted:    184.4K
 * Total Submissions: 302.3K
 * Testcase Example:  '[5,5,4]\n1'
 *
 * Given an array of integers arr and an integer k. Find the least number of
 * unique integers after removing exactly k elements.
 *
 *
 *
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [5,5,4], k = 1
 * Output: 1
 * Explanation: Remove the single 4, only 5 is left.
 *
 * Example 2:
 *
 *
 * Input: arr = [4,3,1,1,3,3,2], k = 3
 * Output: 2
 * Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3
 * will be left.
 *
 *
 * Constraints:
 *
 *
 * 1 <= arr.length <= 10^5
 * 1 <= arr[i] <= 10^9
 * 0 <= k <= arr.length
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, mut k: i32) -> i32 {
        let freqs = arr
            .into_iter()
            .fold(HashMap::<i32, i32>::new(), |mut acc, curr| {
                *acc.entry(curr).or_default() += 1;
                acc
            });
        let mut unique = freqs.len() as i32;
        let mut cnt = vec![];
        for freq in freqs.into_values() {
            if cnt.len() <= freq as usize {
                cnt.resize(freq as usize + 1, 0);
            }
            cnt[freq as usize] += 1;
        }
        for (freq, cnt) in cnt.into_iter().enumerate().filter(|(_, x)| *x > 0) {
            let freq = freq as i32;
            let diff = (k / freq).min(cnt);
            k -= freq * diff;
            unique -= diff;
            if freq >= k {
                break;
            }
        }
        unique
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::find_least_num_of_unique_ints(e.0, e.1),
        vec![
            ((vec![5, 5, 4], 1), 1),
            ((vec![4, 3, 1, 1, 3, 3, 2], 3), 2),
            ((vec![2, 1, 1, 3, 3, 3], 3), 1),
            ((vec![2, 4, 1, 8, 3, 5, 1, 3], 3), 3),
        ],
        |a, b| a == b,
    )
}
