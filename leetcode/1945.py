class Solution:
    def getLucky(self, s: str, k: int) -> int:
        start = ""
        for char in s:
            start += str(ord(char) - 96)
        
        ans = 0
        
        for i in range(k):
            if i == 0:
                ans = self.transform(int(start))
            else:
                ans = self.transform(int(ans))
        
        return ans
    
    def transform(self, val):
        sum = 0
        while val > 0:
            d = val % 10
            val = val // 10
            
            sum += d
        
        return sum
            