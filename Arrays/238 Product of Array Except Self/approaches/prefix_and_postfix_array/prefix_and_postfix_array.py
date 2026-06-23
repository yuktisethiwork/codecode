# Problem: 238. Product of Array Except Self
# Approach: Prefix and postfix array
# Language: python3
# Time: O(n)
# Space: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums=[1]+nums +[1]
        prefix=[1]*(n+2)
        postfix=[1]*(n+2)
        res=[]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i]
        for i in range(n, -1, -1):
            postfix[i]=postfix[i+1]*nums[i]
        print(prefix)
        print(postfix)
        for i in range(1,n+1):
            res.append(prefix[i-1]*postfix[i+1])
        return res

