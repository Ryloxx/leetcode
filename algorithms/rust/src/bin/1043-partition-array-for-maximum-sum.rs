/*
 * @lc app=leetcode id=1043 lang=rust
 *
 * [1043] Partition Array for Maximum Sum
 *
 * https://leetcode.com/problems/partition-array-for-maximum-sum/description/
 *
 * algorithms
 * Medium (72.28%)
 * Likes:    4462
 * Dislikes: 384
 * Total Accepted:    166.6K
 * Total Submissions: 217.7K
 * Testcase Example:  '[1,15,7,9,2,5,10]\n3'
 *
 * Given an integer array arr, partition the array into (contiguous)
 * subarrays of length at most k. After partitioning, each subarray has their
 * values changed to become the maximum value of that subarray.
 *
 * Return the largest sum of the given array after partitioning. Test cases
 * are generated so that the answer fits in a 32-bit integer.
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [1,15,7,9,2,5,10], k = 3
 * Output: 84
 * Explanation: arr becomes [15,15,15,9,10,10,10]
 *
 *
 * Example 2:
 *
 *
 * Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
 * Output: 83
 *
 *
 * Example 3:
 *
 *
 * Input: arr = [1], k = 1
 * Output: 1
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= arr.length <= 500
 * 0 <= arr[i] <= 10^9
 * 1 <= k <= arr.length
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn max_sum_after_partitioning(arr: Vec<i32>, k: i32) -> i32 {
        let mut dp = vec![0; arr.len() + 1];
        for i in 0..arr.len() {
            dp[i + 1] = (0..(k as usize).min(i + 1))
                .fold((0, 0), |mut acc, j| {
                    acc.0 = acc.0.max(arr[i - j]);
                    acc.1 = acc.1.max(acc.0 * (j as i32 + 1) + dp[i - j]);
                    acc
                })
                .1;
        }
        *dp.last().unwrap()
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::max_sum_after_partitioning(e.0, e.1),
        vec![
            ((vec![1, 15, 7, 9, 2, 5, 10], 3), 84),
            ((vec![1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4), 83),
            ((vec![1], 1), 1),
        ],
        |a, b| a == b,
    )
}
