class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sod = 0
        pod = 1
        
        while n > 0:
            d = n%10
            n //= 10
            
            
            sod += d
            pod *= d
        
        return pod - sod