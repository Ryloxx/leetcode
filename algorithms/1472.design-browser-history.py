#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#
# https://leetcode.com/problems/design-browser-history/description/
#
# algorithms
# Medium (76.19%)
# Likes:    2527
# Dislikes: 155
# Total Accepted:    138.8K
# Total Submissions: 179.7K
# Testcase Example:  '["BrowserHistory","visit","visit","visit","back","back"
# ,"forward","visit","forward","back","back"]\n' +
# '[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],
# [1],["linkedin.com"],[2],[2],[7]]'
#
# You have a browser of one tab where you start on the homepage and you can
# visit another url, get back in the history number of steps or move forward in
# the history number of steps.
#
# Implement the BrowserHistory class:
#
#
# BrowserHistory(string homepage) Initializes the object with the homepage of
# the browser.
# void visit(string url) Visits url from the current page. It clears up all the
# forward history.
# string back(int steps) Move steps back in history. If you can only return x
# steps in the history and steps > x, you will return only x steps. Return the
# current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only
# forward x steps in the history and steps > x, you will forward only x steps.
# Return the current url after forwarding in history at most steps.
#
#
#
# Example:
#
#
# Input:
#
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit",
# "forward","back","back"]
#
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1]
# ,[1],["linkedin.com"],[2],[2],[7]]
# Output:
#
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,
# "linkedin.com","google.com","leetcode.com"]
#
# Explanation:
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit
# "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit
# "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit
# "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move
# back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move
# back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move
# forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit
# "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you
# cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move
# back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can
# move back only one step to "leetcode.com". return "leetcode.com"
#
#
#
# Constraints:
#
#
# 1 <= homepage.length <= 20
# 1 <= url.length <= 20
# 1 <= steps <= 100
# homepage and url consist of  '.' or lower case English letters.
# At most 5000 calls will be made to visit, back, and forward.
#
#
#
from algo_input import run, wrapp_class


# @lc code=start
class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.len = self.index = 0

    def visit(self, url: str) -> None:
        self.len = self.index = self.index + 1
        if self.index >= len(self.stack):
            self.stack.append(url)
        else:
            self.stack[self.index] = url

    def back(self, steps: int) -> str:
        self.index = max(0, self.index - steps)
        return self.stack[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(self.len, self.index + steps)
        return self.stack[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end
if __name__ == "__main__":
    run(
        wrapp_class(BrowserHistory),
        [
            ([["leetcode.com"],
              [
                  ["visit", ["google.com"]],
                  ["visit", ["facebook.com"]],
                  ["visit", ["youtube.com"]],
                  ["back", [1]],
                  ["back", [1]],
                  ["forward", [1]],
                  ["visit", ["linkedin.com"]],
                  ["forward", [2]],
                  ["back", [2]],
                  ["back", [7]],
              ]], [
                  None, None, None, "facebook.com", "google.com",
                  "facebook.com", None, "linkedin.com", "google.com",
                  "leetcode.com"
              ]),
            ([["esgriv.com"],
              [
                  ["visit", ["cgrt.com"]],
                  ["visit", ["tip.com"]],
                  ["back", [9]],
                  ["visit", ["kttzxgh.com"]],
                  ["forward", [7]],
                  ["visit", ["crqje.com"]],
                  ["visit", ["iybch.com"]],
                  ["forward", [5]],
                  ["visit", ["uun.com"]],
                  ["back", [10]],
                  ["visit", ["hci.com"]],
                  ["visit", ["whula.com"]],
                  ["forward", [10]],
              ]], [
                  None, None, "esgriv.com", None, "kttzxgh.com", None, None,
                  "iybch.com", None, "esgriv.com", None, None, "whula.com"
              ]),
        ],
    )
