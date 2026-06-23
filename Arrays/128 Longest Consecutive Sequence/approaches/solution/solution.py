# Problem: 128. Longest Consecutive Sequence
# Approach: Solution
# Language: python3
# Time: O(n)
# Space: O(1)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        maxl=0
        for i in s:
            length=1
            if i-1 not in s:
                length=1
                j=i
                while j+1 in s:
                    length+=1
                    j+=1
            maxl=max(maxl,length)
        return maxl
