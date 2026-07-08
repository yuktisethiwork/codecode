# Practice: Reverse a linked list (recursive)
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
        if (head==nullptr || head->next==nullptr){
            return head;
        }
        Node* newhead=this->reverseList(head->next);
        head->next->next=head;
        head->next=nullptr;
        return newhead;
    }
};