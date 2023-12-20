class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        low1,low2 = 10**20, 10**20
        for price in prices:
            if price<low1:
                low2=low1
                low1=price
            elif price<low2:
                low2=price
                
        return money-low1-low2 if low1+low2<=money else money