# Practice: Reverse a linked list
# Language: cpp
# Date: 08/07/2026

/*
class Node {
 public:
    int data ;
    Node *next ;

    Node(int x) {
        data = x ;
        next = nullptr ;
    }
};
*/

class Solution {
  public:
    Node* reverseList(Node* head) {
        Node* temp=nullptr;
        Node* curr=head;
        while (curr!=nullptr){
            Node* nxt=curr->next;
            curr->next=temp;
            temp=curr;
            curr=nxt;
        }
        return temp;
        
    }
};