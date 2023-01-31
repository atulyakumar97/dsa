class Solution:
    def countEven(self, num: int) -> int:
        
        c = 0
        
        for i in range(1, num+1):
            if sumDigit(i) % 2 == 0:
                c += 1
        
        return c

def sumDigit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    
    return sum