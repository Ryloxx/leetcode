/*
 * @lc app=leetcode id=403 lang=rust
 *
 * [403] Frog Jump
 *
 * https://leetcode.com/problems/frog-jump/description/
 *
 * algorithms
 * Hard (43.16%)
 * Likes:    4293
 * Dislikes: 206
 * Total Accepted:    197.3K
 * Total Submissions: 451.4K
 * Testcase Example:  '[0,1,3,5,6,8,12,17]'
 *
 * A frog is crossing a river. The river is divided into some number of
 * units, and at each unit, there may or may not exist a stone. The frog can
 * jump on a stone, but it must not jump into the water.
 *
 * Given a list of stones' positions (in units) in sorted ascending order,
 * determine if the frog can cross the river by landing on the last stone.
 * Initially, the frog is on the first stone and assumes the first jump must
 * be 1 unit.
 *
 * If the frog's last jump was k units, its next jump must be either k - 1,
 * k, or k + 1 units. The frog can only jump in the forward direction.
 *
 *
 * Example 1:
 *
 *
 * Input: stones = [0,1,3,5,6,8,12,17]
 * Output: true
 * Explanation: The frog can jump to the last stone by jumping 1 unit to the
 * 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone,
 * then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to
 * the 8th stone.
 *
 *
 * Example 2:
 *
 *
 * Input: stones = [0,1,2,3,4,8,9,11]
 * Output: false
 * Explanation: There is no way to jump to the last stone as the gap between
 * the 5th and 6th stone is too large.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= stones.length <= 2000
 * 0 <= stones[i] <= 2^31 - 1
 * stones[0] == 0
 * stones is sorted in a strictly increasing order.
 *
 *
 */

struct Solution;

// @lc code=start
impl Solution {
    pub fn can_cross(stones: Vec<i32>) -> bool {
        use std::collections::HashMap;
        #[allow(unused_imports)]
        use std::iter::FromIterator;

        fn dp(
            i: u16,
            k: u16,
            stones: &Vec<i32>,
            lookup: &HashMap<i32, u16>,
            memo: &mut HashMap<u32, bool>,
        ) -> bool {
            if i as usize >= stones.len() {
                return false;
            }
            if i as usize == stones.len() - 1 {
                return true;
            }

            let key = ((i as u32) << 16) | k as u32;
            if let Some(&res) = memo.get(&key) {
                return res;
            }

            let mut res = false;
            for dx in (k.max(2) - 1)..k + 2 {
                if let Some(&n_i) = lookup.get(&(stones[i as usize] + dx as i32)) {
                    if dp(n_i, dx, stones, lookup, memo) {
                        res = true;
                        break;
                    }
                }
            }
            memo.insert(key, res);
            res
        }

        dp(
            0,
            0,
            &stones,
            &HashMap::from_iter(stones.iter().enumerate().map(|(i, &x)| (x, i as u16))),
            &mut HashMap::new(),
        )
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        Solution::can_cross,
        vec![
            ((vec![0, 1, 3, 5, 6, 8, 12, 17]), true),
            ((vec![0, 1, 2, 3, 4, 8, 9, 11]), false),
            ((vec![0, 2, 3, 5, 6, 8, 12, 17]), false),
            ((vec![0, 1]), true),
            ((vec![0, 2]), false),
        ],
        |a, b| a == b,
    );
}
