# 46. Permutations — Solution

| Field | Value |
|-------|-------|
| **Problem** | [46. Permutations](https://leetcode.com/problems/permutations/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Runtime** | 0 ms |
| **Memory** | 19.2 MB |
| **Patterns** | Array, Backtracking |
| **Date** | 16/06/2026 |

---

## 💡 Key Idea
Swap approach to save space. Only add on the leaves not on every node because we have not done all possible swaps on the node. And increment i. call the function by fixing i instead of k. k is just for swapping. 

## 🧠 How I Solved It
Swap approach to save space

**Code:** [`solution.py`](./solution.py)
