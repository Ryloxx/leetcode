/*
 * @lc app=leetcode id=1441 lang=rust
 *
 * [1441] Build an Array With Stack Operations
 *
 * https://leetcode.com/problems/build-an-array-with-stack-operations/description/
 *
 * algorithms
 * Medium (72.40%)
 * Likes:    339
 * Dislikes: 122
 * Total Accepted:    86.5K
 * Total Submissions: 117.2K
 * Testcase Example:  '[1,3]\n3'
 *
 * You are given an integer array target and an integer n.
 *
 * You have an empty stack with the two following operations:
 *
 *
 * "Push": pushes an integer to the top of the stack.
 * "Pop": removes the integer on the top of the stack.
 *
 *
 * You also have a stream of the integers in the range [1, n].
 *
 * Use the two stack operations to make the numbers in the stack (from the
 * bottom to the top) equal to target. You should follow the following
 * rules:
 *
 *
 * If the stream of the integers is not empty, pick the next integer from the
 * stream and push it to the top of the stack.
 * If the stack is not empty, pop the integer at the top of the stack.
 * If, at any moment, the elements in the stack (from the bottom to the top)
 * are equal to target, do not read new integers from the stream and do not
 * do more operations on the stack.
 *
 *
 * Return the stack operations needed to build target following the mentioned
 * rules. If there are multiple valid answers, return any of them.
 *
 *
 * Example 1:
 *
 *
 * Input: target = [1,3], n = 3
 * Output: ["Push","Push","Pop","Push"]
 * Explanation: Initially the stack s is empty. The last element is the top
 * of the stack.
 * Read 1 from the stream and push it to the stack. s = [1].
 * Read 2 from the stream and push it to the stack. s = [1,2].
 * Pop the integer on the top of the stack. s = [1].
 * Read 3 from the stream and push it to the stack. s = [1,3].
 *
 *
 * Example 2:
 *
 *
 * Input: target = [1,2,3], n = 3
 * Output: ["Push","Push","Push"]
 * Explanation: Initially the stack s is empty. The last element is the top
 * of the stack.
 * Read 1 from the stream and push it to the stack. s = [1].
 * Read 2 from the stream and push it to the stack. s = [1,2].
 * Read 3 from the stream and push it to the stack. s = [1,2,3].
 *
 *
 * Example 3:
 *
 *
 * Input: target = [1,2], n = 4
 * Output: ["Push","Push"]
 * Explanation: Initially the stack s is empty. The last element is the top
 * of the stack.
 * Read 1 from the stream and push it to the stack. s = [1].
 * Read 2 from the stream and push it to the stack. s = [1,2].
 * Since the stack (from the bottom to the top) is equal to target, we stop
 * the stack operations.
 * The answers that read integer 3 from the stream are not accepted.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= target.length <= 100
 * 1 <= n <= 100
 * 1 <= target[i] <= n
 * target is strictly increasing.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn build_array(target: Vec<i32>, _: i32) -> Vec<String> {
        let mut last = 0;
        let mut res = Vec::with_capacity(2 * *target.last().unwrap() as usize - target.len());
        for i in target {
            let idx = (i - last - 1) as usize;
            res.extend(std::iter::repeat_with(|| "Push".to_string()).take(idx));
            res.extend(std::iter::repeat_with(|| "Pop".to_string()).take(idx));
            res.push("Push".to_string());
            last = i;
        }
        res
    }
}

// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::build_array(e.0, e.1),
        vec![
            (
                (vec![1, 3], 3),
                vec![
                    "Push".to_string(),
                    "Push".to_string(),
                    "Pop".to_string(),
                    "Push".to_string(),
                ],
            ),
            (
                (vec![1, 2, 3], 3),
                vec!["Push".to_string(), "Push".to_string(), "Push".to_string()],
            ),
            (
                (vec![1, 2], 4),
                vec!["Push".to_string(), "Push".to_string()],
            ),
            ((vec![1], 4), vec!["Push".to_string()]),
            (
                (vec![4], 4),
                vec![
                    "Push".to_string(),
                    "Push".to_string(),
                    "Push".to_string(),
                    "Pop".to_string(),
                    "Pop".to_string(),
                    "Pop".to_string(),
                    "Push".to_string(),
                ],
            ),
        ],
        |a, b| a == b,
    );
}
