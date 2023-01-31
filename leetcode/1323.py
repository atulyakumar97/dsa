class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = str(num)
        ans = ""
        flag = True
        
        for char in nums:
            if char == '6' and flag:
                ans += '9'
                flag = False
            else:
                ans += char
            
        return int(ans)
            
            
            