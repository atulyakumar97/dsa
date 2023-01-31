class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True        
        elif num % 10 == 0:
            return False
        else:
            return True
        
# Trivial solution
# class Solution:
#     def isSameAfterReversals(self, num: int) -> bool:
#         return reverseDigit(reverseDigit(num)) == num
    
# def reverseDigit(n):
#     rev = 0

#     while n > 0:

#         rev = rev * 10 + n % 10
#         n //= 10

#     return rev