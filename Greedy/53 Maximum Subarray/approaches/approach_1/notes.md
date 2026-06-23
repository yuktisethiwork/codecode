# 53. Maximum Subarray — Approach 1

| Field | Value |
|-------|-------|
| **Problem** | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Runtime** | 0 ms |
| **Memory** | 19.1 MB |
| **Patterns** | Array, Divide and Conquer, Dynamic Programming |
| **Date** | 24/06/2026 |

---

## 🧠 How I Solved It
sliding window kind of approach in which we keep shofting the right pointer and take the maximum sum of the subarray as long as the sum is all positive. the moment we encounter a negative sum. we remove the negative prefix and shift the left pointer to the current right position and restart the subarray.

**Code:** [`approach_1.py`](./approach_1.py)
