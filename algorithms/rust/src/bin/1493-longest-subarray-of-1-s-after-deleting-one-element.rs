/*
 * @lc app=leetcode id=1493 lang=rust
 *
 * [1493] Longest Subarray of 1's After Deleting One Element
 *
 * https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
 *
 * algorithms
 * Medium (60.19%)
 * Likes:    1730
 * Dislikes: 32
 * Total Accepted:    76.6K
 * Total Submissions: 123.3K
 * Testcase Example:  '[1,1,0,1]'
 *
 * Given a binary array nums, you should delete one element from it.
 *
 * Return the size of the longest non-empty subarray containing only 1's in
 * the resulting array. Return 0 if there is no such subarray.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,1,0,1]
 * Output: 3
 * Explanation: After deleting the number in position 2, [1,1,1] contains 3
 * numbers with value of 1's.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [0,1,1,1,0,1,1,0,1]
 * Output: 5
 * Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1]
 * longest subarray with value of 1's is [1,1,1,1,1].
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [1,1,1]
 * Output: 2
 * Explanation: You must delete one element.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * nums[i] is either 0 or 1.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn longest_subarray(mut nums: Vec<i32>) -> i32 {
        nums.push(0);
        let mut curr = 0;
        let mut pair = [0, 0];
        let mut flag = false;
        let mut res = 0;
        for i in 0..nums.len() {
            if nums[i] == 0 {
                if flag {
                    res = res.max(pair[0] + pair[1]);
                }
                flag = i > 0 && i < nums.len() - 1 && nums[i - 1] == 1 && nums[i + 1] == 1;
                curr += 1;
                pair[curr % 2] = 0;
            } else {
                pair[curr % 2] += 1;
                res = res.max(pair[curr % 2]);
            }
        }
        res.clamp(0, nums.len() as i32 - 2)
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::longest_subarray,
        vec![
            ((vec![1, 1, 0, 1]), 3),
            ((vec![0, 1, 1, 1, 0, 1, 1, 0, 1]), 5),
            ((vec![1, 1, 1]), 2),
            ((vec![1, 1, 0, 0, 1]), 2),
            ((vec![1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]), 6),
            ((vec![1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1]), 5),
            ((vec![1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1]), 4),
            ((vec![0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1]), 5),
            ((vec![0]), 0),
            ((vec![1]), 0),
        ],
        |a, b| a == b,
    );
}
