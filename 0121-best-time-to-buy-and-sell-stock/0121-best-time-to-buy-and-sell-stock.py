class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy = prices[0]
        
        for curr in prices[1:]:
            buy = min(buy,curr)
            best = max(best, curr - buy)
        
        return best