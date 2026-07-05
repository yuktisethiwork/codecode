# 153. Find Minimum in Rotated Sorted Array — Approach 1

| Field | Value |
|-------|-------|
| **Problem** | [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Runtime** | 0 ms |
| **Memory** | 19.1 MB |
| **Patterns** | Array, Binary Search |
| **Date** | 05/07/2026 |

---

## 🧠 How I Solved It
If we are in the left sorted portion, search the right for smaller elements. If right sorted, search left. keep updating mini and also break out if overall sorted.

**Code:** [`approach_1.py`](./approach_1.py)
