# 76. Minimum Window Substring — Optimised have and need approach

| Field | Value |
|-------|-------|
| **Problem** | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| **Platform** | LeetCode |
| **Difficulty** | Hard |
| **Language** | python3 |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(n) |
| **Runtime** | 0 ms |
| **Memory** | 19.4 MB |
| **Patterns** | Hash Table, String, Sliding Window |
| **Date** | 01/07/2026 |

---

## 🧠 How I Solved It
I used 2 hashmaps to store the count of characters i have in t and those needed in s for a given window. I kept on adding elements to the window until I reach havecount == needcount. By only incrementing and checking the count of the added element and seeing if it is exactly same as the one needed, only then i increment the havecount global variable. Then I keep removing the elements from the left and decrementing their count and i decrement their havecount globally only when they are less than the need[s[l]] of that character. while decrementing, i keep updating the minimum window and the reslength. 

**Code:** [`optimised_have_and_need_approach.py`](./optimised_have_and_need_approach.py)
