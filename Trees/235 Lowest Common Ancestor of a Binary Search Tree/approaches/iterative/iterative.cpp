# Problem: 235. Lowest Common Ancestor of a Binary Search Tree
# Approach: Iterative
# Language: cpp
# Time: O(log n)
# Space: O(log n)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* curr=root;
        while (curr!=nullptr){
            if (p->val<curr->val && q->val<curr->val){
                curr=curr->left;
            }else if (p->val<curr->val && q->val<curr->val){
                curr=curr->right;
            }else{
                return curr;
            }
        }
        return curr;
    }
};