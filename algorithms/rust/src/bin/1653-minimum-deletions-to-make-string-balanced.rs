/*
 * @lc app=leetcode id=1653 lang=rust
 *
 * [1653] Minimum Deletions to Make String Balanced
 *
 * https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/
 *
 * algorithms
 * Medium (58.76%)
 * Likes:    1411
 * Dislikes: 43
 * Total Accepted:    54.7K
 * Total Submissions: 90.3K
 * Testcase Example:  '"aababbab"'
 *
 * You are given a string s consisting only of characters 'a' and 'b'​​​​.
 *
 * You can delete any number of characters in s to make s balanced. s is
 * balanced if there is no pair of indices (i,j) such that i < j and s[i] =
 * 'b' and s[j]= 'a'.
 *
 * Return the minimum number of deletions needed to make s balanced.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "aababbab"
 * Output: 2
 * Explanation: You can either:
 * Delete the characters at 0-indexed positions 2 and 6 ("aababbab" ->
 * "aaabbb"), or
 * Delete the characters at 0-indexed positions 3 and 6 ("aababbab" ->
 * "aabbbb").
 *
 *
 * Example 2:
 *
 *
 * Input: s = "bbaaaaabb"
 * Output: 2
 * Explanation: The only solution is to delete the first two characters.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s[i] is 'a' or 'b'​​.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn minimum_deletions(s: String) -> i32 {
        std::iter::once(&b'a')
            .chain(s.as_bytes().iter())
            .scan(0, |acc, curr| {
                *acc += (((curr - b'a') as i32) << 1) - 1;
                Some(*acc)
            })
            .min()
            .unwrap_or_default()
            + (s.as_bytes().iter().filter(|&&x| x == b'a').count() as i32)
            + 1
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::minimum_deletions,
        vec![
            (("aababbab".to_string()), 2),
            (("bbaaaaabb".to_string()), 2),
            (("b".to_string()), 0),
            (("a".to_string()), 0),
            (("".to_string()), 0),
        ],
        |a, b| a == b,
    )
}
