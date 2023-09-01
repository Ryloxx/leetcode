/*
 * @lc app=leetcode id=239 lang=rust
 *
 * [239] Sliding Window Maximum
 *
 * https://leetcode.com/problems/sliding-window-maximum/description/
 *
 * algorithms
 * Hard (46.56%)
 * Likes:    16294
 * Dislikes: 547
 * Total Accepted:    845.5K
 * Total Submissions: 1.8M
 * Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
 *
 * You are given an array of integers nums, there is a sliding window of size
 * k which is moving from the very left of the array to the very right. You
 * can only see the k numbers in the window. Each time the sliding window
 * moves right by one position.
 *
 * Return the max sliding window.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
 * Output: [3,3,5,5,6,7]
 * Explanation:
 * Window position                Max
 * ---------------               -----
 * [1  3  -1] -3  5  3  6  7       3
 * ⁠1 [3  -1  -3] 5  3  6  7       3
 * ⁠1  3 [-1  -3  5] 3  6  7       5
 * ⁠1  3  -1 [-3  5  3] 6  7       5
 * ⁠1  3  -1  -3 [5  3  6] 7       6
 * ⁠1  3  -1  -3  5 [3  6  7]      7
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1], k = 1
 * Output: [1]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 * 1 <= k <= nums.length
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    // O(N) time complexity
    // O(K) space complexity
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        use std::collections::VecDeque;
        let k = k as usize;
        let mut q: VecDeque<usize> = VecDeque::new();
        let mut res = vec![0; nums.len() - k as usize + 1];
        for i in 0..nums.len() {
            while !q.is_empty() && (q[0] + k <= i) {
                q.pop_front();
            }
            while !q.is_empty() && nums[*q.back().unwrap()] < nums[i] {
                q.pop_back();
            }
            q.push_back(i);
            if i >= k - 1 {
                res[(i + 1 - k) as usize] = nums[q[0]];
            }
        }
        res
    }

    // O(NlogN) time complexity
    // O(K) space complexity
    // pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
    //     use std::collections::BinaryHeap;
    //     let mut h = BinaryHeap::new();
    //     let mut res = vec![0; nums.len() - k as usize + 1];
    //     for i in 0..nums.len() as i32 {
    //         h.push((nums[i as usize], i));
    //         while i - k >= h.peek().unwrap().1 {
    //             h.pop();
    //         }
    //         if i - k + 1 >= 0 {
    //             res[(i - k + 1) as usize] = h.peek().unwrap().0;
    //         }
    //     }
    //     res
    // }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::max_sliding_window(e.0, e.1),
        vec![
            ((vec![1, 3, -1, -3, 5, 3, 6, 7], 3), vec![3, 3, 5, 5, 6, 7]),
            ((vec![1], 1), vec![1]),
            ((vec![1, 3, 1, 2, 0, 5], 3), vec![3, 3, 2, 5]),
            ((vec![1, 1, 1, 1, 1, 1], 2), vec![1, 1, 1, 1, 1]),
            (
                (vec![0, 1, 7, 1, 10, 8, 4, 3, 4, 9, 1, 2, 8, 10], 1),
                vec![0, 1, 7, 1, 10, 8, 4, 3, 4, 9, 1, 2, 8, 10],
            ),
            ((vec![6, 0, 8, 9, 4, 4, 1, 10, 8], 5), vec![9, 9, 9, 10, 10]),
            ((vec![8, 6, 5, 1, 10, 4, 3, 9, 9], 7), vec![10, 10, 10]),
            ((vec![1; 10_000], 10), vec![1; 10_000 - 9]),
            ((vec![1; 10_000], 100), vec![1; 10_000 - 99]),
            ((vec![1; 10_000], 1_000), vec![1; 10_000 - 999]),
            ((vec![1; 10_000], 10_000), vec![1; 10_000 - 9999]),
        ],
        |a, b| a == b,
    )
}
