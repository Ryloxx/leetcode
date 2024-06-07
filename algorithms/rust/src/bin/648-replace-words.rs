/*
 * @lc app=leetcode id=648 lang=rust
 *
 * [648] Replace Words
 *
 * https://leetcode.com/problems/replace-words/description/
 *
 * algorithms
 * Medium (62.86%)
 * Likes:    2663
 * Dislikes: 197
 * Total Accepted:    205.9K
 * Total Submissions: 311.7K
 * Testcase Example:  '["cat","bat","rat"]\n"the cattle was rattled by the
 * battery"'
 *
 * In English, we have a concept called root, which can be followed by some
 * other word to form another longer word - let's call this word derivative.
 * For example, when the root "help" is followed by the word "ful", we can
 * form a derivative "helpful".
 *
 * Given a dictionary consisting of many roots and a sentence consisting of
 * words separated by spaces, replace all the derivatives in the sentence
 * with the root forming it. If a derivative can be replaced by more than one
 * root, replace it with the root that has the shortest length.
 *
 * Return the sentence after the replacement.
 *
 *
 * Example 1:
 *
 *
 * Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was
 * rattled by the battery"
 * Output: "the cat was rat by the bat"
 *
 *
 * Example 2:
 *
 *
 * Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab
 * cadsfafs" Output: "a a b c"
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= dictionary.length <= 1000
 * 1 <= dictionary[i].length <= 100
 * dictionary[i] consists of only lower-case letters.
 * 1 <= sentence.length <= 10^6
 * sentence consists of only lower-case letters and spaces.
 * The number of words in sentence is in the range [1, 1000]
 * The length of each word in sentence is in the range [1, 1000]
 * Every two consecutive words in sentence will be separated by exactly one
 * space.
 * sentence does not have leading or trailing spaces.
 *
 *
 */
struct Solution;
// @lc code=start
impl Solution {
    pub fn replace_words(dictionary: Vec<String>, sentence: String) -> String {
        use std::{
            collections::{hash_map::DefaultHasher, HashSet},
            hash::Hasher,
        };
        let dictionary: HashSet<u64> = dictionary
            .into_iter()
            .map(|word| {
                word.as_bytes()
                    .iter()
                    .fold(DefaultHasher::new(), |mut acc, curr| {
                        acc.write_u8(*curr);
                        acc
                    })
                    .finish()
            })
            .collect();
        let mut ret = vec![];
        for word in sentence.split(" ") {
            if !ret.is_empty() {
                ret.push(b' ');
            }
            let mut hasher = DefaultHasher::new();
            for c in word.as_bytes() {
                ret.push(*c);
                hasher.write_u8(*c);
                if dictionary.contains(&hasher.finish()) {
                    break;
                }
            }
        }
        unsafe { String::from_utf8_unchecked(ret) }
    }

    // pub fn replace_words(words: Vec<String>, sentence: String) -> String {
    //     #[derive(Default)]
    //     struct Trie {
    //         word: Option<String>,
    //         children: [Option<Box<Trie>>; 26],
    //     }
    //     let mut root = Trie::default();
    //     for word in words.into_iter() {
    //         let mut curr = &mut root;
    //         for c in word.chars() {
    //             curr =
    //                 curr.children[c as usize - 'a' as
    // usize].get_or_insert_with(Default::default);         }
    //         curr.word = Some(word);
    //     }
    //     sentence
    //         .split_ascii_whitespace()
    //         .map(|word| {
    //             let mut curr = &root;
    //             for c in word.chars() {
    //                 if let Some(next) = curr.children[c as usize - 'a' as
    // usize].as_ref() {                     curr = next;
    //                     if let Some(word) = next.word.as_ref() {
    //                         return word.as_ref();
    //                     }
    //                 } else {
    //                     break;
    //                 }
    //             }
    //             word
    //         })
    //         .collect::<Vec<&str>>()
    //         .join(" ")
    // }
}
// @lc code=end

fn main() {
    rust::test_algo(
        |e| Solution::replace_words(e.0, e.1),
        vec![
            (
                (
                    ["cat", "bat", "rat"]
                        .into_iter()
                        .map(String::from)
                        .collect(),
                    "the cattle was rattled by the battery".to_string(),
                ),
                "the cat was rat by the bat".to_string(),
            ),
            (
                (
                    ["a", "b", "c"].into_iter().map(String::from).collect(),
                    "aadsfasf absbs bbab cadsfafs".to_string(),
                ),
                "a a b c".to_string(),
            ),
        ],
        |a, b| a == b,
    )
}
