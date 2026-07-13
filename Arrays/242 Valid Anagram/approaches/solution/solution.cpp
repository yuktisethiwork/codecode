# Problem: 242. Valid Anagram
# Approach: Solution
# Language: cpp

class Solution {
public:
    bool isAnagram(string s, string t) {

        unordered_map<char,int> mp;
        for (char c: s){
            mp[c]++;
        }
        for (char c: t){
            mp[c]--;
            if (mp[c]<0){
                return false;
            }
        }
        return true;

    }
};