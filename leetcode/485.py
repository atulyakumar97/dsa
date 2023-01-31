class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
    int max_ones = 0;
    int counter =0;
        
     for (int i = 0; i < nums.length; i++) {
    // Do something with element nums[i].
    if (nums[i] != 1){counter=0;}
    else {counter+=1;};
     if ( counter > max_ones){
         max_ones = counter;
     };
         }
        return max_ones;
    }
        
    }