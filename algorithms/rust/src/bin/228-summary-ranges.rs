/*
 * @lc app=leetcode id=228 lang=rust
 *
 * [228] Summary Ranges
 *
 * https://leetcode.com/problems/summary-ranges/description/
 *
 * algorithms
 * Easy (46.94%)
 * Likes:    2996
 * Dislikes: 1600
 * Total Accepted:    379K
 * Total Submissions: 786.4K
 * Testcase Example:  '[0,1,2,4,5,7]'
 *
 * You are given a sorted unique integer array nums.
 *
 * A range [a,b] is the set of all integers from a to b (inclusive).
 *
 * Return the smallest sorted list of ranges that cover all the numbers in
 * the array exactly. That is, each element of nums is covered by exactly one
 * of the ranges, and there is no integer x such that x is in one of the
 * ranges but not in nums.
 *
 * Each range [a,b] in the list should be output as:
 *
 *
 * "a->b" if a != b
 * "a" if a == b
 *
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [0,1,2,4,5,7]
 * Output: ["0->2","4->5","7"]
 * Explanation: The ranges are:
 * [0,2] --> "0->2"
 * [4,5] --> "4->5"
 * [7,7] --> "7"
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [0,2,3,4,6,8,9]
 * Output: ["0","2->4","6","8->9"]
 * Explanation: The ranges are:
 * [0,0] --> "0"
 * [2,4] --> "2->4"
 * [6,6] --> "6"
 * [8,9] --> "8->9"
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= nums.length <= 20
 * -2^31 <= nums[i] <= 2^31 - 1
 * All the values of nums are unique.
 * nums is sorted in ascending order.
 *
 *
 */

struct Solution;

// @lc code=start
impl Solution {
    pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
        let mut res = vec![];
        let mut i = 0;
        let mut j = 0;

        while j < nums.len() {
            while j + 1 < nums.len() && nums[j + 1] == nums[j] + 1 {
                j += 1;
            }

            if i == j {
                res.push(format!("{}", nums[i]))
            } else {
                res.push(format!("{}->{}", nums[i], nums[j]))
            }
            j += 1;
            i = j;
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::summary_ranges(e),
        vec![
            (
                (vec![0, 1, 2, 4, 5, 7]),
                vec!["0->2", "4->5", "7"]
                    .into_iter()
                    .map(String::from)
                    .collect(),
            ),
            (
                (vec![0, 2, 3, 4, 6, 8, 9]),
                vec!["0", "2->4", "6", "8->9"]
                    .into_iter()
                    .map(String::from)
                    .collect(),
            ),
            ((vec![0]), vec!["0"].into_iter().map(String::from).collect()),
            (
                ((0..20).into_iter().enumerate().map(|x| x.0 as i32).collect()),
                vec!["0->19"].into_iter().map(String::from).collect(),
            ),
        ],
        |a, b| a == b,
    );
}
