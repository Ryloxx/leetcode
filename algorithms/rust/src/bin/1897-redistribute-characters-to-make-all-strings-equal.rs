/*
 * @lc app=leetcode id=1897 lang=rust
 *
 * [1897] Redistribute Characters to Make All Strings Equal
 *
 * https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/
 *
 * algorithms
 * Easy (59.11%)
 * Likes:    765
 * Dislikes: 59
 * Total Accepted:    74.4K
 * Total Submissions: 113.2K
 * Testcase Example:  '["abc","aabc","bc"]'
 *
 * You are given an array of strings words (0-indexed).
 *
 * In one operation, pick two distinct indices i and j, where words[i] is a
 * non-empty string, and move any character from words[i] to any position in
 * words[j].
 *
 * Return true if you can make every string in words equal using any number
 * of operations, and false otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: words = ["abc","aabc","bc"]
 * Output: true
 * Explanation: Move the first 'a' in words[1] to the front of words[2],
 * to make words[1] = "abc" and words[2] = "abc".
 * All the strings are now equal to "abc", so return true.
 *
 *
 * Example 2:
 *
 *
 * Input: words = ["ab","a"]
 * Output: false
 * Explanation: It is impossible to make all the strings equal using the
 * operation.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= words.length <= 100
 * 1 <= words[i].length <= 100
 * words[i] consists of lowercase English letters.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn make_equal(words: Vec<String>) -> bool {
        let len = words.len();
        let mut cnt = [0; 26];
        for w in words {
            for c in w.as_bytes() {
                cnt[(c - b'a') as usize] += 1;
            }
        }
        for c in cnt {
            if c % len != 0 {
                return false;
            }
        }
        true
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::make_equal,
        vec![
            (
                (["abc", "aabc", "bc"]
                    .into_iter()
                    .map(String::from)
                    .collect()),
                true,
            ),
            ((["ab", "a"].into_iter().map(String::from).collect()), false),
        ],
        |a, b| a == b,
    );
}
