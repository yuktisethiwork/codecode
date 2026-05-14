# Problem: Rotate Array
# Approach: 2 pointer approach to reverse the array
# Language: python3

        
            r-=1
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
        while l<=r:
        k=k%n
        l,r=0,n-1
        n=len(nums)
        Do not return anything, modify nums in-place instead.
        """
        """
    def rotate(self, nums: List[int], k: int) -> None:
class Solution:
