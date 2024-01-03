/*
 * @lc app=leetcode id=2448 lang=rust
 *
 * [2448] Minimum Cost to Make Array Equal
 *
 * https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/
 *
 * algorithms
 * Hard (34.67%)
 * Likes:    1335
 * Dislikes: 15
 * Total Accepted:    30.7K
 * Total Submissions: 73.1K
 * Testcase Example:  '[1,3,5,2]\n[2,3,1,14]'
 *
 * You are given two 0-indexed arrays nums and cost consisting each of n
 * positive integers.
 *
 * You can do the following operation any number of times:
 *
 *
 * Increase or decrease any element of the array nums by 1.
 *
 *
 * The cost of doing one operation on the i^th element is cost[i].
 *
 * Return the minimum total cost such that all the elements of the array nums
 * become equal.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,3,5,2], cost = [2,3,1,14]
 * Output: 8
 * Explanation: We can make all the elements equal to 2 in the following way:
 * - Increase the 0^th element one time. The cost is 2.
 * - Decrease the 1^st element one time. The cost is 3.
 * - Decrease the 2^nd element three times. The cost is 1 + 1 + 1 = 3.
 * The total cost is 2 + 3 + 3 = 8.
 * It can be shown that we cannot make the array equal with a smaller cost.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
 * Output: 0
 * Explanation: All the elements are already equal, so no operations are
 * needed.
 *
 *
 *
 * Constraints:
 *
 *
 * n == nums.length == cost.length
 * 1 <= n <= 10^5
 * 1 <= nums[i], cost[i] <= 10^6
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn min_cost(nums: Vec<i32>, cost: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut order = (0..n).collect::<Vec<usize>>();
        order.sort_unstable_by_key(|x| nums[*x]);
        let full_s = cost.iter().map(|x| *x as i64).sum::<i64>();
        (0..n)
            .scan(
                (
                    nums.iter()
                        .zip(cost.iter())
                        .map(|(x, y)| *x as i64 * *y as i64)
                        .sum::<i64>(),
                    0,
                    0,
                ),
                |acc, i| {
                    let (curr, prefix, prev) = acc;
                    let p = nums[order[i]] as i64;
                    *curr += (2 * *prefix - full_s) * (p - *prev);
                    *prefix += cost[order[i]] as i64;
                    *prev = p;
                    Some(*curr)
                },
            )
            .min()
            .unwrap_or(0)
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::min_cost(e.0, e.1),
        vec![
            // ((vec![1, 3, 5, 2], vec![2, 3, 1, 14]), 8),
            ((vec![2, 2, 2, 2, 2], vec![4, 2, 8, 1, 3]), 0),
            //
        ],
        |a, b| a == b,
    );
}
