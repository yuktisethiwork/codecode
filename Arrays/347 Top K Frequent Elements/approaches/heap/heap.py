# Problem: 347. Top K Frequent Elements
# Approach: Heap
# Language: python3
# Time: O(mlogk)
# Space: O(m+k)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap=[]
        count={}
        for i in nums:
            count[i]=1+count.get(1,0)
        for i,c in count.items():
            heapq.heappush(heap,(c,i))
            if len(heap)>k:
                heapq.heappop(heap)   
        res=[]
        while heap:
            c,i=heapq.heappop(heap)
            res.append(i)
        return res
