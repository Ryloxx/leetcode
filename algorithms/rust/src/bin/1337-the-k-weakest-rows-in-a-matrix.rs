/*
 * @lc app=leetcode id=1337 lang=rust
 *
 * [1337] The K Weakest Rows in a Matrix
 *
 * https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
 *
 * algorithms
 * Easy (71.38%)
 * Likes:    3817
 * Dislikes: 216
 * Total Accepted:    308.9K
 * Total Submissions: 423.2K
 * Testcase Example:
 * '[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]\n3'
 *
 * You are given an m x n binary matrix mat of 1's (representing soldiers)
 * and 0's (representing civilians). The soldiers are positioned in front of
 * the civilians. That is, all the 1's will appear to the left of all the 0's
 * in each row.
 *
 * A row i is weaker than a row j if one of the following is true:
 *
 *
 * The number of soldiers in row i is less than the number of soldiers in row
 * j.
 * Both rows have the same number of soldiers and i < j.
 *
 *
 * Return the indices of the k weakest rows in the matrix ordered from
 * weakest to strongest.
 *
 *
 * Example 1:
 *
 *
 * Input: mat =
 * [[1,1,0,0,0],
 * [[1,1,0,0,0],
 * [1,1,1,1,0],
 * [1,0,0,0,0],
 * [1,1,0,0,0],
 * [1,1,1,1,1]],
 * k = 3
 * Output: [2,0,3]
 * Explanation:
 * The number of soldiers in each row is:
 * - Row 0: 2
 * - Row 1: 4
 * - Row 2: 1
 * - Row 3: 2
 * - Row 4: 5
 * The rows ordered from weakest to strongest are [2,0,3,1,4].
 *
 *
 * Example 2:
 *
 *
 * Input: mat =
 * [[1,0,0,0],
 * [[1,0,0,0],
 * [1,1,1,1],
 * [1,0,0,0],
 * [1,0,0,0]],
 * k = 2
 * Output: [0,2]
 * Explanation:
 * The number of soldiers in each row is:
 * - Row 0: 1
 * - Row 1: 4
 * - Row 2: 1
 * - Row 3: 1
 * The rows ordered from weakest to strongest are [0,2,3,1].
 *
 *
 *
 * Constraints:
 *
 *
 * m == mat.length
 * n == mat[i].length
 * 2 <= n, m <= 100
 * 1 <= k <= m
 * matrix[i][j] is either 0 or 1.
 *
 *
 */

#![feature(test)]

struct Solution;
// @lc code=start
impl Solution {
    pub fn k_weakest_rows(mut mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let n = mat[0].len();
        let mut res = Vec::with_capacity(k);
        for (j, line) in mat.iter_mut().enumerate() {
            if line[0] == 0 {
                res.push(j as i32);
            }
            if res.len() == k {
                return res;
            }
        }
        for i in 1..n {
            for (j, line) in mat.iter().enumerate() {
                if line[i - 1] + line[i] == 1 {
                    res.push(j as i32);
                }
                if res.len() == k {
                    return res;
                }
            }
        }
        let last = n - 1;
        for (j, line) in mat.iter().enumerate() {
            if line[last] == 1 {
                res.push(j as i32);
            }
            if res.len() == k {
                return res;
            }
        }
        res
    }
}

// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::k_weakest_rows(e.0, e.1),
        vec![
            (
                (
                    vec![
                        vec![1, 1, 0, 0, 0],
                        vec![1, 1, 1, 1, 0],
                        vec![1, 0, 0, 0, 0],
                        vec![1, 1, 0, 0, 0],
                        vec![1, 1, 1, 1, 1],
                    ],
                    3,
                ),
                vec![2, 0, 3],
            ),
            (
                (
                    vec![
                        vec![1, 0, 0, 0],
                        vec![1, 1, 1, 1],
                        vec![1, 0, 0, 0],
                        vec![1, 0, 0, 0],
                    ],
                    2,
                ),
                vec![0, 2],
            ),
            (
                (
                    vec![
                        vec![1, 1, 0, 0, 0],
                        vec![1, 1, 1, 1, 0],
                        vec![1, 0, 0, 0, 0],
                        vec![1, 1, 0, 0, 0],
                        vec![0, 0, 0, 0, 0],
                    ],
                    3,
                ),
                vec![4, 2, 0],
            ),
            (
                (
                    vec![
                        vec![1, 1, 1, 1, 1, 1],
                        vec![1, 1, 1, 1, 1, 1],
                        vec![1, 1, 1, 1, 1, 1],
                    ],
                    1,
                ),
                vec![0],
            ),
            (
                (vec![vec![0, 0], vec![0, 0], vec![1, 1], vec![1, 1]], 1),
                vec![0],
            ),
        ],
        |a, b| a == b,
    )
}

