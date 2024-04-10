/*
 * @lc app=leetcode id=992 lang=rust
 *
 * [992] Subarrays with K Different Integers
 *
 * https://leetcode.com/problems/subarrays-with-k-different-integers/description/
 *
 * algorithms
 * Hard (56.43%)
 * Likes:    5657
 * Dislikes: 85
 * Total Accepted:    178.6K
 * Total Submissions: 289.9K
 * Testcase Example:  '[1,2,1,2,3]\n2'
 *
 * Given an integer array nums and an integer k, return the number of good
 * subarrays of nums.
 *
 * A good array is an array where the number of different integers in that
 * array is exactly k.
 *
 *
 * For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
 *
 *
 * A subarray is a contiguous part of an array.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,1,2,3], k = 2
 * Output: 7
 * Explanation: Subarrays formed with exactly 2 different integers: [1,2],
 * [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2,1,3,4], k = 3
 * Output: 3
 * Explanation: Subarrays formed with exactly 3 different integers:
 * [1,2,1,3], [2,1,3], [1,3,4].
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 2 * 10^4
 * 1 <= nums[i], k <= nums.length
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        let mut res = 0;
        let mut left = 0;
        let mut freqs: HashMap<i32, i32> = HashMap::new();
        let mut right = 0;
        let mut prev = 0;
        while right < nums.len() {
            *freqs.entry(nums[right]).or_default() += 1;
            match freqs.len().cmp(&(k as usize)) {
                std::cmp::Ordering::Equal => {
                    res += 1;
                }
                std::cmp::Ordering::Greater => {
                    while freqs.len() > (k as usize) {
                        *freqs.get_mut(&nums[left]).unwrap() -= 1;
                        if freqs[&nums[left]] == 0 {
                            freqs.remove(&nums[left]);
                        }
                        res += 1;
                        left += 1;
                    }
                }
                std::cmp::Ordering::Less => {}
            }
            right += 1;
        }
        loop {
            *freqs.get_mut(&nums[left]).unwrap() -= 1;
            if freqs[&nums[left]] == 0 {
                freqs.remove(&nums[left]);
            }
            if freqs.len() != (k as usize) {
                break;
            }
            res += 1;
            left += 1;
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::subarrays_with_k_distinct(e.0, e.1),
        vec![
            //
            ((vec![1, 2, 1, 2, 3], 2), 7),
            ((vec![1, 2, 1, 3, 4], 3), 3),
        ],
        |a, b| a == b,
    )
}
