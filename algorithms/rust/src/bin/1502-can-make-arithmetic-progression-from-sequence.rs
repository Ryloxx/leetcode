/*
 * @lc app=leetcode id=1502 lang=rust
 *
 * [1502] Can Make Arithmetic Progression From Sequence
 *
 * https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
 *
 * algorithms
 * Easy (68.04%)
 * Likes:    1579
 * Dislikes: 77
 * Total Accepted:    169.4K
 * Total Submissions: 242.5K
 * Testcase Example:  '[3,5,1]'
 *
 * A sequence of numbers is called an arithmetic progression if the
 * difference between any two consecutive elements is the same.
 *
 * Given an array of numbers arr, return true if the array can be rearranged
 * to form an arithmetic progression. Otherwise, return false.
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [3,5,1]
 * Output: true
 * Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with
 * differences 2 and -2 respectively, between each consecutive elements.
 *
 *
 * Example 2:
 *
 *
 * Input: arr = [1,2,4]
 * Output: false
 * Explanation: There is no way to reorder the elements to obtain an
 * arithmetic progression.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= arr.length <= 1000
 * -10^6 <= arr[i] <= 10^6
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn can_make_arithmetic_progression(arr: Vec<i32>) -> bool {
        let (mut s, mut min, mut max) = (0, i32::MAX, i32::MIN);
        for x in arr.iter() {
            s += *x;
            min = min.min(*x);
            max = max.max(*x);
        }
        let n = arr.len() as i32;
        let x0 = arr.iter().min().unwrap();
        let ns = ((n - 1) * n) / 2;
        let r = (s - n * x0) / ns;
        if x0 + r * (n - 1) != max {
            return false;
        }
        if r == 0 {
            return true;
        }
        let mut check = 0;
        for (i, xk) in arr.iter().enumerate() {
            if (xk - x0) % r != 0 {
                return false;
            }
            check ^= (xk - x0) ^ (i as i32 * r);
        }
        return check == 0;
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::can_make_arithmetic_progression(e),
        vec![
            (vec![3, 5, 1], true),
            (vec![0, 0, 0, 0], true),
            (vec![-15, -1, -3, 5, -12, -14], false),
            (vec![1, 10, 10, 10, 19], false),
            (vec![2, 10, 7, 8, 3], false),
            (vec![1, 2, 3, 2, 5], false),
            //
        ],
        |a, b| a == b,
    );
}
