class Solution:
    """Math only"""
    
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
        

# class Solution:
#     def addDigits(self, num: int) -> int:
#         seen = set()
#         while num not in seen:
#             seen.add(num)
#             num = getDigitSum(num)
        
#         return num
        
    
# def getDigitSum(num):
#     sum = 0
        
#     while num > 0:
#         sum += num % 10
#         num //= 10

#     return sum
        
        
            