/*
 * @lc app=leetcode id=1203 lang=rust
 *
 * [1203] Sort Items by Groups Respecting Dependencies
 *
 * https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/
 *
 * algorithms
 * Hard (50.83%)
 * Likes:    1347
 * Dislikes: 234
 * Total Accepted:    36.5K
 * Total Submissions: 56.4K
 * Testcase Example:  '8\n2\n[-1,-1,1,0,0,1,0,-1]\n[[],[6],[5],[6],[3,6],[],[],[]]'
 *
 * There are n items each belonging to zero or one of m groups where group[i]
 * is the group that the i-th item belongs to and it's equal to -1 if the i-th
 * item belongs to no group. The items and the groups are zero indexed. A group
 * can have no item belonging to it.
 *
 * Return a sorted list of the items such that:
 *
 *
 * The items that belong to the same group are next to each other in the sorted
 * list.
 * There are some relations between these items where beforeItems[i] is a list
 * containing all the items that should come before the i-th item in the sorted
 * array (to the left of the i-th item).
 *
 *
 * Return any solution if there is more than one solution and return an empty
 * list if there is no solution.
 *
 *
 * Example 1:
 *
 *
 *
 *
 * Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
 * [[],[6],[5],[6],[3,6],[],[],[]]
 * Output: [6,3,4,1,5,2,0,7]
 *
 *
 * Example 2:
 *
 *
 * Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
 * [[],[6],[5],[6],[3],[],[4],[]]
 * Output: []
 * Explanation: This is the same as example 1 except that 4 needs to be before
 * 6 in the sorted list.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= m <= n <= 3 * 10^4
 * group.length == beforeItems.length == n
 * -1 <= group[i] <= m - 1
 * 0 <= beforeItems[i].length <= n - 1
 * 0 <= beforeItems[i][j] <= n - 1
 * i != beforeItems[i][j]
 * beforeItems[i] does not contain duplicates elements.
 *
 *
 */

struct Solution;

