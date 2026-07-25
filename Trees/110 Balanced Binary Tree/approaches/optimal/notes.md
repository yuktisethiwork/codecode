# 110. Balanced Binary Tree — Optimal

| Field | Value |
|-------|-------|
| **Problem** | [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) |
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | cpp |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(h) |
| **Runtime** | 0 ms |
| **Memory** | 8.2 MB |
| **Patterns** | Tree, Depth-First Search, Binary Tree |
| **Date** | 25/07/2026 |

---

## 🧠 How I Solved It
Checking balance along with height calculation. We return early if left or right subtree returned -1 in case of absolute height being greater than -1.

**Code:** [`optimal.cpp`](./optimal.cpp)
