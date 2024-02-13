#![feature(test)]
/*
 * @lc app=leetcode id=1208 lang=rust
 *
 * [1208] Get Equal Substrings Within Budget
 *
 * https://leetcode.com/problems/get-equal-substrings-within-budget/description/
 *
 * algorithms
 * Medium (50.02%)
 * Likes:    1156
 * Dislikes: 69
 * Total Accepted:    51.4K
 * Total Submissions: 101.5K
 * Testcase Example:  '"abcd"\n"bcdf"\n3'
 *
 * You are given two strings s and t of the same length and an integer
 * maxCost.
 *
 * You want to change s to t. Changing the i^th character of s to i^th
 * character of t costs |s[i] - t[i]| (i.e., the absolute difference between
 * the ASCII values of the characters).
 *
 * Return the maximum length of a substring of s that can be changed to be
 * the same as the corresponding substring of t with a cost less than or
 * equal to maxCost. If there is no substring from s that can be changed to
 * its corresponding substring from t, return 0.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abcd", t = "bcdf", maxCost = 3
 * Output: 3
 * Explanation: "abc" of s can change to "bcd".
 * That costs 3, so the maximum length is 3.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "abcd", t = "cdef", maxCost = 3
 * Output: 1
 * Explanation: Each character in s costs 2 to change to character in t,  so
 * the maximum length is 1.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "abcd", t = "acde", maxCost = 0
 * Output: 1
 * Explanation: You cannot make any change, so the maximum length is 1.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 10^5
 * t.length == s.length
 * 0 <= maxCost <= 10^6
 * s and t consist of only lowercase English letters.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    // O(N) time complexity
    // O(1) space complexity
    pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
        let n = s.len();
        let s_b = s.as_bytes();
        let t_b = t.as_bytes();
        let mut i = 0;
        let mut res = 0;
        let mut curr_cost = 0;
        for j in 0..n {
            curr_cost += t_b[j].abs_diff(s_b[j]) as i32;
            while curr_cost > max_cost {
                curr_cost -= t_b[i].abs_diff(s_b[i]) as i32;
                i += 1;
            }
            res = res.max(j + 1 - i);
        }
        res as i32
    }
    // O(NlogN) time complexity
    // O(N) space complexity
    // pub fn equal_substring(s: String, t: String, max_cost: i32) -> i32 {
    //     let mut stack = vec![0];
    //     let mut curr_sum = 0;
    //     let mut res = 0;
    //     for (t, s) in t.as_bytes().iter().zip(s.as_bytes().iter()) {
    //         curr_sum += t.abs_diff(*s) as i32;
    //         res = res.max(stack.len() - stack.partition_point(|x| (curr_sum - x)
    // > max_cost));         stack.push(curr_sum); } res as i32
    // }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::equal_substring(e.0, e.1, e.2),
        vec![
            (("abcd".to_string(), "bcdf".to_string(), 3), 3),
            (("abcd".to_string(), "cdef".to_string(), 3), 1),
            (("abcd".to_string(), "acde".to_string(), 0), 1),
            (("abcd".to_string(), "abcd".to_string(), 0), 4),
            (("abcd".to_string(), "wxyz".to_string(), 0), 0),
            (("abcd".to_string(), "bcde".to_string(), 4), 4),
            (("abcd".to_string(), "cdef".to_string(), 4), 2),
            (
                (
                    String::from_iter(std::iter::repeat("a").take(10usize.pow(5))),
                    String::from_iter(std::iter::repeat("z").take(10usize.pow(5))),
                    10i32.pow(6),
                ),
                40000,
            ),
            (
                (
                    String::from_iter(std::iter::repeat("a").take(10usize.pow(5))),
                    String::from_iter(std::iter::repeat("z").take(10usize.pow(5))),
                    0,
                ),
                0,
            ),
        ],
        |a, b| a == b,
    )
}

#[cfg(test)]
mod test {
    use test::Bencher;

    use crate::Solution;

    extern crate test;

    #[bench]
    fn tempz(b: &mut Bencher) {
        b.iter(|| {
            Solution::equal_substring("abcd".to_string(), "bcdf".to_string(), 3);
            Solution::equal_substring("abcd".to_string(), "cdef".to_string(), 3);
            Solution::equal_substring("abcd".to_string(), "acde".to_string(), 0);
            Solution::equal_substring("abcd".to_string(), "abcd".to_string(), 0);
            Solution::equal_substring("abcd".to_string(), "wxyz".to_string(), 0);
            Solution::equal_substring("abcd".to_string(), "bcde".to_string(), 4);
            Solution::equal_substring("abcd".to_string(), "cdef".to_string(), 4);
            Solution::equal_substring(
                String::from_iter(std::iter::repeat("a").take(10usize.pow(5))),
                String::from_iter(std::iter::repeat("z").take(10usize.pow(5))),
                10i32.pow(6),
            );
        });
    }
}
