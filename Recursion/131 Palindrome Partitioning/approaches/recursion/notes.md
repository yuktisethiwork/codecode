# 131. Palindrome Partitioning — Recursion

| Field | Value |
|-------|-------|
| **Problem** | [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Time Complexity** | o(2^n) |
| **Space Complexity** | O(n) |
| **Runtime** | 0 ms |
| **Memory** | 19.3 MB |
| **Patterns** | String, Dynamic Programming, Backtracking, Recursion |
| **Date** | 18/06/2026 |

---

## 💡 Key Idea
Use partitionidx array to store the partitions.

## 🧠 How I Solved It
Represented each function call with the index parameter where we want to partition the string. It can be partitioned only when i-> any given index in the array is a palindrome. if it can be partitioned we move to the next index after k. and then recheck. we continue this till we reach the leaf nodes. But we want to record where all we made the partitions so we use the partitionidx dictionary. A list would have been better though. path.append(palindromicstring) and then at the lead append the entire path list. gl.append(path[:]).

**Code:** [`recursion.py`](./recursion.py)
