/*
 * @lc app=leetcode id=1512 lang=rust
 *
 * [1512] Number of Good Pairs
 *
 * https://leetcode.com/problems/number-of-good-pairs/description/
 *
 * algorithms
 * Easy (88.25%)
 * Likes:    4386
 * Dislikes: 206
 * Total Accepted:    514K
 * Total Submissions: 581.7K
 * Testcase Example:  '[1,2,3,1,1,3]'
 *
 * Given an array of integers nums, return the number of good pairs.
 *
 * A pair (i, j) is called good if nums[i] == nums[j] and i < j.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,3,1,1,3]
 * Output: 4
 * Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,1,1,1]
 * Output: 6
 * Explanation: Each pair in the array are good.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [1,2,3]
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 100
 * 1 <= nums[i] <= 100
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        let mut seen = [0i8; 101];
        let mut res = 0i32;
        for n in nums.into_iter() {
            res += seen[n as usize] as i32;
            seen[n as usize] += 1;
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::num_identical_pairs,
        vec![
            ((vec![1, 2, 3, 1, 1, 3]), 4),
            ((vec![1, 1, 1, 1]), 6),
            ((vec![1, 2, 3]), 0),
            (
                (vec![
                    7, 1, 5, 7, 8, 5, 6, 8, 4, 7, 2, 7, 3, 3, 5, 7, 2, 2, 2, 7, 2, 4, 7, 3, 1, 2,
                    7, 7, 5, 6, 6, 1, 8, 5, 4, 7, 6, 1, 4, 7, 7, 6, 5, 2, 2, 4, 5, 2, 2,
                ]),
                164,
            ),
        ],
        |a, b| a == b,
    );
}
