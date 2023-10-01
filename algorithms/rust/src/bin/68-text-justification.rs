/*
 * @lc app=leetcode id=68 lang=rust
 *
 * [68] Text Justification
 *
 * https://leetcode.com/problems/text-justification/description/
 *
 * algorithms
 * Hard (36.97%)
 * Likes:    3143
 * Dislikes: 4142
 * Total Accepted:    347.1K
 * Total Submissions: 850.2K
 * Testcase Example:  '["This", "is", "an", "example", "of", "text",
 * "justification."]\n16'
 *
 * Given an array of strings words and a width maxWidth, format the text such
 * that each line has exactly maxWidth characters and is fully (left and
 * right) justified.
 *
 * You should pack your words in a greedy approach; that is, pack as many
 * words as you can in each line. Pad extra spaces ' ' when necessary so that
 * each line has exactly maxWidth characters.
 *
 * Extra spaces between words should be distributed as evenly as possible. If
 * the number of spaces on a line does not divide evenly between words, the
 * empty slots on the left will be assigned more spaces than the slots on the
 * right.
 *
 * For the last line of text, it should be left-justified, and no extra space
 * is inserted between words.
 *
 * Note:
 *
 *
 * A word is defined as a character sequence consisting of non-space
 * characters only.
 * Each word's length is guaranteed to be greater than 0 and not exceed
 * maxWidth.
 * The input array words contains at least one word.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: words = ["This", "is", "an", "example", "of", "text",
 * "justification."], maxWidth = 16
 * Output:
 * [
 * "This    is    an",
 * "example  of text",
 * "justification.  "
 * ]
 *
 * Example 2:
 *
 *
 * Input: words = ["What","must","be","acknowledgment","shall","be"],
 * maxWidth = 16
 * Output:
 * [
 * "What   must   be",
 * "acknowledgment  ",
 * "shall be        "
 * ]
 * Explanation: Note that the last line is "shall be    " instead of "shall
 * be", because the last line must be left-justified instead of
 * fully-justified.
 * Note that the second line is also left-justified because it contains only
 * one word.
 *
 * Example 3:
 *
 *
 * Input: words =
 * ["Science","is","what","we","understand","well","enough","to","explain","
 * to","a","computer.","Art","is","everything","else","we","do"], maxWidth =
 * 20 Output:
 * [
 * "Science  is  what we",
 * ⁠ "understand      well",
 * "enough to explain to",
 * "a  computer.  Art is",
 * "everything  else  we",
 * "do                  "
 * ]
 *
 *
 * Constraints:
 *
 *
 * 1 <= words.length <= 300
 * 1 <= words[i].length <= 20
 * words[i] consists of only English letters and symbols.
 * 1 <= maxWidth <= 100
 * words[i].length <= maxWidth
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn full_justify(words: Vec<String>, max_width: i32) -> Vec<String> {
        fn add_white_space(len: usize, s: &mut String) {
            s.extend(std::iter::repeat(' ').take(len))
        }
        let mut res = vec![];
        let mut curr_length = 0;
        let mut current_line_words = Vec::with_capacity(1 + (max_width as usize / 2));
        let mut i = 0;
        loop {
            if i < words.len()
                && curr_length + words[i].len() + current_line_words.len() <= max_width as usize
            {
                curr_length += words[i].len();
                current_line_words.push(words[i].as_str());
                i += 1;
            } else {
                if current_line_words.len() == 1 || i == words.len() {
                    let mut line: String = current_line_words.join(" ");
                    add_white_space(max_width as usize - line.len(), &mut line);
                    res.push(line);
                } else {
                    let diff = max_width as usize - curr_length;
                    let white_space_spots = current_line_words.len() - 1;
                    let full = diff / white_space_spots;
                    let left_over = diff % white_space_spots;
                    let mut line: String = String::from(current_line_words[0]);
                    for (u, &w) in current_line_words.iter().skip(1).enumerate() {
                        add_white_space(full + (u < left_over) as usize, &mut line);
                        line.push_str(w);
                    }
                    res.push(line);
                }

                if i == words.len() {
                    break;
                };

                current_line_words.clear();
                curr_length = 0;
            }
        }
        res
    }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::full_justify(e.0, e.1),
        vec![
            (
                (
                    vec![
                        "This",
                        "is",
                        "an",
                        "example",
                        "of",
                        "text",
                        "justification.",
                    ]
                    .into_iter()
                    .map(String::from)
                    .collect(),
                    16,
                ),
                ["This    is    an", "example  of text", "justification.  "]
                    .into_iter()
                    .map(String::from)
                    .collect(),
            ),
            (
                (
                    vec!["What", "must", "be", "acknowledgment", "shall", "be"]
                        .into_iter()
                        .map(String::from)
                        .collect(),
                    16,
                ),
                ["What   must   be", "acknowledgment  ", "shall be        "]
                    .into_iter()
                    .map(String::from)
                    .collect(),
            ),
            (
                (
                    vec![
                        "Science",
                        "is",
                        "what",
                        "we",
                        "understand",
                        "well",
                        "enough",
                        "to",
                        "explain",
                        "to",
                        "a",
                        "computer.",
                        "Art",
                        "is",
                        "everything",
                        "else",
                        "we",
                        "do",
                    ]
                    .into_iter()
                    .map(String::from)
                    .collect(),
                    20,
                ),
                [
                    "Science  is  what we",
                    "understand      well",
                    "enough to explain to",
                    "a  computer.  Art is",
                    "everything  else  we",
                    "do                  ",
                ]
                .into_iter()
                .map(String::from)
                .collect(),
            ),
        ],
        |a, b| a == b,
    );
}
