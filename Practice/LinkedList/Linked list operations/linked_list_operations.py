# Practice: Linked list operations
# Language: python3
# Date: 15/05/2026


class Node:
    def __init__(self,v=None):
        self.value = v
        self.next = None
    def addnode_at_end(self,v):
        temp=self
        while temp.next!=None:
            temp=temp.next
        temp.next=Node(v)
        return self
    def addnode_at_index(self,i,v):
        if i==0:
            newnode=Node(v)
            self.value, newnode.value = newnode.value, self.value
            newnode.next, self.next = self.next, newnode
            return self
        j=0
        temp=self
        while j!=i:
            temp=temp.next
            j+=1
        newnode=Node(v)
        newnode.next=temp.next
        temp.next=newnode
        return self
    def deletenode(self,v):
        temp=self
        if self.value==v and self.next==None:
            self.value=None
            return self
        elif self.value==v and self.next!=None:
            self.value= self.next.value
            self.next= self.next.next
            return self
        else:
            prev=None
            curr=self
            while curr!=None:
                if curr.value==v and curr.next!=None:
                    prev.next=prev.next.next
                    break
                elif curr.value==v and curr.next==None:
                    prev.next=None
                    break
                prev=curr
                curr=curr.next
        return self
    def display(self):
        temp=self
        l=[]
        while temp!=None:
            l.append(temp.value)
            temp=temp.next
        return l
n=Node(1)
print(n.display())
n.addnode_at_end(2)
n.addnode_at_end(2)
n.addnode_at_end(2)
print(n.display())
n.addnode_at_index(0,3)
print(n.display())
n.addnode_at_index(2,3)    
print(n.display())
n.deletenode(3)
print(n.display())
n.deletenode(2)
print(n.display())
n.deletenode(2)
print(n.display())
n.deletenode(2)
print(n.display())
n.deletenode(1)
print(n.display())
    
        
            