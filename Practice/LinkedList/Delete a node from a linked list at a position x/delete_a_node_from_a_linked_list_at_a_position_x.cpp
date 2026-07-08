# Practice: Delete a node from a linked list at a position x
# Language: cpp
# Date: 08/07/2026

/*
class Node {
public:
    int data;
    Node* next;
    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }
};
*/
class Solution {
  public:
    Node* deleteNode(Node* head, int x) {
        if (x==1){
            Node* nnode=head;
            head=head->next;
            delete nnode;
            return head;
        }
        Node* prev=nullptr;
        Node* curr=head;
        int i=1;
        while (i<x && curr){
            prev=curr;
            curr=curr->next;
            i++;
        }
    
        prev->next=curr->next;
        delete curr;
        return head;
        
    }
};