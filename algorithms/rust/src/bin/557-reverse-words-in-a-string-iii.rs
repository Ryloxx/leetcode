/*
 * @lc app=leetcode id=557 lang=rust
 *
 * [557] Reverse Words in a String III
 *
 * https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
 *
 * algorithms
 * Easy (81.99%)
 * Likes:    5370
 * Dislikes: 234
 * Total Accepted:    764.2K
 * Total Submissions: 927K
 * Testcase Example:  `"Let's take LeetCode contest"`
 *
 * Given a string s, reverse the order of characters in each word within a
 * sentence while still preserving whitespace and initial word order.
 *
 *
 * Example 1:
 * Input: s = "Let's take LeetCode contest"
 * Output: "s'teL ekat edoCteeL tsetnoc"
 * Example 2:
 * Input: s = "God Ding"
 * Output: "doG gniD"
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 5 * 10^4
 * s contains printable ASCII characters.
 * s does not contain any leading or trailing spaces.
 * There is at least one word in s.
 * All the words in s are separated by a single space.
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn reverse_words(mut s: String) -> String {
        unsafe {
            s.as_bytes_mut()
                .split_mut(u8::is_ascii_whitespace)
                .for_each(|x| x.reverse());
        }
        s
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::reverse_words,
        vec![
            (
                ("Let's take LeetCode contest".to_string()),
                "s'teL ekat edoCteeL tsetnoc".to_string(),
            ),
            (("God Ding".to_string()), "doG gniD".to_string()),
        ],
        |a, b| a == b,
    )
}
