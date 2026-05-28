# Problem: 40. Combination Sum II
# Approach: Recursion
# Language: python3
# Time: O(2^n)
# Space: O(n)

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        gl=[]
        n=len(candidates)
        def f(i,s,arr):
            if s==target:
                gl.append(arr[:])
                return
            if s>target or i==n:
                return
            arr.append(candidates[i])
            f(i + 1, s + candidates[i], arr)
            arr.pop()
            j=i
            while j<n-1 and candidates[j]!=candidates[j+1]:
                j+=1
            f(j+1,s,arr)

        f(0,0,[])
        return gl
