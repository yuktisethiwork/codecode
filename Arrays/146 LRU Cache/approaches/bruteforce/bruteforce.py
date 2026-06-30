# Problem: 146. LRU Cache
# Approach: Bruteforce
# Language: python3
# Time: O(n)
# Space: O(1)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.d={}
        self.counter=0

    def get(self, key: int) -> int:
        if key in self.d.keys():
            self.d[key][1]=self.counter
            self.counter+=1
            print(self.d)
            return self.d[key][0]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d.keys():
            self.d[key]=[value,self.counter]
            self.counter+=1
        else:
            if len(self.d.keys())==self.capacity:
                minc=float("inf")
                for i in self.d.keys():
                    if self.d[i][1] < minc:
                        minc=min(minc,self.d[i][1])
                        minkey=i
                print(minkey)
                del self.d[minkey]
            self.d[key] =[value,self.counter]
            self.counter+=1
        print(self.d)
                

            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)