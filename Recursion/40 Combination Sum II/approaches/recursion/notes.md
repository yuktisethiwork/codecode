# 40. Combination Sum II — Recursion

| Field | Value |
|-------|-------|
| **Problem** | [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Time Complexity** | O(2^n) |
| **Space Complexity** | O(n) |
| **Runtime** | 0 ms |
| **Memory** | 19.5 MB |
| **Patterns** | Array, Backtracking |
| **Date** | 28/05/2026 |

---

## 🧠 How I Solved It
Tricky part is to skip duplicates in an intelligent way. We use a for loop to skip duplicate recursion calls only in the not take case. Because if we are not taking one element then we have to skip all the occurrences of that element. But if we are taking it, we can take all of them and that would still make a unique combination. 
(dry run using 1,1,1,2 as an example with target as 3)


**Code:** [`recursion.py`](./recursion.py)
