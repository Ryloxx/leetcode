/*
 * @lc app=leetcode id=552 lang=rust
 *
 * [552] Student Attendance Record II
 *
 * https://leetcode.com/problems/student-attendance-record-ii/description/
 *
 * algorithms
 * Hard (42.77%)
 * Likes:    1991
 * Dislikes: 265
 * Total Accepted:    93.7K
 * Total Submissions: 192K
 * Testcase Example:  '2'
 *
 * An attendance record for a student can be represented as a string where
 * each character signifies whether the student was absent, late, or present
 * on that day. The record only contains the following three characters:
 *
 *
 * 'A': Absent.
 * 'L': Late.
 * 'P': Present.
 *
 *
 * Any student is eligible for an attendance award if they meet both of the
 * following criteria:
 *
 *
 * The student was absent ('A') for strictly fewer than 2 days total.
 * The student was never late ('L') for 3 or more consecutive days.
 *
 *
 * Given an integer n, return the number of possible attendance records of
 * length n that make a student eligible for an attendance award. The answer
 * may be very large, so return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 2
 * Output: 8
 * Explanation: There are 8 records with length 2 that are eligible for an
 * award:
 * "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
 * Only "AA" is not eligible because there are 2 absences (there need to be
 * fewer than 2).
 *
 *
 * Example 2:
 *
 *
 * Input: n = 1
 * Output: 3
 *
 *
 * Example 3:
 *
 *
 * Input: n = 10101
 * Output: 183236316
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 10^5
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn check_record(n: i32) -> i32 {
        const MOD: u64 = 1_000_000_007;
        let mut dp = [1; 12];
        let (mut dpa, mut dpb) = dp.split_at_mut(6);
        for _ in 0..n {
            if dpa[0] >= 0x5555555555555555 {
                dpa.iter_mut().for_each(|v| *v %= MOD);
            }
            std::mem::swap(&mut dpa, &mut dpb);
            dpa[5] = dpb[3];
            dpa[4] = dpb[3] + dpb[5];
            dpa[3] = dpb[3] + dpb[4];
            dpa[2] = dpb[3] + dpb[0];
            dpa[1] = dpb[3] + dpb[2] + dpb[0];
            dpa[0] = dpb[3] + dpb[1] + dpb[0];
        }
        (dpa[0] % MOD) as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::check_record,
        vec![((2), 8), ((1), 3), ((10101), 183236316)],
        |a, b| a == b,
    )
}
