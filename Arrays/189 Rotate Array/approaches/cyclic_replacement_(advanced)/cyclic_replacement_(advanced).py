# Problem: 189. Rotate Array
# Approach: Cyclic replacement (advanced)
# Language: python3

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start=0
        count=0
        n=len(nums)
        k=k%n
        while count<n:
            current=start
            while True:
                next_idx = (current + k) % n
