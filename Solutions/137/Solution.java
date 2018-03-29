class Solution {
    public int singleNumber(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int num : nums){
            int curCount = map.getOrDefault(num, 0);
            map.put(num, curCount + 1);
        }
        for(Integer key : map.keySet()){
            if(map.get(key) == 1) return key;
        }
        return 0;
    }
}
