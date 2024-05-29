/*
 * @lc app=leetcode id=1404 lang=rust
 *
 * [1404] Number of Steps to Reduce a Number in Binary Representation to One
 *
 * https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/
 *
 * algorithms
 * Medium (52.90%)
 * Likes:    1062
 * Dislikes: 74
 * Total Accepted:    81.7K
 * Total Submissions: 140.3K
 * Testcase Example:  '"1101"'
 *
 * Given the binary representation of an integer as a string s, return the
 * number of steps to reduce it to 1 under the following rules:
 *
 *
 *
 * If the current number is even, you have to divide it by 2.
 *
 *
 * If the current number is odd, you have to add 1 to it.
 *
 *
 *
 * It is guaranteed that you can always reach one for all test cases.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "1101"
 * Output: 6
 * Explanation: "1101" corressponds to number 13 in their decimal
 * representation.
 * Step 1) 13 is odd, add 1 and obtain 14.
 * Step 2) 14 is even, divide by 2 and obtain 7.
 * Step 3) 7 is odd, add 1 and obtain 8.
 * Step 4) 8 is even, divide by 2 and obtain 4.
 * Step 5) 4 is even, divide by 2 and obtain 2.
 * Step 6) 2 is even, divide by 2 and obtain 1.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "10"
 * Output: 1
 * Explanation: "10" corressponds to number 2 in their decimal
 * representation. Step 1) 2 is even, divide by 2 and obtain 1.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "1"
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 500
 * s consists of characters '0' or '1'
 * s[0] == '1'
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn num_steps(s: String) -> i32 {
        let s_bytes = s.as_bytes();
        let mut carry = 0;
        let mut res = 0;
        for &c in s_bytes.iter().skip(1).rev() {
            let c = (c & 1) as i32;
            res += carry ^ c;
            carry |= c;
        }
        s.len() as i32 + (res + carry) - 1
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::num_steps,
        vec![
            (("1101".to_string()), 6),
            (("10".to_string()), 1),
            (("1".to_string()), 0),
            ((String::from_iter(std::iter::repeat('1').take(500))), 501),
            (
                (String::from_iter(
                    std::iter::repeat('1')
                        .take(1)
                        .chain(std::iter::repeat('0').take(499)),
                )),
                499,
            ),
        ],
        |a, b| a == b,
    )
}
