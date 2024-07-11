/*
 * @lc app=leetcode id=1190 lang=rust
 *
 * [1190] Reverse Substrings Between Each Pair of Parentheses
 *
 * https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
 *
 * algorithms
 * Medium (66.32%)
 * Likes:    2399
 * Dislikes: 94
 * Total Accepted:    146.4K
 * Total Submissions: 209.1K
 * Testcase Example:  '"(abcd)"'
 *
 * You are given a string s that consists of lower case English letters and
 * brackets.
 *
 * Reverse the strings in each pair of matching parentheses, starting from
 * the innermost one.
 *
 * Your result should not contain any brackets.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "(abcd)"
 * Output: "dcba"
 *
 *
 * Example 2:
 *
 *
 * Input: s = "(u(love)i)"
 * Output: "iloveu"
 * Explanation: The substring "love" is reversed first, then the whole string
 * is reversed.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "(ed(et(oc))el)"
 * Output: "leetcode"
 * Explanation: First, we reverse the substring "oc", then "etco", and
 * finally, the whole string.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 2000
 * s only contains lower case English characters and parentheses.
 * It is guaranteed that all parentheses are balanced.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn reverse_parentheses(s: String) -> String {
        let n = s.len();
        let mut stack = vec![];
        let mut pairs = vec![0; n];
        let bytes = s.as_bytes();
        for (i, c) in bytes.iter().enumerate() {
            match *c {
                b'(' => {
                    stack.push(i);
                }
                b')' => {
                    let left = stack.pop().unwrap();
                    pairs[left] = i;
                    pairs[i] = left;
                }
                _ => {}
            }
        }
        let mut res = String::with_capacity(n);
        let mut i = 0;
        let mut dir = 1usize;
        for _ in 0..n {
            match bytes[i] {
                b'(' | b')' => {
                    i = pairs[i];
                    dir = dir.wrapping_neg();
                }
                _ => {
                    res.push(bytes[i] as char);
                }
            }
            i = i.wrapping_add(dir);
        }
        res
    }
}

// @lc code=end

fn main() {
    rust::test_algo(
        Solution::reverse_parentheses,
        vec![
            (("(abcd)".to_string()), "dcba".to_string()),
            (("(u(love)i)".to_string()), "iloveu".to_string()),
            (("(ed(et(oc))el)".to_string()), "leetcode".to_string()),
            (("(u(love)if)".to_string()), "filoveu".to_string()),
            (("alo(u(love)if)".to_string()), "alofiloveu".to_string()),
            (("alo(u(love)if)o".to_string()), "alofiloveuo".to_string()),
            (("alo((love))o".to_string()), "aloloveo".to_string()),
            (("(())".to_string()), "".to_string()),
            (("()()".to_string()), "".to_string()),
            (("(love)(love)".to_string()), "evolevol".to_string()),
            (("((love)(love))".to_string()), "lovelove".to_string()),
        ],
        |a, b| a == b,
    )
}
