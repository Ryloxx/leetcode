/*
 * @lc app=leetcode id=1095 lang=rust
 *
 * [1095] Find in Mountain Array
 *
 * https://leetcode.com/problems/find-in-mountain-array/description/
 *
 * algorithms
 * Hard (35.17%)
 * Likes:    2496
 * Dislikes: 94
 * Total Accepted:    82.9K
 * Total Submissions: 223.9K
 * Testcase Example:  '[1,2,3,4,5,3,1]\n3'
 *
 * (This problem is an interactive problem.)
 *
 * You may recall that an array arr is a mountain array if and only if:
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
 * Given a mountain array mountainArr, return the minimum index such that
 * mountainArr.get(index) == target. If such an index does not exist, return
 * -1.
 *
 * You cannot access the mountain array directly. You may only access the
 * array using a MountainArray interface:
 *
 *
 * MountainArray.get(k) returns the element of the array at index k
 * (0-indexed).
 * MountainArray.length() returns the length of the array.
 *
 *
 * Submissions making more than 100 calls to MountainArray.get will be judged
 * Wrong Answer. Also, any solutions that attempt to circumvent the judge
 * will result in disqualification.
 *
 *
 * Example 1:
 *
 *
 * Input: array = [1,2,3,4,5,3,1], target = 3
 * Output: 2
 * Explanation: 3 exists in the array, at index=2 and index=5. Return the
 * minimum index, which is 2.
 *
 * Example 2:
 *
 *
 * Input: array = [0,1,2,4,2,1], target = 3
 * Output: -1
 * Explanation: 3 does not exist in the array, so we return -1.
 *
 *
 *
 * Constraints:
 *
 *
 * 3 <= mountain_arr.length() <= 10^4
 * 0 <= target <= 10^9
 * 0 <= mountain_arr.get(index) <= 10^9
 *
 *
 */
struct Solution;
use std::{
    cell::RefCell,
    sync::{Arc, Mutex},
};
struct MountainArray(Vec<i32>, Arc<Mutex<RefCell<i32>>>);
impl MountainArray {
    fn new(arr: Vec<i32>) -> Self {
        Self(arr, Arc::new(Mutex::new(RefCell::new(0))))
    }
    fn get(&self, index: i32) -> i32 {
        *self.1.lock().unwrap().borrow_mut() += 1;
        self.0[index as usize]
    }
    fn length(&self) -> i32 {
        self.0.len() as i32
    }
}
// @lc code=start

// This is the MountainArray's API interface.
// You should not implement it, or speculate about its implementation

impl Solution {
    pub fn find_in_mountain_array(target: i32, mountain_arr: &MountainArray) -> i32 {
        let n = mountain_arr.length() as usize;
        let mut lo = 0;
        let mut hi = n;
        // LEFT SEARCH
        while lo < hi {
            let mid = (lo + hi) >> 1;
            let next_after_mid = mid + 1;
            let num = mountain_arr.get(mid as i32);
            let next = if next_after_mid == n {
                i32::MIN
            } else {
                mountain_arr.get(next_after_mid as i32)
            };
            if next > num {
                if num == target {
                    return mid as i32;
                }
                // LEFT SIDE
                if target > num {
                    lo = next_after_mid;
                } else {
                    hi = mid;
                }
            } else {
                // RIGHT SIDE + MOUNTAIN PEAK
                hi = mid;
            }
        }
        let mut lo = 0;
        let mut hi = n;
        // RIGHT SEARCH
        while lo < hi {
            let mid = (lo + hi) >> 1;
            let next_after_mid = mid + 1;
            let num = mountain_arr.get(mid as i32);
            let next = if next_after_mid == n {
                i32::MIN
            } else {
                mountain_arr.get(next_after_mid as i32)
            };
            if next > num {
                // LEFT SIDE
                lo = next_after_mid;
            } else {
                if num == target {
                    return mid as i32;
                }
                // RIGHT SIDE + MOUNTAIN PEAK
                if target > num {
                    hi = mid;
                } else {
                    lo = next_after_mid
                }
            }
        }
        -1
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| {
            let ret = Solution::find_in_mountain_array(e.1, &e.0);
            if e.1 > 100 {
                panic!("Call to 'get' exceeded, got {}", e.1);
            }
            ret
        },
        vec![
            ((MountainArray::new(vec![1, 2, 3, 4, 5, 3, 1]), 3), 2),
            ((MountainArray::new(vec![0, 1, 2, 4, 2, 1]), 3), -1),
            ((MountainArray::new(vec![0, 1, 2, 3, 2, 1]), 3), 3),
            ((MountainArray::new(vec![1, 2, 3, 2, 1]), 3), 2),
            ((MountainArray::new(vec![0, 1, 2, 3, 4, 2]), 4), 4),
            ((MountainArray::new(vec![0, 1, 2, 3, 4, 5, 4]), 5), 5),
            ((MountainArray::new(vec![4, 5, 4, 3, 2, 1, 0]), 5), 1),
            ((MountainArray::new(vec![0, 1, 2, 3, 4, 5, 4]), 4), 4),
            ((MountainArray::new(vec![4, 5, 4, 3, 2, 1, 0]), 4), 0),
            ((MountainArray::new(vec![3, 5, 3, 2, 0]), 3), 0),
        ],
        |a, b| a == b,
    );
}
