class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 10**4
        
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price-buy)
        return profit