# 203. Remove Linked List Elements — Approach 1

| Field | Value |
|-------|-------|
| **Problem** | [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) |
| **Platform** | LeetCode |
| **Difficulty** | Easy |
| **Language** | cpp |
| **Runtime** | 0 ms |
| **Memory** | 8.4 MB |
| **Patterns** | Linked List, Recursion |
| **Date** | 26/07/2026 |

---

## 🧠 How I Solved It
Tricky case is deleting the nodes that are the head of the linked list at the very beginning. they are the ones need to be deleted until it kees on matching the value or the head reaches nullptr. then after that we can go ahead and do the basic prev and curr way of deleting. it will always increment the prev pointer to head since head no longer will be the matching value.

**Code:** [`approach_1.cpp`](./approach_1.cpp)
