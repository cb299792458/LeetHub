class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        prof = [t for t in transactions if t[1]>t[0]]
        loss = [t for t in transactions if t[1]<=t[0]]
        # lowest money right before last gain
        loss.sort(key = lambda t: t[1])
        
        money,lowest = 0,0
        for cost, gain in loss:
            money -= cost
            lowest = min(money, lowest)
            money += gain
        
        if prof:
            money -= max(cost for cost,_ in prof)
            lowest = min(money, lowest)
            
        return -lowest