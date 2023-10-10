/*
 * @lc app=leetcode id=2009 lang=rust
 *
 * [2009] Minimum Number of Operations to Make Array Continuous
 *
 * https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/description/
 *
 * algorithms
 * Hard (45.37%)
 * Likes:    1132
 * Dislikes: 17
 * Total Accepted:    26.3K
 * Total Submissions: 52.5K
 * Testcase Example:  '[4,2,5,3]'
 *
 * You are given an integer array nums. In one operation, you can replace any
 * element in nums with any integer.
 *
 * nums is considered continuous if both of the following conditions are
 * fulfilled:
 *
 *
 * All elements in nums are unique.
 * The difference between the maximum element and the minimum element in nums
 * equals nums.length - 1.
 *
 *
 * For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6]
 * is not continuous.
 *
 * Return the minimum number of operations to make nums continuous.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [4,2,5,3]
 * Output: 0
 * Explanation: nums is already continuous.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2,3,5,6]
 * Output: 1
 * Explanation: One possible solution is to change the last element to 4.
 * The resulting array is [1,2,3,5,4], which is continuous.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [1,10,100,1000]
 * Output: 3
 * Explanation: One possible solution is to:
 * - Change the second element to 2.
 * - Change the third element to 3.
 * - Change the fourth element to 4.
 * The resulting array is [1,2,3,4], which is continuous.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashSet;
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len() as i32;
        if n == 0 {
            return 0;
        }
        let mut i = 0;
        let mut j = 0;
        let mut best = 0;
        let mut uniques = nums
            .into_iter()
            .collect::<HashSet<i32>>()
            .into_iter()
            .collect::<Vec<i32>>();
        uniques.sort_unstable();
        while j < uniques.len() {
            while uniques[j] - uniques[i] >= n {
                i += 1;
            }
            j += 1;
            best = best.max(j - i);
        }
        n - best as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::min_operations,
        vec![
            (vec![4, 2, 5, 3], 0),
            (vec![1, 2, 3, 5, 6], 1),
            (vec![1, 10, 100, 1000], 3),
            (
                vec![
                    28, 49, 23, 87, 98, 21, 85, 68, 72, 65, 94, 96, 60, 38, 51, 61, 100, 75, 61,
                    77, 33, 82, 29, 21, 53, 86, 54, 41, 41, 72, 41, 32, 70, 99, 54, 25, 35, 38,
                ],
                23,
            ),
            (
                vec![
                    79, 26, 56, 96, 78, 86, 27, 83, 94, 27, 61, 80, 80, 47, 99, 21, 41, 82, 96, 73,
                    73, 53, 81, 26, 75,
                ],
                14,
            ),
            (
                vec![
                    86, 87, 79, 24, 66, 43, 62, 25, 65, 92, 57, 77, 64, 31, 70, 58, 71, 56, 31, 57,
                    46, 36, 36, 44, 26, 67, 89, 62, 23, 52, 72, 79, 32, 95, 48, 80, 78,
                ],
                18,
            ),
            (
                vec![
                    40, 47, 27, 85, 51, 95, 71, 22, 83, 99, 79, 69, 100, 47, 51, 69, 47, 42, 41,
                    42, 61, 65, 86,
                ],
                16,
            ),
            (
                vec![
                    42, 51, 48, 93, 71, 20, 89, 66, 21, 54, 91, 99, 32, 96, 26, 95, 38, 63, 100,
                    88, 43, 92, 36, 26, 88, 61, 60, 94, 64, 34, 21, 65, 59, 93,
                ],
                19,
            ),
            (vec![57, 68, 37, 70, 88, 26, 95, 35, 83], 7),
            (
                vec![
                    44, 84, 57, 84, 94, 33, 93, 33, 56, 90, 74, 83, 21, 47, 57, 88, 21, 49, 83, 27,
                    64,
                ],
                14,
            ),
            (
                vec![
                    57, 30, 48, 58, 20, 72, 34, 26, 38, 28, 55, 78, 39, 53, 40, 71, 48, 92, 30, 50,
                    48, 71,
                ],
                13,
            ),
            (
                vec![
                    87, 56, 46, 79, 76, 31, 60, 67, 50, 62, 22, 29, 92, 70, 78, 99, 28, 80, 88,
                ],
                12,
            ),
            (
                vec![71, 35, 38, 47, 43, 85, 71, 68, 51, 69, 34, 58, 36, 53, 64],
                9,
            ),
        ],
        |a, b| a == b,
    );
}
