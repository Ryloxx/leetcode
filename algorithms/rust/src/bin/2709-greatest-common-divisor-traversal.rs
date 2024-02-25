/*
 * @lc app=leetcode id=2709 lang=rust
 *
 * [2709] Greatest Common Divisor Traversal
 *
 * https://leetcode.com/problems/greatest-common-divisor-traversal/description/
 *
 * algorithms
 * Hard (22.97%)
 * Likes:    696
 * Dislikes: 114
 * Total Accepted:    56.9K
 * Total Submissions: 131.5K
 * Testcase Example:  '[2,3,6]'
 *
 * You are given a 0-indexed integer array nums, and you are allowed to
 * traverse between its indices. You can traverse between index i and index
 * j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the
 * greatest common divisor.
 *
 * Your task is to determine if for every pair of indices i and j in nums,
 * where i < j, there exists a sequence of traversals that can take us from i
 * to j.
 *
 * Return true if it is possible to traverse between all such pairs of
 * indices, or false otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [2,3,6]
 * Output: true
 * Explanation: In this example, there are 3 possible pairs of indices: (0,
 * 1), (0, 2), and (1, 2).
 * To go from index 0 to index 1, we can use the sequence of traversals 0 ->
 * 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0],
 * nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1
 * because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
 * To go from index 0 to index 2, we can just go directly because
 * gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to
 * index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6)
 * = 3 > 1.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [3,9,5]
 * Output: false
 * Explanation: No sequence of traversals can take us from index 0 to index 2
 * in this example. So, we return false.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [4,3,12,8]
 * Output: true
 * Explanation: There are 6 possible pairs of indices to traverse between:
 * (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of
 * traversals exists for each pair, so we return true.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^5
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn can_traverse_all_pairs(nums: Vec<i32>) -> bool {
        fn find(roots: &[usize], mut x: usize) -> usize {
            while roots[x] != x {
                x = roots[x];
            }
            x
        }
        fn union(roots: &mut [usize], rank: &mut [usize], x: usize, y: usize) {
            let root_x = find(roots, x);
            let root_y = find(roots, y);
            if root_x == root_y {
                return;
            }
            match rank[root_x].cmp(&rank[root_y]) {
                std::cmp::Ordering::Less => {
                    roots[root_x] = root_y;
                }
                std::cmp::Ordering::Equal => {
                    roots[root_y] = root_x;
                    rank[root_x] += 1;
                }
                std::cmp::Ordering::Greater => {
                    roots[root_y] = root_x;
                }
            }
        }
        if nums.len() == 1 {
            return true;
        }
        let n = 1 + *nums.iter().max().unwrap_or(&0) as usize;
        let mut primes = (0..n).collect::<Vec<usize>>();
        let mut roots = (0..n).collect::<Vec<usize>>();
        let mut ranks = vec![0usize; n];
        for i in 2..n {
            if primes[i] == i {
                let mut j = i;
                while j < n {
                    primes[j] = i;
                    j += i;
                }
            }
        }
        for &n in nums.iter() {
            if n == 1 {
                return false;
            }
            let mut curr = n as usize;
            loop {
                let factor = primes[curr];
                if factor == 1 {
                    break;
                }
                while curr % factor == 0 {
                    curr /= factor;
                }
                union(&mut roots, &mut ranks, factor, n as usize);
            }
        }
        let target = find(&roots, nums[0] as usize);
        nums.into_iter().all(|x| find(&roots, x as usize) == target)
    }
}

// @lc code=end

fn main() {
    rust::test_algo(
        Solution::can_traverse_all_pairs,
        vec![
            (vec![2, 3, 6], true),
            (vec![3, 9, 5], false),
            (vec![4, 3, 12, 8], true),
            (vec![1, 1], false),
            (vec![1], true),
        ],
        |a, b| a == b,
    )
}
