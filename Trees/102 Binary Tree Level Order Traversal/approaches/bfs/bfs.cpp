# Problem: 102. Binary Tree Level Order Traversal
# Approach: BFS
# Language: cpp
# Time: O(n)
# Space: O(n)

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
#include<queue>
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        vector<vector<int>> arr;
        if (root==nullptr){
            return arr;
        }
        while (!q.empty()){
            int size=q.size();
            vector<int> level;
            for(int i=0;i<q.size();i++){
                TreeNode* j= q.front();
                q.pop();
                level.push_back(j->val);
                if (j->left!=nullptr){
                    q.push(j->left);
                }
                if(j->right!=nullptr){
                    q.push(j->right);
                }
            }
            arr.push_back(level);
        }
        return arr;
    }
};