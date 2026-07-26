# Problem: 49. Group Anagrams
# Approach: Solution
# Language: cpp
# Time: O(n*k)
# Space: O(n)

#include<bits/stdc++.h>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> mp;
        vector<vector<string>> ans;
        for(int i=0;i<strs.size();i++){
            string word = strs[i];
            vector<int> freq(26,0);
            for (char c : word){
                freq[c-'a']++;
            }
            string s="";
            for(int j=0;j<26;j++){
                s+=to_string(freq[j])+'#';
            }
            mp[s].push_back(word);
        }
        for(auto it : mp){
            ans.push_back(it.second);
        }
        return ans;
    }
};