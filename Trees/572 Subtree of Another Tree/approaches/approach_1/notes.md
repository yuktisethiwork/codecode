# 572. Subtree of Another Tree — Approach 1

| Field | Value |
|-------|-------|
| **Problem** | [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) |
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | cpp |
| **Runtime** | 0 ms |
| **Memory** | 8.3 MB |
| **Patterns** | Tree, Depth-First Search, String Matching, Binary Tree, Hash Function |
| **Date** | 25/07/2026 |

---

## 🧠 How I Solved It
make the issubtree also recursively check for different nodes . whether that is same as the subroot or not. if same(base case) then return true.. otherwise the root will reach the nullptr to return false.

**Code:** [`approach_1.cpp`](./approach_1.cpp)
