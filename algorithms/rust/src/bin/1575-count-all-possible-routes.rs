/*
 * @lc app=leetcode id=1575 lang=rust
 *
 * [1575] Count All Possible Routes
 *
 * https://leetcode.com/problems/count-all-possible-routes/description/
 *
 * algorithms
 * Hard (56.77%)
 * Likes:    1032
 * Dislikes: 40
 * Total Accepted:    31.9K
 * Total Submissions: 49.6K
 * Testcase Example:  '[2,3,6,8,4]\n1\n3\n5'
 *
 * You are given an array of distinct positive integers locations where
 * locations[i] represents the position of city i. You are also given
 * integers start, finish and fuel representing the starting city, ending
 * city, and the initial amount of fuel you have, respectively.
 *
 * At each step, if you are at city i, you can pick any city j such that j !=
 * i and 0 <= j < locations.length and move to city j. Moving from city i to
 * city j reduces the amount of fuel you have by |locations[i] -
 * locations[j]|. Please notice that |x| denotes the absolute value of x.
 *
 * Notice that fuel cannot become negative at any point in time, and that you
 * are allowed to visit any city more than once (including start and finish).
 *
 * Return the count of all possible routes from start to finish. Since the
 * answer may be too large, return it modulo 10^9 + 7.
 *
 *
 * Example 1:
 *
 *
 * Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
 * Output: 4
 * Explanation: The following are all possible routes, each uses 5 units of
 * fuel:
 * 1 -> 3
 * 1 -> 2 -> 3
 * 1 -> 4 -> 3
 * 1 -> 4 -> 2 -> 3
 *
 *
 * Example 2:
 *
 *
 * Input: locations = [4,3,1], start = 1, finish = 0, fuel = 6
 * Output: 5
 * Explanation: The following are all possible routes:
 * 1 -> 0, used fuel = 1
 * 1 -> 2 -> 0, used fuel = 5
 * 1 -> 2 -> 1 -> 0, used fuel = 5
 * 1 -> 0 -> 1 -> 0, used fuel = 3
 * 1 -> 0 -> 1 -> 0 -> 1 -> 0, used fuel = 5
 *
 *
 * Example 3:
 *
 *
 * Input: locations = [5,2,1], start = 0, finish = 2, fuel = 3
 * Output: 0
 * Explanation: It is impossible to get from 0 to 2 using only 3 units of
 * fuel since the shortest route needs 4 units of fuel.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= locations.length <= 100
 * 1 <= locations[i] <= 10^9
 * All integers in locations are distinct.
 * 0 <= start, finish < locations.length
 * 1 <= fuel <= 200
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn count_routes(locations: Vec<i32>, start: i32, finish: i32, fuel: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        fn dfs(
            curr_station: usize,
            curr_fuel: i32,
            finish: usize,
            locations: &Vec<i32>,
            memo: &mut Vec<Vec<i32>>,
        ) -> i32 {
            let ptr = &mut memo[curr_station][curr_fuel as usize] as *mut i32;
            unsafe {
                if *ptr >= 0 {
                    return *ptr;
                }
                *ptr = 0;
                if (locations[curr_station] - locations[finish]).abs() <= curr_fuel {
                    if curr_station == finish {
                        *ptr += 1;
                    }
                    for (j, cost) in locations.iter().enumerate() {
                        if j == curr_station {
                            continue;
                        }
                        let curr_fuel = curr_fuel - (cost - locations[curr_station]).abs();
                        if curr_fuel >= 0 {
                            *ptr += dfs(j, curr_fuel, finish, locations, memo);
                            *ptr %= MOD;
                        }
                    }
                }
                *ptr
            }
        }

        dfs(
            start as usize,
            fuel,
            finish as usize,
            &locations,
            &mut vec![vec![-1; fuel as usize + 1]; locations.len()],
        )
    }
}
// @lc code=end
fn main() {
    rust::test_algo(
        |e| Solution::count_routes(e.0, e.1, e.2, e.3),
        vec![
            //
            ((vec![2, 3, 6, 8, 4], 1, 3, 5), 4),
            ((vec![4, 3, 1], 1, 0, 6), 5),
            ((vec![5, 2, 1], 0, 2, 3), 0),
            ((Vec::from_iter(1..101), 0, 99, 200), 709861113),
        ],
        |a, b| a == b,
    )
}
