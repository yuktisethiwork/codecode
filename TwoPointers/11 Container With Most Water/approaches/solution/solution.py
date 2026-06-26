# Problem: 11. Container With Most Water
# Approach: Solution
# Language: python3
# Time: O(n)
# Space: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxarea=float("-inf")
        while i<j:
            l=min(height[i], height[j])
            b=j-i
            area=l*b
            if area>maxarea:
                maxarea=area
            if height[i]>height[j]:
                j-=1
            elif height[i]<=height[j]:
                i+=1
        return maxarea

                