# Problem: 3. Longest Substring Without Repeating Characters
# Approach: Solution
# Language: python3
# Time: O(n)
# Space: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)!=0:
            maxc=1
        else:
            return 0
        count=0
        n=len(s)
        i=0
        j=0
        ss=set()
        while j<n:
            while s[j] in ss:
                count-=1
                ss.remove(s[i])
                i+=1
            count+=1
            ss.add(s[j])
            maxc=max(maxc,count)
            j+=1
        return maxc