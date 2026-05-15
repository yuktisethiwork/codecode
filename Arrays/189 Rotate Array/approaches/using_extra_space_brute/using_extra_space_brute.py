# Problem: 189. Rotate Array
# Approach: Using extra space brute
# Language: python3
# Time: O(n)
# Space: O(n)

        k=k%n
        for _ in range(n):
            B[(_+k)%n] = nums[_]
        B=[None]*n 
        n=len(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:]=B[:]
        return nums
