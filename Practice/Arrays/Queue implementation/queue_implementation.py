# Practice: Queue implementation
# Language: python3
# Date: 15/05/2026


class Queue:
    def __init__(self):
        self.queue=[]
    def addq(self,v):
        self.queue.append(v)
        return
    def isempty(self):
        return (self.queue==[])
    def delq(self):
        if not self.isempty():
            v=self.queue.pop()
            return v
        else:
            return None
    def __str__(self):
        return str(self.queue)
q=Queue()
q.addq(5)
q.addq(6)
print(q)
q.delq()
print(q)
q.delq()
print(q)
        