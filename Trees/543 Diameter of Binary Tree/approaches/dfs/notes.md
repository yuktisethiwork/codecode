# 543. Diameter of Binary Tree — DFS

| Field | Value |
|-------|-------|
| **Problem** | [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) |
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | python3 |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(n) |
| **Runtime** | 0 ms |
| **Memory** | 19.2 MB |
| **Patterns** | Tree, Depth-First Search, Binary Tree |
| **Date** | 02/07/2026 |

---

## 🧠 How I Solved It
Traversed through the height of the binary tree and then diameter is max sum of left and right height. so kept it as a global variable an dupdated it in the height function

**Code:** [`dfs.py`](./dfs.py)
