class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        
        bool removedOne = false;
        int previous = nums[0];
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] < previous){
                if(!removedOne){
                    removedOne = true;
                } else{
                    return false;
                }
                if (i - 2 >= 0 && nums[i-2] > nums[i]){
                    continue;
                }
            }
            previous = nums[i];
        }
        return true;
    }
};
