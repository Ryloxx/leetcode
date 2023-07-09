/*
 * @lc app=leetcode id=2272 lang=rust
 *
 * [2272] Substring With Largest Variance
 *
 * https://leetcode.com/problems/substring-with-largest-variance/description/
 *
 * algorithms
 * Hard (37.34%)
 * Likes:    1465
 * Dislikes: 172
 * Total Accepted:    48.8K
 * Total Submissions: 108.2K
 * Testcase Example:  '"aababbb"'
 *
 * The variance of a string is defined as the largest difference between the
 * number of occurrences of any 2 characters present in the string. Note the
 * two characters may or may not be the same.
 *
 * Given a string s consisting of lowercase English letters only, return the
 * largest variance possible among all substrings of s.
 *
 * A substring is a contiguous sequence of characters within a string.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "aababbb"
 * Output: 3
 * Explanation:
 * All possible variances along with their respective substrings are listed
 * below:
 * - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b",
 * "bb", and "bbb".
 * - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb",
 * "aababbb", and "bab".
 * - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
 * - Variance 3 for substring "babbb".
 * Since the largest possible variance is 3, we return it.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "abcde"
 * Output: 0
 * Explanation:
 * No letter occurs more than once in s, so the variance of every substring
 * is 0.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^4
 * s consists of lowercase English letters.
 *
 *
 */

struct Solution;

// @lc code=start
impl Solution {
    pub fn largest_variance(s: String) -> i32 {
        let mut res = 0;
        let letters = s
            .as_bytes()
            .iter()
            .fold(0, |acc, curr| acc | 1 << curr - b'a');
        for a in b'a'..=b'z' {
            if letters & 1 << a - b'a' == 0 {
                continue;
            }
            for b in b'a'..=b'z' {
                if letters & 1 << b - b'a' == 0 {
                    continue;
                }
                let mut curr_a = 0;
                let mut curr_b = 0;
                let mut count_b = s.as_bytes().iter().filter(|&&x| x == b).count();
                let mut max = 0;
                for c in s.as_bytes() {
                    if *c == a {
                        curr_a += 1;
                    }
                    if *c == b {
                        curr_b += 1;
                        count_b -= 1;
                    }
                    let diff = curr_a - curr_b;
                    if diff < 0 && count_b > 0 {
                        curr_a = 0;
                        curr_b = 0;
                    }
                    if curr_b > 0 {
                        max = max.max(diff);
                    }
                }
                res = res.max(max);
            }
        }
        res
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::largest_variance(e),
        vec![
            //
            (("aababbb".to_string()), 3),
            (("abcde".to_string()), 0),
            (("bbbbbb".to_string()), 0),
            (("abb".to_string()), 1),
            (("abbaaabzaabaaaaaaaaaaaaa".to_string()), 18),
        ],
        |a, b| a == b,
    );
}
