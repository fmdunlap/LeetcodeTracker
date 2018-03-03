class Solution {
    public boolean validPalindrome(String s) {
        boolean deletedFront = false;
        boolean deletedRear = false;
        for(int i = 0; i < s.length() / 2; i++){
            int shiftFront = deletedFront? 1:0;
            int shiftRear = deletedRear? 1:0;
            
            char frontChar = s.charAt(i + shiftFront);
            char rearChar = s.charAt(s.length() - i - 1 - shiftRear);
            
            if(frontChar != rearChar){
                if(!deletedFront && !deletedRear){
                    if(s.charAt(i+1) == rearChar){
                        deletedFront = true;
                    } else if(s.charAt(s.length() - i - 2) == frontChar){
                        deletedRear = true;
                    } else {
                        return false;
                    }
                } else {
                    //Check if the prior delete was not correct
                    if(deletedFront && !deletedRear && s.charAt(i-1) == s.charAt(s.length() - i - 1)){
                        deletedFront = false;
                        deletedRear = true;
                    } else if(!deletedFront && deletedRear && s.charAt(i) == s.charAt(s.length() - i - 2)){
                        deletedFront = true;
                        deletedRear = false;
                    } else {
                        return false;
                    }
                }
            }
            
        }
        return true;
    }
}
