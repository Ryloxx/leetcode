/*
 * @lc app=leetcode id=846 lang=rust
 *
 * [846] Hand of Straights
 *
 * https://leetcode.com/problems/hand-of-straights/description/
 *
 * algorithms
 * Medium (55.85%)
 * Likes:    2539
 * Dislikes: 177
 * Total Accepted:    170.4K
 * Total Submissions: 304.8K
 * Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
 *
 * Alice has some number of cards and she wants to rearrange the cards into
 * groups so that each group is of size groupSize, and consists of groupSize
 * consecutive cards.
 *
 * Given an integer array hand where hand[i] is the value written on the i^th
 * card and an integer groupSize, return true if she can rearrange the cards,
 * or false otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
 * Output: true
 * Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
 *
 *
 * Example 2:
 *
 *
 * Input: hand = [1,2,3,4,5], groupSize = 4
 * Output: false
 * Explanation: Alice's hand can not be rearranged into groups of 4.
 *
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= hand.length <= 10^4
 * 0 <= hand[i] <= 10^9
 * 1 <= groupSize <= hand.length
 *
 *
 *
 * Note: This question is the same as 1296:
 * https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
 *
 */
struct Solution;
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn is_n_straight_hand(hand: Vec<i32>, group_size: i32) -> bool {
        if hand.len() % group_size as usize != 0 {
            return false;
        }
        let mut freqs: HashMap<i32, i32> = HashMap::new();
        for num in hand {
            *(freqs.entry(num).or_default()) += 1;
        }
        while let Some(right) = freqs.keys().copied().next() {
            let mut left = right;
            while freqs.get(&(left - 1)).unwrap_or(&0) > &0 {
                left -= 1;
            }
            while left <= right {
                let cnt = freqs[&left];
                if cnt < 0 {
                    return false;
                }
                if cnt > 0 {
                    for curr in left..(left + group_size) {
                        if let Some(value) = freqs.get_mut(&curr) {
                            *value -= cnt;
                        } else {
                            return false;
                        }
                    }
                }
                freqs.remove(&left);
                left += 1;
            }
        }
        true
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::is_n_straight_hand(e.0, e.1),
        vec![
            ((vec![1, 2, 3, 6, 2, 3, 4, 7, 8], 3), true),
            ((vec![1, 2, 3, 4, 5], 4), false),
            ((vec![8, 10, 12], 3), false),
            ((vec![1, 2, 2, 2, 2, 3], 2), false),
        ],
        |a, b| a == b,
    )
}
