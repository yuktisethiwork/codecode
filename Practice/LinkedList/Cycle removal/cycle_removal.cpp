# Practice: Cycle removal
# Language: cpp
# Date: 09/07/2026

/* Structure of linked list Node
class Node {
  public:
    int data;
    Node* next;

    Node(int val) {
        data = val;
        next = nullptr;
    }
};
*/
class Solution {
  public:
    void removeLoop(Node* head) {
        Node* slow=head;
        Node* fast=head;
        // to detect the cycle
        while(fast && fast->next){
            slow=slow->next;
            fast=fast->next->next;
            if(slow==fast){
                break;
            }
        }
        // if no cycle
        if (fast == nullptr || fast->next == nullptr)
            return;
        // reach the starting node of the cycle
        slow=head;
        while (slow!=fast){
            slow=slow->next;
            fast=fast->next;
        }
        // get the pointer to the starting node of the cycle to delete that link.
        Node*temp=slow;
        while (temp->next!=slow){
            temp=temp->next;
        }
        temp->next=nullptr;

    }
};