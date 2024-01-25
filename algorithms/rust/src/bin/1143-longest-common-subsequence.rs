#![feature(test)]
/*
 * @lc app=leetcode id=1143 lang=rust
 *
 * [1143] Longest Common Subsequence
 *
 * https://leetcode.com/problems/longest-common-subsequence/description/
 *
 * algorithms
 * Medium (57.57%)
 * Likes:    12897
 * Dislikes: 172
 * Total Accepted:    928.2K
 * Total Submissions: 1.6M
 * Testcase Example:  '"abcde"\n"ace"'
 *
 * Given two strings text1 and text2, return the length of their longest
 * common subsequence. If there is no common subsequence, return 0.
 *
 * A subsequence of a string is a new string generated from the original
 * string with some characters (can be none) deleted without changing the
 * relative order of the remaining characters.
 *
 *
 * For example, "ace" is a subsequence of "abcde".
 *
 *
 * A common subsequence of two strings is a subsequence that is common to
 * both strings.
 *
 *
 * Example 1:
 *
 *
 * Input: text1 = "abcde", text2 = "ace"
 * Output: 3
 * Explanation: The longest common subsequence is "ace" and its length is 3.
 *
 *
 * Example 2:
 *
 *
 * Input: text1 = "abc", text2 = "abc"
 * Output: 3
 * Explanation: The longest common subsequence is "abc" and its length is 3.
 *
 *
 * Example 3:
 *
 *
 * Input: text1 = "abc", text2 = "def"
 * Output: 0
 * Explanation: There is no such common subsequence, so the result is 0.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= text1.length, text2.length <= 1000
 * text1 and text2 consist of only lowercase English characters.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn longest_common_subsequence(mut text1: String, mut text2: String) -> i32 {
        if text1.len() > text2.len() {
            std::mem::swap(&mut text1, &mut text2);
        }
        let text1 = &mut text1.as_bytes();
        let text2 = &mut text2.as_bytes();
        let mut row1 = vec![0; text1.len()];
        let mut row2 = vec![0; row1.len()];
        for text2 in text2.iter() {
            let mut left = 0;
            let mut top_left = 0;
            for ((top, current), text1) in row1.iter().zip(row2.iter_mut()).zip(text1.iter()) {
                *current = if text1 == text2 {
                    top_left + 1
                } else {
                    left.max(*top)
                };
                left = *current;
                top_left = *top;
            }
            std::mem::swap(&mut row1, &mut row2);
        }
        *row1.last().unwrap()
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::longest_common_subsequence(e.0, e.1),
        vec![
            //
            (("abcde".to_string(), "ace".to_string()), 3),
            (("abc".to_string(), "abc".to_string()), 3),
            (("abc".to_string(), "def".to_string()), 0),
            (("ac".to_string(), "bc".to_string()), 1),
            (("bl".to_string(), "yby".to_string()), 1),
            (
                (
                    "fcvqfcnglshwpgxujwrylqzejmdubkxs".to_string(),
                    "bctsfwdelkdqzshupmrufyxklsjurevip".to_string(),
                ),
                11,
            ),
            (("abcdefghij".to_string(), "ace".to_string()), 3),
        ],
        |a, b| a == b,
    )
}

#[cfg(test)]
mod test {
    use test::Bencher;

    use crate::Solution;

    extern crate test;

    #[bench]
    fn tempz(b: &mut Bencher) {
        b.iter(|| {
            Solution::longest_common_subsequence(
                "fcvqfcnglshwpgxujwrylqzejmdubkxs".to_string(),
                "bctsfwdelkdqzshupmrufyxklsjurevip".to_string(),
            );
        });
    }
}
