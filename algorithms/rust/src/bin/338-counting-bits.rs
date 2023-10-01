/*
 * @lc app=leetcode id=338 lang=rust
 *
 * [338] Counting Bits
 *
 * https://leetcode.com/problems/counting-bits/description/
 *
 * algorithms
 * Easy (75.37%)
 * Likes:    9654
 * Dislikes: 451
 * Total Accepted:    860.5K
 * Total Submissions: 1.1M
 * Testcase Example:  '2'
 *
 * Given an integer n, return an array ans of length n + 1 such that for each
 * i (0 <= i <= n), ans[i] is the number of 1's in the binary representation
 * of i.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 2
 * Output: [0,1,1]
 * Explanation:
 * 0 --> 0
 * 1 --> 1
 * 2 --> 10
 *
 *
 * Example 2:
 *
 *
 * Input: n = 5
 * Output: [0,1,1,2,1,2]
 * Explanation:
 * 0 --> 0
 * 1 --> 1
 * 2 --> 10
 * 3 --> 11
 * 4 --> 100
 * 5 --> 101
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= n <= 10^5
 *
 *
 *
 * Follow up:
 *
 *
 * It is very easy to come up with a solution with a runtime of O(n log n).
 * Can you do it in linear time O(n) and possibly in a single pass?
 * Can you do it without using any built-in function (i.e., like
 * __builtin_popcount in C++)?
 *
 *
 */
struct Solution;
// @lc code=start

impl Solution {
    // O(N) time complexity
    // O(1) space complexity
    pub fn count_bits(n: i32) -> Vec<i32> {
        let n = n as usize + 1;
        let mut res = vec![0; n];
        let mut i = 1;
        while i < n {
            for j in 0..i.min(n - i) {
                res[i + j] = res[j] + 1;
            }
            i <<= 1;
        }
        res
    }
    // Shorter
    // O(N) time complexity
    // O(1) space complexity
    // pub fn count_bits(n: i32) -> Vec<i32> {
    //     let n = n as usize + 1;
    //     let mut res = Vec::with_capacity(n);
    //     res.push(0);
    //     for i in 1..n {
    //         res.push(res[i & (i - 1)] + 1);
    //     }
    //     res
    // }

    // O(N) time complexity (count_ones() use ctpop intrinsic which is constant
    // time)
    // O(1) space complexity
    // pub fn count_bits(n: i32) -> Vec<i32> {
    //     let mut res = Vec::with_capacity(n as usize + 1);
    //     for i in 0..(n + 1) {
    //         res.push(i.count_ones() as i32);
    //     }
    //     res
    // }

    // O(NlogN) time complexity
    // O(1) space complexity
    // pub fn count_bits(n: i32) -> Vec<i32> {
    //     let mut res = Vec::with_capacity(n as usize + 1);
    //     for mut i in 0..(n + 1) {
    //         let mut val = 0;
    //         while i > 0 {
    //             val += i & 1;
    //             i >>= 1;
    //         }
    //         res.push(val);
    //     }
    //     res
    // }
}

// const N: usize = 1 << 17;
// const PRE_COMPUTED: [i32; N] = {
//     let mut res = [0; N];
//     let mut i: usize = 1;
//     while i < N {
//         let mut j = 0;
//         while j < i {
//             res[i + j] = res[j] + 1;
//             j += 1;
//         }
//         i <<= 1;
//     }
//     res
// };
// impl Solution {
//     // Precomputed
//     // O(N) time complexity
//     // O(1) space complexity
//     pub fn count_bits(n: i32) -> Vec<i32> {
//         Vec::from(&PRE_COMPUTED[..(n + 1) as usize])
//     }
// }
// @lc code=end
fn main() {
    rust::test_algo(
        Solution::count_bits,
        vec![
            ((2), vec![0, 1, 1]),
            ((5), vec![0, 1, 1, 2, 1, 2]),
            ((0), vec![0]),
            (
                (100),
                vec![
                    0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3,
                    3, 4, 3, 4, 4, 5, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4,
                    3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4,
                    4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3,
                ],
            ),
        ],
        |a, b| a == b,
    );
}
