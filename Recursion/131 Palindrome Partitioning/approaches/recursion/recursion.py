# Problem: 131. Palindrome Partitioning
# Approach: Recursion
# Language: python3
# Time: o(2^n)
# Space: O(n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        from collections import defaultdict
        n=len(s)
        partitionidx=defaultdict(list)
        gl=[]
        def ispalindrome(i,j):
            l,r=i,j
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def f(i):
            if i==n:
                gl.append([x[0] for x in partitionidx.values() if x])
                return 
            for k in range(i,n):
                if ispalindrome(i,k):
                    partitionidx[i].append(s[i:k+1])
                    f(k+1)
                    partitionidx[i].pop()
        f(0)
        res=[]
        for i in gl:
            if i!=[]:
                res.append(i)
        return res
            
                