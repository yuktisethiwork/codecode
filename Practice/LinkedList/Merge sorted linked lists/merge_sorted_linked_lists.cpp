# Practice: Merge sorted linked lists
# Language: cpp
# Date: 09/07/2026

/*
class Node {
 public:
    int data;
    Node *next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};
*/

class Solution {
  public:
    Node* sortedMerge(Node* head1, Node* head2) {
        Node* i = head1;
        Node* j = head2;
        Node* temp1 = new Node(0);
        Node* temp=temp1;
        while (i!=nullptr && j!=nullptr){
            if (i->data<=j->data){
                temp->next=i;
                temp=temp->next;
                i=i->next;
            }
            else if (i->data>j->data){
                temp->next=j;
                temp=temp->next;
                j=j->next;
            }
        }
        
        if (i!=nullptr && j==nullptr){
            temp->next=i;
        }
        else if(i==nullptr && j!=nullptr){
            temp->next=j;
        }
        return temp1->next;
    }
};