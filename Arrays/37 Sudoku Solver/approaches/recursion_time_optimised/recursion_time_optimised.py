# Problem: 37. Sudoku Solver
# Approach: Recursion time optimised
# Language: python3
# Time: O(9^m)
# Space: O(m)

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Modify the board in-place to solve the Sudoku.
        """
        n=9
        res=[]
        hashmap=[False]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]

                    rows[r].add(num)
                    cols[c].add(num)

                    box = (r // 3) * 3 + (c // 3)
                    boxes[box].add(num)
        def canfill(row,col,num):
            box=(row // 3) * 3 + (col // 3)
            if num in rows[row] or num in cols[col] or num in boxes[box]:
                return False
            return True
        mat=[]
        for i in range(n):
            for j in range(n):
                if board[i][j]=='.':
                    mat.append([i,j])
        def f(idx):
            if idx ==len(mat):
                return True
            row,col=mat[idx]
            for num in '123456789':
                if canfill(row,col,num):
                    box=(row // 3) * 3 + (col // 3)
                    board[row][col]=num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box].add(num)
                    if f(idx+1) == True:
                        return True
                    else:
                        board[row][col]='.'
                        rows[row].remove(num)
                        cols[col].remove(num)
                        boxes[box].remove(num)
            return False
        f(0)

                    


