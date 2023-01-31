class Solution {
    public int findNumbers(int[] nums) {
        int even_digits = 0;
        
        for (int i=0; i<nums.length; i++)
        {
            
            int nums_digits = 0;
            while(nums[i]!=0){
                nums_digits+= 1;
                nums[i] = nums[i]/10;
                
            }
            
            if (nums_digits%2 == 0){
                even_digits+=1;
            }
            
            
        }// end of for
        
        return even_digits;
        
    }//end of func
}