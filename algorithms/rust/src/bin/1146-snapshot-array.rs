/*
 * @lc app=leetcode id=1146 lang=rust
 *
 * [1146] Snapshot Array
 *
 * https://leetcode.com/problems/snapshot-array/description/
 *
 * algorithms
 * Medium (37.31%)
 * Likes:    2641
 * Dislikes: 355
 * Total Accepted:    158.9K
 * Total Submissions: 427.1K
 * Testcase Example:  '["SnapshotArray","set","snap","set","get"]\n[[3],[0,5],[],[0,6],[0,0]]'
 *
 * Implement a SnapshotArray that supports the following interface:
 *
 *
 * SnapshotArray(int length) initializes an array-like data structure with
 * the given length. Initially, each element equals 0.
 * void set(index, val) sets the element at the given index to be equal to
 * val.
 * int snap() takes a snapshot of the array and returns the snap_id: the
 * total number of times we called snap() minus 1.
 * int get(index, snap_id) returns the value at the given index, at the time
 * we took the snapshot with the given snap_id
 *
 *
 *
 * Example 1:
 *
 *
 * Input: ["SnapshotArray","set","snap","set","get"]
 * [[3],[0,5],[],[0,6],[0,0]]
 * Output: [null,null,0,null,5]
 * Explanation:
 * SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be
 * 3 snapshotArr.set(0,5);  // Set array[0] = 5
 * snapshotArr.snap();  // Take a snapshot, return snap_id = 0
 * snapshotArr.set(0,6);
 * snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0,
 * return 5
 *
 *
 * Constraints:
 *
 *
 * 1 <= length <= 5 * 10^4
 * 0 <= index < length
 * 0 <= val <= 10^9
 * 0 <= snap_id < (the total number of times we call snap())
 * At most 5 * 10^4 calls will be made to set, snap, and get.
 *
 *
 */

// @lc code=start
struct SnapshotArray {
    arr: Vec<Vec<[i32; 2]>>,
    curr_snap_id: i32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SnapshotArray {
    fn new(length: i32) -> Self {
        Self {
            arr: vec![vec![]; length as usize],
            curr_snap_id: 0,
        }
    }

    fn set(&mut self, index: i32, val: i32) {
        let snapshots = &mut self.arr[index as usize];
        if let Some(b) = snapshots.last() {
            if b[0] < self.curr_snap_id {
                snapshots.push([self.curr_snap_id, 0]);
            }
        } else {
            snapshots.push([self.curr_snap_id, 0]);
        }
        snapshots.last_mut().unwrap()[1] = val;
    }

    fn snap(&mut self) -> i32 {
        let res = self.curr_snap_id;
        self.curr_snap_id += 1;
        res
    }

    fn get(&self, index: i32, snap_id: i32) -> i32 {
        let snapshots = &self.arr[index as usize];
        let snapshot_idx = snapshots.partition_point(|a| a[0].le(&(snap_id)));
        if snapshot_idx >= snapshots.len() {
            if let Some(x) = snapshots.last() {
                return x[1];
            }
            return 0;
        }
        if snapshot_idx == 0 {
            if snapshots[snapshot_idx][0] > snap_id {
                return 0;
            } else {
                return snapshots[snapshot_idx][1];
            }
        }

        snapshots[snapshot_idx - 1][1]
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray::new(length);
 * obj.set(index, val);
 * let ret_2: i32 = obj.snap();
 * let ret_3: i32 = obj.get(index, snap_id);
 */
// @lc code=end
enum Input {
    New(i32),
    Set(i32, i32),
    Snap,
    Get(i32, i32),
}
fn main() {
    rust::test_algo(
        |e: Vec<Input>| {
            let mut obj = None;
            e.into_iter()
                .map(|input| match input {
                    Input::New(a) => {
                        obj = Some(SnapshotArray::new(a));
                        None
                    }
                    Input::Set(a, b) => {
                        obj.as_mut().unwrap().set(a, b);
                        None
                    }
                    Input::Snap => Some(obj.as_mut().unwrap().snap()),
                    Input::Get(a, b) => Some(obj.as_ref().unwrap().get(a, b)),
                })
                .collect()
        },
        vec![
            (
                vec![
                    Input::New(3),
                    Input::Set(0, 5),
                    Input::Snap,
                    Input::Set(0, 6),
                    Input::Get(0, 0),
                ],
                vec![None, None, Some(0), None, Some(5)],
            ),
            (
                vec![
                    Input::New(4),
                    Input::Snap,
                    Input::Snap,
                    Input::Get(3, 1),
                    Input::Set(2, 4),
                    Input::Snap,
                    Input::Set(1, 4),
                ],
                vec![
                    None,
                    //
                    Some(0),
                    Some(1),
                    Some(0),
                    None,
                    Some(2),
                    None,
                ],
            ),
            (
                vec![
                    Input::New(1),
                    Input::Set(0, 15),
                    Input::Snap,
                    Input::Snap,
                    Input::Snap,
                    Input::Get(0, 2),
                    Input::Snap,
                    Input::Snap,
                    Input::Get(0, 0),
                ],
                vec![
                    None,
                    //
                    None,
                    Some(0),
                    Some(1),
                    Some(2),
                    Some(15),
                    Some(3),
                    Some(4),
                    Some(15),
                ],
            ),
            (
                vec![
                    Input::New(2),
                    Input::Snap,
                    Input::Get(1, 0),
                    Input::Get(0, 0),
                    Input::Set(1, 8),
                    Input::Get(1, 0),
                    Input::Set(0, 20),
                    Input::Get(0, 0),
                    Input::Set(0, 7),
                ],
                vec![
                    None,
                    Some(0),
                    Some(0),
                    Some(0),
                    None,
                    Some(0),
                    None,
                    Some(0),
                    None,
                ],
            ),
            (
                vec![
                    Input::New(3),
                    Input::Set(1, 18),
                    Input::Set(1, 4),
                    Input::Snap,
                    Input::Get(0, 0),
                    Input::Set(0, 20),
                    Input::Snap,
                    Input::Set(0, 2),
                    Input::Set(1, 1),
                    Input::Get(1, 1),
                    Input::Get(1, 0),
                ],
                vec![
                    None,
                    None,
                    None,
                    Some(0),
                    Some(0),
                    None,
                    Some(1),
                    None,
                    None,
                    Some(4),
                    Some(4),
                ],
            ),
            (
                vec![
                    Input::New(1),
                    Input::Snap,
                    Input::Snap,
                    Input::Set(0, 4),
                    Input::Snap,
                    Input::Get(0, 1),
                    Input::Set(0, 12),
                    Input::Get(0, 1),
                    Input::Snap,
                    Input::Get(0, 3),
                ],
                vec![
                    None,
                    Some(0),
                    Some(1),
                    None,
                    Some(2),
                    Some(0),
                    None,
                    Some(0),
                    Some(3),
                    Some(12),
                ],
            ), //
        ],
        |a, b| a == b,
    );
}
