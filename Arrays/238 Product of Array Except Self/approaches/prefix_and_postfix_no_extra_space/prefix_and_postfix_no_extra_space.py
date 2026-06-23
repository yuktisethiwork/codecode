# Problem: 238. Product of Array Except Self
# Approach: Prefix and postfix no extra space
# Language: python3
# Time: O(n)
# Space: O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        prefix=1
        for i in range(len(nums)):
            res[i]*=prefix
            prefix=res[i]*nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix=res[i]*nums[i]
        return res
