/*
 * @lc app=leetcode id=752 lang=rust
 *
 * [752] Open the Lock
 *
 * https://leetcode.com/problems/open-the-lock/description/
 *
 * algorithms
 * Medium (55.96%)
 * Likes:    4211
 * Dislikes: 175
 * Total Accepted:    253.4K
 * Total Submissions: 441K
 * Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
 *
 * You have a lock in front of you with 4 circular wheels. Each wheel has 10
 * slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can
 * rotate freely and wrap around: for example we can turn '9' to be '0', or
 * '0' to be '9'. Each move consists of turning one wheel one slot.
 *
 * The lock initially starts at '0000', a string representing the state of
 * the 4 wheels.
 *
 * You are given a list of deadends dead ends, meaning if the lock displays
 * any of these codes, the wheels of the lock will stop turning and you will
 * be unable to open it.
 *
 * Given a target representing the value of the wheels that will unlock the
 * lock, return the minimum total number of turns required to open the lock,
 * or -1 if it is impossible.
 *
 *
 * Example 1:
 *
 *
 * Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
 * Output: 6
 * Explanation:
 * A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" ->
 * "1201" -> "1202" -> "0202".
 * Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202"
 * would be invalid,
 * because the wheels of the lock become stuck after the display becomes the
 * dead end "0102".
 *
 *
 * Example 2:
 *
 *
 * Input: deadends = ["8888"], target = "0009"
 * Output: 1
 * Explanation: We can turn the last wheel in reverse to move from "0000" ->
 * "0009".
 *
 *
 * Example 3:
 *
 *
 * Input: deadends =
 * ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
 * Output: -1
 * Explanation: We cannot reach the target without getting stuck.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= deadends.length <= 500
 * deadends[i].length == 4
 * target.length == 4
 * target will not be in the list deadends.
 * target and deadends[i] consist of digits only.
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::VecDeque;
impl Solution {
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {
        fn to_u32(input: String) -> u32 {
            input
                .as_bytes()
                .iter()
                .fold(0u32, |acc, curr| (acc << 4) | (curr - b'0') as u32)
        }
        fn to_idx(input: u32) -> usize {
            (0..4).fold(0, |acc, i| acc * 10 + ((input >> (i * 4)) & 0b1111)) as usize
        }
        let mut q = VecDeque::<(u32, i32)>::new();
        let mut seen = [false; 10_000];
        let target = to_u32(target);
        deadends
            .into_iter()
            .for_each(|deadend| seen[to_idx(to_u32(deadend))] = true);
        q.push_back((0, 0));
        while let Some((current, step)) = q.pop_front() {
            let idx = to_idx(current);
            if seen[idx] {
                continue;
            }
            if current == target {
                return step;
            }
            seen[idx] = true;
            let step = step + 1;
            for i in 0..4 {
                let place = i * 4;
                let mask = 0b1111 << place;
                let out = current & !mask;
                let (a, b) = match (current & mask) >> place {
                    0 => ((1 << place), (9 << place)),
                    9 => ((8 << place), (0 << place)),
                    n => (((n + 1) << place), ((n - 1) << place)),
                };
                q.push_back((out | a, step));
                q.push_back((out | b, step));
            }
        }
        -1
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::open_lock(e.0, e.1),
        vec![
            (
                (
                    ["0201", "0101", "0102", "1212", "2002"]
                        .into_iter()
                        .map(String::from)
                        .collect(),
                    "0202".to_string(),
                ),
                6,
            ),
            (
                (
                    [
                        "8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888",
                    ]
                    .into_iter()
                    .map(String::from)
                    .collect(),
                    "8888".to_string(),
                ),
                -1,
            ),
            (
                (
                    ["0000"].into_iter().map(String::from).collect(),
                    "8888".to_string(),
                ),
                -1,
            ),
            (
                (
                    ["8888"].into_iter().map(String::from).collect(),
                    "0009".to_string(),
                ),
                1,
            ),
            (
                (
                    ["9999"].into_iter().map(String::from).collect(),
                    "0000".to_string(),
                ),
                0,
            ),
        ],
        |a, b| a == b,
    )
}
