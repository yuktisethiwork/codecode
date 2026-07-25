# 572. Subtree of Another Tree — Solution

| Field | Value |
|-------|-------|
| **Problem** | [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) |
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | cpp |
| **Time Complexity** | O(n^2) |
| **Space Complexity** | O(h) |
| **Runtime** | 0 ms |
| **Memory** | 8.3 MB |
| **Patterns** | Tree, Depth-First Search, String Matching, Binary Tree, Hash Function |
| **Date** | 25/07/2026 |

---

## 🧠 How I Solved It
make the issubtree also recursively check for different nodes . whether that is same as the subroot or not. if same(base case) then return true.. otherwise the root will reach the nullptr to return false.

**Code:** [`solution.cpp`](./solution.cpp)
