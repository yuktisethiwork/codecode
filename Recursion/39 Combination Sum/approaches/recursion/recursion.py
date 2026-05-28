# Problem: 39. Combination Sum
# Approach: Recursion
# Language: python3
# Time: O(2**n)
# Space: O(n)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        gl=[]
        n=len(candidates)
        def f(i,s,arr):
            if s==target:
                gl.append(arr[:])
                return
            elif s>=target or i==n:
                return
            print(i)
            arr.append(candidates[i])
            s+=candidates[i]
            f(i,s,arr)
            arr.pop()
            s-=candidates[i]
            if i<n-1:
                f(i+1,s,arr)
        f(0,0,[])
        return gl



        