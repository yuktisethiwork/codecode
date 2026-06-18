# Practice: M-coloring
# Language: python3
# Date: 18/06/2026

# User function Template for python3

class Solution:
    def graphColoring(self, v, edges, m):
        d={}
        color={}
        for i in range(v):
            d[i]=[]
            color[i]=-1
        for i,j in edges:
            d[i].append(j)
        var=0
        def cancolor(i,k):
            for v in d[i]:
                if color[v]==k:
                    return False
            return True
        
        def f(i):
            if i==v:
                return True
            for k in range(m):
                if cancolor(i,k):
                    color[i]=k
                    if f(i+1) == True:
                        return True
                    color[i]=-1
            return False
        return f(0)
        
        
        
                    
                
      