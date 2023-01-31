class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while num!=0:
            digit = num % 10
            num = num // 10
            digits.append(digit)
            
        digits.sort()
        sum = digits[0]*10 + digits[2] + digits[1]*10 + digits[3]
        
        return sum
