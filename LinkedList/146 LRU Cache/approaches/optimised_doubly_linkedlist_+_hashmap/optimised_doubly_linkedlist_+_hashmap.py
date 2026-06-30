# Problem: 146. LRU Cache
# Approach: Optimised Doubly linkedlist + hashmap
# Language: python3
# Time: O(1)
# Space: O(n)

import heapq
class Node:
    def __init__(self,key,val):
        self.val=val
        self.key=key
        self.next=None
        self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.d={}
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
        self.left.prev,self.right.next=None,None

    def insertend(self,node):
        prev = self.right.prev
        prev.next=node
        node.prev=prev
        node.next=self.right
        self.right.prev=node

    def remove(self,node):
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            self.insertend(self.d[key])
            return self.d[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
            self.insertend(self.d[key])
            self.d[key].val=value
        else:
            if len(self.d)==self.capacity:
                dkval=self.left.next.key
                self.remove(self.left.next)
                del self.d[dkval]
            self.d[key]=Node(key,value)
            self.insertend(self.d[key])
        
            
                



            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)