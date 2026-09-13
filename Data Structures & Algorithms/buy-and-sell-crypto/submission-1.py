class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap = prices[0]
        maxprofit = 0
        for i in range(len(prices)):
            cheap = min(prices[i], cheap)
            maxprofit = max(prices[i]-cheap, maxprofit)
        
        return maxprofit
            
            
