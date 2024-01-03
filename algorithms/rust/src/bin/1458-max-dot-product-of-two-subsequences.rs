/*
 * @lc app=leetcode id=1458 lang=rust
 *
 * [1458] Max Dot Product of Two Subsequences
 *
 * https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/
 *
 * algorithms
 * Hard (47.36%)
 * Likes:    1494
 * Dislikes: 31
 * Total Accepted:    69.6K
 * Total Submissions: 111.2K
 * Testcase Example:  '[2,1,-2,5]\n[3,0,-6]'
 *
 * Given two arrays nums1 and nums2.
 *
 * Return the maximum dot product between non-empty subsequences of nums1 and
 * nums2 with the same length.
 *
 * A subsequence of a array is a new array which is formed from the original
 * array by deleting some (can be none) of the characters without disturbing
 * the relative positions of the remaining characters. (ie, [2,3,5] is a
 * subsequence of [1,2,3,4,5] while [1,5,3] is not).
 *
 *
 * Example 1:
 *
 *
 * Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
 * Output: 18
 * Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6]
 * from nums2.
 * Their dot product is (2*3 + (-2)*(-6)) = 18.
 *
 * Example 2:
 *
 *
 * Input: nums1 = [3,-2], nums2 = [2,-6,7]
 * Output: 21
 * Explanation: Take subsequence [3] from nums1 and subsequence [7] from
 * nums2. Their dot product is (3*7) = 21.
 *
 * Example 3:
 *
 *
 * Input: nums1 = [-1,-1], nums2 = [1,1]
 * Output: -1
 * Explanation: Take subsequence [-1] from nums1 and subsequence [1] from
 * nums2.
 * Their dot product is -1.
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums1.length, nums2.length <= 500
 * -1000 <= nums1[i], nums2[i] <= 1000
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        const MIN_DOT_PRODUCT: i32 = -(500 * 500 * 500 + 1);
        fn dp(
            i: u16,
            j: u16,
            is_empty: bool,
            nums1: &Vec<i32>,
            nums2: &Vec<i32>,
            memo: &mut HashMap<u32, i32>,
        ) -> i32 {
            if i as usize >= nums1.len() || j as usize >= nums2.len() {
                return if is_empty { MIN_DOT_PRODUCT } else { 0 };
            }
            let key = (is_empty as u32) << 31 | (i as u32) << 16 | j as u32;
            if let Some(memo) = memo.get(&key) {
                return *memo;
            }
            let res = (dp(i + 1, j + 1, false, nums1, nums2, memo)
                + nums1[i as usize] * nums2[j as usize])
                .max(dp(i + 1, j, is_empty, nums1, nums2, memo))
                .max(dp(i, j + 1, is_empty, nums1, nums2, memo));
            memo.insert(key, res);
            res
        }
        dp(0, 0, true, &nums1, &nums2, &mut HashMap::new())
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::max_dot_product(e.0, e.1),
        vec![
            ((vec![2, 1, -2, 5], vec![3, 0, -6]), 18),
            ((vec![3, -2], vec![2, -6, 7]), 21),
            ((vec![-1, -1], vec![1, 1]), -1),
            ((vec![-1], vec![1]), -1),
            ((vec![1], vec![1]), 1),
            ((vec![1], vec![-1]), -1),
            ((vec![-1], vec![-1]), 1),
        ],
        |a, b| a == b,
    );
}
