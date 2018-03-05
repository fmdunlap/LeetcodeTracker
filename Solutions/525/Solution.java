class Solution {
    public int findMaxLength(int[] nums) {
        //First make it such that we can do sums
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0){
                nums[i] = -1;
            }
        }
        
        int count = 0;
        int max = 0;
        HashMap<Integer, Integer> indexMap = new HashMap<>();
        indexMap.put(0,-1);
        
        for(int i = 0; i < nums.length; i++){
            count += nums[i];
            if (indexMap.containsKey(count)) {
                max = Math.max(max, i - indexMap.get(count));
            }
            else {
                indexMap.put(count, i);
            }
        }
        return max;
    }
}
