class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        
        for curr in prices[1:]:
            profit = max(profit, curr - buy)
            buy = min(buy, curr)
        
        return profit