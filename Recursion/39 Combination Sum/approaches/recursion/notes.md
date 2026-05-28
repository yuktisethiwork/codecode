# 39. Combination Sum — Recursion

| Field | Value |
|-------|-------|
| **Problem** | [39. Combination Sum](https://leetcode.com/problems/combination-sum/submissions/2015366589/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Time Complexity** | O(2**n) |
| **Space Complexity** | O(n) |
| **Runtime** | 21 ms |
| **Memory** | 19.7 MB |
| **Patterns** | Array, Backtracking |
| **Date** | 28/05/2026 |

---

## 💡 Key Idea
recursion

## 🧠 How I Solved It
Used general recursion, carries an array and a sum variable. Base case is when we hit the target we need to add the array to the global list and we need to mandatorily return from there to avoid adding the same array to the global list when we decide not to pick any element down the recursion tree. The other case is to continue the index+1 recursive call only when i is in the bounds of the array index. stop recursion when sum greater than target.

**Code:** [`recursion.py`](./recursion.py)