mod bench {
    extern crate test;
    #[allow(unused_imports)]
    use test::Bencher;

    #[bench]
    fn v_1(bencher: &mut Bencher) {
        pub fn k_weakest_rows(mut mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
            let k = k as usize;
            let n = mat[0].len();
            let mut res = Vec::with_capacity(k);
            for (j, line) in mat.iter_mut().enumerate() {
                line.push(0);
                if line[0] == 0 {
                    res.push(j as i32);
                }
                if res.len() == k {
                    return res;
                }
            }
            for i in 1..n {
                for (j, line) in mat.iter().enumerate() {
                    if line[i - 1] + line[i] == 1 {
                        res.push(j as i32);
                    }
                    if res.len() == k {
                        return res;
                    }
                }
            }
            res
        }
        let test = vec![
            (
                vec![
                    vec![1, 1, 0, 0, 0],
                    vec![1, 1, 1, 1, 0],
                    vec![1, 0, 0, 0, 0],
                    vec![1, 1, 0, 0, 0],
                    vec![1, 1, 1, 1, 1],
                ],
                3,
            ),
            (
                vec![
                    vec![1, 0, 0, 0],
                    vec![1, 1, 1, 1],
                    vec![1, 0, 0, 0],
                    vec![1, 0, 0, 0],
                ],
                2,
            ),
            (
                vec![
                    vec![1, 1, 0, 0, 0],
                    vec![1, 1, 1, 1, 0],
                    vec![1, 0, 0, 0, 0],
                    vec![1, 1, 0, 0, 0],
                    vec![0, 0, 0, 0, 0],
                ],
                3,
            ),
            (
                vec![
                    vec![1, 1, 1, 1, 1, 1],
                    vec![1, 1, 1, 1, 1, 1],
                    vec![1, 1, 1, 1, 1, 1],
                ],
                1,
            ),
            (vec![vec![0, 0], vec![0, 0], vec![1, 1], vec![1, 1]], 1),
        ];
        bencher.iter(|| {
            for (a, b) in test.iter() {
                k_weakest_rows(a.clone(), *b);
            }
        });
    }

    #[bench]
    fn v_2(bencher: &mut Bencher) {
        pub fn k_weakest_rows(mut mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
            let k = k as usize;
            let n = mat[0].len();
            let mut res = Vec::with_capacity(k);
            for (j, line) in mat.iter_mut().enumerate() {
                if line[0] == 0 {
                    res.push(j as i32);
                }
                if res.len() == k {
                    return res;
                }
            }
            for i in 1..n {
                for (j, line) in mat.iter().enumerate() {
                    if line[i - 1] + line[i] == 1 {
                        res.push(j as i32);
                    }
                    if res.len() == k {
                        return res;
                    }
                }
            }
            let last = n - 1;
            for (j, line) in mat.iter().enumerate() {
                if line[last] == 1 {
                    res.push(j as i32);
                }
                if res.len() == k {
                    return res;
                }
            }
            res
        }
        let test = vec![
            (
                vec![
                    vec![1, 1, 0, 0, 0],
                    vec![1, 1, 1, 1, 0],
                    vec![1, 0, 0, 0, 0],
                    vec![1, 1, 0, 0, 0],
                    vec![1, 1, 1, 1, 1],
                ],
                3,
            ),
            (
                vec![
                    vec![1, 0, 0, 0],
                    vec![1, 1, 1, 1],
                    vec![1, 0, 0, 0],
                    vec![1, 0, 0, 0],
                ],
                2,
            ),
            (
                vec![
                    vec![1, 1, 0, 0, 0],
                    vec![1, 1, 1, 1, 0],
                    vec![1, 0, 0, 0, 0],
                    vec![1, 1, 0, 0, 0],
                    vec![0, 0, 0, 0, 0],
                ],
                3,
            ),
            (
                vec![
                    vec![1, 1, 1, 1, 1, 1],
                    vec![1, 1, 1, 1, 1, 1],
                    vec![1, 1, 1, 1, 1, 1],
                ],
                1,
            ),
            (vec![vec![0, 0], vec![0, 0], vec![1, 1], vec![1, 1]], 1),
        ];
        bencher.iter(|| {
            for (a, b) in test.iter() {
                k_weakest_rows(a.clone(), *b);
            }
        });
    }
}
