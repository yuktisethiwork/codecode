# Problem: 90. Subsets II
# Approach: Solution
# Language: python3
# Time: O(2**n)
# Space: O(n)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        def f(ind,l):
            res.append(l[:])
            for k in range(ind,n):
                if nums[k]==nums[k-1] and k!=ind:
                    continue
                l.append(nums[k])
                f(k+1,l)
                l.pop()
        f(0,[])
        return res