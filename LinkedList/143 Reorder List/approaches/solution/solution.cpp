# Problem: 143. Reorder List
# Approach: Solution
# Language: cpp
# Time: O(n)
# Space: O(1)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {
        ListNode* slow=head;
        ListNode* fast=head;
        while (fast!=nullptr && fast->next!=nullptr){
            slow=slow->next;
            fast=fast->next->next;
        }
        ListNode* temp=slow->next;
        slow->next=nullptr;
        ListNode* prev=nullptr;
        while (temp!=nullptr){
            ListNode* curr=temp->next;
            temp->next=prev;
            prev=temp;
            temp=curr;
        }
        ListNode* temp2=prev;
        ListNode* temp1=head;
        while (temp2!=nullptr){
            ListNode* l=temp1->next;
            ListNode* r=temp2->next;
            temp1->next=temp2;
            temp2->next=l;
            temp1=l;
            temp2=r;
        }
        return ;
    }
};