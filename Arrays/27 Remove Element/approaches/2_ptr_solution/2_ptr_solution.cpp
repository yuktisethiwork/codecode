# Problem: 27. Remove Element
# Approach: 2 ptr solution
# Language: cpp
# Time: O(n)
# Space: O(1)

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left=0;
        int right=nums.size()-1;
        while (left<=right){
            if (nums[left]==val){
                nums[left]=nums[right];
                right--;
            }else{
                left++;
            }
        }
        return left;
    }
};