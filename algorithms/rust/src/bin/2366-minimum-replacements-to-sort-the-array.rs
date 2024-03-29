/*
 * @lc app=leetcode id=2366 lang=rust
 *
 * [2366] Minimum Replacements to Sort the Array
 *
 * https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/
 *
 * algorithms
 * Hard (40.01%)
 * Likes:    784
 * Dislikes: 26
 * Total Accepted:    20.2K
 * Total Submissions: 42K
 * Testcase Example:  '[3,9,3]'
 *
 * You are given a 0-indexed integer array nums. In one operation you can
 * replace any element of the array with any two elements that sum to it.
 *
 *
 * For example, consider nums = [5,6,7]. In one operation, we can replace
 * nums[1] with 2 and 4 and convert nums to [5,2,4,7].
 *
 *
 * Return the minimum number of operations to make an array that is sorted in
 * non-decreasing order.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [3,9,3]
 * Output: 2
 * Explanation: Here are the steps to sort the array in non-decreasing order:
 * - From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
 * - From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes
 * [3,3,3,3,3]
 * There are 2 steps to sort the array in non-decreasing order. Therefore, we
 * return 2.
 *
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2,3,4,5]
 * Output: 0
 * Explanation: The array is already in non-decreasing order. Therefore, we
 * return 0.
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
impl Solution {
    pub fn minimum_replacement(nums: Vec<i32>) -> i64 {
        let mut last = *nums.last().unwrap();
        let mut res = 0i64;
        for &n in nums.iter().rev() {
            let slots = (n + (last - 1)) / last;
            last = n / slots;
            res += slots as i64;
        }
        res - nums.len() as i64
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        Solution::minimum_replacement,
        vec![
            ((vec![3, 9, 3]), 2),
            ((vec![1, 2, 3, 4, 5]), 0),
            ((vec![5, 4, 3, 2, 1]), 10),
            ((vec![88, 18, 49]), 4),
            ((vec![22, 100, 97]), 1),
            ((vec![1, 59, 36, 48, 19, 14]), 18),
            ((vec![3, 9, 9]), 0),
            ((vec![9, 9, 3]), 4),
            (
                (vec![
                    88, 18, 49, 34, 65, 1, 71, 30, 48, 57, 77, 2, 78, 75, 92, 63, 59, 60, 62, 98,
                    82, 64, 100, 89, 55, 86, 40, 35, 54, 78, 76, 86, 43, 52, 39, 98, 87, 14, 59,
                    49, 21, 28, 45, 46, 33, 95, 47, 45, 6, 29, 19, 26, 53, 55, 88, 16, 91, 13, 17,
                    1, 29, 54, 34, 67, 24, 83, 70, 49, 80, 93, 52, 81, 70, 55, 78, 6, 29, 68, 21,
                    68, 42, 75, 83, 11, 59, 8, 47, 86, 88, 20, 9, 15, 1, 68,
                ]),
                4749,
            ),
            (
                (vec![
                    1, 59, 36, 48, 19, 14, 38, 50, 84, 95, 7, 66, 13, 28, 21, 65, 97, 93, 51, 25,
                    33, 6, 62, 63, 15, 67, 1, 6, 37, 63, 39, 58, 45, 61, 52, 19, 91, 22, 100, 97,
                    15, 100, 18, 88, 91, 31, 50, 62, 85, 26, 5, 6, 15, 90, 86, 2, 37, 2, 11, 11,
                    52, 2, 60, 72, 40, 91, 75, 66, 21, 14, 2, 38, 3, 9, 6, 86, 35, 43, 34, 33, 26,
                    23,
                ]),
                3124,
            ),
            (
                (vec![
                    87, 61, 54, 29, 24, 22, 17, 71, 80, 95, 52, 26, 47, 89, 10, 61, 75, 97, 94, 10,
                    48, 55, 83, 45, 89, 90, 45, 40, 5, 14, 10, 100, 55, 12, 91, 94, 96, 16, 51, 37,
                    80, 25, 75, 80, 31, 89, 61, 60, 62, 47,
                ]),
                1840,
            ),
            ((vec![82, 16, 49]), 5),
            (
                (vec![
                    83, 21, 32, 99, 12, 92, 18, 68, 73, 59, 72, 10, 94, 55, 45, 48, 64, 36, 81, 97,
                    34, 55, 64, 52, 95, 75, 44, 100, 24, 82, 16, 63, 17, 10, 53, 50, 18, 21, 83,
                    64, 32, 46, 26, 24, 55, 62, 72, 49, 98, 90, 61, 58, 74, 11, 61, 23,
                ]),
                2185,
            ),
            (
                (vec![
                    31, 32, 60, 54, 10, 81, 65, 38, 59, 63, 48, 67, 4, 60, 89, 43, 63, 76, 28, 25,
                    67, 90, 95, 55, 4, 87, 38, 40, 5, 84, 72, 9, 68, 35, 30, 29, 29, 82, 80, 65,
                    40, 74, 91, 4,
                ]),
                2053,
            ),
            (
                (vec![
                    64, 51, 41, 25, 37, 58, 85, 90, 54, 72, 55, 54, 90, 89, 43, 45,
                ]),
                79,
            ),
            ((vec![54, 4, 50, 61, 48]), 15),
            (
                (vec![
                    16, 68, 2, 47, 15, 44, 59, 35, 52, 50, 47, 91, 71, 34, 38, 20, 4, 57, 17, 83,
                    84, 94, 80, 82, 87, 39, 40, 57, 5, 65, 47, 2, 74, 23, 8, 41, 91, 95, 55, 15,
                    35, 31, 93, 90, 54, 20, 60, 18, 75, 94, 96, 57,
                ]),
                1682,
            ),
            (
                (vec![
                    87, 98, 36, 96, 12, 26, 55, 42, 90, 92, 26, 97, 90, 96, 100, 89, 53, 14, 52,
                    16, 6, 61, 26, 79, 29, 35, 5, 50, 78, 60, 14, 79, 56, 96, 68, 48, 14, 75, 90,
                    71, 71, 58, 76, 7, 83, 94, 3, 91, 49, 1, 86, 27, 68, 65, 45, 83, 31, 33, 49,
                    65, 14, 73, 68, 8, 11, 54, 69, 26, 69, 47, 65, 84, 94, 19, 65, 30, 33, 12, 37,
                    64, 91, 95, 28, 12,
                ]),
                4088,
            ),
            ((vec![46, 6]), 7),
            (
                (vec![
                    81, 77, 63, 29, 74, 30, 32, 93, 45, 26, 56, 24, 10, 63, 55, 7, 84, 97, 1, 55,
                    69, 86,
                ]),
                928,
            ),
            (
                (vec![
                    26, 18, 62, 37, 88, 48, 64, 34, 36, 8, 53, 67, 94, 68, 43, 95, 87, 91, 4, 6,
                    17, 45, 81, 5, 8, 51, 60, 60, 71, 50, 1, 89, 30, 56, 22, 58, 21, 21, 64, 53,
                    80, 54, 92, 22, 45, 66, 81, 54, 57, 19, 76,
                ]),
                1612,
            ),
            (
                (vec![
                    23, 34, 16, 49, 98, 34, 27, 67, 81, 53, 50, 85, 85, 36, 59, 37, 28, 7, 68, 40,
                    75, 40, 73, 73, 59, 98, 92, 43, 13, 30, 28, 83, 57, 86, 23, 59, 7, 15, 87, 11,
                    45, 33, 40, 59, 19, 3, 56, 94, 63, 32, 87, 64, 15, 27, 56, 69, 46, 34, 41, 78,
                    26, 92, 10, 25,
                ]),
                2673,
            ),
            (
                (vec![
                    68, 27, 15, 19, 20, 58, 56, 13, 10, 32, 65, 30, 91, 78, 72, 15, 7, 54, 51, 75,
                    37, 34, 42, 27, 25, 49, 45, 71, 34, 99, 81, 38, 8, 56, 100, 10, 20, 65, 41, 4,
                    17, 63, 88, 38, 73, 36, 75, 82, 13, 58, 60, 7, 85, 7, 41, 48,
                ]),
                2223,
            ),
            (
                (vec![
                    18, 74, 63, 41, 89, 38, 28, 93, 35, 12, 72, 17, 51, 7, 72, 47, 53, 25, 97, 75,
                    91, 78, 46, 29, 47, 51, 57, 63, 85, 89, 2, 5, 20, 54, 7, 80, 39, 68, 62, 29,
                    14, 70, 47, 15, 80, 77, 63, 93, 2, 41, 82, 97, 6, 46, 54, 45, 34, 61, 33, 37,
                    31, 70, 15, 83, 17, 26, 36, 68, 3, 46, 96, 26, 1, 62, 39, 14, 62, 62, 38, 58,
                    2, 65, 85,
                ]),
                3643,
            ),
            (
                (vec![
                    41, 82, 62, 67, 75, 78, 57, 54, 9, 20, 41, 38, 19, 85, 30, 63, 18, 98, 18, 3,
                    57, 70, 68, 74, 53, 22, 43, 66, 55, 8, 4, 87, 63, 7, 83, 34, 46, 43, 72, 12,
                    45, 28, 4, 44, 13, 43, 68, 18, 44, 82, 96, 93, 6, 88, 97, 56, 7, 93, 85, 5, 75,
                    28, 70, 17, 20, 9, 19, 6, 34, 81, 30, 93, 10, 25, 29, 52, 37, 49, 21, 14, 79,
                    31, 58, 14, 8, 44, 22, 75, 46, 22, 40, 92, 91, 37, 2, 48, 63, 23, 59, 94,
                ]),
                4210,
            ),
            (
                (vec![
                    17, 79, 10, 80, 10, 45, 26, 26, 48, 33, 2, 64, 32, 49, 93, 16, 91, 28, 59, 96,
                    1, 10, 13, 48, 65, 62, 62, 100, 82, 19, 15, 55, 24, 72, 44, 55, 98,
                ]),
                954,
            ),
            (
                (vec![
                    90, 72, 71, 13, 44, 90, 12, 61, 5, 70, 93, 75, 8, 15, 56, 52, 98, 36, 55, 2,
                    16, 95, 46, 15, 24, 68, 78, 100, 63, 75, 49, 56, 80, 37, 46, 41, 90, 75, 20,
                    26, 76, 70, 65, 49, 80, 82, 67, 73, 87, 97, 41, 77, 79, 77, 94, 93, 73, 67, 71,
                    1, 94, 6,
                ]),
                3492,
            ),
            (
                (vec![
                    23, 46, 59, 64, 18, 86, 21, 34, 30, 89, 68, 56, 66, 48, 14, 39, 37, 10, 25, 64,
                    24, 22, 98, 73, 25, 14, 38, 2, 81, 35, 5, 90, 78, 31, 74, 79, 88, 17, 40, 31,
                    60, 73, 82, 18, 28, 63, 84, 49, 84, 68, 53, 56, 33, 11, 96, 70, 10, 54, 80, 74,
                    79, 95, 66, 99, 82, 68, 33, 98,
                ]),
                2375,
            ),
            (
                (vec![
                    15, 94, 42, 23, 27, 82, 31, 10, 25, 41, 2, 91, 32, 91, 58, 90, 88, 21, 88, 35,
                    2, 11, 8, 68, 52, 84, 65, 84, 93, 17, 47, 24, 89, 18, 18, 61, 80, 60, 23, 98,
                    92,
                ]),
                1135,
            ),
            (
                (vec![
                    56, 99, 60, 15, 30, 77, 65, 79, 94, 85, 58, 76, 85, 81, 25, 24, 16, 65, 100,
                    58, 74, 56, 10, 60, 28, 97, 25, 1, 71, 84, 70, 2, 54, 29, 17, 73, 71, 28, 44,
                    44, 16, 12, 67, 77, 77, 68, 95, 54, 78, 37, 32, 48, 8, 72, 39, 18, 4, 40, 11,
                    11, 78, 5, 3, 78, 26, 52, 72,
                ]),
                3026,
            ),
            (
                (vec![
                    1, 71, 1, 8, 60, 44, 83, 4, 99, 39, 73, 49, 10, 97, 57, 84, 74, 49, 49, 2, 93,
                    50, 45, 19, 88, 80, 71, 97, 42, 64, 100, 75, 80, 54, 62, 73, 73, 56, 6, 80, 77,
                    66, 59, 51, 26, 1, 60, 23, 86, 21, 87, 59, 86, 54, 13, 34, 10, 64, 2, 67, 58,
                    41, 49, 77, 67, 82, 71, 90,
                ]),
                3032,
            ),
            (
                (vec![
                    96, 88, 84, 14, 9, 83, 95, 35, 100, 84, 97, 29, 22, 54, 88, 32, 93, 78, 15, 44,
                    85, 91, 9, 47, 16, 76, 70, 48, 94, 53, 16, 3, 63, 81, 23, 46, 25, 53, 43, 65,
                    79, 18, 35, 80, 29, 83, 52, 99, 34, 84, 79, 38, 2, 30, 49, 89, 69, 52, 75, 72,
                    97, 75, 11, 65, 41, 27, 91, 91,
                ]),
                2926,
            ),
            (
                (vec![
                    77, 93, 93, 2, 35, 43, 28, 35, 65, 43, 86, 54, 81, 80, 57, 25, 75, 10, 65, 66,
                    1, 77, 85, 30, 17, 70, 50, 13, 53, 50, 50, 48,
                ]),
                1133,
            ),
            ((vec![64]), 0),
            (
                (vec![
                    42, 33, 79, 48, 5, 55, 2, 65, 80, 58, 77, 59, 3, 42, 17, 86, 18, 2, 44, 95, 20,
                    35, 71, 44, 55, 18, 30, 5, 74, 73, 17, 27, 15, 88, 7, 22, 91, 20, 64, 96, 84,
                    25, 87, 37, 16, 57, 10, 55, 87, 56, 88, 90, 43, 58, 55, 85, 20, 70, 24, 1, 5,
                    88, 61, 84, 26, 13,
                ]),
                2790,
            ),
            ((vec![50, 61, 52, 7, 67, 100, 4, 28]), 146),
            (
                (vec![
                    43, 59, 99, 42, 98, 6, 1, 49, 39, 40, 4, 83, 83, 100, 86, 38, 13, 64, 69, 50,
                    90, 78, 92, 41, 1, 25, 62, 34, 14, 22, 82, 39, 10, 80, 83, 88, 22, 19, 35, 31,
                    29, 54, 87, 33, 69, 69, 80, 64, 33, 99, 44, 15, 97,
                ]),
                2008,
            ),
            ((vec![86, 14, 56, 96, 61, 77, 12, 61]), 39),
            (
                (vec![
                    87, 95, 16, 16, 16, 42, 44, 39, 5, 69, 96, 44, 37, 77, 97, 47, 40, 29, 11, 28,
                    7, 25, 82, 7, 71, 56, 23, 60, 13, 66, 84, 74, 92, 26, 87, 7, 86, 34, 43, 57,
                    87, 24, 55, 43, 7, 99, 10, 2, 56, 56, 32, 55,
                ]),
                2161,
            ),
            (
                (vec![
                    5, 45, 98, 95, 70, 47, 93, 97, 40, 51, 30, 71, 88, 80, 4, 42, 77, 37, 96, 40,
                    91, 62, 7, 19, 41, 26, 12, 7, 1, 28, 63, 91, 61, 59, 14, 56, 16, 17, 55, 17,
                    74, 62, 82, 15, 100, 70, 93, 42, 92, 94, 93, 19, 75, 44, 90, 74, 3, 98, 68, 45,
                    94, 74, 32, 36, 15, 59, 58, 51, 50, 100, 31, 75, 80, 23, 89, 39, 90, 73, 34,
                    36, 29, 5, 55, 19, 14,
                ]),
                4189,
            ),
            (
                (vec![
                    32, 85, 8, 92, 31, 8, 92, 33, 91, 47, 51, 10, 30, 41, 68, 99, 79, 64, 66, 75,
                    1, 24, 70, 88, 82, 19, 34, 2, 4, 55, 12, 91, 64, 74, 20, 5, 24, 86, 89, 54, 57,
                    40, 90, 1, 49, 32, 9, 67, 23, 30, 77, 65,
                ]),
                2156,
            ),
            (
                (vec![
                    14, 64, 59, 79, 12, 47, 82, 91, 22, 13, 52, 6, 14, 36, 14, 92, 29, 69, 72, 22,
                    69, 20, 48, 26, 36, 25, 55, 36, 95, 93, 70, 48, 87, 51, 32, 51, 47, 71, 16, 92,
                    36, 20, 91, 47, 1, 61, 11, 17, 65, 68,
                ]),
                2112,
            ),
            (
                (vec![
                    12, 84, 90, 65, 98, 20, 56, 6, 63, 91, 56, 68, 35, 95, 41, 54, 15, 36, 33, 14,
                    94, 23, 6, 6, 52, 6, 25, 3, 58, 64, 18, 44, 49, 16, 58, 66, 4, 22, 95, 95, 20,
                    11, 4, 84, 82, 75, 74, 97, 24, 65, 41, 89, 2, 22, 12, 1, 31, 86, 53, 55, 4, 66,
                    87, 83, 81, 34, 85, 19, 49, 17, 25, 32, 50, 90, 87,
                ]),
                2895,
            ),
            (
                (vec![
                    73, 42, 28, 46, 76, 17, 8, 98, 45, 96, 11, 52, 10, 19, 60, 3, 89, 15, 56, 24,
                    68, 48, 22, 56, 10, 60, 77, 21, 19, 43, 58, 2, 99, 49, 89, 66, 16, 12, 9, 91,
                    5, 92, 97, 84, 82, 45, 64, 39, 54, 41, 43, 72, 23, 80, 51, 96, 9, 11, 78, 92,
                    66, 1, 72, 75, 82, 7, 91, 30, 55, 69, 12, 43, 79, 54, 78, 74, 78, 15, 92, 26,
                    100, 72, 43, 16, 17, 7, 88, 42, 2, 90, 98, 29, 86, 79, 26, 27,
                ]),
                4289,
            ),
            (
                (vec![
                    40, 3, 29, 78, 47, 76, 65, 44, 66, 14, 79, 17, 74, 62, 86, 6, 97, 98, 86, 6,
                    66, 80, 50, 76, 44, 91, 24, 57, 11, 82,
                ]),
                968,
            ),
            (
                (vec![
                    70, 37, 1, 4, 96, 80, 95, 50, 97, 3, 22, 41, 27, 34, 41, 91, 65, 48, 35, 92,
                    39, 24, 57, 86, 5, 94, 44, 28, 33, 43, 72, 68, 55, 82, 76, 46, 33, 52, 34, 4,
                    87,
                ]),
                1886,
            ),
            ((vec![10, 26, 42, 78, 26, 72]), 4),
            (
                (vec![
                    87, 25, 91, 14, 55, 56, 66, 48, 74, 48, 24, 55, 34, 100, 82, 7, 91, 71, 18,
                ]),
                422,
            ),
            (
                (vec![
                    91, 35, 79, 72, 80, 42, 43, 40, 44, 17, 6, 81, 92, 18, 37, 60, 52, 24, 70, 59,
                    5, 39, 66, 42, 80, 82, 70, 49, 41, 57, 96, 40, 36, 58, 59, 12, 13, 23, 15, 55,
                    46, 73, 56, 85, 79, 92, 49, 61, 40, 6, 33, 7, 55, 48, 11, 60, 4, 23, 77, 63,
                    49, 78, 6, 59, 52, 29, 14, 27, 60, 34, 26, 89, 56, 68, 1, 20, 78, 55, 36, 72,
                    78, 74, 63, 50, 18, 49, 62, 68, 63, 92, 42, 16, 31, 86, 10, 10, 29, 53, 6, 68,
                ]),
                4515,
            ),
            (
                (vec![23, 38, 1, 39, 9, 11, 99, 9, 64, 73, 46, 88, 48, 88]),
                88,
            ),
            (
                (vec![76, 49, 51, 67, 66, 41, 14, 61, 5, 66, 1, 1, 14, 2]),
                492,
            ),
            (
                (vec![
                    86, 54, 56, 69, 53, 54, 39, 2, 11, 18, 51, 4, 70, 73, 59, 81, 94, 63, 48, 2,
                    59, 13, 3, 30, 41, 63, 41, 38, 22, 25, 7, 54, 37, 19, 57, 44, 35, 1, 83, 48,
                    31, 28, 89, 29, 63, 69, 44, 93, 76, 51, 1, 70, 51, 8, 37, 81, 33, 43, 96, 94,
                    76, 65, 58, 18, 13, 10,
                ]),
                2595,
            ),
            (
                (vec![
                    2, 2, 3, 47, 6, 81, 87, 70, 84, 33, 87, 1, 100, 27, 53, 56, 21, 69, 2, 67, 11,
                    37, 39, 50, 92, 21, 74, 73, 97, 94, 44, 48, 17, 38, 35, 26, 93, 30, 48, 8, 94,
                    70, 69, 61, 97, 57, 19, 9, 74, 30, 71, 7, 14, 49, 32, 43, 56, 74, 13, 38, 35,
                    52, 91, 50, 70, 40,
                ]),
                2572,
            ),
            (
                (vec![
                    59, 2, 37, 43, 51, 4, 63, 39, 11, 81, 54, 32, 72, 15, 14, 72, 60, 27, 12, 77,
                    23, 5, 70, 39, 40, 78, 42, 74, 60, 11, 48, 56, 15, 69, 36, 5, 67, 39, 49, 42,
                    19, 83, 79, 61, 42, 91, 19, 18, 95, 10, 55, 59, 32, 56, 100, 90, 70, 81, 71, 7,
                    71, 2, 34, 39, 52, 62, 94, 18, 25, 86, 66,
                ]),
                2826,
            ),
            (
                (vec![
                    87, 42, 84, 43, 25, 90, 50, 57, 72, 38, 52, 74, 12, 55, 69, 71, 20, 39, 31, 16,
                    42, 37, 52, 44, 82, 94, 60, 6, 31, 27, 63, 44, 41, 3, 44, 88, 46,
                ]),
                1538,
            ),
            (
                (vec![
                    75, 2, 56, 78, 24, 67, 71, 29, 35, 7, 92, 16, 99, 34, 57, 57, 60, 86, 100, 1,
                    22, 39, 67, 24, 17, 83, 84, 22, 85, 98, 26, 64, 91, 50, 46, 80, 17, 37, 39, 2,
                    57, 62, 85, 97, 15, 40, 82, 66, 44, 93, 17, 71, 61, 69, 33, 44, 18, 68, 16, 56,
                    67, 80, 30, 99, 88, 37, 16, 50,
                ]),
                2780,
            ),
            ((vec![57, 88, 41, 80, 67, 50, 31, 36, 10, 5]), 326),
            (
                (vec![
                    54, 27, 94, 79, 19, 54, 9, 70, 88, 52, 74, 45, 66, 54, 69, 82, 27, 34, 97, 46,
                    91, 95, 64, 70, 26, 98, 80, 40, 66, 1, 38, 90, 64, 62, 58, 49, 49, 82, 55, 12,
                    65, 61, 63, 83, 74, 73, 72, 57, 36, 28, 91, 100, 37, 13, 1, 24, 19, 29, 67, 6,
                    92, 2, 89, 14, 96, 15, 20, 76, 68, 19, 9, 30, 16, 85, 15, 30, 24, 70, 20, 61,
                    42, 20, 74, 69,
                ]),
                3698,
            ),
            (
                (vec![58, 36, 73, 29, 14, 71, 18, 83, 12, 86, 26, 85, 40, 31]),
                67,
            ),
            (
                (vec![
                    2, 35, 39, 10, 83, 59, 18, 5, 16, 62, 63, 22, 13, 7, 59, 87, 63, 77, 75, 67,
                    45, 93, 17, 62, 47, 54, 100, 97, 27, 68, 37, 79, 20, 87, 1, 96, 1, 41, 22, 19,
                    70, 20, 25, 24, 62, 7, 95, 13, 57, 18, 41, 59, 83, 73, 61, 54, 14, 9, 44, 98,
                    84, 29, 53, 96, 12, 61, 22, 34,
                ]),
                2515,
            ),
            (
                (vec![
                    21, 47, 49, 75, 74, 55, 75, 45, 27, 44, 12, 14, 8, 88, 72, 41, 97, 78, 2, 9,
                    86, 71, 91, 83, 41, 24, 1, 95, 58, 55, 21, 25, 76, 21, 31, 38, 91, 28, 46, 30,
                    95, 24, 98,
                ]),
                1453,
            ),
            (
                (vec![
                    97, 57, 3, 36, 97, 92, 85, 79, 6, 32, 74, 98, 12, 72, 27, 70, 35, 23, 43, 98,
                    62, 78, 60, 83, 99, 10, 47, 94, 9, 13, 16, 99, 16, 24, 34, 11, 56, 58, 73, 21,
                    9, 23, 1, 96, 79, 65, 10, 2, 57, 46, 100, 86, 84, 15, 91, 74, 62, 20, 29, 1,
                    38, 37, 21, 49, 23, 58, 91, 58, 48, 56, 95, 83, 71, 94, 56, 75, 82, 49, 12, 60,
                    89, 5, 24, 38, 63, 18, 74, 13, 100, 63, 80, 48, 9, 42, 97, 4, 74, 53, 25, 32,
                ]),
                4657,
            ),
            ((vec![10]), 0),
            (
                (vec![74, 80, 31, 47, 71, 72, 34, 6, 91, 73, 71, 91, 29]),
                234,
            ),
            (
                (vec![
                    71, 24, 74, 8, 25, 99, 25, 63, 33, 4, 40, 85, 80, 71, 36, 46, 17, 17, 35, 53,
                    98, 9, 31, 56, 4, 32, 81, 5, 28, 8, 65, 85, 85, 35, 48, 46, 74, 48, 34, 43, 61,
                    70, 17, 96, 84, 93, 86, 58, 24, 4, 25,
                ]),
                2197,
            ),
            (
                (vec![
                    72, 51, 35, 17, 80, 8, 96, 48, 23, 65, 93, 77, 73, 58, 69, 55, 45, 55, 75, 15,
                    59, 78, 69, 77, 71, 44, 67, 75, 36, 83, 12, 76, 72, 73, 27, 81, 52, 68, 40,
                    100, 13, 42, 100, 15, 27, 3, 57, 92, 42, 93, 76, 1, 24, 51, 7, 87, 18, 71, 94,
                    46, 97, 24, 10, 99, 30, 32, 10, 68, 82, 100, 26, 44, 53, 32, 4, 19, 66, 31, 58,
                    5, 87, 75, 38, 9, 57, 6, 32, 4, 47, 51, 17, 65, 25, 92, 30, 26,
                ]),
                4328,
            ),
            (
                (vec![
                    37, 8, 25, 5, 95, 5, 28, 55, 63, 17, 47, 50, 82, 24, 2, 13, 67, 3, 49, 66, 15,
                    91, 22, 76, 2, 90, 87, 74, 29, 22, 8, 58, 27, 59, 74, 22, 92, 85, 27, 5, 19,
                    63, 23, 62, 2, 75, 45, 29, 11, 86, 31, 46, 22, 49, 42, 25, 20, 61, 45, 81, 78,
                    11, 9, 98, 71, 55, 82, 80, 34, 9, 62, 4, 64, 35, 29,
                ]),
                2883,
            ),
            (
                (vec![
                    51, 14, 81, 6, 7, 23, 97, 49, 73, 80, 48, 43, 90, 19, 59, 17, 12, 93, 38, 64,
                    34, 4, 97, 76, 26, 69, 88, 61, 24, 92, 62, 13, 34, 65, 71, 18, 38, 11, 95, 42,
                    55, 73, 97, 25, 87, 37, 3, 81, 86, 78, 8, 96, 31, 3, 100, 27, 92, 98, 21, 37,
                    48, 89, 47, 20,
                ]),
                2558,
            ),
            (
                (vec![
                    4, 82, 29, 100, 74, 42, 44, 7, 67, 32, 50, 38, 76, 40, 36, 95, 29, 61, 39, 13,
                    99, 33, 40, 55, 13, 83, 56, 61, 26, 60, 89, 68, 21, 67, 36, 98, 71, 7, 51, 19,
                    65, 40, 73, 3, 18, 32, 86, 30, 52, 72, 48, 70, 33, 11, 32, 40, 9, 33, 93, 89,
                    10, 5, 92, 82, 95,
                ]),
                2667,
            ),
            (
                (vec![
                    61, 27, 87, 35, 14, 11, 64, 88, 6, 97, 87, 6, 24, 35, 71, 89, 5, 46, 29, 86,
                    53, 15, 55, 16, 64, 9, 74, 99, 7, 10, 84, 38, 9, 36, 60, 75, 26, 34, 67, 92,
                    39, 15, 85, 17, 77, 27, 50, 48, 90, 53, 63, 71, 67, 9, 21, 87, 37, 5, 94, 87,
                    19, 71, 87, 43,
                ]),
                2510,
            ),
            (
                (vec![
                    62, 99, 59, 10, 45, 47, 93, 4, 35, 71, 33, 45, 30, 46, 32, 76, 28, 4, 34, 83,
                    26, 93, 78, 24, 44, 4, 33, 49, 34, 25, 14, 67, 37, 89, 80, 50, 2, 24, 81, 26,
                    35, 71, 58, 93, 86, 24, 63, 61, 74, 7, 74, 20, 5, 39, 60, 30, 83, 72, 3,
                ]),
                2546,
            ),
            ((vec![95]), 0),
            (
                (vec![
                    67, 91, 70, 1, 28, 30, 6, 98, 8, 15, 97, 67, 86, 28, 61, 66, 41, 33, 79, 6, 5,
                    34, 94, 72, 7, 82, 60, 87, 32, 39, 54, 34, 22, 41, 38, 93, 69, 95, 31, 26, 29,
                    38, 25, 27, 33, 72, 19, 9, 99, 39, 13, 71, 42, 53, 11, 80, 43, 74, 71, 38, 25,
                    49, 52, 60, 67, 36, 51, 27, 82, 37, 9, 74, 53, 90, 73, 6, 98, 13, 1, 76, 28,
                    47, 4, 89, 47, 84, 63, 74, 63, 22, 18,
                ]),
                3805,
            ),
            (
                (vec![
                    68, 53, 87, 63, 70, 41, 80, 54, 94, 28, 3, 44, 69, 15, 55, 1, 22, 97, 24, 66,
                    91, 37, 75, 31, 82, 53, 5, 58, 86, 10, 45, 60, 53, 47, 18, 48, 70, 6, 37, 77,
                    30, 18, 61, 27, 21, 61, 14, 13, 77, 2, 82, 26, 85, 17, 19, 3, 72, 27, 42, 24,
                    8, 77, 62, 73, 42, 85, 35, 30, 51, 61, 44, 81, 75, 82, 83, 51, 41, 71, 96, 12,
                    93, 36, 61, 46, 60, 91, 25, 18, 5, 8, 29, 29,
                ]),
                4071,
            ),
            ((vec![48, 78, 1, 6, 85, 50, 46, 64, 38]), 133),
            (
                (vec![
                    39, 62, 18, 30, 71, 23, 36, 53, 83, 7, 11, 8, 71, 42, 77, 34, 59, 43, 93, 85,
                    84, 66, 91, 22, 22, 20, 87, 11, 29, 56,
                ]),
                897,
            ),
            (
                (vec![
                    49, 10, 75, 62, 60, 33, 97, 19, 47, 44, 89, 29, 49, 81, 1, 23, 29, 44, 37, 85,
                    76, 73, 25, 83, 82, 90, 94, 71, 55, 90, 65, 14, 46, 19, 57, 100, 99, 26, 26,
                    94, 92, 93, 65, 17, 41, 62, 44, 30, 79, 18, 67, 89, 41,
                ]),
                2103,
            ),
            (
                (vec![
                    44, 91, 64, 46, 55, 28, 75, 46, 16, 97, 17, 27, 42, 2, 65, 3, 6, 31, 79, 69,
                    52, 97, 58, 33, 17, 24, 20, 75, 57, 21, 66, 72, 93, 15, 5, 69, 95, 22, 11, 19,
                    33, 21, 67, 79, 14, 73, 93, 32, 86, 84, 55, 41, 27, 52, 26, 3, 25, 74, 54, 88,
                    3, 62, 31, 77, 27, 94, 48, 11, 7, 34, 36, 34, 37, 47, 48, 43, 25, 79, 32, 18,
                    62, 60, 64, 99, 41, 74, 47, 86, 87, 40, 32, 79, 82, 79,
                ]),
                3495,
            ),
            (
                (vec![
                    82, 31, 25, 67, 52, 54, 60, 61, 92, 40, 76, 50, 2, 9, 99, 70, 69, 60, 27, 96,
                    1, 57, 66, 52, 29, 13, 43, 97, 36, 69, 91, 37, 38, 57, 65, 9, 91, 95, 43, 33,
                    67, 22, 32, 98, 48, 64, 36, 68, 12, 21, 90, 32, 32, 84, 34, 6, 52, 61, 66, 23,
                    68, 66, 9, 71, 49, 38, 33, 28, 37, 34, 54, 100, 5, 86, 40, 22, 79, 7, 2, 75,
                    66, 63, 54, 87, 28, 93, 21, 8, 46, 45, 16, 2, 41, 94, 6,
                ]),
                4424,
            ),
            (
                (vec![
                    70, 19, 70, 85, 83, 39, 3, 99, 76, 4, 59, 66, 96, 68, 1, 81, 14, 58, 55, 52,
                    80, 29, 67, 38, 94, 88, 96, 5, 55, 99, 59, 35, 85, 64, 80, 48, 41, 85, 23, 95,
                    20, 75, 85, 8, 89, 15, 35, 17, 54, 55, 12, 70, 18, 91, 92, 17, 24, 74, 75, 87,
                    64, 37, 77, 51, 8, 95, 89, 90, 31, 43,
                ]),
                3161,
            ),
            ((vec![92, 74, 1, 41, 16, 95, 55, 39, 22, 65, 88]), 178),
            (
                (vec![
                    94, 43, 45, 67, 97, 100, 71, 9, 6, 46, 8, 54, 57, 76, 6, 6, 68, 62, 98, 41, 49,
                    40, 59, 90, 18, 22, 41, 21, 13, 56, 66, 47, 81,
                ]),
                852,
            ),
            (
                (vec![
                    13, 62, 79, 58, 28, 83, 13, 83, 36, 29, 5, 54, 29, 7, 87, 18, 67, 6, 41, 92,
                    27, 4, 42, 30, 90, 100, 79, 13, 98, 51, 89, 13, 60, 1, 82, 56, 23, 54, 4, 62,
                    8, 95, 43, 35, 53, 92, 23, 4, 52, 22, 53, 64, 68, 38, 95, 73, 38, 28, 78, 97,
                    73, 97, 64, 20, 76, 34, 49, 9,
                ]),
                2903,
            ),
            ((vec![33, 56, 56, 94, 56, 20, 7, 46, 62]), 63),
            (
                (vec![
                    99, 75, 52, 27, 5, 63, 13, 46, 71, 79, 17, 98, 15, 32, 68, 24, 59, 2, 57, 64,
                    91, 28, 43, 30, 23, 50, 33, 87, 56, 84, 19, 67, 50, 77, 45, 17, 69, 63, 19, 26,
                    23, 24, 6, 42, 92, 85, 22, 28, 2, 1, 50, 69, 95, 38, 58, 67, 27, 59, 23, 41,
                ]),
                2268,
            ),
            (
                (vec![
                    22, 85, 3, 5, 59, 18, 6, 70, 19, 80, 70, 37, 81, 51, 68, 79, 27, 32, 46, 47,
                    95, 6, 28, 53, 14, 9, 42, 1, 50, 2, 43, 87, 58, 13, 7, 51, 10, 12, 80, 43, 47,
                    24, 1, 3, 20, 57, 36, 78, 94, 77, 16, 66, 78, 84, 28, 97, 37,
                ]),
                1668,
            ),
            (
                (vec![
                    45, 78, 97, 73, 57, 10, 22, 33, 63, 89, 1, 15, 88, 57, 3, 33, 79, 90, 70, 82,
                    70, 41, 91, 97, 78, 72, 82, 63, 60, 5, 43, 72, 64, 35,
                ]),
                1346,
            ),
            (
                (vec![
                    90, 15, 100, 21, 76, 99, 79, 31, 19, 11, 86, 97, 92, 21, 42, 84, 84, 11, 18,
                    23, 68, 55, 64, 54, 51, 77, 50, 11, 56, 37, 5, 31, 33, 80, 75, 15, 11, 15, 80,
                    6, 51, 16, 70, 89, 7, 60, 16, 27, 78, 6, 55, 57, 93, 93, 97, 2,
                ]),
                2685,
            ),
            (
                (vec![
                    62, 15, 94, 72, 12, 44, 85, 62, 68, 38, 85, 27, 29, 35, 22, 30, 21, 6, 83, 72,
                    32, 67, 31, 94, 34, 91, 64, 50, 78, 72, 87, 8, 62, 39, 29, 53, 62, 89, 38, 36,
                    57, 51, 99, 20, 74, 3, 5, 33, 54, 2, 47, 66, 89, 43, 56, 37, 73, 24, 14, 48,
                ]),
                2432,
            ),
            (
                (vec![
                    58, 74, 45, 10, 11, 2, 64, 52, 94, 17, 19, 21, 28, 40, 82, 13, 36, 91, 7, 77,
                    42, 71, 76, 46, 19, 62, 62, 71, 99, 4, 81, 95, 48, 35, 68, 39, 39,
                ]),
                1182,
            ),
            (
                (vec![
                    78, 5, 37, 41, 67, 6, 15, 15, 54, 76, 26, 40, 12, 19, 70, 45, 98, 67, 25, 78,
                    8, 63, 6, 35, 69, 38, 70, 8, 61, 88, 36, 35, 2, 87, 29, 49, 50, 62, 64, 47, 79,
                    30, 44, 12, 32, 52, 3, 57, 94, 88, 76, 57, 71, 32, 78, 1, 42, 41, 36, 12, 50,
                    70, 4, 69, 52, 1, 49, 15, 54, 39, 2, 3, 5, 84, 47, 27, 73, 100, 66, 26, 79, 72,
                    54, 83, 53,
                ]),
                3079,
            ),
            (
                (vec![
                    14, 38, 85, 53, 31, 29, 58, 37, 46, 77, 98, 8, 55, 97, 45, 86, 4, 29, 49, 51,
                    8, 93, 53, 87, 86, 7, 9, 95, 88, 9, 32, 15, 90, 53, 53, 51, 92, 59, 86, 71, 25,
                    35, 23, 94, 79, 26, 87, 67,
                ]),
                1845,
            ),
            (
                (vec![
                    63, 60, 39, 76, 67, 18, 10, 50, 66, 6, 27, 11, 44, 86, 72, 25, 55, 22, 37, 79,
                    26, 16, 72, 57, 50, 51, 15, 10, 75, 24, 5, 9, 18, 88, 43, 38, 46, 37, 87, 80,
                    10, 87, 7, 46, 84, 16, 12, 2, 81, 98, 20, 15, 74, 44, 95, 24, 16, 59, 24, 12,
                    75, 3, 7, 3, 64, 49, 26, 89, 100, 45, 70, 66, 32, 68, 67, 41, 6, 70, 6, 46, 48,
                    3, 10, 49, 74, 72, 55,
                ]),
                3368,
            ),
            (
                (vec![
                    83, 98, 66, 85, 52, 53, 75, 4, 87, 38, 38, 87, 69, 73, 81, 91, 69, 96, 66, 68,
                    56, 83, 87, 72, 21, 18, 70, 43, 6, 96, 100, 2, 81, 79, 61, 72, 59,
                ]),
                1885,
            ),
            (
                (vec![
                    62, 91, 4, 47, 21, 85, 59, 79, 88, 63, 19, 51, 45, 48, 36, 53, 3, 43, 53, 16,
                    27, 16, 76, 14, 27, 2, 48, 17, 35, 60, 22, 12, 12, 16, 41, 37, 33, 42, 70, 98,
                    76, 15, 47, 75, 26, 76, 22, 68, 40, 17, 29, 43, 96, 97, 83, 11, 80, 25, 44, 37,
                    90, 37, 72, 54, 91, 52, 33, 92, 63,
                ]),
                2367,
            ),
            (
                (vec![
                    18, 44, 37, 75, 71, 95, 10, 12, 39, 77, 26, 90, 64, 17, 39, 18, 74, 46, 8, 52,
                    48, 88, 11, 16, 64, 91, 92, 5, 3, 45, 58, 1, 12, 10, 39, 51, 36, 80, 53, 4, 43,
                    69, 15, 44, 61, 91, 84, 100, 22, 5, 100, 33, 99, 41, 79, 44, 98, 6, 94, 32, 14,
                    33, 2, 75, 73, 92, 59, 30, 47, 88, 37, 55, 83, 23,
                ]),
                2924,
            ),
            (
                (vec![
                    40, 5, 90, 75, 87, 15, 77, 42, 53, 30, 21, 67, 32, 88, 97, 9, 7, 8, 87, 22, 38,
                    16, 8, 81, 8, 24, 13, 48, 68, 21, 69, 1, 13, 57, 99, 9, 61, 92, 69, 93, 87, 80,
                    26, 47, 79, 33, 2, 78, 32, 16, 99, 20, 90, 32, 33, 87, 25, 28, 10, 65, 15, 38,
                    74, 88, 75, 93, 32, 8, 62, 99, 44, 46, 83, 16, 43, 58, 6, 6,
                ]),
                3350,
            ),
            (
                (vec![
                    7, 34, 25, 38, 80, 59, 19, 86, 9, 9, 40, 54, 6, 29, 80, 37, 50, 37, 89, 6, 38,
                    11, 40, 2, 2, 17, 51,
                ]),
                835,
            ),
            (
                (vec![
                    18, 29, 12, 30, 46, 64, 27, 52, 64, 66, 83, 2, 57, 59, 78, 93, 8, 76, 47, 25,
                    22, 54, 51, 38, 91, 39, 10, 36, 76, 39, 81, 51, 68, 42, 59, 90, 95, 88, 58, 96,
                    77, 1, 30, 60, 72, 45, 47, 16, 81, 8, 47, 11, 4, 72, 98, 55, 17, 30, 12, 91,
                    33, 62, 51, 61, 91, 73, 8, 99, 91, 60, 34, 14, 40, 94, 100, 8, 39, 32, 16, 6,
                    38, 63, 37, 54, 27, 61, 36, 64, 11, 88, 1, 49, 95, 27, 19, 86,
                ]),
                4407,
            ),
            (
                (vec![
                    80, 91, 21, 12, 49, 77, 82, 14, 60, 65, 100, 95, 9, 36, 46, 3, 86, 1, 76, 61,
                    18, 84, 4, 60, 96, 85, 5, 83, 75, 72, 58, 87, 1, 90, 76, 18, 79, 19, 80, 93,
                    23, 22, 45, 15, 59, 74, 81, 92, 79, 79, 56, 42, 39, 50, 49, 33, 73, 10, 90, 96,
                    74, 62, 37, 99, 42, 12, 80, 67, 83, 93, 17, 51, 18, 82, 53, 38, 57, 76, 62, 42,
                    56, 66, 20,
                ]),
                3954,
            ),
            (
                (vec![
                    21, 49, 80, 62, 96, 33, 24, 6, 13, 71, 60, 37, 25, 96, 59, 12, 13, 42, 26, 57,
                    81, 63, 10, 71, 24, 59, 99, 29, 32, 5, 52, 3, 59,
                ]),
                1340,
            ),
            ((vec![67, 41, 16, 19, 49, 92, 97, 80, 24]), 31),
            (
                (vec![
                    28, 81, 5, 43, 74, 58, 80, 24, 23, 70, 83, 16, 62, 74, 20, 93, 17, 98, 27, 62,
                    69, 3, 66, 83, 100, 56, 69, 24, 62, 62, 61, 3, 19, 19, 96, 83, 34, 18, 13, 2,
                    64, 8, 88, 59, 74, 96, 66, 25,
                ]),
                1958,
            ),
            (
                (vec![
                    56, 36, 98, 88, 47, 43, 73, 83, 47, 78, 98, 46, 16, 96, 22, 27, 90, 47, 90, 44,
                    4, 22, 25, 90, 32, 30, 78, 96, 45, 92, 81, 75, 17, 3, 21, 63, 18, 50, 62, 85,
                    4, 33, 56, 84, 60, 16, 64,
                ]),
                2018,
            ),
            (
                (vec![
                    18, 83, 70, 11, 63, 21, 82, 45, 22, 80, 51, 36, 70, 82, 65, 61, 67, 46, 40, 2,
                    95, 78, 31, 74, 47, 78, 56, 93, 50, 52, 79, 53, 56, 91, 1, 36, 20, 62, 80, 87,
                    18, 100, 69, 39, 49, 72, 59, 23, 3, 48,
                ]),
                2571,
            ),
            (
                (vec![
                    47, 99, 3, 41, 36, 71, 34, 53, 73, 78, 35, 61, 26, 29, 16, 8, 5, 23, 12, 71,
                    72, 79, 89, 72, 28, 32, 65, 69, 88, 2, 93, 47, 85, 16, 47, 18, 78, 28, 47, 7,
                    75, 36, 79, 99, 70, 84, 32, 100, 25, 25, 18, 5, 33, 66, 27, 22, 34, 60, 19, 50,
                    57, 31, 7, 36, 62, 90, 69, 29, 68, 74, 94, 63, 4,
                ]),
                3256,
            ),
            (
                (vec![
                    34, 46, 54, 22, 56, 71, 35, 88, 75, 90, 68, 48, 2, 75, 11, 87, 64, 74, 49, 28,
                    26, 10, 25, 86, 8, 72, 14, 7, 49, 40, 87, 40, 94, 33, 83, 66, 2, 98, 77, 9, 48,
                    67, 66, 68, 16,
                ]),
                1779,
            ),
            (
                (vec![
                    20, 14, 15, 13, 93, 24, 36, 36, 89, 9, 24, 60, 55, 89, 9, 87, 15, 77, 15, 2, 3,
                    64, 70, 29, 14, 24, 48, 24, 45, 92, 77, 89, 11, 87, 57, 68, 7, 47, 98, 54, 31,
                    96, 41, 79, 99, 10, 68, 42, 58, 68, 48, 90, 51, 77, 61, 54, 19, 78, 45, 83, 67,
                    3, 63, 33, 89, 77, 67, 72, 91, 70, 54, 30, 37, 25, 25, 100, 25, 86, 38, 34, 79,
                    66, 59, 33, 3, 7, 5,
                ]),
                4095,
            ),
        ],
        |a, b| a == b,
    );
}
