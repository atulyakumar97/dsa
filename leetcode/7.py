class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        copy = abs(x)
        if x < 0:
            sign = -1
        else:
            sign = 1
        
        while copy > 0:
            
            digit = copy % 10
            rev = rev * 10 + digit
            copy //= 10
        
        ans = rev*sign
        
        if ans < -(2**31) or ans > (2**31) - 1:
            return 0
        else:
            return ans
        
        