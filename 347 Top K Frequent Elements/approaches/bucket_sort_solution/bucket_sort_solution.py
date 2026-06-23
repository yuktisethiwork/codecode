# Problem: 347. Top K Frequent Elements
# Approach: Bucket Sort solution
# Language: python3
# Time: O(n)
# Space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count.keys():
                count[i]+=1
            else:
                count[i]=1
        uniqnum=len(count.keys())
        revcount={}
        n= len(nums)
        for i in range(len(nums)+1): 
            revcount[i]=[]
        for num, freq in count.items():
            revcount[freq].append(num)
        res=[]
        c=0
        for i in range(len(nums), 0, -1):
            for j in revcount[i]:
                res.append(j)
        return res[:k]





    