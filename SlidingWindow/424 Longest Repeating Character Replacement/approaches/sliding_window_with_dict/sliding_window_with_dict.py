# Problem: 424. Longest Repeating Character Replacement
# Approach: sliding window with dict
# Language: python3
# Time: O(26*n)
# Space: O(26*n)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        i=0
        j=0
        if s=='':
            return 0
        res=1
        maxfreq=0
        while j<len(s):
            if s[j] in d.keys():
                d[s[j]]+=1
            else:
                d[s[j]]=1
            maxfreq=max(maxfreq,d[s[j]])
            while j-i+1-maxfreq>k:
                d[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
            j+=1
        return res
            

