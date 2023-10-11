/*
 * @lc app=leetcode id=2251 lang=rust
 *
 * [2251] Number of Flowers in Full Bloom
 *
 * https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/
 *
 * algorithms
 * Hard (50.95%)
 * Likes:    948
 * Dislikes: 20
 * Total Accepted:    32.3K
 * Total Submissions: 59.6K
 * Testcase Example:  '[[1,6],[3,7],[9,12],[4,13]]\n[2,3,7,11]'
 *
 * You are given a 0-indexed 2D integer array flowers, where flowers[i] =
 * [starti, endi] means the i^th flower will be in full bloom from starti to
 * endi (inclusive). You are also given a 0-indexed integer array people of
 * size n, where people[i] is the time that the i^th person will arrive to
 * see the flowers.
 *
 * Return an integer array answer of size n, where answer[i] is the number of
 * flowers that are in full bloom when the i^th person arrives.
 *
 *
 * Example 1:
 *
 *
 * Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
 * Output: [1,2,2,2]
 * Explanation: The figure above shows the times when the flowers are in full
 * bloom and when the people arrive.
 * For each person, we return the number of flowers in full bloom during
 * their arrival.
 *
 *
 * Example 2:
 *
 *
 * Input: flowers = [[1,10],[3,3]], poeple = [3,3,2]
 * Output: [2,2,1]
 * Explanation: The figure above shows the times when the flowers are in full
 * bloom and when the people arrive.
 * For each person, we return the number of flowers in full bloom during
 * their arrival.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= flowers.length <= 5 * 10^4
 * flowers[i].length == 2
 * 1 <= starti <= endi <= 10^9
 * 1 <= people.length <= 5 * 10^4
 * 1 <= people[i] <= 10^9
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn full_bloom_flowers(mut flowers: Vec<Vec<i32>>, people: Vec<i32>) -> Vec<i32> {
        use std::collections::BinaryHeap;
        flowers.sort_by_key(|flower| -flower[0]);
        let mut order = (0..people.len()).collect::<Vec<usize>>();
        order.sort_unstable_by_key(|&idx| people[idx]);
        let mut res = vec![0; people.len()];
        let mut h = BinaryHeap::<i32>::new();
        for i in order {
            let time = people[i];
            while !flowers.is_empty() && flowers.last().unwrap()[0] <= time {
                let flower = flowers.pop().unwrap();
                h.push(-flower[1])
            }
            while !h.is_empty() && -h.peek().unwrap() < time {
                h.pop().unwrap();
            }
            if h.is_empty() && flowers.is_empty() {
                break;
            }
            res[i] = h.len() as i32;
        }
        res
    }

    // pub fn full_bloom_flowers(flowers: Vec<Vec<i32>>, people: Vec<i32>) ->
    // Vec<i32> {     let mut res = vec![0; people.len()];
    //     let mut start = vec![];
    //     let mut end = vec![];
    //     for flower in flowers {
    //         start.push(flower[0]);
    //         end.push(flower[1]);
    //     }
    //     start.sort_unstable();
    //     end.sort_unstable();
    //     for (i, time) in people.into_iter().enumerate() {
    //         res[i] =
    //             (start.partition_point(|&x| x <= time) - end.partition_point(|&x|
    // x < time)) as i32;     }
    //     res
    // }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::full_bloom_flowers(e.0, e.1),
        vec![
            (
                (
                    vec![vec![1, 6], vec![3, 7], vec![9, 12], vec![4, 13]],
                    vec![2, 3, 7, 11],
                ),
                vec![1, 2, 2, 2],
            ),
            (
                (vec![vec![1, 10], vec![3, 3]], vec![3, 3, 2]),
                vec![2, 2, 1],
            ),
            ((vec![], vec![3, 3, 2]), vec![0, 0, 0]),
            ((vec![vec![1, 10], vec![3, 3]], vec![]), vec![]),
            ((vec![vec![1, 1], vec![1, 1]], vec![1, 2, 3]), vec![2, 0, 0]),
        ],
        |a, b| a == b,
    );
}
