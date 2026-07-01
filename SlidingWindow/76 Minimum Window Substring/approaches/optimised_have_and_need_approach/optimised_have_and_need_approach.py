# Problem: 76. Minimum Window Substring
# Approach: Optimised have and need approach
# Language: python3
# Time: O(n)
# Space: O(n)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s) or t=='':
            return ""
        need={}
        have={}
        for i in t:
            if i in need.keys():
                need[i]+=1
            else:
                need[i]=1
        for j in t:
            have[j] =0
        l=0
        havec=0
        needc=len(need)
        res=[-1,-1]
        reslen=float('inf')
        for r in range(len(s)):
            if s[r] in need:
                have[s[r]]+=1
                if have[s[r]]==need[s[r]]:
                    havec+=1
                while havec==needc:
                    if r - l + 1 < reslen:
                        reslen = r - l + 1
                        res = [l, r]
                    if s[l] in need:
                        have[s[l]]-=1
                        if need[s[l]]>have[s[l]]:
                            havec-=1
                    l+=1
        return res
                
                        
                

