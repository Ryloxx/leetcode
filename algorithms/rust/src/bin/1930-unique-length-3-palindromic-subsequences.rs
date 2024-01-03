/*
 * @lc app=leetcode id=1930 lang=rust
 *
 * [1930] Unique Length-3 Palindromic Subsequences
 *
 * https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
 *
 * algorithms
 * Medium (53.39%)
 * Likes:    1138
 * Dislikes: 42
 * Total Accepted:    52.7K
 * Total Submissions: 86.1K
 * Testcase Example:  '"aabca"'
 *
 * Given a string s, return the number of unique palindromes of length three
 * that are a subsequence of s.
 *
 * Note that even if there are multiple ways to obtain the same subsequence,
 * it is still only counted once.
 *
 * A palindrome is a string that reads the same forwards and backwards.
 *
 * A subsequence of a string is a new string generated from the original
 * string with some characters (can be none) deleted without changing the
 * relative order of the remaining characters.
 *
 *
 * For example, "ace" is a subsequence of "abcde".
 *
 *
 *
 * Example 1:
 *
 *
 * Input: s = "aabca"
 * Output: 3
 * Explanation: The 3 palindromic subsequences of length 3 are:
 * - "aba" (subsequence of "aabca")
 * - "aaa" (subsequence of "aabca")
 * - "aca" (subsequence of "aabca")
 *
 *
 * Example 2:
 *
 *
 * Input: s = "adc"
 * Output: 0
 * Explanation: There are no palindromic subsequences of length 3 in "adc".
 *
 *
 * Example 3:
 *
 *
 * Input: s = "bbcbaba"
 * Output: 4
 * Explanation: The 4 palindromic subsequences of length 3 are:
 * - "bbb" (subsequence of "bbcbaba")
 * - "bcb" (subsequence of "bbcbaba")
 * - "bab" (subsequence of "bbcbaba")
 * - "aba" (subsequence of "bbcbaba")
 *
 *
 *
 * Constraints:
 *
 *
 * 3 <= s.length <= 10^5
 * s consists of only lowercase English letters.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    // Using prefix array
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let s_bytes = s.as_bytes();
        let mut prefix = vec![0; (s.len() + 1) * 26];
        let mut first = [!0; 26];
        let mut last = [!0; 26];
        let mut res = 0;
        for (idx, c) in s_bytes.iter().enumerate() {
            prefix.copy_within(idx * 26..idx * 26 + 26, (idx + 1) * 26);
            prefix[(idx + 1) * 26 + (c - b'a') as usize] += 1;
            last[(c - b'a') as usize] = idx;
            if first[(c - b'a') as usize] == !0 {
                first[(c - b'a') as usize] = idx;
            }
        }
        for idx in first {
            if idx >= s.len() {
                continue;
            }
            let c = s_bytes[idx];
            let right = (last[(c - b'a') as usize]) * 26;
            let left = (idx + 1) * 26;
            for offset in b'a'..=b'z' {
                let offset = (offset - b'a') as usize;
                res += (prefix[right + offset] - prefix[left + offset] > 0) as i32;
            }
        }
        res
    }

    // pub fn count_palindromic_subsequence(s: String) -> i32 {
    //     let s_bytes = s.as_bytes();
    //     let mut first = [!0; 26];
    //     let mut last = [!0; 26];
    //     let mut res = 0;
    //     for (idx, c) in s_bytes.iter().enumerate() {
    //         last[(c - b'a') as usize] = idx;
    //         if first[(c - b'a') as usize] == !0 {
    //             first[(c - b'a') as usize] = idx;
    //         }
    //     }
    //     let mut seen = [false; 26];
    //     for first in first {
    //         if first >= s.len() {
    //             continue;
    //         }
    //         seen.fill(false);
    //         let c = s_bytes[first];
    //         let last = last[(c - b'a') as usize];
    //         for idx in first + 1..last {
    //             let seen = &mut seen[(s_bytes[idx] - b'a') as usize];
    //             if !*seen {
    //                 res += 1;
    //             }
    //             *seen = true;
    //         }
    //     }
    //     res
    // }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::count_palindromic_subsequence,
        vec![
            (("aabca".to_string()), 3),
            (("adc".to_string()), 0),
            (("bbcbaba".to_string()), 4),
            (("".to_string()), 0),
            (("a".to_string()), 0),
            (("aa".to_string()), 0),
            (("aaa".to_string()), 1),
            ((String::from_iter(std::iter::repeat('a').take(10_000))), 1),
        ],
        |a, b| a == b,
    );
}
