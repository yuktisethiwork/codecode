# 128. Longest Consecutive Sequence — Solution

| Field | Value |
|-------|-------|
| **Problem** | [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(1) |
| **Runtime** | 0 ms |
| **Memory** | 19.3 MB |
| **Patterns** | Array, Hash Table, Union-Find |
| **Date** | 23/06/2026 |

---

## 🧠 How I Solved It
Check if the earlier element is present in the set or not. if not present, then start the sequence from there and check if the next element from there is present or not. if present then do nothing.

**Code:** [`solution.py`](./solution.py)
