# 33. Search in Rotated Sorted Array — Binary search

| Field | Value |
|-------|-------|
| **Problem** | [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/2056814535/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Time Complexity** | O(logn) |
| **Space Complexity** | O(1) |
| **Runtime** | 0 ms |
| **Memory** | 19.5 MB |
| **Patterns** | Array, Binary Search |
| **Date** | 05/07/2026 |

---

## 💡 Key Idea
Binary search

## 🧠 How I Solved It
Binary search -> left sorted portion -> compare target and nums[l]. right sorted portion-> compare target and nums[r]. also use nums[mid] to specify the exact range.


**Code:** [`binary_search.py`](./binary_search.py)
