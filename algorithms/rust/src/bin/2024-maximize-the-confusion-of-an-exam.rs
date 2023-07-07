/*
 * @lc app=leetcode id=2024 lang=rust
 *
 * [2024] Maximize the Confusion of an Exam
 *
 * https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/
 *
 * algorithms
 * Medium (59.72%)
 * Likes:    1054
 * Dislikes: 21
 * Total Accepted:    27.2K
 * Total Submissions: 44.6K
 * Testcase Example:  '"TTFF"\n2'
 *
 * A teacher is writing a test with n true/false questions, with 'T' denoting
 * true and 'F' denoting false. He wants to confuse the students by
 * maximizing the number of consecutive questions with the same answer
 * (multiple trues or multiple falses in a row).
 *
 * You are given a string answerKey, where answerKey[i] is the original
 * answer to the i^th question. In addition, you are given an integer k, the
 * maximum number of times you may perform the following operation:
 *
 *
 * Change the answer key for any question to 'T' or 'F' (i.e., set
 * answerKey[i] to 'T' or 'F').
 *
 *
 * Return the maximum number of consecutive 'T's or 'F's in the answer key
 * after performing the operation at most k times.
 *
 *
 * Example 1:
 *
 *
 * Input: answerKey = "TTFF", k = 2
 * Output: 4
 * Explanation: We can replace both the 'F's with 'T's to make answerKey =
 * "TTTT".
 * There are four consecutive 'T's.
 *
 *
 * Example 2:
 *
 *
 * Input: answerKey = "TFFT", k = 1
 * Output: 3
 * Explanation: We can replace the first 'T' with an 'F' to make answerKey =
 * "FFFT".
 * Alternatively, we can replace the second 'T' with an 'F' to make answerKey
 * = "TFFF".
 * In both cases, there are three consecutive 'F's.
 *
 *
 * Example 3:
 *
 *
 * Input: answerKey = "TTFTTFTT", k = 1
 * Output: 5
 * Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
 * Alternatively, we can replace the second 'F' to make answerKey =
 * "TTFTTTTT".
 * In both cases, there are five consecutive 'T's.
 *
 *
 *
 * Constraints:
 *
 *
 * n == answerKey.length
 * 1 <= n <= 5 * 10^4
 * answerKey[i] is either 'T' or 'F'
 * 1 <= k <= n
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn max_consecutive_answers(answer_key: String, k: i32) -> i32 {
        let answer_key = answer_key.as_bytes();
        let mut left = 0;
        let mut count = [0, 0];
        let mut res = 0;
        for (right, &c) in answer_key.iter().enumerate() {
            count[(c as usize >> 1) & 1] += 1;
            while count[0].min(count[1]) > k {
                count[(answer_key[left] as usize >> 1) & 1] -= 1;
                left += 1;
            }
            res = res.max(right - left + 1);
        }
        res as i32
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::max_consecutive_answers(e.0, e.1),
        vec![
            (("TTFF".to_string(), 2), 4),
            (("TFFT".to_string(), 1), 3),
            (("TTFTTFTT".to_string(), 1), 5),
            (("T".to_string(), 1), 1),
            (("F".to_string(), 1), 1),
            (("F".to_string(), 5), 1),
            (("T".to_string(), 5), 1),
        ],
        |a, b| a == b,
    );
}
