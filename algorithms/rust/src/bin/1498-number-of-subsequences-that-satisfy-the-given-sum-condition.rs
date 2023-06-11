/*
 * @lc app=leetcode id=1498 lang=rust
 *
 * [1498] Number of Subsequences That Satisfy the Given Sum Condition
 *
 * https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
 *
 * algorithms
 * Medium (37.89%)
 * Likes:    2602
 * Dislikes: 232
 * Total Accepted:    61.2K
 * Total Submissions: 148.2K
 * Testcase Example:  '[3,5,6,7]\n9'
 *
 * You are given an array of integers nums and an integer target.
 *
 * Return the number of non-empty subsequences of nums such that the sum of
 * the minimum and maximum element on it is less or equal to target. Since
 * the answer may be too large, return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [3,5,6,7], target = 9
 * Output: 4
 * Explanation: There are 4 subsequences that satisfy the condition.
 * [3] -> Min value + max value <= target (3 + 3 <= 9)
 * [3,5] -> (3 + 5 <= 9)
 * [3,5,6] -> (3 + 6 <= 9)
 * [3,6] -> (3 + 6 <= 9)
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [3,3,6,8], target = 10
 * Output: 6
 * Explanation: There are 6 subsequences that satisfy the condition. (nums
 * can have repeated numbers).
 * [3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [2,3,3,4,6,7], target = 12
 * Output: 61
 * Explanation: There are 63 non-empty subsequences, two of them do not
 * satisfy the condition ([6,7], [7]).
 * Number of valid subsequences (63 - 2 = 61).
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^6
 * 1 <= target <= 10^6
 *
 *
 */
struct Solution;
// @lc code=start

impl Solution {
    pub fn num_subseq(nums: Vec<i32>, target: i32) -> i32 {
        const M: i32 = 1000000007;
        let mut nums = nums;
        nums.sort();
        let mut power = 1;
        let (mut hi, mut res) = (nums.partition_point(|&x| x <= (target / 2)), 0);
        if hi == 0 {
            return 0;
        }
        hi -= 1;
        let mut lo = hi;
        loop {
            while hi < nums.len() - 1 && nums[lo] + nums[hi + 1] <= target {
                hi += 1;
                power = (power * 2) % M;
            }
            res = (res + power) % M;
            if lo == 0 {
                break res;
            }
            power = (power * 2) % M;
            lo -= 1;
        }
    }
}

// @lc code=end
fn main() {
    rust::test_algo(
        |(s, k)| Solution::num_subseq(s, k),
        vec![
            ((vec![3, 5, 6, 7], 9), 4),
            ((vec![3, 3, 6, 8], 10), 6),
            ((vec![2, 3, 3, 4, 6, 7], 12), 61),
            ((vec![3, 2, 4, 1, 5], 6), 21),
            ((vec![3, 5, 6, 7], 10), 9),
            ((vec![1; 1000], 2), 688423209),
        ],
        |a, b| a == b,
    )
}
