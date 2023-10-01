/*
 * @lc app=leetcode id=486 lang=rust
 *
 * [486] Predict the Winner
 *
 * https://leetcode.com/problems/predict-the-winner/description/
 *
 * algorithms
 * Medium (50.88%)
 * Likes:    4620
 * Dislikes: 218
 * Total Accepted:    166.8K
 * Total Submissions: 312.3K
 * Testcase Example:  '[1,5,2]'
 *
 * You are given an integer array nums. Two players are playing a game with
 * this array: player 1 and player 2.
 *
 * Player 1 and player 2 take turns, with player 1 starting first. Both
 * players start the game with a score of 0. At each turn, the player takes
 * one of the numbers from either end of the array (i.e., nums[0] or
 * nums[nums.length - 1]) which reduces the size of the array by 1. The
 * player adds the chosen number to their score. The game ends when there are
 * no more elements in the array.
 *
 * Return true if Player 1 can win the game. If the scores of both players
 * are equal, then player 1 is still the winner, and you should also return
 * true. You may assume that both players are playing optimally.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,5,2]
 * Output: false
 * Explanation: Initially, player 1 can choose between 1 and 2.
 * If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If
 * player 2 chooses 5, then player 1 will be left with 1 (or 2).
 * So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
 * Hence, player 1 will never be the winner and you need to return false.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,5,233,7]
 * Output: true
 * Explanation: Player 1 first chooses 1. Then player 2 has to choose between
 * 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
 * Finally, player 1 has more score (234) than player 2 (12), so you need to
 * return True representing player1 can win.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 20
 * 0 <= nums[i] <= 10^7
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn predict_the_winner(nums: Vec<i32>) -> bool {
        if nums.len() % 2 == 0 {
            return true;
        }
        fn dp(i: i32, j: i32, nums: &Vec<i32>, turn: bool, memo: &mut HashMap<u64, i32>) -> i32 {
            if i > j {
                return 0;
            }
            let key = 1u64 << (22 + i) | 1u64 << (1 + j) | turn as u64;
            if let Some(&memo) = memo.get(&key) {
                return memo;
            }
            let cmp = if turn {
                std::cmp::max::<i32>
            } else {
                std::cmp::min::<i32>
            };
            let res = cmp(
                turn as i32 * nums[i as usize] + dp(i + 1, j, nums, !turn, memo),
                turn as i32 * nums[j as usize] + dp(i, j - 1, nums, !turn, memo),
            );
            memo.insert(key, res);
            res
        }
        return dp(0, nums.len() as i32 - 1, &nums, true, &mut HashMap::new())
            >= (nums.iter().to_owned().sum::<i32>() + 1) >> 1;
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        Solution::predict_the_winner,
        vec![
            ((vec![1, 5, 2]), false),
            ((vec![1, 5, 233, 7]), true),
            (
                vec![
                    8506201, 2073020, 4063431, 3185770, 5536370, 4366045, 2683887, 372795, 6658378,
                    5398930, 8410055, 5392747, 796987, 2974185, 3388472, 289708, 9534030, 4899677,
                    7713843, 3410778,
                ],
                true,
            ),
            (
                vec![
                    7896780, 3666004, 4095582, 386906, 3799717, 3419503, 7329024, 4930948, 2558941,
                    2561562, 623819, 2687748, 9184159, 6516158, 9903808, 8824698, 4037803, 7964605,
                    5526959, 2258947,
                ],
                true,
            ),
            (
                vec![
                    3576682, 9944747, 9531001, 2041865, 331316, 8359596, 2638381, 1188869, 9486264,
                    5088496, 1932068, 8501270, 1250679, 6388890, 122978, 8164900, 8943873, 1879387,
                    2523095,
                ],
                false,
            ),
            (vec![8117974, 4643558, 5628145, 4700384, 7042728], true),
            (
                vec![
                    5928693, 8492846, 8574730, 4585026, 3784693, 2110747, 2294526, 3766328,
                    6288569, 3870174, 8071891, 3151838, 1816311, 3469272, 4799606, 1996790,
                    5032730,
                ],
                false,
            ),
            (
                vec![
                    5902981, 4398648, 9215100, 2868759, 3041456, 5684502, 5718584, 6689024,
                    2208787, 1632911, 2582495, 3362238, 4211172, 6339797, 1751674, 4046389,
                ],
                true,
            ),
            (
                vec![
                    1242003, 1644620, 817776, 2855214, 1479992, 2887945, 8796585, 399159, 5993564,
                    7009346, 3139886,
                ],
                false,
            ),
            (
                vec![
                    7105412, 3489992, 7232681, 7405030, 552879, 3037223, 1978414, 3692082, 4403276,
                    3256998, 7766798, 1751695,
                ],
                true,
            ),
            (vec![8034326, 92163, 3699071, 5848505, 1779043], true),
            (
                vec![
                    1077230, 7857933, 1081378, 3038051, 5062918, 5719465, 3130834, 3898396,
                    9605597, 4433095, 8392241,
                ],
                true,
            ),
        ],
        |a, b| a == b,
    );
}
