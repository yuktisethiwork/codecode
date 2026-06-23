# 347. Top K Frequent Elements — Heap

| Field | Value |
|-------|-------|
| **Problem** | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| **Platform** | LeetCode |
| **Difficulty** | Medium |
| **Language** | python3 |
| **Time Complexity** | O(mlogk) |
| **Space Complexity** | O(m+k) |
| **Runtime** | 0 ms |
| **Memory** | 19.3 MB |
| **Patterns** | Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect |
| **Date** | 23/06/2026 |

---

## 💡 Key Idea
heap

## 🧠 How I Solved It
Pass the count dict into the heapq object and make it a min heap. (minimum element to be popped first)
keep popping from the maxheap if length increases k.
then append the elements from the min heap to a result. since the heap contains tuples of frequency and number.

**Code:** [`heap.py`](./heap.py)
