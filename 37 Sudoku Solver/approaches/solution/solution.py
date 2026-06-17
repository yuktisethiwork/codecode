# Problem: 37. Sudoku Solver
# Approach: Solution
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
        def canfill(row,col,num):
            for i in range(n):
                if board[i][col]==num:
                    return False
            for j in range(n):
                if board[row][j]==num:
                    return False
            sr=row//3 * 3
            sc=col//3 * 3
            for i in range(sr,sr+3):
                for j in range(sc,sc+3):
                    if board[i][j]==num:
                        return False
            return True
        
        def f():
            for row in range(n):
                for col in range(n):
                    if board[row][col]=='.':
                        for num in '123456789':
                            if canfill(row,col,num):
                                board[row][col]=num
                                if f() == True:
                                    return True
                                else:
                                    board[row][col]='.'
                        return False
            return True
        f()

                    


