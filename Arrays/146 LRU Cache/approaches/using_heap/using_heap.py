# Problem: 146. LRU Cache
# Approach: Using heap
# Language: python3
# Time: O(logn)
# Space: O(n)

import heapq
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.heap=[]
        self.d={}
        self.counter=0

    def get(self, key: int) -> int:
        if key in self.d.keys():
            self.d[key][1]=self.counter
            heapq.heappush(self.heap,[self.counter,key])
            self.counter+=1
            return self.d[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        heapq.heappush(self.heap,[self.counter,key])
        self.d[key]=[value,self.counter]
        self.counter+=1
        if len(self.d)>self.capacity:
            while self.heap:
                c,i=heapq.heappop(self.heap)
                if i in self.d.keys() and c==self.d[i][1]:
                    del self.d[i]
                    break
        



            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)