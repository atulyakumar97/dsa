class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        carry = 0
        digits[i] = digits[i] + 1
                
        while i >= 0:
            
            digits[i] = digits[i] + carry
            
            if digits[i] > 9:
                carry = digits[i] // 10
                digits[i] = digits[i] % 10
            else:
                carry = 0
                        
            i -= 1
        
        if carry > 0:
            digits = [carry] + digits
        
        return digits