class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        
        for curr in prices[1:]:
            # sell today
            if curr - buy > profit:
                profit = curr - buy
                
            # buy today
            if curr < buy:
                buy = curr
        
        return profit