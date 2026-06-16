# Problem: Permutations
# Approach: Solution
# Language: python3

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        gl=[]
        d={}
        for i in range(n):
            d[i]=False
        def f (i,d,arr):
            if i==n:
                gl.append(arr[:])
                return
            for k in range(0,n):
                if not d[k]:
                    d[k]=True
                    arr.append(nums[k])
                    f(i+1,d,arr)
                    d[k]=False
                    arr.pop()
        arrr=[]
        f(0,d,arrr)
        return gl