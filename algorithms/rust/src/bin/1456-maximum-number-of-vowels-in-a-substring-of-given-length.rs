/*
 * @lc app=leetcode id=1456 lang=rust
 *
 * [1456] Maximum Number of Vowels in a Substring of Given Length
 *
 * https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
 *
 * algorithms
 * Medium (58.13%)
 * Likes:    1956
 * Dislikes: 68
 * Total Accepted:    99.6K
 * Total Submissions: 167.2K
 * Testcase Example:  '"abciiidef"\n3'
 *
 * Given a string s and an integer k, return the maximum number of vowel
 * letters in any substring of s with length k.
 *
 * Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abciiidef", k = 3
 * Output: 3
 * Explanation: The substring "iii" contains 3 vowel letters.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "aeiou", k = 2
 * Output: 2
 * Explanation: Any substring of length 2 contains 2 vowels.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "leetcode", k = 3
 * Output: 2
 * Explanation: "lee", "eet" and "ode" contain 2 vowels.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s consists of lowercase English letters.
 * 1 <= k <= s.length
 *
 *
 */
struct Solution;

// @lc code=start
impl Solution {
    pub fn max_vowels(s: String, k: i32) -> i32 {
        let s = s.as_bytes();
        (0..s.len())
            .fold((0, 0), |mut acc, idx| {
                acc.1 += 0x104111 >> (s[idx] - b'a') & 1;
                let idx = idx as i32 - k;
                if idx >= 0 {
                    acc.1 -= 0x104111 >> (s[idx as usize] - b'a') & 1
                }
                acc.0 = acc.0.max(acc.1);
                acc
            })
            .0
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |(s, k)| Solution::max_vowels(s.to_string(), k),
        vec![
            (("abciiidef", 3), 3),
            (("aeiou", 2), 2),
            (("leetcode", 3), 2),
            (("", 3), 0),
            (("aaaaa", 5), 5),
            (("aaaaa", 3), 3),
            (("zzzz", 5), 0),
            (("zzzzz", 5), 0),
            (("a", 1), 1),
            (("a", 0), 0),
            (("tryhard", 4), 1),
        ],
        |a, b| a == b,
    )
}
