# Problem: 543. Diameter of Binary Tree
# Approach: Solution
# Language: cpp

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
    int ll=0;
    int maxd(TreeNode* root){
        if (root==nullptr){
            return 0;
        };
        int l = maxd(root->left);
        int r= maxd(root->right);
        ll = l+r;
        return 1+max(l, r);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        maxd(root);
        return ll;
    }
};