/*
 * @lc app=leetcode id=2402 lang=rust
 *
 * [2402] Meeting Rooms III
 *
 * https://leetcode.com/problems/meeting-rooms-iii/description/
 *
 * algorithms
 * Hard (33.53%)
 * Likes:    1312
 * Dislikes: 81
 * Total Accepted:    68.7K
 * Total Submissions: 165.3K
 * Testcase Example:  '2\n[[0,10],[1,5],[2,7],[3,4]]'
 *
 * You are given an integer n. There are n rooms numbered from 0 to n - 1.
 *
 * You are given a 2D integer array meetings where meetings[i] = [starti,
 * endi] means that a meeting will be held during the half-closed time
 * interval [starti, endi). All the values of starti are unique.
 *
 * Meetings are allocated to rooms in the following manner:
 *
 *
 * Each meeting will take place in the unused room with the lowest number.
 * If there are no available rooms, the meeting will be delayed until a room
 * becomes free. The delayed meeting should have the same duration as the
 * original meeting.
 * When a room becomes unused, meetings that have an earlier original start
 * time should be given the room.
 *
 *
 * Return the number of the room that held the most meetings. If there are
 * multiple rooms, return the room with the lowest number.
 *
 * A half-closed interval [a, b) is the interval between a and b including a
 * and not including b.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
 * Output: 0
 * Explanation:
 * - At time 0, both rooms are not being used. The first meeting starts in
 *   room
 * 0.
 * - At time 1, only room 1 is not being used. The second meeting starts in
 * room 1.
 * - At time 2, both rooms are being used. The third meeting is delayed.
 * - At time 3, both rooms are being used. The fourth meeting is delayed.
 * - At time 5, the meeting in room 1 finishes. The third meeting starts in
 * room 1 for the time period [5,10).
 * - At time 10, the meetings in both rooms finish. The fourth meeting starts
 * in room 0 for the time period [10,11).
 * Both rooms 0 and 1 held 2 meetings, so we return 0.
 *
 *
 * Example 2:
 *
 *
 * Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
 * Output: 1
 * Explanation:
 * - At time 1, all three rooms are not being used. The first meeting starts
 *   in
 * room 0.
 * - At time 2, rooms 1 and 2 are not being used. The second meeting starts
 *   in
 * room 1.
 * - At time 3, only room 2 is not being used. The third meeting starts in
 *   room
 * 2.
 * - At time 4, all three rooms are being used. The fourth meeting is
 *   delayed.
 * - At time 5, the meeting in room 2 finishes. The fourth meeting starts in
 * room 2 for the time period [5,10).
 * - At time 6, all three rooms are being used. The fifth meeting is delayed.
 * - At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting
 *   starts
 * in room 1 for the time period [10,12).
 * Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we
 * return 1.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 100
 * 1 <= meetings.length <= 10^5
 * meetings[i].length == 2
 * 0 <= starti < endi <= 5 * 10^5
 * All the values of starti are unique.
 *
 *
 */
struct Solution;
// @lc code=start
use std::collections::BinaryHeap;
impl Solution {
    pub fn most_booked(n: i32, mut meetings: Vec<Vec<i32>>) -> i32 {
        let mut h: BinaryHeap<(i64, i32)> = BinaryHeap::new();
        let mut free_rooms = (0..n).map(|x| -x).collect::<BinaryHeap<i32>>();
        let mut room_usage = [0; 101];
        meetings.sort_unstable();
        let n = n as usize;
        for (meeting_start, meeting_end) in meetings
            .into_iter()
            .map(|meeting| (meeting[0] as i64, meeting[1] as i64))
        {
            while !h.is_empty() && (-h.peek().unwrap().0 <= meeting_start) {
                free_rooms.push(h.pop().unwrap().1);
            }
            let (end, room) = if let Some(room) = free_rooms.pop() {
                (0, room)
            } else {
                h.pop().unwrap()
            };
            h.push((
                (meeting_start - (-end).max(meeting_start) - meeting_end),
                room,
            ));
            room_usage[(-room) as usize] += 1;
        }
        (0..n)
            .rev()
            .max_by_key(|idx| room_usage[*idx])
            .unwrap_or_default() as i32
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::most_booked(e.0, e.1),
        vec![
            (
                (2, vec![vec![0, 10], vec![1, 5], vec![2, 7], vec![3, 4]]),
                0,
            ),
            (
                (
                    3,
                    vec![vec![1, 20], vec![2, 10], vec![3, 5], vec![4, 9], vec![6, 8]],
                ),
                1,
            ),
            (
                (
                    4,
                    vec![
                        vec![18, 19],
                        vec![3, 12],
                        vec![17, 19],
                        vec![2, 13],
                        vec![7, 10],
                    ],
                ),
                0,
            ),
            (
                (
                    5,
                    vec![vec![12, 18], vec![8, 11], vec![19, 20], vec![5, 11]],
                ),
                0,
            ),
        ],
        |a, b| a == b,
    )
}
