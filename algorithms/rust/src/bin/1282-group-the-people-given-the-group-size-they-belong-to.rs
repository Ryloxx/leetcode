/*
 * @lc app=leetcode id=1282 lang=rust
 *
 * [1282] Group the People Given the Group Size They Belong To
 *
 * https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
 *
 * algorithms
 * Medium (85.49%)
 * Likes:    2330
 * Dislikes: 613
 * Total Accepted:    148.1K
 * Total Submissions: 169.9K
 * Testcase Example:  '[3,3,3,3,3,1,3]'
 *
 * There are n people that are split into some unknown number of groups. Each
 * person is labeled with a unique ID from 0 to n - 1.
 *
 * You are given an integer array groupSizes, where groupSizes[i] is the size
 * of the group that person i is in. For example, if groupSizes[1] = 3, then
 * person 1 must be in a group of size 3.
 *
 * Return a list of groups such that each person i is in a group of size
 * groupSizes[i].
 *
 * Each person should appear in exactly one group, and every person must be
 * in a group. If there are multiple answers, return any of them. It is
 * guaranteed that there will be at least one valid solution for the given
 * input.
 *
 *
 * Example 1:
 *
 *
 * Input: groupSizes = [3,3,3,3,3,1,3]
 * Output: [[5],[0,1,2],[3,4,6]]
 * Explanation:
 * The first group is [5]. The size is 1, and groupSizes[5] = 1.
 * The second group is [0,1,2]. The size is 3, and groupSizes[0] =
 * groupSizes[1] = groupSizes[2] = 3.
 * The third group is [3,4,6]. The size is 3, and groupSizes[3] =
 * groupSizes[4] = groupSizes[6] = 3.
 * Other possible solutions are [[2,1,6],[5],[0,4,3]] and
 * [[5],[0,6,2],[4,3,1]].
 *
 *
 * Example 2:
 *
 *
 * Input: groupSizes = [2,1,3,3,3,2]
 * Output: [[1],[0,5],[2,3,4]]
 *
 *
 *
 * Constraints:
 *
 *
 * groupSizes.length == n
 * 1 <= n <= 500
 * 1 <= groupSizes[i] <= n
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        let mut build = vec![vec![]; group_sizes.len() + 1];
        let mut res = vec![];
        for (i, &size) in group_sizes.iter().enumerate() {
            let size = size as usize;
            build[size].push(i as i32);
            if build[size].len() == size {
                res.push(std::mem::take(&mut build[size]));
            }
        }
        res
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        Solution::group_the_people,
        vec![
            (
                vec![3, 3, 3, 3, 3, 1, 3],
                vec![vec![5], vec![0, 1, 2], vec![3, 4, 6]],
            ),
            (
                vec![2, 1, 3, 3, 3, 2],
                vec![vec![1], vec![0, 5], vec![2, 3, 4]],
            ),
            (
                vec![1, 1, 1, 1, 1],
                vec![vec![0], vec![1], vec![2], vec![3], vec![4]],
            ),
            (vec![1], vec![vec![0]]),
        ],
        |a, b| {
            let mut a = a.clone();
            let mut b = b.clone();
            a.sort_unstable();
            b.sort_unstable();
            a == b
        },
    )
}
