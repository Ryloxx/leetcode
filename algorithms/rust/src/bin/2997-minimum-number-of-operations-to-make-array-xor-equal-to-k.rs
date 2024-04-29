/*
 * @lc app=leetcode id=2997 lang=rust
 *
 * [2997] Minimum Number of Operations to Make Array XOR Equal to K
 *
 * https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/
 *
 * algorithms
 * Medium (77.25%)
 * Likes:    333
 * Dislikes: 34
 * Total Accepted:    58.2K
 * Total Submissions: 68.7K
 * Testcase Example:  '[2,1,3,4]\n1'
 *
 * You are given a 0-indexed integer array nums and a positive integer k.
 *
 * You can apply the following operation on the array any number of
 * times:
 *
 *
 * Choose any element of the array and flip a bit in its binary
 * representation. Flipping a bit means changing a 0 to 1 or vice versa.
 *
 *
 * Return the minimum number of operations required to make the bitwise XOR
 * of all elements of the final array equal to k.
 *
 * Note that you can flip leading zero bits in the binary representation of
 * elements. For example, for the number (101)2 you can flip the fourth bit
 * and obtain (1101)2.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [2,1,3,4], k = 1
 * Output: 2
 * Explanation: We can do the following operations:
 * - Choose element 2 which is 3 == (011)2, we flip the first bit and we
 *   obtain
 * (010)2 == 2. nums becomes [2,1,2,4].
 * - Choose element 0 which is 2 == (010)2, we flip the third bit and we
 *   obtain
 * (110)2 = 6. nums becomes [6,1,2,4].
 * The XOR of elements of the final array is (6 XOR 1 XOR 2 XOR 4) == 1 == k.
 * It can be shown that we cannot make the XOR equal to k in less than 2
 * operations.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [2,0,2,0], k = 0
 * Output: 0
 * Explanation: The XOR of elements of the array is (2 XOR 0 XOR 2 XOR 0) ==
 * 0 == k. So no operation is needed.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * 0 <= nums[i] <= 10^6
 * 0 <= k <= 10^6
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        ((nums.into_iter().fold(k, |acc, curr| acc ^ curr)) as u32).count_ones() as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::min_operations(e.0, e.1),
        vec![
            ((vec![2, 1, 3, 4], 1), 2),
            ((vec![2, 0, 2, 0], 0), 0),
            ((vec![2, 0, 2, 0], 0), 0),
            ((vec![183693, 468362, 187535, 753191], 686598), 8),
            (
                (
                    vec![
                        374477, 99579, 17220, 210136, 289284, 32693, 149636, 804831, 865877,
                        934930, 968903, 685339, 945667, 747399, 498426, 883120, 794526, 665481,
                        930861,
                    ],
                    371295,
                ),
                9,
            ),
            (
                (
                    vec![24632, 838162, 675305, 183686, 49998, 948324, 737984, 950976],
                    655422,
                ),
                8,
            ),
            (
                (
                    vec![
                        481698, 298266, 729739, 537967, 872035, 280843, 755486, 500429, 240975,
                        101236, 109841, 360816, 321898, 353436, 892406, 772416, 86727, 510010,
                        830291,
                    ],
                    355144,
                ),
                10,
            ),
            (
                (
                    vec![
                        525603, 35467, 472627, 350600, 792331, 949127, 285211, 414006, 934171,
                        405479, 17408, 769458, 833291, 115660, 358894, 331002, 726138, 438352,
                    ],
                    178607,
                ),
                9,
            ),
            (
                (vec![204836, 267230, 775785, 920338, 528060, 958570], 266451),
                4,
            ),
            ((vec![59032, 536446, 138655], 153029), 8),
            (
                (vec![437549, 118271, 440917, 304485, 304485, 626999], 933685),
                9,
            ),
            (
                (
                    vec![
                        499108, 345336, 854412, 606898, 869329, 305883, 752342, 702314, 809726,
                        920362, 433578, 39803, 739683, 807943, 640108, 666054, 252843, 490973,
                    ],
                    631560,
                ),
                7,
            ),
            ((vec![340055, 342953, 103056, 457330, 347455], 565256), 10),
        ],
        |a, b| a == b,
    )
}
