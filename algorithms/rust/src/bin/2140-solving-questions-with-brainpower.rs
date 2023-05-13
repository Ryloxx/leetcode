/*
 * @lc app=leetcode id=2140 lang=rust
 *
 * [2140] Solving Questions With Brainpower
 *
 * https://leetcode.com/problems/solving-questions-with-brainpower/description/
 *
 * algorithms
 * Medium (46.10%)
 * Likes:    1557
 * Dislikes: 36
 * Total Accepted:    54.3K
 * Total Submissions: 102.2K
 * Testcase Example:  '[[3,2],[4,3],[4,4],[2,5]]'
 *
 * You are given a 0-indexed 2D integer array questions where questions[i] =
 * [pointsi, brainpoweri].
 *
 * The array describes the questions of an exam, where you have to process the
 * questions in order (i.e., starting from question 0) and make a decision
 * whether to solve or skip each question. Solving question i will earn you
 * pointsi points but you will be unable to solve each of the next brainpoweri
 * questions. If you skip question i, you get to make the decision on the next
 * question.
 *
 *
 * For example, given questions = [[3, 2], [4, 3], [4, 4], [2,
 * 5]]:
 *
 *
 * If question 0 is solved, you will earn 3 points but you will be unable to
 * solve questions 1 and 2.
 * If instead, question 0 is skipped and question 1 is solved, you will earn 4
 * points but you will be unable to solve questions 2 and 3.
 *
 *
 *
 *
 * Return the maximum points you can earn for the exam.
 *
 *
 * Example 1:
 *
 *
 * Input: questions = [[3,2],[4,3],[4,4],[2,5]]
 * Output: 5
 * Explanation: The maximum points can be earned by solving questions 0 and 3.
 * - Solve question 0: Earn 3 points, will be unable to solve the next 2
 * questions
 * - Unable to solve questions 1 and 2
 * - Solve question 3: Earn 2 points
 * Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more
 * points.
 *
 *
 * Example 2:
 *
 *
 * Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
 * Output: 7
 * Explanation: The maximum points can be earned by solving questions 1 and 4.
 * - Skip question 0
 * - Solve question 1: Earn 2 points, will be unable to solve the next 2
 * questions
 * - Unable to solve questions 2 and 3
 * - Solve question 4: Earn 5 points
 * Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more
 * points.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= questions.length <= 10^5
 * questions[i].length == 2
 * 1 <= pointsi, brainpoweri <= 10^5
 *
 *
 */

struct Solution;

// @lc code=start
impl Solution {
    pub fn most_points(questions: Vec<Vec<i32>>) -> i64 {
        let n = questions.len();
        let mut dp = vec![0i64; n];
        dp[n - 1] = questions[n - 1][0] as i64;
        (0..(n - 1)).rev().into_iter().for_each(|i| {
            dp[i] = dp[i + 1].max(
                dp.get(1 + i + questions[i][1] as usize).unwrap_or(&0) + questions[i][0] as i64,
            )
        });
        dp[0]
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::most_points(e),
        vec![
            (vec![vec![3, 2], vec![4, 3], vec![4, 4], vec![2, 5]], 5),
            (
                vec![vec![1, 1], vec![2, 2], vec![3, 3], vec![4, 4], vec![5, 5]],
                7,
            ),
            (vec![vec![3, 2]], 3),
            (vec![vec![3, 0], vec![3, 0], vec![3, 0], vec![3, 0]], 12),
        ],
        |a, b| a == b,
    );
}
