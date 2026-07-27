# Problem: 230. Kth Smallest Element in a BST
# Approach: Solution
# Language: cpp
# Time: O(n)
# Space: O(h)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int i=0;
    int ans=0;
    int inorder(TreeNode* root, int k){
        if (root==nullptr){
            return 0;
        }
        int l=inorder(root->left,k);
        if (l==-1){
            return -1;
        }
        i++;
        if (i==k){
            ans=root->val;
            return -1;
        }

        int r= inorder(root->right,k);
        if(r==-1){
            return -1;
        }
        return -1;
    }
    int kthSmallest(TreeNode* root, int k) {
        inorder(root, k);
        return ans;

    }
};