/*
 * @lc app=leetcode id=1802 lang=rust
 *
 * [1802] Maximum Value at a Given Index in a Bounded Array
 *
 * https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/
 *
 * algorithms
 * Medium (31.96%)
 * Likes:    1594
 * Dislikes: 256
 * Total Accepted:    34.6K
 * Total Submissions: 92.3K
 * Testcase Example:  '4\n2\n6'
 *
 * You are given three positive integers: n, index, and maxSum. You want to
 * construct an array nums (0-indexed) that satisfies the following
 * conditions:
 *
 *
 * nums.length == n
 * nums[i] is a positive integer where 0 <= i < n.
 * abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
 * The sum of all the elements of nums does not exceed maxSum.
 * nums[index] is maximized.
 *
 *
 * Return nums[index] of the constructed array.
 *
 * Note that abs(x) equals x if x >= 0, and -x otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 4, index = 2,  maxSum = 6
 * Output: 2
 * Explanation: nums = [1,2,2,1] is one array that satisfies all the
 * conditions.
 * There are no arrays that satisfy all the conditions and have nums[2] == 3,
 * so 2 is the maximum nums[2].
 *
 *
 * Example 2:
 *
 *
 * Input: n = 6, index = 1,  maxSum = 10
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= maxSum <= 10^9
 * 0 <= index < n
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    // O(logN) time complexity
    // O(1) space complexity
    pub fn max_value(n: i32, index: i32, mut max_sum: i32) -> i32 {
        max_sum -= n;
        let n = n as i64;
        let index = index as i64;
        let max_sum = max_sum as i64;
        let mut lo = 0;
        let mut hi = max_sum;
        while lo < hi {
            let mid = (lo + hi + 1) / 2;
            let left_0 = (mid - index - 1).max(0);
            let right_0 = (mid - (n - index - 1) - 1).max(0);
            let upper = (mid - 1) * mid;
            let right = (upper - (right_0 * (right_0 + 1))) / 2;
            let left = (upper - (left_0 * (left_0 + 1))) / 2;
            if right + mid + left <= max_sum {
                lo = mid;
            } else {
                hi = mid - 1
            }
        }
        (lo + 1) as i32
    }
    // O(N) time complexity
    // O(1) space complexity
    // pub fn max_value(n: i32, index: i32, mut max_sum: i32) -> i32 {
    //     max_sum -= n;
    //     let mut curr = 0;
    //     for i in 0..n {
    //         curr += 1 + i.min(index) + i.min(n - index - 1);
    //         if curr > max_sum {
    //             return i + 1;
    //         }
    //     }
    //     1 + n + (max_sum - curr) / n
    // }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::max_value(e.0, e.1, e.2),
        vec![
            ((4, 2, 6), 2),
            ((6, 1, 10), 3),
            ((6, 1, 14), 4),
            ((11, 5, 66), 8),
            ((6, 0, 10), 3),
            ((3, 0, 815094800), 271698267),
            ((3, 1, 815094800), 271698267),
            ((10i32.pow(9), 0, 10i32.pow(9)), 1),
        ],
        |a, b| a == b,
    );
}
