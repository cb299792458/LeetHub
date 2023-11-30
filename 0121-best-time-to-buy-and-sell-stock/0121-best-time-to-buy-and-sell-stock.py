class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy = prices[0]
        
        for curr in prices[1:]:
            # if curr < buy:
            #     buy = curr
            buy = min(buy,curr)
            
            # if curr - buy > best:
            #     best = curr - buy
            best = max(best, curr - buy)
        
        return best