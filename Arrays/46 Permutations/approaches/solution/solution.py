# Problem: 46. Permutations
# Approach: Solution
# Language: python3

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        gl=[]
        def f(i):
            if i==
            gl.append(nums[:])
            for k in range(i,n):
                nums[k], nums[i] = nums[i], nums[k]
                f(i+1)
                nums[k], nums[i] = nums[i], nums[k] 
        arrr=[]
        f(0)
        return gl