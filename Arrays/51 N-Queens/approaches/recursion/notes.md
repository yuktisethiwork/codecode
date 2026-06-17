# 51. N-Queens — Recursion

| Field | Value |
|-------|-------|
| **Problem** | [51. N-Queens](https://leetcode.com/problems/n-queens/) |
| **Platform** | LeetCode |
| **Difficulty** | Hard |
| **Language** | python3 |
| **Time Complexity** | O(n!*n) |
| **Space Complexity** | O(n**2) |
| **Runtime** | 0 ms |
| **Memory** | 19.4 MB |
| **Patterns** | Array, Backtracking |
| **Date** | 17/06/2026 |

---

## 💡 Key Idea
Recursion and hashmap to maintain the state of the board in a given recursive call.

## 🧠 How I Solved It
Used recursion and matrix operations.

## ⚠️ Mistakes / Edge Cases
Traversing the upper diagonal and lower diagonal etc required some matrix python knowledge. [('').join(row) for row in board] kinda syntax errors.

**Code:** [`recursion.py`](./recursion.py)
