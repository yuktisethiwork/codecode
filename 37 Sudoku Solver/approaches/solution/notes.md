# 37. Sudoku Solver — Solution

| Field | Value |
|-------|-------|
| **Problem** | [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) |
| **Platform** | LeetCode |
| **Difficulty** | Hard |
| **Language** | python3 |
| **Time Complexity** | O(9^m) |
| **Space Complexity** | O(m) |
| **Runtime** | 31 ms |
| **Memory** | 19.3 MB |
| **Patterns** | Array, Hash Table, Backtracking, Matrix, Recursion |
| **Date** | 17/06/2026 |

---

## 💡 Key Idea
Recursion

## 🧠 How I Solved It
Recursion but without any index because if we use f(col) then we will have to increase the column index in the next recursion call but there can be other cells in the same column and different rows which can still be empty and need to be filled. Do not modify already filled cells. Logic to find the 3*3 box area is to find the topleft row and column using math and then travers the box and check if the number is there. we return early if we are able to find a solution and we return false if we are not able to find any number than can fill a cell because then there is no point going down that branch of the recursion tree.

## ⚠️ Mistakes / Edge Cases
Need to optimise as its a TLE

## 🎯 Interview Insight
Need to optimise as its a TLE

**Code:** [`solution.py`](./solution.py)
