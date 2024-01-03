/*
 * @lc app=leetcode id=2610 lang=rust
 *
 * [2610] Convert an Array Into a 2D Array With Conditions
 *
 * https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
 *
 * algorithms
 * Medium (83.49%)
 * Likes:    1252
 * Dislikes: 54
 * Total Accepted:    131.4K
 * Total Submissions: 149.6K
 * Testcase Example:  '[1,3,4,1,2,3,1]'
 *
 * You are given an integer array nums. You need to create a 2D array from
 * nums satisfying the following conditions:
 *
 *
 * The 2D array should contain only the elements of the array nums.
 * Each row in the 2D array contains distinct integers.
 * The number of rows in the 2D array should be minimal.
 *
 *
 * Return the resulting array. If there are multiple answers, return any of
 * them.
 *
 * Note that the 2D array can have a different number of elements on each
 * row.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,3,4,1,2,3,1]
 * Output: [[1,3,4,2],[1,3],[1]]
 * Explanation: We can create a 2D array that contains the following rows:
 * - 1,3,4,2
 * - 1,3
 * - 1
 * All elements of nums were used, and each row of the 2D array contains
 * distinct integers, so it is a valid answer.
 * It can be shown that we cannot have less than 3 rows in a valid array.
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2,3,4]
 * Output: [[4,3,2,1]]
 * Explanation: All elements of the array are distinct, so we can keep all of
 * them in the first row of the 2D array.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 200
 * 1 <= nums[i] <= nums.length
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res = vec![];
        let mut cnt = vec![0; nums.len() + 1];
        for n in nums {
            cnt[n as usize] += 1;
        }
        for (i, cnt) in cnt.into_iter().enumerate() {
            for j in 0..cnt {
                if res.len() <= j {
                    res.push(vec![]);
                }
                res[j].push(i as i32)
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::find_matrix,
        vec![
            (
                vec![1, 3, 4, 1, 2, 3, 1],
                vec![vec![1, 3, 4, 2], vec![1, 3], vec![1]],
            ),
            (vec![1, 2, 3, 4], vec![vec![4, 3, 2, 1]]),
            (vec![1], vec![vec![1]]),
            (vec![1, 1, 1, 1], vec![vec![1], vec![1], vec![1], vec![1]]),
            (vec![4, 4, 4, 4], vec![vec![4], vec![4], vec![4], vec![4]]),
        ],
        |a, b| {
            if a.len() != b.len() {
                return false;
            }
            let mut a = a.clone();
            let mut b = b.clone();
            return a.iter_mut().zip(b.iter_mut()).all(|(a, b)| {
                a.sort_unstable();
                b.sort_unstable();
                a == b
            });
        },
    );
}
