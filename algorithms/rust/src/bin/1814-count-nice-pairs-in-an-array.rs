/*
 * @lc app=leetcode id=1814 lang=rust
 *
 * [1814] Count Nice Pairs in an Array
 *
 * https://leetcode.com/problems/count-nice-pairs-in-an-array/description/
 *
 * algorithms
 * Medium (41.85%)
 * Likes:    1219
 * Dislikes: 52
 * Total Accepted:    56K
 * Total Submissions: 118.9K
 * Testcase Example:  '[42,11,1,97]'
 *
 * You are given an array nums that consists of non-negative integers. Let us
 * define rev(x) as the reverse of the non-negative integer x. For example,
 * rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it
 * satisfies all of the following conditions:
 *
 *
 * 0 <= i < j < nums.length
 * nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
 *
 *
 * Return the number of nice pairs of indices. Since that number can be too
 * large, return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [42,11,1,97]
 * Output: 2
 * Explanation: The two pairs are:
 * ⁠- (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 * ⁠- (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [13,10,35,24,76]
 * Output: 4
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * 0 <= nums[i] <= 10^9
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn count_nice_pairs(nums: Vec<i32>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut res = 0;
        let mut seen = HashMap::new();
        for j in nums.into_iter() {
            let diff = {
                let mut num = j;
                let mut ret = 0;
                while num > 0 {
                    ret = (ret * 10) + num % 10;
                    num /= 10;
                }
                ret - j
            };
            let entry = seen.entry(diff).or_insert(0);
            res += *entry;
            res %= MOD;
            *entry += 1;
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::count_nice_pairs,
        vec![
            ((vec![42, 11, 1, 97]), 2),
            ((vec![13, 10, 35, 24, 76]), 4),
            ((vec![1; 100_000]), 999949972),
        ],
        |a, b| a == b,
    );
}
