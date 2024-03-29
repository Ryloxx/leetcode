/*
 * @lc app=leetcode id=2962 lang=rust
 *
 * [2962] Count Subarrays Where Max Element Appears at Least K Times
 *
 * https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
 *
 * algorithms
 * Medium (44.90%)
 * Likes:    901
 * Dislikes: 42
 * Total Accepted:    86.7K
 * Total Submissions: 150.6K
 * Testcase Example:  '[1,3,2,3,3]\n2'
 *
 * You are given an integer array nums and a positive integer k.
 *
 * Return the number of subarrays where the maximum element of nums appears
 * at least k times in that subarray.
 *
 * A subarray is a contiguous sequence of elements within an array.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,3,2,3,3], k = 2
 * Output: 6
 * Explanation: The subarrays that contain the element 3 at least 2 times
 * are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,4,2,1], k = 3
 * Output: 0
 * Explanation: No subarray contains the element 4 at least 3 times.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^6
 * 1 <= k <= 10^5
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let mut res = 0i64;
        let n = nums.len();
        let max = nums.iter().copied().max().unwrap_or_default();
        let mut q = vec![!0];
        let mut left = 0;
        for (right, num) in nums.iter().enumerate() {
            if *num == max {
                q.push(right);
                if q.len() - left > k as usize {
                    res += ((n - q.last().unwrap()) * (q[left + 1].wrapping_sub(q[left]))) as i64;
                    left += 1;
                }
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::count_subarrays(e.0, e.1),
        vec![
            ((vec![1, 3, 2, 3, 3], 2), 6),
            ((vec![1, 4, 2, 1], 3), 0),
            ((vec![1], 1), 1),
            ((vec![1, 1, 1, 1], 1), 10),
            (
                (
                    vec![
                        61, 23, 38, 23, 56, 40, 82, 56, 82, 82, 82, 70, 8, 69, 8, 7, 19, 14, 58,
                        42, 82, 10, 82, 78, 15, 82,
                    ],
                    2,
                ),
                224,
            ),
        ],
        |a, b| a == b,
    )
}
