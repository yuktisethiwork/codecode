# Problem: 347. Top K Frequent Elements
# Approach: Hashmap
# Language: python3
# Time: O(n log n)
# Space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count.keys():
                count[i]+=1
            else:
                count[i]=1
        res=[k for k,v in (sorted(count.items(), key=lambda x: x[1], reverse=True))]
        return res[:k]

    