/*
 * @lc app=leetcode id=1759 lang=rust
 *
 * [1759] Count Number of Homogenous Substrings
 *
 * https://leetcode.com/problems/count-number-of-homogenous-substrings/description/
 *
 * algorithms
 * Medium (48.90%)
 * Likes:    919
 * Dislikes: 57
 * Total Accepted:    49.2K
 * Total Submissions: 89.9K
 * Testcase Example:  '"abbcccaa"'
 *
 * Given a string s, return the number of homogenous substrings of s. Since
 * the answer may be too large, return it modulo 10^9 + 7.
 *
 * A string is homogenous if all the characters of the string are the same.
 *
 * A substring is a contiguous sequence of characters within a string.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abbcccaa"
 * Output: 13
 * Explanation: The homogenous substrings are listed as below:
 * "a"   appears 3 times.
 * "aa"  appears 1 time.
 * "b"   appears 2 times.
 * "bb"  appears 1 time.
 * "c"   appears 3 times.
 * "cc"  appears 2 times.
 * "ccc" appears 1 time.
 * 3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
 *
 * Example 2:
 *
 *
 * Input: s = "xy"
 * Output: 2
 * Explanation: The homogenous substrings are "x" and "y".
 *
 * Example 3:
 *
 *
 * Input: s = "zzzzz"
 * Output: 15
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s consists of lowercase letters.
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn count_homogenous(s: String) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let mut streak = 0;
        let mut res = 0;
        let mut last = b'\0';
        for &c in s.as_bytes() {
            if c == last {
                streak += 1;
            } else {
                streak = 1;
                last = c;
            }
            res += streak;
            res %= MOD;
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::count_homogenous,
        vec![
            (("abbcccaa".to_string()), 13),
            (("xy".to_string()), 2),
            (("zzzzz".to_string()), 15),
            (("".to_string()), 0),
        ],
        |a, b| a == b,
    );
}
