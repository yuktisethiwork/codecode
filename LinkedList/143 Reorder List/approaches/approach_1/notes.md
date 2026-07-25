# 143. Reorder List — Approach 1

| Field | Value |
|-------|-------|
| **Problem** | [143. Reorder List](https://leetcode.com/problems/reorder-list/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | cpp |
| **Runtime** | 0 ms |
| **Memory** | 8 MB |
| **Patterns** | Linked List, Two Pointers, Stack, Recursion |
| **Date** | 25/07/2026 |

---

## 🧠 How I Solved It
slow and fast pointer will lead to the mid position and then we split the lists and reverse the second half and then merge both of them. the while condition in merge should be on the temp that exhausts early which will always be one of them depedning on where we stop the mid-point calculation.

**Code:** [`approach_1.cpp`](./approach_1.cpp)
