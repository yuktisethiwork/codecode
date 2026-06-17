# 37. Sudoku Solver — Recursion time optimised

| Field | Value |
|-------|-------|
| **Problem** | [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) |
| **Platform** | LeetCode |
| **Difficulty** | Hard |
| **Language** | python3 |
| **Time Complexity** | O(9^m) |
| **Space Complexity** | O(m) |
| **Runtime** | 3 ms |
| **Memory** | 19.4 MB |
| **Patterns** | Array, Hash Table, Backtracking, Matrix, recursion |
| **Date** | 17/06/2026 |

---

## 💡 Key Idea
Optimise using sets and extra arrays.

## 🧠 How I Solved It
m= number of empty cells in sudoku box.
from the previous solution, have used a lists of sets to store what all numbers are there in each row, column and box. Have used a mathematical formula to detect the box number given a row and column. need to update these sets when adding a number to an empty cell in the recursion calls too. Also have used an array to store the empty cells in the box instead of scanning all of the rows and columns to detect the empty cell again and again in each recursion call. so added the index of the array storing empty cells in the parameter of the recursive function and base case is when we reach the end of it.

**Code:** [`recursion_time_optimised.py`](./recursion_time_optimised.py)
