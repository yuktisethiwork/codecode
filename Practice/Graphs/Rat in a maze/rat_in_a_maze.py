# Practice: Rat in a maze
# Language: python3
# Date: 18/06/2026

class Solution:
    def ratInMaze(self, maze):
        # code here
        l = [(1,0), (0,-1), (0,1), (-1,0)]
        s = "DLRU"
        gl=[]
        n=len(maze)
        path=[]
        visited=[[False for i in range(n)] for j in range(n)]
        if maze[0][0] == 0 or maze[n-1][n-1] == 0:
                return []
        def f(i,j):
            if i==n-1 and j==n-1:
                gl.append(''.join(path))
                return
            for ix in range(len(l)):
                idx=l[ix][0]
                idxx=l[ix][1]
                if 0 <= i+idx < n and 0 <= j+idxx < n and not visited[i+idx][j+idxx] and maze[i+idx][j+idxx]!=0:
                    path.append(s[ix])
                    visited[i+idx][j+idxx]=True
                    f(i+idx,j+idxx)
                    path.pop()
                    visited[i+idx][j+idxx]=False
        visited[0][0]=True
        f(0,0)
        return gl