/*
 * @lc app=leetcode id=1248 lang=rust
 *
 * [1248] Count Number of Nice Subarrays
 *
 * https://leetcode.com/problems/count-number-of-nice-subarrays/description/
 *
 * algorithms
 * Medium (65.28%)
 * Likes:    3906
 * Dislikes: 84
 * Total Accepted:    148.3K
 * Total Submissions: 221.7K
 * Testcase Example:  '[1,1,2,1,1]\n3'
 *
 * Given an array of integers nums and an integer k. A continuous subarray is
 * called nice if there are k odd numbers on it.
 *
 * Return the number of nice sub-arrays.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,1,2,1,1], k = 3
 * Output: 2
 * Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and
 * [1,2,1,1].
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [2,4,6], k = 1
 * Output: 0
 * Explanation: There are no odd numbers in the array.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
 * Output: 16
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 50000
 * 1 <= nums[i] <= 10^5
 * 1 <= k <= nums.length
 *
 *
 */

struct Solution;

// @lc code=start
impl Solution {
    pub fn number_of_subarrays(nums: Vec<i32>, mut k: i32) -> i32 {
        let mut left = 0;
        let mut prefix_length = 0;
        nums.iter()
            .map(|num| {
                k -= num & 1;
                if k == 0 {
                    prefix_length = 0;
                    while k == 0 {
                        k += nums[left] & 1;
                        prefix_length += 1;
                        left += 1;
                    }
                }
                prefix_length
            })
            .sum()
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::number_of_subarrays(e.0, e.1),
        vec![
            ((vec![1, 1, 2, 1, 1], 3), 2),
            ((vec![2, 4, 6], 1), 0),
            ((vec![2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2), 16),
            ((vec![2, 2, 1, 2, 2, 1, 2], 2), 6),
        ],
        |a, b| a == b,
    )
}
