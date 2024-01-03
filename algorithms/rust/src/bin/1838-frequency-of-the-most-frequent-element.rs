/*
 * @lc app=leetcode id=1838 lang=rust
 *
 * [1838] Frequency of the Most Frequent Element
 *
 * https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
 *
 * algorithms
 * Medium (39.83%)
 * Likes:    3378
 * Dislikes: 107
 * Total Accepted:    74K
 * Total Submissions: 174.2K
 * Testcase Example:  '[1,2,4]\n5'
 *
 * The frequency of an element is the number of times it occurs in an array.
 *
 * You are given an integer array nums and an integer k. In one operation,
 * you can choose an index of nums and increment the element at that index by
 * 1.
 *
 * Return the maximum possible frequency of an element after performing at
 * most k operations.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,4], k = 5
 * Output: 3
 * Explanation: Increment the first element three times and the second
 * element two times to make nums = [4,4,4].
 * 4 has a frequency of 3.
 *
 * Example 2:
 *
 *
 * Input: nums = [1,4,8,13], k = 5
 * Output: 2
 * Explanation: There are multiple optimal solutions:
 * - Increment the first element three times to make nums = [4,4,8,13]. 4 has
 *   a
 * frequency of 2.
 * - Increment the second element four times to make nums = [1,8,8,13]. 8 has
 *   a
 * frequency of 2.
 * - Increment the third element five times to make nums = [1,4,13,13]. 13
 *   has
 * a frequency of 2.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [3,9,6], k = 2
 * Output: 1
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^5
 * 1 <= k <= 10^5
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn max_frequency(mut nums: Vec<i32>, k: i32) -> i32 {
        nums.sort_unstable();
        let mut j = 0;
        let mut s = 0;
        for (i, n) in nums.iter().enumerate() {
            s += n;
            if (i - j + 1) as i32 * n - s > k {
                s -= nums[j];
                j += 1;
            }
        }
        (nums.len() - j) as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::max_frequency(e.0, e.1),
        vec![
            ((vec![1, 2, 4], 5), 3),
            ((vec![1, 4, 8, 13], 5), 2),
            ((vec![3, 9, 6], 2), 1),
            ((vec![1, 4, 8, 13, 18], 15), 3),
            ((vec![3, 9, 6], 0), 1),
            ((vec![3], 10), 1),
            ((vec![3], 0), 1),
            ((vec![], 0), 0),
            ((vec![], 10), 0),
            ((std::iter::repeat(13).take(10_000).collect(), 0), 10_000),
            ((std::iter::repeat(13).take(10_000).collect(), 10), 10_000),
        ],
        |a, b| a == b,
    );
}
