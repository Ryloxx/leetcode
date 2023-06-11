/*
 * @lc app=leetcode id=1406 lang=rust
 *
 * [1406] Stone Game III
 *
 * https://leetcode.com/problems/stone-game-iii/description/
 *
 * algorithms
 * Hard (59.57%)
 * Likes:    1865
 * Dislikes: 57
 * Total Accepted:    71.1K
 * Total Submissions: 110.4K
 * Testcase Example:  '[1,2,3,7]'
 *
 * Alice and Bob continue their games with piles of stones. There are several
 * stones arranged in a row, and each stone has an associated value which is
 * an integer given in the array stoneValue.
 *
 * Alice and Bob take turns, with Alice starting first. On each player's
 * turn, that player can take 1, 2, or 3 stones from the first remaining
 * stones in the row.
 *
 * The score of each player is the sum of the values of the stones taken. The
 * score of each player is 0 initially.
 *
 * The objective of the game is to end with the highest score, and the winner
 * is the player with the highest score and there could be a tie. The game
 * continues until all the stones have been taken.
 *
 * Assume Alice and Bob play optimally.
 *
 * Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they
 * will end the game with the same score.
 *
 *
 * Example 1:
 *
 *
 * Input: values = [1,2,3,7]
 * Output: "Bob"
 * Explanation: Alice will always lose. Her best move will be to take three
 * piles and the score become 6. Now the score of Bob is 7 and Bob wins.
 *
 *
 * Example 2:
 *
 *
 * Input: values = [1,2,3,-9]
 * Output: "Alice"
 * Explanation: Alice must choose all the three piles at the first move to
 * win and leave Bob with negative score.
 * If Alice chooses one pile her score will be 1 and the next move Bob's
 * score becomes 5. In the next move, Alice will take the pile with value =
 * -9 and lose.
 * If Alice chooses two piles her score will be 3 and the next move Bob's
 * score becomes 3. In the next move, Alice will take the pile with value =
 * -9 and also lose.
 * Remember that both play optimally so here Alice will choose the scenario
 * that makes her win.
 *
 *
 * Example 3:
 *
 *
 * Input: values = [1,2,3,6]
 * Output: "Tie"
 * Explanation: Alice cannot win this game. She can end the game in a draw if
 * she decided to choose all the first three piles, otherwise she will
 * lose.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= stoneValue.length <= 5 * 10^4
 * -1000 <= stoneValue[i] <= 1000
 *
 *
 */

struct Solution;
// @lc code=start
use std::{cmp::Ordering, collections::HashMap};
impl Solution {
    pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
        fn dp(
            idx: usize,
            alice_turn: bool,
            piles: &Vec<i32>,
            memo: &mut HashMap<(usize, bool), i32>,
        ) -> i32 {
            if let Some(&res) = memo.get(&(idx, alice_turn)) {
                return res;
            }
            let it = (1..=3).into_iter().scan(0i32, |acc, x| {
                if idx + x > piles.len() {
                    return None;
                }
                *acc += piles[idx + x - 1];
                return Some(
                    dp(idx + x, !alice_turn, &piles, memo) + if alice_turn { *acc } else { 0 },
                );
            });
            let res = if alice_turn {
                it.max().unwrap_or(0)
            } else {
                it.min().unwrap_or(0)
            };
            memo.insert((idx, alice_turn), res);
            return res;
        }
        match (2 * dp(0, true, &stone_value, &mut HashMap::new()))
            .cmp(&stone_value.iter().sum::<i32>())
        {
            Ordering::Equal => "Tie".to_string(),
            Ordering::Less => "Bob".to_string(),
            Ordering::Greater => "Alice".to_string(),
        }
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |s| Solution::stone_game_iii(s),
        vec![
            (vec![1, 2, 3, 7], "Bob".to_string()),
            (vec![1, 2, 3, -9], "Alice".to_string()),
            (vec![1, 2, 3, 6], "Tie".to_string()),
            (vec![-1, -2, -3], "Tie".to_string()),
            (vec![-2], "Bob".to_string()),
        ],
        |a, b| a == b,
    )
}
