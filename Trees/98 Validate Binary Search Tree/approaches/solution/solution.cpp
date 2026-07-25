# Problem: 98. Validate Binary Search Tree
# Approach: Solution
# Language: cpp
# Time: O(n)
# Space: 0(n)

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
#include<bits/stdc++.h>
class Solution {
public:
    bool isvalid(TreeNode* root, int low, int high){
        if (root==nullptr){
              return true;
        }else if (low>=root->val || root->val>=high){
            return false;
        }else{
            return isvalid(root->right,root->val,high) && isvalid(root->left,low,root->val);;
        }
    }
    bool isValidBST(TreeNode* root) {
        return isvalid(root,INT_MIN,INT_MAX);
    }
};