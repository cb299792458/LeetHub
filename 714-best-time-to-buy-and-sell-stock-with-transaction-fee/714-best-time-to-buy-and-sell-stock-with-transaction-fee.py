class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        withstock=[-prices[0]]
        without=[0]
        # prices.pop()
        
        for price in prices[1:]:
            # buy
            buy = without[-1] - price
            
            # sell
            sell = price + withstock[-1] - fee
            
            withstock.append(max(buy,withstock[-1]))
            without.append(max(sell,without[-1]))
            
        return max(withstock[-1],without[-1])