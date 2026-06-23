# Problem: 53. Maximum Subarray
# Approach: Kadane's algo
# Language: python3
# Time: O(n)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        j=0
        summ=0
        maxsumm=nums[0]
        for i in range(len(nums)):
            if summ<0:
                summ=0
            summ+=nums[i]
            maxsumm=max(maxsumm,summ)
        return maxsumm

