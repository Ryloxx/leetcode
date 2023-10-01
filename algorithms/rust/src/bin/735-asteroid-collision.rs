/*
 * @lc app=leetcode id=735 lang=rust
 *
 * [735] Asteroid Collision
 *
 * https://leetcode.com/problems/asteroid-collision/description/
 *
 * algorithms
 * Medium (44.38%)
 * Likes:    5594
 * Dislikes: 561
 * Total Accepted:    303.8K
 * Total Submissions: 682.5K
 * Testcase Example:  '[5,10,-5]'
 *
 * We are given an array asteroids of integers representing asteroids in a
 * row.
 *
 * For each asteroid, the absolute value represents its size, and the sign
 * represents its direction (positive meaning right, negative meaning left).
 * Each asteroid moves at the same speed.
 *
 * Find out the state of the asteroids after all collisions. If two asteroids
 * meet, the smaller one will explode. If both are the same size, both will
 * explode. Two asteroids moving in the same direction will never meet.
 *
 *
 * Example 1:
 *
 *
 * Input: asteroids = [5,10,-5]
 * Output: [5,10]
 * Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never
 * collide.
 *
 *
 * Example 2:
 *
 *
 * Input: asteroids = [8,-8]
 * Output: []
 * Explanation: The 8 and -8 collide exploding each other.
 *
 *
 * Example 3:
 *
 *
 * Input: asteroids = [10,2,-5]
 * Output: [10]
 * Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide
 * resulting in 10.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= asteroids.length <= 10^4
 * -1000 <= asteroids[i] <= 1000
 * asteroids[i] != 0
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut stack: Vec<i32> = vec![];
        'outer: for asteroid in asteroids {
            while let Some(&last) = stack.last() {
                if last.signum() == asteroid.signum() || last < 0 {
                    break;
                }
                match last.abs().cmp(&asteroid.abs()) {
                    std::cmp::Ordering::Less => {
                        stack.pop();
                    }
                    std::cmp::Ordering::Equal => {
                        stack.pop();
                        continue 'outer;
                    }
                    std::cmp::Ordering::Greater => continue 'outer,
                }
            }
            stack.push(asteroid);
        }

        stack
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::asteroid_collision,
        vec![
            ((vec![5, 10, -5]), vec![5, 10]),
            ((vec![5, 5, -5]), vec![5]),
            ((vec![5, -5, 5]), vec![5]),
            ((vec![0, 0, -1]), vec![-1]),
            ((vec![1, 2, 3, -4]), vec![-4]),
            ((vec![1, -10, 3, -4]), vec![-10, -4]),
            ((vec![1, -10, 3, -2]), vec![-10, 3]),
            ((vec![8, -8]), vec![]),
            ((vec![10, 2, -5]), vec![10]),
            ((vec![-2, 5]), vec![-2, 5]),
            (
                (vec![
                    709, -361, -256, 414, 229, 323, 299, -38, -911, 716, 243, 882, 932, -873,
                    -1000, 544, -573, -967,
                ]),
                vec![-911, -1000, -573, -967],
            ),
        ],
        |a, b| a == b,
    )
}
