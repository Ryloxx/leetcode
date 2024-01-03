/*
 * @lc app=leetcode id=859 lang=rust
 *
 * [859] Buddy Strings
 *
 * https://leetcode.com/problems/buddy-strings/description/
 *
 * algorithms
 * Easy (29.13%)
 * Likes:    1898
 * Dislikes: 1191
 * Total Accepted:    151.8K
 * Total Submissions: 515.2K
 * Testcase Example:  '"ab"\n"ba"'
 *
 * Given two strings s and goal, return true if you can swap two letters in s
 * so the result is equal to goal, otherwise, return false.
 *
 * Swapping letters is defined as taking two indices i and j (0-indexed) such
 * that i != j and swapping the characters at s[i] and s[j].
 *
 *
 * For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 *
 *
 *
 * Example 1:
 *
 *
 * Input: s = "ab", goal = "ba"
 * Output: true
 * Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is
 * equal to goal.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "ab", goal = "ab"
 * Output: false
 * Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b',
 * which results in "ba" != goal.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "aa", goal = "aa"
 * Output: true
 * Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is
 * equal to goal.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length, goal.length <= 2 * 10^4
 * s and goal consist of lowercase letters.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn buddy_strings(s: String, goal: String) -> bool {
        if s.len() != goal.len() {
            return false;
        }
        let mut swap = [usize::MAX, usize::MAX];
        let mut curr = 0;
        let mut seen = 0;
        let mut duplicate = false;
        for (i, (a, b)) in s.bytes().zip(goal.bytes()).enumerate() {
            let key = 1 << (a - b'a');
            duplicate = duplicate || seen & key != 0;
            seen |= key;
            if a != b {
                swap[curr % 2] = i;
                curr += 1;
            }
        }
        curr == 0 && duplicate
            || curr == 2
                && s.as_bytes()[swap[0]] == goal.as_bytes()[swap[1]]
                && s.as_bytes()[swap[1]] == goal.as_bytes()[swap[0]]
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::buddy_strings(e.0, e.1),
        vec![
            (("ab".to_string(), "ba".to_string()), true),
            (("ab".to_string(), "ab".to_string()), false),
            (("aa".to_string(), "aa".to_string()), true),
            (("ab".to_string(), "babbb".to_string()), false),
            (("a".to_string(), "a".to_string()), false),
            (("aaab".to_string(), "aaab".to_string()), true),
            (("abac".to_string(), "abad".to_string()), false),
            (
                (
                    ('a'..'b')
                        .cycle()
                        .take(2 * 10usize.pow(4))
                        .collect::<String>(),
                    ('a'..'b')
                        .cycle()
                        .take(2 * 10usize.pow(4))
                        .collect::<String>(),
                ),
                true,
            ),
        ],
        |a, b| a == b,
    );
}
