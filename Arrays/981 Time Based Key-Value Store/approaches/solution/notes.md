# 981. Time Based Key-Value Store — Solution

| Field | Value |
|-------|-------|
| **Problem** | [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | cpp |
| **Time Complexity** | O(logn |
| **Runtime** | 0 ms |
| **Memory** | 9 MB |
| **Patterns** | Hash Table, String, Binary Search, Design |
| **Date** | 27/07/2026 |

---

## 🧠 How I Solved It
Create a map of key and the values as vectors storing pairs of value and timestamps. then while getting a value, we need to find the timestamp that is smaller than the provided timestamp but largest among the provided options. While decrementing to the lower side, we update the answer to mid. also an important optimisation is to use the vector pointer instead of creating a vector from scratch again and again to check the values of map.


**Code:** [`solution.cpp`](./solution.cpp)
