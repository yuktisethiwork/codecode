# 189. Rotate Array — Cyclic replacement (advanced)

| Field | Value |
|-------|-------|
| **Problem** | [189. Rotate Array](https://leetcode.com/problems/rotate-array/submissions/2003970844/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Time Complexity** | O(n) |
| **Space Complexity** | O(1) |
| **Runtime** | 11 ms |
| **Memory** | 26.9 MB |
| **Patterns** | Array, Math, Two Pointers |
| **Date** | 15/05/2026 |

---

## 💡 Key Idea
Cyclic Replacement

## 🧠 How I Solved It
Bring each element directly to its correct position until we reach the starting index itself. Repeat this for all the elements of the array so that all the elements are rotated until starting index is reached.

**Code:** [`cyclic_replacement_(advanced).py`](./cyclic_replacement_(advanced).py)
