# 3. Longest Substring Without Repeating Characters — Approach 1

| Field | Value |
|-------|-------|
| **Problem** | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Runtime** | 0 ms |
| **Memory** | 19.3 MB |
| **Patterns** | Hash Table, String, Sliding Window |
| **Date** | 26/06/2026 |

---

## 💡 Key Idea
use set

## 🧠 How I Solved It
use a set to keep track of what characters have appears in the current and if there is a duplicate character, then keep removing the elements from the set form the left position fo the window until we remove that duplicate and restart the window's left pointer from there keeping the right pointer at the next position.

**Code:** [`approach_1.py`](./approach_1.py)
