# Problem: 706. Design HashMap
# Approach: Solution
# Language: cpp
# Time: O(n)
# Space: O(n)

class MyHashMap {
private:
    vector<vector<pair<int,int>>> mp;
    int size=1009;
public:
    MyHashMap() {
        mp.resize(size);
    }
    int hash(int key){
        return (key%size);
    }
    void put(int key, int value) {
        int idx=hash(key);
        for (auto &i:mp[idx]){
            if (i.first==key){
                i.second=value;
                return;
            }
        }
        mp[idx].push_back({key,value});
        return;
    }
    int get(int key) {
        int idx=hash(key);
        for (auto &i:mp[idx]){
            if (i.first==key){
                return i.second;
            }
        }
        return -1;
    }
    void remove(int key) {
        int idx=hash(key);
        for (auto it=mp[idx].begin(); it!=mp[idx].end();it++){
            if (it->first==key){
                mp[idx].erase(it);
                return;
            }
        }
        return;
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */