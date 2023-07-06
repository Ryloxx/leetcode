/*
 * @lc app=leetcode id=209 lang=rust
 *
 * [209] Minimum Size Subarray Sum
 *
 * https://leetcode.com/problems/minimum-size-subarray-sum/description/
 *
 * algorithms
 * Medium (44.63%)
 * Likes:    9834
 * Dislikes: 280
 * Total Accepted:    727K
 * Total Submissions: 1.6M
 * Testcase Example:  '7\n[2,3,1,2,4,3]'
 *
 * Given an array of positive integers nums and a positive integer target,
 * return the minimal length of a subarray whose sum is greater than or equal
 * to target. If there is no such subarray, return 0 instead.
 *
 *
 * Example 1:
 *
 *
 * Input: target = 7, nums = [2,3,1,2,4,3]
 * Output: 2
 * Explanation: The subarray [4,3] has the minimal length under the problem
 * constraint.
 *
 *
 * Example 2:
 *
 *
 * Input: target = 4, nums = [1,4,4]
 * Output: 1
 *
 *
 * Example 3:
 *
 *
 * Input: target = 11, nums = [1,1,1,1,1,1,1,1]
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= target <= 10^9
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^4
 *
 *
 *
 * Follow up: If you have figured out the O(n) solution, try coding another
 * solution of which the time complexity is O(n log(n)).
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut s = 0;
        let mut res = nums.len() + 1;
        let mut left = 0;
        let mut right = 0;
        while left < nums.len() {
            while right < nums.len() && s < target {
                s += nums[right];
                right += 1;
            }
            if s >= target {
                res = res.min(right - left);
            }
            s -= nums[left];
            left += 1;
        }
        (res % (nums.len() + 1)) as i32
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::min_sub_array_len(e.0, e.1),
        vec![
            ((7, vec![2, 3, 1, 2, 4, 3]), 2),
            ((4, vec![1, 4, 4]), 1),
            ((11, vec![1, 1, 1, 1, 1, 1, 1, 1]), 0),
            ((5, vec![1, 1, 1, 1, 1, 3, 2]), 2),
            ((15, vec![1, 2, 3, 4, 5]), 5),
            ((7, vec![5]), 0),
            ((11, vec![1, 2, 3, 4, 5]), 3),
        ],
        |a, b| a == b,
    );
}
