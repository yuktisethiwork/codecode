# 102. Binary Tree Level Order Traversal — BFS

| Field | Value |
|-------|-------|
| **Problem** | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | cpp |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(n) |
| **Runtime** | 0 ms |
| **Memory** | 8.4 MB |
| **Patterns** | Tree, Breadth-First Search, Binary Tree |
| **Date** | 25/07/2026 |

---

## 🧠 How I Solved It
the number of elements in the queue are all at one level so store size and then pop all of them in the level array, 2 loops. one for level and then one for the overall traversal.

**Code:** [`bfs.cpp`](./bfs.cpp)
