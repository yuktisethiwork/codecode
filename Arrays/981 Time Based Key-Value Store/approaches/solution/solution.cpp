# Problem: 981. Time Based Key-Value Store
# Approach: Solution
# Language: cpp
# Time: O(logn

class TimeMap {
public:
    unordered_map<string,vector<pair<string,int>>> mp;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        mp[key].push_back({value, timestamp});
    }
    
    string get(string key, int timestamp) {
        if (mp.find(key)==mp.end()){
            return "";
        }
        vector<pair<string,int>> arr = mp[key];
        int l=0;
        int r=arr.size()-1;
        int ans=-1;
        while (l<=r){
            int mid = (l+r)/2;
            if (timestamp >= arr[mid].second){
                ans=mid;
                l=mid+1;
            } else if (timestamp < arr[mid].second){
                r=mid-1;
            }
        }
        if (ans==-1){
            return "";
        }
        return arr[ans].first;

    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */