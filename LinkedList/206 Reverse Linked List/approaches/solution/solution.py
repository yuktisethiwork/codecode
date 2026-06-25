# Problem: 206. Reverse Linked List
# Approach: Solution
# Language: python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None or head.next ==None:
            return head # it is returning khudko he so that the earlier func calls can use it.
        newhead=head
        c=0
        if head.next !=None:
            newhead = self.reverseList(head.next)
            head.next.next= head
            head.next=None
        return newhead