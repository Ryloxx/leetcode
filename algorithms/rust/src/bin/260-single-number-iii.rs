/*
 * @lc app=leetcode id=260 lang=rust
 *
 * [260] Single Number III
 *
 * https://leetcode.com/problems/single-number-iii/description/
 *
 * algorithms
 * Medium (68.37%)
 * Likes:    6038
 * Dislikes: 247
 * Total Accepted:    408.4K
 * Total Submissions: 584.9K
 * Testcase Example:  '[1,2,1,3,2,5]'
 *
 * Given an integer array nums, in which exactly two elements appear only
 * once and all the other elements appear exactly twice. Find the two
 * elements that appear only once. You can return the answer in any order.
 *
 * You must write an algorithm that runs in linear runtime complexity and
 * uses only constant extra space.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,1,3,2,5]
 * Output: [3,5]
 * Explanation:  [5, 3] is also a valid answer.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [-1,0]
 * Output: [-1,0]
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [0,1]
 * Output: [1,0]
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= nums.length <= 3 * 10^4
 * -2^31 <= nums[i] <= 2^31 - 1
 * Each integer in nums will appear twice, only two integers will appear
 * once.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    // Lets call the numbers we are looking for a and b.
    // There are 2 things important to notice.
    // 1. a and b are different, this means that their binary representation differs
    //    by at least one bit.
    // 2. Other pairs of number are equal so their bit representation does not
    //    differ.
    //
    // We can take advantage of those 2 properties to partition the array in a way
    // that would let us derive the value of a and b.
    // We will partition on a bit that is set on a^b, let's call it i.
    // We know for a fact that i will be different for a and b, therefore one of
    // the partition will contain a and the other will contain b and we also know
    // for a fact that every pair of numbers will be placed in the same partition
    // since they have i equal.
    // We can get a^b by xoring all numbers.
    // By xoring each partition numbers respectively, we can find a and b, since
    // they are the only number in their partition that has no duplicate.
    //
    // O(N) time complexity
    // O(1) space complexity
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        let a_xor_b = nums.iter().fold(0, |acc, curr| acc ^ curr);
        let partition_bit = a_xor_b & a_xor_b.wrapping_neg();
        nums.into_iter()
            .fold([0, 0], |mut acc, curr| {
                acc[((partition_bit & curr) as usize).min(1)] ^= curr;
                acc
            })
            .to_vec()
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::single_number,
        vec![
            ((vec![1, 2, 1, 3, 2, 5]), vec![3, 5]),
            ((vec![-1, 0]), vec![-1, 0]),
            ((vec![0, 1]), vec![1, 0]),
            ((vec![1, 2, 3, 3]), vec![1, 2]),
            ((vec![1, 1, 0, -2147483648]), vec![0, -2147483648]),
            (
                (vec![1, 1, 2147483647, -2147483648]),
                vec![2147483647, -2147483648],
            ),
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
