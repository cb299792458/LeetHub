class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        prices = []
        for shop in values:
            for price in shop:
                prices.append(price)
                
        prices.sort()
        
        return sum([price*(i+1) for i,price in enumerate(prices)])