# 15. 3Sum — Approach 1

| Field | Value |
|-------|-------|
| **Problem** | [15. 3Sum](https://leetcode.com/problems/3sum/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Runtime** | 0 ms |
| **Memory** | 19.2 MB |
| **Patterns** | Array, Two Pointers, Sorting |
| **Date** | 25/06/2026 |

---

## 🧠 How I Solved It
Skip duplicates in both the inner and outer loops. fix ne number and then solve it like two sum sorted -> the only difference being after appending triplet, always do a while loop to skip all possible duplicates with respect to left and right pointer.

## ⚠️ Mistakes / Edge Cases
skip dups

**Code:** [`approach_1.py`](./approach_1.py)
