/*
 * @lc app=leetcode id=2707 lang=rust
 *
 * [2707] Extra Characters in a String
 *
 * https://leetcode.com/problems/extra-characters-in-a-string/
 *
 * algorithms
 * Medium (47.5%)
 * Likes:    1096
 * Dislikes: 51
 * Total Accepted:    38.1K
 * Total Submissions: 80.5K
 * Testcase Example:  '"leetscode"\n["leet","code","leetcode"]'
 *
 * You are given a 0-indexed string s and a dictionary of words dictionary.
 * You have to break s into one or more non-overlapping substrings such that
 * each substring is present in dictionary. There may be some extra
 * characters in s which are not present in any of the substrings.
 * Return the minimum number of extra characters left over if you break up s
 * optimally. 
 * 
 * Example 1:
 * Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
 * Output: 1
 * Explanation: We can break s in two substrings: "leet" from index 0 to 3
 * and "code" from index 5 to 8. There is only 1 unused character (at index
 * 4), so we return 1.  
 * 
 * Example 2:
 * Input: s = "sayhelloworld", dictionary = ["hello","world"]
 * Output: 3
 * Explanation: We can break s in two substrings: "hello" from index 3 to 7
 * and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not
 * used in any substring and thus are considered as extra characters. Hence,
 * we return 3.
 * 
 * Constraints:
 * 1 <= s.length <= 50
 * 1 <= dictionary.length <= 50
 * 1 <= dictionary[i].length <= 50
 * dictionary[i] and s consists of only lowercase English letters
 * dictionary contains distinct words
 */

struct Solution;

// @lc code=start
impl Solution {
    pub fn min_extra_char(s: String, dictionary: Vec<String>) -> i32 {
        use std::collections::HashSet;
        let mut memo = vec![-1; s.len() + 1];
        memo[s.len()] = 0;
        fn dp(i: usize, s: &str, memo: &mut Vec<i32>, dictionary: &HashSet<String>) -> i32 {
            if memo[i] >= 0 {
                return memo[i];
            }
            let mut res = s.len() as i32;
            for j in i + 1..s.len() + 1 {
                res = res.min(
                    (1 - (dictionary.contains(&s[i..j]) as i32)) * (j - i) as i32
                        + dp(j, s, memo, dictionary),
                )
            }
            memo[i] = res;
            res
        }
        dp(
            0,
            &s,
            &mut memo,
            &dictionary.into_iter().collect::<HashSet<String>>(),
        )
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::min_extra_char(e.0, e.1),
        vec![
            (
                (
                    "leetscode".to_string(),
                    vec!["leet", "code", "leetcode"]
                        .into_iter()
                        .map(String::from)
                        .collect(),
                ),
                1,
            ),
            (
                (
                    "sayhelloworld".to_string(),
                    vec!["hello", "world"]
                        .into_iter()
                        .map(String::from)
                        .collect(),
                ),
                3,
            ),
            (
                (
                    "sayhelloworld".to_string(),
                    vec!["hello", "world"]
                        .into_iter()
                        .map(String::from)
                        .collect(),
                ),
                3,
            ),
        ],
        |a, b| a == b,
    );
}
