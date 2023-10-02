/*
 * @lc app=leetcode id=2038 lang=rust
 *
 * [2038] Remove Colored Pieces if Both Neighbors are the Same Color
 *
 * https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description/
 *
 * algorithms
 * Medium (57.55%)
 * Likes:    571
 * Dislikes: 52
 * Total Accepted:    36.3K
 * Total Submissions: 61K
 * Testcase Example:  '"AAABABB"'
 *
 * There are n pieces arranged in a line, and each piece is colored either by
 * 'A' or by 'B'. You are given a string colors of length n where colors[i]
 * is the color of the i^th piece.
 *
 * Alice and Bob are playing a game where they take alternating turns
 * removing pieces from the line. In this game, Alice moves first.
 *
 *
 * Alice is only allowed to remove a piece colored 'A' if both its neighbors
 * are also colored 'A'. She is not allowed to remove pieces that are colored
 * 'B'.
 * Bob is only allowed to remove a piece colored 'B' if both its neighbors
 * are also colored 'B'. He is not allowed to remove pieces that are colored
 * 'A'.
 * Alice and Bob cannot remove pieces from the edge of the line.
 * If a player cannot make a move on their turn, that player loses and the
 * other player wins.
 *
 *
 * Assuming Alice and Bob play optimally, return true if Alice wins, or
 * return false if Bob wins.
 *
 *
 * Example 1:
 *
 *
 * Input: colors = "AAABABB"
 * Output: true
 * Explanation:
 * AAABABB -> AABABB
 * Alice moves first.
 * She removes the second 'A' from the left since that is the only 'A' whose
 * neighbors are both 'A'.
 *
 * Now it's Bob's turn.
 * Bob cannot make a move on his turn since there are no 'B's whose neighbors
 * are both 'B'.
 * Thus, Alice wins, so return true.
 *
 *
 * Example 2:
 *
 *
 * Input: colors = "AA"
 * Output: false
 * Explanation:
 * Alice has her turn first.
 * There are only two 'A's and both are on the edge of the line, so she
 * cannot move on her turn.
 * Thus, Bob wins, so return false.
 *
 *
 * Example 3:
 *
 *
 * Input: colors = "ABBBBBBBAAA"
 * Output: false
 * Explanation:
 * ABBBBBBBAAA -> ABBBBBBBAA
 * Alice moves first.
 * Her only option is to remove the second to last 'A' from the right.
 *
 * ABBBBBBBAA -> ABBBBBBAA
 * Next is Bob's turn.
 * He has many options for which 'B' piece to remove. He can pick any.
 *
 * On Alice's second turn, she has no more pieces that she can remove.
 * Thus, Bob wins, so return false.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= colors.length <= 10^5
 * colors consists of only the letters 'A' and 'B'
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn winner_of_game(colors: String) -> bool {
        let mut alice = 0;
        let mut bob = 0;
        let mut length = -2;
        let mut curr_c = 'A';
        for c in colors
            .chars()
            .chain(std::iter::once(if colors.ends_with('A') {
                'B'
            } else {
                'A'
            }))
        {
            if curr_c == c {
                length += 1;
                continue;
            }
            if length > 0 {
                *(if curr_c == 'A' { &mut alice } else { &mut bob }) += length;
            }
            length = -1;
            curr_c = c;
        }
        alice > bob
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        Solution::winner_of_game,
        vec![
            ("AAABABB".to_string(), true),
            ("AA".to_string(), false),
            ("ABBBBBBBAAA".to_string(), false),
            ("A".to_string(), false),
            ("B".to_string(), false),
            ("BBBAAABBBBAABBBABBBAABABBABAABAAABBBBABABAAABBBAAABABAABBABABABABAAABAABAAABBAB".
            to_string(), false), ("ABABBBBBAABBBAABBABAAAABBBBBBBABA".to_string(),
            false), ("ABBABAABBABAAAAABABAABABAAAAAABAA".to_string(), true),
            ("BBBAABABBABAAAAAABABAABBABABABBABAABBAABABBBBAAABAABABBBBBABABABAABBBBAAAAAABAABA"
            .to_string(), true), ("A".to_string(), false),
            ("ABABAABA".to_string(), false),
            ("BBAABBBBAABAABABBBABBABBBBAAAABABABABBAAABBAAABABBBBBABBAAABBABAABBAAAABBAAABAABB"
            .to_string(), false), ("BAA".to_string(), false),
            ("BBBBABBA".to_string(), false),
            ("BABBABAABBBB".to_string(), false),
            ("AAABBBAABABBAAB".to_string(), false),
            ("BBAABBBABA".to_string(), false),
            ("BAAABABA".to_string(), true),
            ("AAABABABAABBAAAAABBABAAABBBABABB".to_string(), true),
            ("BABBABABBBAAAAAAAAABBABBBA".to_string(), true),
            ("BAABABBABBBABABAABAABBBABABBBBABAABBBBABAABBBABAABBBBBBBBABBABBABABBABBAAAABBBAAAABABABBA".to_string(), false),
            ("BBBAABAABABBBBBBBABAAAAAABABABBBABABBAABBBBBAAAABBBAAABB".to_string(), false),
            ("BABABBBBABABAAABBBBBAAAABBABBBAABABBBBABABBAAABBAABBAABBBABBBBBBBB".to_string(),
            false), ("BBBBBB".to_string(), false),
            ("BBBAAAABBAABAAAABAAABBBAABAAABAABABAABBBBBBBABABAABBABABABBABAB".to_string(),
            false),
            ("BBBBAABAAABABBABBAABABABAABBBBBABBBABAAABAAAAABAABBABABABBBBABAABBABABBBBBBBABBBBBAABBBBBAABBB".to_string(), false),
            ("AABABAABBAAAABAAAAABAAAAAAAABAAAAABAABAABBAABBBBABBBBBAABBAABAABABBBBBABABBAABBBAABABBBBAAABAAABAAB".to_string(), true),
            ("BBABABBABAAABAAAAABABABAABAAAAABAAABBABABBAABBBAABAABBABBABBBBBAABBBAABAABAA".
            to_string(), true), ("BBAAAABABBBAABABABABBABAABBAABBAAAABBAAA".
            to_string(), true),
            ("ABAAABABAAAAAABBAABABAABAAABBBAAABBAAAAABAABBAABBBAAAAABBABBBBBBBABABBAABABBA".
            to_string(), true), ("ABAAABBBABAABABAABABBAABBAABAABAAABBBAABABA".
            to_string(), false), ("AAABAAABBBBBBBBABBBBABBAB".to_string(), false),
            ("AABBBABAABABBABAABBAAABABABAABAABBBBBBBAAABBABABAAAABBBABBBABBAAABBBABAABABAABAABAAAABBABBAABBAAAB".to_string(), false),
            ("BAAAABBBBAABBAAABAABBAAAABAAAABBBAABABABABAAABBABBBAABAAAABBBBBBBBB".to_string(),
            false), ("AAAABABAAAAABAAAAABAAAABBBBABBAABBBBAB".to_string(), true),
            ("AABBBABABBAABAABAAAABABABABAABAABBBABBAAABAAAABAAAABAAAAAAAAAABABAAABBABAABABBAABBAABAA".to_string(), true),
            ("AAABBABABAAAABBBBABAAABBBBABBAAABABBBABABBBBABBABAAAA".to_string(), false),
            ("BAAABBBAABBBAAABBABABBBAAABAABBBAAABBBBBABABABBABBBABABABABBBABAAABAA".
            to_string(), false), ("ABABBABAABBBA".to_string(), false),
            ("ABAABAABBBABABBABAAAAABBBBBBABAAAABAABABABABBAAABBBAABAAABBABAAABAABBBABBBBBAABBAAAAABBAAABA".to_string(), true),
            ("BABAAAAAABBAABBABBBABBABBABABBABBBBAABBABAABBBABBAABABAAAAABBAAABABBABBBAABBABA".
            to_string(), true),
            ("BBBBBBBBABABABBABAABAAABBBAABBBBABBAAABBBAABBBBABABBAAAABABAA".to_string(),
            false), ("AAABBBABABAAAAAAABABBBAABBAAABBBAABABBBABBAABABBBBAAB".
            to_string(), true), ("ABBBABABAAAABAAABAAAABBBBABB".to_string(), true),
            ("AB".to_string(), false),
            ("BBBBABBBBABBABBBAABBAABAAABABBBABABAABBBAABABABABBBAAAAABBABAABBBBBAABAABABABAB".
            to_string(), false), ("AAAB".to_string(), true),
            ("BAABABBBBBABBAABBBAABBBABBABBAAAABBBABAAABBAABBABBBBBAABBABBBBABBBABAABABBAABABAABBBBB".to_string(), false),
            ("AAAAABBBAABBBAAAAABBAABBAAABBBABBBBBABABAABBBBAAAAAAB".to_string(), true),
            ("ABAABBBAABBBBBBBABABAABBAAAABAAAABBABAAABAABBBBAAAAABABBABAABBAB".to_string(),
            false), ("BABABBAAABBABAABBBBABBBABAAAABBA".to_string(), false),
            ("ABABBBABBAABBABABABBAABBAABABAAAAAAABAABABAAAABAABBBBABABA".to_string(), true),
            ("BBAABABAAAABBAABBABABABBABBBABAAAAABABAAAAAABABBABAABBBAAAABBBBBAAAABBAAAABABBBBABABBABBBAABAABBAA".to_string(), true),
            ("AAAABAABBBABAABAAABABABBBAABAABAAABABABBBBBABAABBAABABAAAABBBAAAAAAABBBABAAA".
            to_string(), true), ("BBA".to_string(), false),
            ("AAAABBAAAAABBABABBBBA".to_string(), true),
            ("BABABAAAAABBBBAAABABBBBAABABBBBBBABAABBAAABAABABBAB".to_string(), false),
            ("BBBBABBAAAAAAABABABAABABBABABBAAAAAAABBBBBABBBAAAAAAABBABABBABAABABAAABBBABABAA".
            to_string(), true),
            ("AABBABAABBBBBBABABAABBBBABBBAABABAABBBABABABBABABABAABBBBBBAABABBABBAABABBA".
            to_string(), false), ("BBBABAAA".to_string(), false),
            ("ABBBAABBAABABAAAAAABBBBBAABBBABABBBABABBBABBBBAAAAABBABBBAABBAAABABBBBABBBABBAA".
            to_string(), false), ("ABBBBABBBABAAAABAAABAB".to_string(), false),
            ("BABBAABBABAABBABBBABBBBBAAAABAAAAABBBAABABABBBAABBBAABABBAABAABBBAAABABBBBBBBBBABBABBABAABAAABBBA".to_string(), false),
            ("ABABABBBBABBAAABAABABAAABBBBBAAAAABAAABBAAABAAABAABBABAAAAAABBAABAABABBBAAABABBABAABA".to_string(), true),
            ("BAABBABBBBAAABBBBBBABBABBBABBABBBABBAABAAAABBAABAAAABABAAAABABAABAAAAABBBBBBBAABBBAABBAAA".to_string(), false),
            ("AAABBAABBABABABAABAAABBAABABBAABBAAAAABBBBBBBAAAAABB".to_string(), true),
            ("ABBAABBABBAABABAAAAABBBABAABBBBAABBBBAAAABABBABBABAABAABABAABBBBAABBABABABBBABBAABBBABBABBBBBBBBAAB".to_string(), false),
            ("BBABAABBB".to_string(), false),
            ("BBBAAABBBAAAABABABBBBAAAABBBBBAABBBBBBBBABABAAABBBBABBABBBAAAABBABBBBAAA".
            to_string(), false),
            ("AABBBBABBBABBABBABBAAABAAAABBABBABBBABBBBABABBBAABBBBA".to_string(), false),
            ("AAABABBBBABABAABABBAABBAAAAAAABABAABABBABBAAAABBAABABABAAABAAAABBBAAABBABBBBAABABBBAABBBBA".to_string(), true),
            ("BBABABABBBAABBBBBABBBBABAABBBABAABAABBBABBAABBBAAABBBAABBBAAABBBBAAAABAAABAABAAAAAB".to_string(), false),
            ("ABBBAABABBAAABAABABAAABABBABBBAABBABABABBBBBAAAAAAABABAABBABBB".to_string(),
            true),
            ("AAABBBBABBBAABAAABBAABAABABABAAAABBABAAABAABBBBABBAABABBBBAABAAAAAA".to_string(),
            true),
            ("AABAAAAABAAABAAABAABBBBAAAAAAAAABBBBABAABBAAAABBABAABAABAAABAAABBBAAABBABAAABBABBAABBBBBABAAAAAAB".to_string(), true),
            ("BBAABBABAABAABAABBBBABBBBBBABBBABAAABABAAAABBBABBAABBBAAABABBBBBBBBAAB".
            to_string(), false), ("ABBAABAABBBBBB".to_string(), false),
            ("ABAAAAABABBBBAAAABABAABBAAABAABBAA".to_string(), true),
            ("AAABABBABBBBABBBAAABAAAAABABBAABBBAABBABBBABAAAABAAAAABB".to_string(), true),
            ("AAAA".to_string(), true),
            ("ABAABAABBBAABAABBAABAABBA".to_string(), false),
            ("ABBBBBAABABABBBBBBABAAAAABBBBBABAAABBBAAAAABABAABABAABABBAB".to_string(), false),
            ("ABAAABABA".to_string(), true),
            ("BBAABBBBABAABABBABABAAABBABAABBABAAAAABBABABBBBABABBBAABABBABBABABABABBAAABBBBA".
            to_string(), false),
            ("BAABBBBABBBAAABBBAABABBBBBBBBBABAAABABAABABBABBBAAAAABBBBBABBAABAABAABBBBBAAAABAAABBBAA".to_string(), false),
            ("BAAABABAABBAAABBBBABAAABAABBAAABAAAA".to_string(), true),
            ("B".to_string(), false),
            ("BABBAAAABBBABBAAAABBABBAAABBBBBBBBBBABAAABABBBABBABABBBBBAABAAAABABBBBAABBAAABABABBBABBBABBBBBBBA".to_string(), false),
            ("AAABABAAABBABAABBBBAAABABABBAAABAAAAAAAABBAAABAABBABBBABBBBABAB".to_string(),
            true),
            ("BBBAAAAAABAAABBBBAAAABBBABABAABBBBAAAAABBBABAAABAAAABAAABABBAAABABAAAABABABBBBABBAB".to_string(), true),
            ("BAAAAABBABABAABBBABBBBABABAAABABAAAAA".to_string(), true),
            ("BABBABBBAABAABAB".to_string(), false),
            ("AAABBABBBAABABABBBBBAAAAABABAAABBBBABABBBBABBBAABBBBBABAAAAAAABBBBAAB".
            to_string(), false), ("AAABBBBBABBABAABAABABAAAABABAABBAAABAABBBBB".
            to_string(), false),
            ("AAAABBBBABBABBBBBABABBAABBABABBBBABBBBAAAAAAAAAAABAABBBBAABA".to_string(), false),
            ("ABBABAABBAAAABBBBAAAAAAABBAAAABABAAAAABBB".to_string(), true),
            ("BBAABBAAABBABBABAABBAABABBBAABBABBABBBBAABAAAABAABABBBABAABAABABBBABBBABBAAABBABAAAABABABBABAABABA".to_string(), false),
            ("AAABABBABAAAABBABABABABAAAAAABAABABBBAAAABBBABABAABAA".to_string(), true),
            ("AABBBAAABABBABBBBBAAA".to_string(), false),
            ("AABABABABAAAAAAABBAAAABAAAABBBBABAAAABABBBABAABABAABBBAAABAAAABAAAAAAAAAABBBAABBBAABBB".to_string(), true),
            ("ABAAABBABABBAAABAABAAABB".to_string(), true),
            ("ABABBAAAAA".to_string(), true),
            ("AAABBABAABAAABBBABBBABABAAABABBABBBAAAABABAAABAAABABABAABABABAABABABABBBABAABABBAABBABBABABAAABAB".to_string(), true),
            ("AABABBABAABBAAABAABBAAABABAABAABAAA".to_string(), true),
            ("BABBB".to_string(), false),
        ],
        |a, b| a == b,
    );
}
