/*
 * @lc app=leetcode id=2149 lang=rust
 *
 * [2149] Rearrange Array Elements by Sign
 *
 * https://leetcode.com/problems/rearrange-array-elements-by-sign/description/
 *
 * algorithms
 * Medium (81.94%)
 * Likes:    2827
 * Dislikes: 146
 * Total Accepted:    243.4K
 * Total Submissions: 291K
 * Testcase Example:  '[3,1,-2,-5,2,-4]'
 *
 * You are given a 0-indexed integer array nums of even length consisting of
 * an equal number of positive and negative integers.
 *
 * You should rearrange the elements of nums such that the modified array
 * follows the given conditions:
 *
 *
 * Every consecutive pair of integers have opposite signs.
 * For all integers with the same sign, the order in which they were present
 * in nums is preserved.
 * The rearranged array begins with a positive integer.
 *
 *
 * Return the modified array after rearranging the elements to satisfy the
 * aforementioned conditions.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [3,1,-2,-5,2,-4]
 * Output: [3,-2,1,-5,2,-4]
 * Explanation:
 * The positive integers in nums are [3,1,2]. The negative integers are
 * [-2,-5,-4].
 * The only possible way to rearrange them such that they satisfy all
 * conditions is [3,-2,1,-5,2,-4].
 * Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2]
 * are incorrect because they do not satisfy one or more conditions.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [-1,1]
 * Output: [1,-1]
 * Explanation:
 * 1 is the only positive integer and -1 the only negative integer in nums.
 * So nums is rearranged to [1,-1].
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= nums.length <= 2 * 10^5
 * nums.length is even
 * 1 <= |nums[i]| <= 10^5
 * nums consists of equal number of positive and negative integers.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn rearrange_array(nums: Vec<i32>) -> Vec<i32> {
        let mut res = vec![0; nums.len()];
        let mut i = 0;
        let mut j = 1;
        for n in nums.into_iter() {
            if n > 0 {
                res[i] = n;
                i += 2;
            } else {
                res[j] = n;
                j += 2;
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::rearrange_array,
        vec![
            ((vec![3, 1, -2, -5, 2, -4]), vec![3, -2, 1, -5, 2, -4]),
            ((vec![-1, 1]), vec![1, -1]),
        ],
        |a, b| a == b,
    )
}
