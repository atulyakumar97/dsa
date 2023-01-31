class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for banks in accounts:
            w = 0
            for wealth in banks:
                w += wealth
            
            if w > max_wealth:
                max_wealth = w
        return max_wealth