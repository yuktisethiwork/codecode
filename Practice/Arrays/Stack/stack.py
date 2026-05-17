# Practice: Stack
# Language: python3
# Date: 17/05/2026


class Stack:
    def __init__(self):
        self.stack=[]
    def adds(self,v):
        self.stack=[v]+self.stack
        return
    def isempty(self):
        return (self.stack==[])
    def dels(self):
        if not self.isempty():
            v=self.stack.pop()
            return v
        else:
            return None
    def __str__(self):
        return str(self.stack)
q=Stack()
q.adds(5)
q.adds(6)
print(q)
q.dels()
print(q)
q.dels()
print(q)
        