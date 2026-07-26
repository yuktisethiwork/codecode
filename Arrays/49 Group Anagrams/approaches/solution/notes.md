# 49. Group Anagrams — Solution

| Field | Value |
|-------|-------|
| **Problem** | [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | cpp |
| **Time Complexity** | O(n*k) |
| **Space Complexity** | O(n) |
| **Runtime** | 0 ms |
| **Memory** | 8.9 MB |
| **Patterns** | Array, Hash Table, String, Sorting |
| **Date** | 26/07/2026 |

---

## 🧠 How I Solved It
key=> freq of chars in everyword and append the word having those freq. since vector cannot be hashed as a key in map we convert it into a string and then use it.

**Code:** [`solution.cpp`](./solution.cpp)
