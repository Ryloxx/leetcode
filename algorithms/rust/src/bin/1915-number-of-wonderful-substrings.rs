/*
 * @lc app=leetcode id=1915 lang=rust
 *
 * [1915] Number of Wonderful Substrings
 *
 * https://leetcode.com/problems/number-of-wonderful-substrings/description/
 *
 * algorithms
 * Medium (46.81%)
 * Likes:    1080
 * Dislikes: 96
 * Total Accepted:    21.4K
 * Total Submissions: 40.2K
 * Testcase Example:  '"aba"'
 *
 * A wonderful string is a string where at most one letter appears an odd
 * number of times.
 *
 *
 * For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
 *
 *
 * Given a string word that consists of the first ten lowercase English
 * letters ('a' through 'j'), return the number of wonderful non-empty
 * substrings in word. If the same substring appears multiple times in word,
 * then count each occurrence separately.
 *
 * A substring is a contiguous sequence of characters in a string.
 *
 *
 * Example 1:
 *
 *
 * Input: word = "aba"
 * Output: 4
 * Explanation: The four wonderful substrings are underlined below:
 * - "aba" -> "a"
 * - "aba" -> "b"
 * - "aba" -> "a"
 * - "aba" -> "aba"
 *
 *
 * Example 2:
 *
 *
 * Input: word = "aabb"
 * Output: 9
 * Explanation: The nine wonderful substrings are underlined below:
 * - "aabb" -> "a"
 * - "aabb" -> "aa"
 * - "aabb" -> "aab"
 * - "aabb" -> "aabb"
 * - "aabb" -> "a"
 * - "aabb" -> "abb"
 * - "aabb" -> "b"
 * - "aabb" -> "bb"
 * - "aabb" -> "b"
 *
 *
 * Example 3:
 *
 *
 * Input: word = "he"
 * Output: 2
 * Explanation: The two wonderful substrings are underlined below:
 * - "he" -> "h"
 * - "he" -> "e"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= word.length <= 10^5
 * word consists of lowercase English letters from 'a' to 'j'.
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn wonderful_substrings(word: String) -> i64 {
        let mut freqs: [i64; 1024] = [0; 1024];
        let mut mask = 0;
        let mut res = 0;
        freqs[0] = 1;
        for c in word.as_bytes() {
            mask ^= 1 << (*c - b'a');
            res += freqs[mask] + (0..10).map(|i| freqs[mask ^ 1 << i]).sum::<i64>();
            freqs[mask] += 1;
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::wonderful_substrings,
        vec![(("aba".to_string()), 4), (("aabb".to_string()), 9)],
        |a, b| a == b,
    )
}