// @lc code=start
impl Solution {
    pub fn sort_items(
        n: i32,
        mut m: i32,
        mut group: Vec<i32>,
        before_items: Vec<Vec<i32>>,
    ) -> Vec<i32> {
        use std::collections::HashSet;
        fn sort(
            curr: i32,
            out: &mut Vec<i32>,
            deps: &Vec<Vec<i32>>,
            cycle: &mut HashSet<i32>,
            seen: &mut HashSet<i32>,
            cmp: &impl Fn(i32, i32) -> bool,
        ) -> bool {
            if cycle.contains(&curr) {
                return false;
            }
            if seen.contains(&curr) {
                return true;
            }
            seen.insert(curr);
            cycle.insert(curr);
            for &j in &deps[curr as usize] {
                if cmp(curr, j) && !sort(j, out, deps, cycle, seen, cmp) {
                    return false;
                }
            }
            cycle.remove(&curr);
            out.push(curr);
            true
        }

        let mut groups: Vec<Vec<i32>> = vec![vec![]; m as usize];
        for (i, g) in group.iter_mut().enumerate() {
            if *g == -1 {
                groups.push(vec![i as i32]);
                *g = m;
                m += 1;
            } else {
                groups[*g as usize].push(i as i32);
            }
        }
        let mut group_graph_deps: Vec<Vec<i32>> = vec![vec![]; m as usize];
        for (u, vs) in before_items.iter().enumerate() {
            let group_u = group[u];
            for v in vs {
                group_graph_deps[group_u as usize].push(group[*v as usize]);
            }
        }

        let mut res = Vec::with_capacity(n as usize);
        let mut group_order = Vec::with_capacity(m as usize);
        let mut seen = HashSet::with_capacity(m as usize);
        for j in 0..m {
            if !sort(
                j,
                &mut group_order,
                &mut group_graph_deps,
                &mut HashSet::new(),
                &mut seen,
                &|u, v| u != v,
            ) {
                return vec![];
            }
        }

        for g in group_order {
            let mut seen = HashSet::with_capacity(groups[g as usize].len());
            for &k in &groups[g as usize] {
                if !sort(
                    k,
                    &mut res,
                    &before_items,
                    &mut HashSet::new(),
                    &mut seen,
                    &|u, v| group[u as usize] == group[v as usize],
                ) {
                    return vec![];
                };
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::sort_items(e.0, e.1, e.2, e.3),
        vec![
            (
                (
                    8,
                    2,
                    vec![-1, -1, 1, 0, 0, 1, 0, -1],
                    vec![
                        vec![],
                        vec![6],
                        vec![5],
                        vec![6],
                        vec![3, 6],
                        vec![],
                        vec![],
                        vec![],
                    ],
                ),
                vec![6, 3, 4, 5, 2, 0, 1, 7],
            ),
            (
                (
                    8,
                    2,
                    vec![-1, -1, 1, 0, 0, 1, 0, -1],
                    vec![
                        vec![],
                        vec![6],
                        vec![5],
                        vec![6],
                        vec![3],
                        vec![],
                        vec![4],
                        vec![],
                    ],
                ),
                vec![],
            ),
            (
                (
                    4,
                    4,
                    vec![0, 1, 2, 3],
                    vec![vec![1], vec![2], vec![3], vec![0]],
                ),
                vec![],
            ),
            (
                (
                    6,
                    4,
                    vec![0, 1, 2, 3, 0, 0],
                    vec![vec![4], vec![2], vec![3], vec![0], vec![5], vec![0]],
                ),
                vec![],
            ),
            ((1, 1, vec![0], vec![vec![]]), vec![0]),
            (
                (3, 100, vec![0, 0, 0], vec![vec![], vec![], vec![]]),
                vec![0, 1, 2],
            ),
            (
                (
                    5,
                    3,
                    vec![0, 0, 2, 1, 0],
                    vec![vec![3], vec![], vec![], vec![], vec![1, 3, 2]],
                ),
                vec![3, 2, 0, 1, 4],
            ),
            (
                (
                    500,
                    440,
                    vec![
                        413, 165, 353, 26, 346, 201, 369, 340, 300, 104, 105, 66, 361, 15, 257,
                        438, 375, 115, 325, 290, 436, 107, 394, 237, 232, 79, 43, 202, 185, 187,
                        134, 298, 183, 367, 326, 78, 163, 79, 88, 289, 377, 171, 141, 107, 381,
                        132, 177, 402, 332, 232, 147, 266, 208, 181, 109, 260, 160, 422, 21, 20,
                        333, 262, 186, 155, 436, 136, 46, 299, 214, 58, 194, 92, 90, 286, 74, 21,
                        196, 197, 186, 261, 372, 181, 312, 63, 28, 108, 237, 358, 337, 335, 307,
                        153, 110, 395, 238, 255, 154, 263, 382, 154, 125, 172, 113, 367, 124, 307,
                        129, 436, 122, 396, 432, 292, 57, 182, 404, 278, 117, 404, 221, 12, 430,
                        176, 377, 390, 388, 333, 25, 16, 342, 216, 127, 2, 32, 154, 11, 296, 412,
                        76, 22, 345, 209, 256, 256, 347, 240, 362, 8, 43, 122, 311, 123, 379, 166,
                        0, 285, 224, 67, 246, 58, 359, 37, 157, 117, 221, 7, 158, 140, 129, 273,
                        299, 121, 32, 190, 36, 409, 229, 49, 78, 141, 189, 333, 105, 205, 301, 403,
                        0, 386, 431, 76, 56, 200, 222, 7, 120, 275, 0, 225, 361, 382, 209, 404, 39,
                        26, 199, 417, 215, 410, 316, 108, 359, 314, 260, 413, 29, 337, 61, 336,
                        422, 260, 16, 141, 114, 10, 348, 215, 309, 12, 295, 332, 191, 226, 155,
                        337, 107, 193, 148, 175, 288, 58, 287, 270, 84, 362, 268, 218, 363, 395,
                        345, 183, 411, 82, 345, 219, 390, 222, 408, 205, 276, 7, 9, 340, 342, 413,
                        49, 363, 6, 238, 4, 416, 397, 196, 74, 228, 401, 200, 32, 17, 153, 421,
                        294, 401, 100, 410, 273, 415, 76, 141, 217, 438, 239, 217, 257, 321, 315,
                        306, 299, 155, 38, 43, 199, 337, 97, 324, 250, 268, 284, 111, 377, 430,
                        396, 298, 234, 256, 358, 11, 380, 56, 233, 155, 28, 401, 211, 134, 305,
                        258, 125, 334, 372, 317, 104, 380, 197, 359, 139, 224, 302, 283, 401, 79,
                        261, 68, 412, 269, 259, 175, 269, 231, 181, 164, 278, 367, 165, 241, 404,
                        130, 64, 48, 371, 203, 198, 52, 115, 19, 426, 358, 380, 159, 304, 270, 143,
                        99, 272, 249, 228, 49, 230, 10, 171, 251, 213, 270, 74, 377, 133, 272, 349,
                        409, 226, 421, 286, 198, 65, 222, 400, 76, 302, 76, 207, 364, 422, 266,
                        428, 223, 305, 155, 167, 302, 350, 160, 237, 431, 19, 22, 217, 75, 281,
                        269, 438, 290, 205, 50, 342, 144, 97, 142, 171, 53, 114, 48, 329, 422, 324,
                        84, 275, 144, 270, 275, 158, 190, 421, 281, 182, 210, 187, 185, 419, 424,
                        162, 123, 24, 375, 19, 424, 402, 95, 101, 377, 298, 78, 426, 20, 222, 415,
                        47, 429, 333, 429, 328, 249, 314, 318, 46, 217, 44, 133, 348, 189, 38, 19,
                        308, 57, 70, 8, 119, 33, 311, 143, 134, 160, 177, 187, 418, 326, 66, 324,
                        100, 172, 56, 233, 33,
                    ],
                    vec![
                        vec![
                            381, 393, 87, 478, 272, 447, 2, 141, 43, 222, 156, 52, 41, 149, 395,
                            374, 474, 232, 106, 23, 88, 101, 488, 217, 100, 332, 498, 227, 290,
                            243, 291, 192, 247, 37, 93, 463, 216, 320, 187, 376, 35, 31, 490, 167,
                            471, 275, 487, 86, 453, 287, 139, 89, 265, 122, 49, 45, 130, 399, 136,
                            269, 133, 384, 329, 163, 331, 42, 160, 162, 164, 484, 445, 223, 357,
                            34, 188, 154, 142, 65, 24, 236, 230, 315, 255, 18, 126, 279, 115, 61,
                            270, 392, 412, 312, 12, 363, 63, 212, 91, 220, 184, 388, 420, 449, 482,
                            151, 333, 155, 21, 317, 282, 346, 76, 479, 339, 310, 152, 416, 417,
                            289, 240, 499, 391, 262, 206, 57, 322, 29, 176, 274, 201, 172, 77, 477,
                            60, 401, 476, 480, 75, 182, 432, 190, 95, 177, 431, 137, 234, 129, 33,
                            297, 246, 288, 361, 435, 308, 112, 273, 345, 335, 39, 169, 375, 461,
                            283, 92, 469, 47, 411, 13, 121, 438, 179, 496, 303, 99, 330, 210, 380,
                            452, 455, 385, 434, 404, 443, 254, 466, 51, 11, 485, 10, 425, 135, 397,
                            316, 410, 307, 252, 344, 261, 418, 202, 372, 402, 146, 305, 264, 20,
                            319, 186, 351, 276, 204, 242, 168, 153, 200, 341, 454, 311, 198, 324,
                            98, 296, 235, 424, 394, 5, 405, 9, 114, 66, 180, 113, 73, 406, 79, 194,
                            117, 185, 448, 373, 258, 53, 90, 157, 62, 360, 248, 250, 266, 107, 386,
                            191, 119, 105, 125, 196, 80, 14, 30, 225, 294, 278, 78, 85, 285, 249,
                            459, 442, 382, 321, 450, 253, 84, 3, 181, 343, 166, 481, 70, 28, 301,
                            195, 174, 457, 421, 134, 390, 183, 347, 292, 189, 229, 193, 494, 377,
                            419, 170, 171, 138, 298, 214, 144, 38, 81, 218, 429, 354, 423, 175,
                            446, 215, 233, 483, 161, 426, 72, 422, 118, 208, 8, 491, 19, 468, 140,
                            336, 413, 55, 145, 383, 337, 6, 306, 205, 56, 309, 340, 407, 314, 348,
                            108, 159, 462, 352, 433, 497,
                        ],
                        vec![85, 486, 326, 405, 88, 464],
                        vec![
                            496, 272, 340, 244, 414, 315, 343, 382, 310, 415, 77, 320, 299, 302,
                            245, 335, 151, 127, 499, 495, 417, 74, 122, 280, 208, 242, 10, 259,
                            447, 70, 125, 487, 361, 439, 477, 274, 181, 413, 184, 8, 476, 451, 295,
                            84, 484, 424, 119, 207, 58, 86, 345, 75, 405, 366, 466, 371, 386, 406,
                            106, 289, 123, 55, 379, 473, 216, 385, 478, 270, 494, 98, 107, 441,
                            137, 493, 82, 287, 195, 192, 306, 165, 257, 115, 365, 264, 138, 470,
                            59, 368, 230, 491, 189, 62, 396, 102, 265, 53, 463, 285, 99, 434, 356,
                            294, 28, 363, 21, 175, 456, 133, 88,
                        ],
                        vec![80, 95, 144, 318],
                        vec![
                            80, 158, 369, 178, 105, 443, 262, 208, 60, 263, 266, 147, 408, 398,
                            422, 274, 217, 142, 0, 469, 332, 212, 63, 489, 157, 455, 396, 367, 185,
                            153, 444, 261, 2, 121, 129, 415, 470, 10, 288, 298, 381, 287, 277, 309,
                            248, 51, 11, 246, 3, 169, 485, 189,
                        ],
                        vec![],
                        vec![],
                        vec![94],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                        vec![],
                    ],
                ),
                vec![
                    153, 185, 195, 131, 267, 265, 164, 192, 258, 146, 482, 259, 222, 376, 134, 314,
                    119, 226, 13, 127, 219, 276, 362, 411, 451, 478, 59, 460, 58, 75, 138, 412,
                    449, 126, 80, 327, 95, 144, 63, 231, 296, 318, 404, 3, 202, 84, 319, 213, 132,
                    171, 275, 484, 499, 173, 160, 297, 477, 201, 26, 147, 298, 473, 66, 471, 463,
                    356, 428, 176, 263, 374, 420, 360, 426, 189, 316, 497, 112, 480, 69, 158, 238,
                    215, 83, 355, 391, 11, 493, 156, 340, 481, 74, 271, 381, 414, 137, 188, 285,
                    394, 396, 35, 177, 458, 25, 37, 338, 250, 241, 432, 38, 72, 71, 454, 301, 423,
                    370, 281, 495, 455, 9, 329, 10, 181, 21, 43, 233, 85, 208, 54, 92, 306, 102,
                    221, 427, 17, 361, 116, 162, 483, 193, 170, 108, 148, 150, 448, 104, 100, 325,
                    130, 106, 167, 354, 45, 383, 474, 30, 322, 487, 65, 333, 166, 42, 178, 220,
                    286, 424, 369, 486, 422, 434, 50, 235, 91, 277, 96, 99, 133, 161, 165, 437,
                    366, 56, 408, 488, 447, 36, 348, 326, 405, 88, 214, 232, 300, 464, 466, 1, 351,
                    152, 41, 377, 425, 101, 496, 236, 344, 121, 46, 489, 53, 81, 347, 113, 441, 32,
                    248, 28, 444, 62, 78, 29, 443, 490, 179, 476, 172, 438, 229, 234, 70, 76, 270,
                    77, 331, 359, 390, 203, 299, 190, 274, 5, 27, 358, 182, 256, 419, 397, 52, 140,
                    199, 442, 321, 379, 68, 205, 224, 129, 287, 290, 413, 472, 244, 252, 118, 163,
                    191, 254, 392, 461, 402, 155, 334, 196, 230, 387, 272, 373, 175, 375, 346, 24,
                    49, 317, 498, 311, 23, 86, 409, 94, 266, 289, 352, 157, 372, 468, 303, 378,
                    141, 142, 312, 14, 291, 324, 343, 55, 211, 218, 79, 339, 61, 97, 51, 400, 243,
                    304, 342, 345, 416, 240, 368, 380, 435, 371, 384, 168, 283, 194, 433, 436, 257,
                    115, 349, 415, 440, 336, 305, 154, 73, 389, 239, 237, 39, 19, 418, 111, 279,
                    227, 135, 31, 310, 457, 67, 169, 295, 8, 183, 335, 395, 406, 367, 323, 403,
                    294, 90, 105, 479, 225, 149, 485, 82, 210, 469, 293, 207, 328, 470, 292, 302,
                    431, 494, 18, 34, 492, 467, 429, 48, 228, 60, 125, 180, 465, 89, 216, 7, 260,
                    128, 261, 421, 139, 247, 251, 393, 87, 313, 364, 315, 330, 365, 40, 122, 307,
                    382, 456, 273, 280, 320, 337, 245, 264, 151, 15, 288, 417, 145, 242, 278, 388,
                    439, 184, 174, 386, 123, 253, 385, 98, 198, 20, 64, 107, 491, 363, 459, 2, 57,
                    217, 399, 430, 159, 209, 332, 93, 246, 187, 410, 47, 453, 136, 341, 269, 445,
                    223, 475, 357, 255, 12, 197, 206, 282, 401, 33, 103, 350, 120, 308, 446, 452,
                    186, 204, 114, 117, 200, 353, 249, 16, 450, 6, 109, 309, 407, 284, 462, 212,
                    262, 0, 398, 4, 143, 44, 124, 22, 268, 110,
                ],
            ),
        ],
        |a, b| a == b,
    );
}