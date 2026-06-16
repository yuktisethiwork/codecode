# 90. Subsets II — Solution

| Field | Value |
|-------|-------|
| **Problem** | [90. Subsets II](https://leetcode.com/problems/subsets-ii/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Time Complexity** | O(2**n) |
| **Space Complexity** | O(n) |
| **Runtime** | 0 ms |
| **Memory** | 19.3 MB |
| **Patterns** | Array, Backtracking, Bit Manipulation |
| **Date** | 16/06/2026 |

---

## 💡 Key Idea
recursion

## 🧠 How I Solved It
We add the subset to the resukt not only when we reach the last index or the leaves but on every node addition because we are not doing the pick not pick method here, we are just using a for loop.

**Code:** [`solution.py`](./solution.py)
