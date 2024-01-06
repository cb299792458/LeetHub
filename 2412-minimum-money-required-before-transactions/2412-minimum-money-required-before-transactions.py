class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        prof = [t for t in transactions if t[1]>t[0]]
        loss = [t for t in transactions if t[1]<=t[0]]
        
        prof.sort(key = lambda t: -t[0])
        loss.sort(key = lambda t: t[1])
        
        money,lowest = 0,0
        for cost, gain in loss:
            money -= cost
            lowest = min(money, lowest)
            money += gain
        
        if prof:
            money -= max(t[0] for t in prof)
            lowest = min(money, lowest)
            
        return -lowest