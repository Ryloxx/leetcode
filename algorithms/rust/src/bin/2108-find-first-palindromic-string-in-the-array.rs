/*
 * @lc app=leetcode id=2108 lang=rust
 *
 * [2108] Find First Palindromic String in the Array
 *
 * https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
 *
 * algorithms
 * Easy (79.09%)
 * Likes:    1332
 * Dislikes: 46
 * Total Accepted:    197.4K
 * Total Submissions: 237.4K
 * Testcase Example:  '["abc","car","ada","racecar","cool"]'
 *
 * Given an array of strings words, return the first palindromic string in
 * the array. If there is no such string, return an empty string "".
 *
 * A string is palindromic if it reads the same forward and backward.
 *
 *
 * Example 1:
 *
 *
 * Input: words = ["abc","car","ada","racecar","cool"]
 * Output: "ada"
 * Explanation: The first string that is palindromic is "ada".
 * Note that "racecar" is also palindromic, but it is not the first.
 *
 *
 * Example 2:
 *
 *
 * Input: words = ["notapalindrome","racecar"]
 * Output: "racecar"
 * Explanation: The first and only string that is palindromic is "racecar".
 *
 *
 * Example 3:
 *
 *
 * Input: words = ["def","ghi"]
 * Output: ""
 * Explanation: There are no palindromic strings, so the empty string is
 * returned.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= words.length <= 100
 * 1 <= words[i].length <= 100
 * words[i] consists only of lowercase English letters.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn first_palindrome(words: Vec<String>) -> String {
        'outer: for word in words.into_iter() {
            let word_b = word.as_bytes();
            let mut i = 0;
            let mut j = word_b.len() - 1;
            while i < j {
                if word_b[i] != word_b[j] {
                    continue 'outer;
                }
                i += 1;
                j -= 1;
            }
            return word;
        }
        "".to_string()
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::first_palindrome,
        vec![
            (
                ["abc", "car", "ada", "racecar", "cool"]
                    .into_iter()
                    .map(String::from)
                    .collect::<Vec<String>>(),
                "ada".to_string(),
            ),
            (
                ["notapalindrome", "racecar"]
                    .into_iter()
                    .map(String::from)
                    .collect::<Vec<String>>(),
                "racecar".to_string(),
            ),
            (
                ["def", "ghi"]
                    .into_iter()
                    .map(String::from)
                    .collect::<Vec<String>>(),
                "".to_string(),
            ),
        ],
        |a, b| a == b,
    )
}
