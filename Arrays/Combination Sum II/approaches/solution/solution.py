# Problem: Combination Sum II
# Approach: Solution
# Language: python3
# Time: O(2**n)
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
            elif s>target or i==n:
                return
            for k in range(i,n):
                if candidates[k]==candidates[k-1] and k!=i:
                    continue
                arr.append(candidates[k])
                f(k+1,s+candidates[k], arr)
                arr.pop()
        f(0,0,[])
        return gl