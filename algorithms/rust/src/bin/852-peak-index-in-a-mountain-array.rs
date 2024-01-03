/*
 * @lc app=leetcode id=852 lang=rust
 *
 * [852] Peak Index in a Mountain Array
 *
 * https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
 *
 * algorithms
 * Medium (69.36%)
 * Likes:    6226
 * Dislikes: 1864
 * Total Accepted:    640.1K
 * Total Submissions: 927.6K
 * Testcase Example:  '[0,1,0]'
 *
 * An array arr a mountain if the following properties hold:
 *
 *
 * arr.length >= 3
 * There exists some i with 0 < i < arr.length - 1 such that:
 *
 * arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
 * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
 *
 *
 *
 *
 * Given a mountain array arr, return the index i such that arr[0] < arr[1] <
 * ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
 *
 * You must solve it in O(log(arr.length)) time complexity.
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [0,1,0]
 * Output: 1
 *
 *
 * Example 2:
 *
 *
 * Input: arr = [0,2,1,0]
 * Output: 1
 *
 *
 * Example 3:
 *
 *
 * Input: arr = [0,10,5,2]
 * Output: 1
 *
 *
 *
 * Constraints:
 *
 *
 * 3 <= arr.length <= 10^5
 * 0 <= arr[i] <= 10^6
 * arr is guaranteed to be a mountain array.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    // O(logN) time complexity
    // O(1) space complexity
    pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
        let mut lo: usize = 0;
        let mut hi: usize = arr.len() - 1;

        while lo < hi {
            let mid = (lo + hi + 1) >> 1;
            if arr[mid - 1] > arr[mid] {
                hi = mid - 1;
            } else {
                lo = mid;
            }
        }
        lo as i32
    }

    // O(N) time complexity
    // O(1) space complexity
    // pub fn peak_index_in_mountain_array(arr: Vec<i32>) -> i32 {
    //     let mut i = 0;
    //     while i < arr.len() - 1 && arr[i + 1] > arr[i] {
    //         i += 1;
    //     }
    //     i as i32
    // }
}
// @lc code=end
fn main() {
    rust::test_algo(
        Solution::peak_index_in_mountain_array,
        vec![
            ((vec![0, 1, 0]), 1),
            ((vec![0, 2, 1, 0]), 1),
            ((vec![0, 10, 5, 2]), 1),
            ((vec![1, 2, 3, 4, 0]), 3),
            ((vec![0, 1, 2]), 2),
            ((vec![2, 1, 0]), 0),
            ((vec![0, 1, 2, 3]), 3),
            ((vec![3, 2, 1, 0]), 0),
        ],
        |a, b| a == b,
    )
}
