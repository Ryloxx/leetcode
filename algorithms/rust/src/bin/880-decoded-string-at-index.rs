/*
 * @lc app=leetcode id=880 lang=rust
 *
 * [880] Decoded String at Index
 *
 * https://leetcode.com/problems/decoded-string-at-index/description/
 *
 * algorithms
 * Medium (28.57%)
 * Likes:    1589
 * Dislikes: 236
 * Total Accepted:    46.3K
 * Total Submissions: 151.8K
 * Testcase Example:  '"leet2code3"\n10'
 *
 * You are given an encoded string s. To decode the string to a tape, the
 * encoded string is read one character at a time and the following steps are
 * taken:
 *
 *
 * If the character read is a letter, that letter is written onto the tape.
 * If the character read is a digit d, the entire current tape is repeatedly
 * written d - 1 more times in total.
 *
 *
 * Given an integer k, return the k^th letter (1-indexed) in the decoded
 * string.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "leet2code3", k = 10
 * Output: "o"
 * Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
 * The 10^th letter in the string is "o".
 *
 *
 * Example 2:
 *
 *
 * Input: s = "ha22", k = 5
 * Output: "h"
 * Explanation: The decoded string is "hahahaha".
 * The 5^th letter is "h".
 *
 *
 * Example 3:
 *
 *
 * Input: s = "a2345678999999999999999", k = 1
 * Output: "a"
 * Explanation: The decoded string is "a" repeated 8301530446056247680 times.
 * The 1^st letter is "a".
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= s.length <= 100
 * s consists of lowercase English letters and digits 2 through 9.
 * s starts with a letter.
 * 1 <= k <= 10^9
 * It is guaranteed that k is less than or equal to the length of the decoded
 * string.
 * The decoded string is guaranteed to have less than 2^63 letters.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn decode_at_index(s: String, k: i32) -> String {
        let mut k = (k as i64) - 1;
        let mut total_length = 0i64;
        let mut i = 0;
        while i < s.len() {
            let c = s.as_bytes()[i];
            if c.is_ascii_digit() {
                total_length *= (c - b'0') as i64;
            } else {
                total_length += 1;
            }
            i += 1;
            if total_length > k {
                break;
            }
        }
        while i > 0 {
            i -= 1;
            let c = s.as_bytes()[i];
            if c.is_ascii_digit() {
                total_length /= (c - b'0') as i64;
                k %= total_length;
            } else {
                total_length -= 1;
                if total_length == k {
                    return (c as char).to_string();
                }
            }
        }
        panic!()
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::decode_at_index(e.0, e.1),
        vec![
            (("leet2code3".to_string(), 10), "o".to_string()),
            (("ha22".to_string(), 5), "h".to_string()),
            (("a2345678999999999999999".to_string(), 1), "a".to_string()),
            (("leet2code3".to_string(), 7), "e".to_string()),
            (("leet2code3".to_string(), 8), "t".to_string()),
            (("leet2code3".to_string(), 9), "c".to_string()),
            (("leet2code3".to_string(), 17), "l".to_string()),
            (("leet2code3".to_string(), 30), "e".to_string()),
            (("leet2code3".to_string(), 30), "e".to_string()),
            (("leet2code3".to_string(), 36), "e".to_string()),
            (("leet2code3".to_string(), 35), "d".to_string()),
            (("leetcode".to_string(), 3), "e".to_string()),
            (("leetcode".to_string(), 5), "c".to_string()),
            (("leetcode".to_string(), 1), "l".to_string()),
        ],
        |a, b| a == b,
    )
}
