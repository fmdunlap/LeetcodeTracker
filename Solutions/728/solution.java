import java.util.*;
import java.lang.*;


class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        ArrayList<Integer> retList = new ArrayList<Integer>();
        for(int i = left; i <= right; i++){
            double logDigits = Math.log10(i);
            int numDigits = (int)logDigits;
            int currNum = i;
            
            boolean isValid = true;
            for(int j = numDigits; j >= 0; j--){
                int tenPow = (int) Math.pow(10, j);
                int digit = (int) Math.floor(currNum / tenPow);
                if(digit == 0 || i % digit != 0){
                    isValid = false;
                    break;
                }
                currNum -= digit*tenPow;
            }
            if(isValid){
                retList.add(i);
            }
        }
        return retList;
    }
}
