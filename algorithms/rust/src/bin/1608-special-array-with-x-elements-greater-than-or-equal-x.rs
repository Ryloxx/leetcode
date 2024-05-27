/*
 * @lc app=leetcode id=1608 lang=rust
 *
 * [1608] Special Array With X Elements Greater Than or Equal X
 *
 * https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/
 *
 * algorithms
 * Easy (60.14%)
 * Likes:    1881
 * Dislikes: 329
 * Total Accepted:    127.1K
 * Total Submissions: 198.4K
 * Testcase Example:  '[3,5]'
 *
 * You are given an array nums of non-negative integers. nums is considered
 * special if there exists a number x such that there are exactly x numbers
 * in nums that are greater than or equal to x.
 *
 * Notice that x does not have to be an element in nums.
 *
 * Return x if the array is special, otherwise, return -1. It can be proven
 * that if nums is special, the value for x is unique.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [3,5]
 * Output: 2
 * Explanation: There are 2 values (3 and 5) that are greater than or equal
 * to 2.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [0,0]
 * Output: -1
 * Explanation: No numbers fit the criteria for x.
 * If x = 0, there should be 0 numbers >= x, but there are 2.
 * If x = 1, there should be 1 number >= x, but there are 0.
 * If x = 2, there should be 2 numbers >= x, but there are 0.
 * x cannot be greater since there are only 2 numbers in nums.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [0,4,3,0,4]
 * Output: 3
 * Explanation: There are 3 values that are greater than or equal to 3.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 100
 * 0 <= nums[i] <= 1000
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn special_array(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut freqs = vec![0; n + 1];
        for i in nums {
            freqs[n.min(i as usize)] += 1;
        }
        let mut res = 0;
        for (i, j) in freqs.into_iter().enumerate().rev() {
            res += j;
            if i == res {
                return res as i32;
            }
        }
        -1
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::special_array,
        vec![
            ((vec![3, 5]), 2),
            ((vec![0, 0]), -1),
            ((vec![0, 4, 3, 0, 4]), 3),
            ((vec![1000; 1000]), 1000),
        ],
        |a, b| a == b,
    )
}
