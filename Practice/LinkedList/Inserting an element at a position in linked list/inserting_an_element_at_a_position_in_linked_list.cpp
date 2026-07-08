# Practice: Inserting an element at a position in linked list
# Language: cpp
# Date: 08/07/2026

/*
class Node {
  public:
    int data;
    Node *next;
    Node(int x) {
        data = x;
        next = nullptr;
    }
};
*/

class Solution {
  public:
    Node *insertPos(Node *head, int pos, int val) {
        if (pos==1){
            Node* newnode= new Node(val);
            newnode->next=head;
            head=newnode;
            return head;
        }
        Node* temp=head;
        int i=1;
        
        while(i<pos-1){
            i+=1;
            temp=temp->next;
        }
        Node* newnode=new Node(val);
        newnode->next= temp->next;
        temp->next=newnode;
        return head;
    }
};