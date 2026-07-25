# 235. Lowest Common Ancestor of a Binary Search Tree — Approach 1

| Field | Value |
|-------|-------|
| **Problem** | [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | cpp |
| **Runtime** | 0 ms |
| **Memory** | 8.3 MB |
| **Patterns** | Tree, Depth-First Search, Binary Search Tree, Binary Tree |
| **Date** | 25/07/2026 |

---

## 🧠 How I Solved It
Need to use && for the range comparison in c++ unlike python. wherever there is a split, that root node is the lca, otherwise if both are less than root, we check the left part and if both are more we check the right path. 

**Code:** [`approach_1.cpp`](./approach_1.cpp)
