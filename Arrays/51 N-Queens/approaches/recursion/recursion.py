# Problem: 51. N-Queens
# Approach: Recursion
# Language: python3
# Time: O(n!*n)
# Space: O(n**2)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mat=[['.' for i in range(n)] for k in range(n)]
        gl=[]
        def canfill(i,j):
            for k in range(j):
                if mat[i][k]=='Q':
                    return False
            r,c=i-1, j-1
            while r>=0 and c>=0:
                if mat[r][c]=='Q':
                    return False
                r-=1
                c-=1
            r,c=i+1,j-1
            while r<n and c>=0:
                if mat[r][c]=='Q':
                    return False
                r+=1
                c-=1
            return True
        def f(col):
            if col==n:
                lll=[]
                for _ in range(n):
                    s=''
                    for __ in range(n):
                        s+=mat[_][__]
                    lll.append(s)
                gl.append(lll[:]) 
            for k in range(0,n):
                if canfill(k,col) :
                    mat[k][col] = 'Q'
                    f(col+1)
                    mat[k][col] = '.'
        f(0)
        print(gl)
        return gl
