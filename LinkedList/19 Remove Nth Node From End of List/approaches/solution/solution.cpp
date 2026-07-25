# Problem: 19. Remove Nth Node From End of List
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next==nullptr){
            return nullptr;
        }
        ListNode* slow=head;
        ListNode* fast=head;
        int i=1;
        while (i<n){
            fast=fast->next;
            i++;
        }
        if (fast->next==nullptr){
            ListNode* temp = head;
            head=head->next;
            delete temp;
            return head;
        }
        while (fast->next->next!=nullptr){
            fast=fast->next;
            slow=slow->next;
        }
        ListNode* node = slow->next;
        slow->next=node->next;
        delete node;
        return head;

    }
};