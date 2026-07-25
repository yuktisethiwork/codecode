# 19. Remove Nth Node From End of List — Approach 1

| Field | Value |
|-------|-------|
| **Problem** | [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | cpp |
| **Runtime** | 0 ms |
| **Memory** | 8.4 MB |
| **Patterns** | Linked List, Two Pointers |
| **Date** | 25/07/2026 |

---

## 🧠 How I Solved It
bring fast pointer at a distance of n-1 nodes. then check if it is the last node, in which case we have to delete the head of the list. if not, continue moving the slow and fast till we reach the end of the list (n-1)th position and delete the node right after slow, which is the one to be deleted. better approach is to put a dummy node infront and do the same for n steps.

**Code:** [`approach_1.cpp`](./approach_1.cpp)
