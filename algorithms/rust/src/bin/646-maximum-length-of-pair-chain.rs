/*
 * @lc app=leetcode id=646 lang=rust
 *
 * [646] Maximum Length of Pair Chain
 *
 * https://leetcode.com/problems/maximum-length-of-pair-chain/description/
 *
 * algorithms
 * Medium (56.46%)
 * Likes:    3283
 * Dislikes: 118
 * Total Accepted:    151.7K
 * Total Submissions: 264.6K
 * Testcase Example:  '[[1,2],[2,3],[3,4]]'
 *
 * You are given an array of n pairs pairs where pairs[i] = [lefti, righti]
 * and lefti < righti.
 *
 * A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs
 * can be formed in this fashion.
 *
 * Return the length longest chain which can be formed.
 *
 * You do not need to use up all the given intervals. You can select pairs in
 * any order.
 *
 *
 * Example 1:
 *
 *
 * Input: pairs = [[1,2],[2,3],[3,4]]
 * Output: 2
 * Explanation: The longest chain is [1,2] -> [3,4].
 *
 *
 * Example 2:
 *
 *
 * Input: pairs = [[1,2],[7,8],[4,5]]
 * Output: 3
 * Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 *
 *
 *
 * Constraints:
 *
 *
 * n == pairs.length
 * 1 <= n <= 1000
 * -1000 <= lefti < righti <= 1000
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn find_longest_chain(mut pairs: Vec<Vec<i32>>) -> i32 {
        pairs.sort_unstable_by_key(|x| x[1]);
        pairs
            .iter()
            .fold(&mut (i32::MIN, 0), |acc, curr| {
                let p = (curr[0] > acc.0) as i32;
                (*acc).0 = acc.0 * (1 - p) + curr[1] * p;
                (*acc).1 += p;
                acc
            })
            .1
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::find_longest_chain(e),
        vec![
            ((vec![vec![1, 2], vec![2, 3], vec![3, 4]]), 2),
            ((vec![vec![1, 2], vec![7, 8], vec![4, 5]]), 3),
            ((vec![vec![3, 4], vec![2, 3], vec![1, 2]]), 2),
            ((vec![vec![1, 2]]), 1),
            (
                (vec![
                    vec![-10, -8],
                    vec![8, 9],
                    vec![-5, 0],
                    vec![6, 10],
                    vec![-6, -4],
                    vec![1, 7],
                    vec![9, 10],
                    vec![-4, 7],
                ]),
                4,
            ),
        ],
        |a, b| a == b,
    );
}
