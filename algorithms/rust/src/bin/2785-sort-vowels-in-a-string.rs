/*
 * @lc app=leetcode id=2785 lang=rust
 *
 * [2785] Sort Vowels in a String
 *
 * https://leetcode.com/problems/sort-vowels-in-a-string/description/
 *
 * algorithms
 * Medium (76.07%)
 * Likes:    502
 * Dislikes: 27
 * Total Accepted:    57.9K
 * Total Submissions: 71.6K
 * Testcase Example:  '"lEetcOde"'
 *
 * Given a 0-indexed string s, permute s to get a new string t such that:
 *
 *
 * All consonants remain in their original places. More formally, if there is
 * an index i with 0 <= i < s.length such that s[i] is a consonant, then t[i]
 * = s[i].
 * The vowels must be sorted in the nondecreasing order of their ASCII
 * values. More formally, for pairs of indices i, j with 0 <= i < j <
 * s.length such that s[i] and s[j] are vowels, then t[i] must not have a
 * higher ASCII value than t[j].
 *
 *
 * Return the resulting string.
 *
 * The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in
 * lowercase or uppercase. Consonants comprise all letters that are not
 * vowels.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "lEetcOde"
 * Output: "lEOtcede"
 * Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd'
 * are all consonants. The vowels are sorted according to their ASCII values,
 * and the consonants remain in the same places.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "lYmpH"
 * Output: "lYmpH"
 * Explanation: There are no vowels in s (all characters in s are
 * consonants), so we return "lYmpH".
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * s consists only of letters of the English alphabet in uppercase and
 * lowercase.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn sort_vowels(mut s: String) -> String {
        const BASE: u8 = b'A';
        const SIZE: usize = (b'z' - BASE) as usize + 1;
        const SKIP_CHARS: [u8; 10] = [b'a', b'e', b'i', b'o', b'u', b'A', b'E', b'I', b'O', b'U'];
        const SKIP_LIST: [bool; SIZE] = {
            let mut temp = [true; SIZE];
            let mut i = 0;
            while i < SKIP_CHARS.len() {
                temp[(SKIP_CHARS[i] - BASE) as usize] = false;
                i += 1;
            }
            temp
        };
        let mut cnts = vec![0; SIZE];
        unsafe {
            let s_bytes = s.as_bytes_mut();
            for c in s_bytes.iter() {
                if !SKIP_LIST[(*c - BASE) as usize] {
                    cnts[(c - BASE) as usize] += 1;
                }
            }
            let mut i = 0;
            for c in s_bytes {
                if SKIP_LIST[(*c - BASE) as usize] {
                    continue;
                }
                while i < cnts.len() && cnts[i] == 0 {
                    i += 1;
                }
                if i == cnts.len() {
                    break;
                }
                cnts[i] -= 1;
                *c = (i as u8) + BASE;
            }
        }
        s
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::sort_vowels,
        vec![
            (("lEetcOde".to_string()), "lEOtcede".to_string()),
            (("lYmpH".to_string()), "lYmpH".to_string()),
            (("".to_string()), "".to_string()),
            (("aeiou".to_string()), "aeiou".to_string()),
            (("uoiea".to_string()), "aeiou".to_string()),
            (("ziF".to_string()), "ziF".to_string()),
        ],
        |a, b| a == b,
    );
}
