/*
 * @lc app=leetcode id=1035 lang=rust
 *
 * [1035] Uncrossed Lines
 *
 * https://leetcode.com/problems/uncrossed-lines/description/
 *
 * algorithms
 * Medium (58.81%)
 * Likes:    2962
 * Dislikes: 37
 * Total Accepted:    108.5K
 * Total Submissions: 177.9K
 * Testcase Example:  '[1,4,2]\n[1,2,4]'
 *
 * You are given two integer arrays nums1 and nums2. We write the integers of
 * nums1 and nums2 (in the order they are given) on two separate horizontal
 * lines.
 *
 * We may draw connecting lines: a straight line connecting two numbers
 * nums1[i] and nums2[j] such that:
 *
 *
 * nums1[i] == nums2[j], and
 * the line we draw does not intersect any other connecting (non-horizontal)
 * line.
 *
 *
 * Note that a connecting line cannot intersect even at the endpoints (i.e.,
 * each number can only belong to one connecting line).
 *
 * Return the maximum number of connecting lines we can draw in this way.
 *
 *
 * Example 1:
 *
 *
 * Input: nums1 = [1,4,2], nums2 = [1,2,4]
 * Output: 2
 * Explanation: We can draw 2 uncrossed lines as in the diagram.
 * We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to
 * nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
 *
 *
 * Example 2:
 *
 *
 * Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
 * Output: 3
 *
 *
 * Example 3:
 *
 *
 * Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
 * Output: 2
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums1.length, nums2.length <= 500
 * 1 <= nums1[i], nums2[j] <= 2000
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn max_uncrossed_lines(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut nums1 = nums1;
        let mut nums2 = nums2;
        if nums1.len() < nums2.len() {
            std::mem::swap(&mut nums1, &mut nums2);
        }
        let mut dp = vec![0; nums2.len() + 3];
        let n = nums2.len();
        for n1 in nums1.iter() {
            dp[n + 1] = 0;
            for j in 1..(n + 1) {
                dp[n + 2] = dp[j];
                dp[j] = dp[j].max(dp[j - 1]);
                if *n1 == nums2[j - 1] {
                    dp[j] = dp[j].max(dp[n + 1] + 1);
                }
                dp[n + 1] = dp[n + 2];
            }
        }
        dp[n]
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::max_uncrossed_lines(e.0, e.1),
        vec![
            ((vec![1, 4, 2], vec![1, 2, 4]), 2),
            ((vec![2, 5, 1, 2, 5], vec![10, 5, 2, 1, 5, 2]), 3),
            ((vec![1, 3, 7, 1, 7, 5], vec![1, 9, 2, 5, 1]), 2),
        ],
        |a, b| a == b,
    );
}
