/*
 * @lc app=leetcode id=300 lang=rust
 *
 * [300] Longest Increasing Subsequence
 *
 * https://leetcode.com/problems/longest-increasing-subsequence/description/
 *
 * algorithms
 * Medium (53.64%)
 * Likes:    19832
 * Dislikes: 395
 * Total Accepted:    1.5M
 * Total Submissions: 2.7M
 * Testcase Example:  '[10,9,2,5,3,7,101,18]'
 *
 * Given an integer array nums, return the length of the longest strictly
 * increasing subsequence.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [10,9,2,5,3,7,101,18]
 * Output: 4
 * Explanation: The longest increasing subsequence is [2,3,7,101], therefore
 * the length is 4.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [0,1,0,3,2,3]
 * Output: 4
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [7,7,7,7,7,7,7]
 * Output: 1
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 2500
 * -10^4 <= nums[i] <= 10^4
 *
 *
 *
 * Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
 * complexity?
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut seq = vec![];
        for n1 in nums {
            let p = seq.partition_point(|&n2| n2 < n1);
            if p >= seq.len() {
                seq.push(p as i32);
            }
            seq[p] = n1;
        }
        seq.len() as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::length_of_lis,
        vec![
            //
            (vec![10, 9, 2, 5, 3, 7, 101, 18], 4),
            (vec![0, 1, 0, 3, 2, 3], 4),
            (vec![7, 7, 7, 7, 7, 7, 7], 1),
            ((0..2500).collect(), 2500),
        ],
        |a, b| a == b,
    )
}
