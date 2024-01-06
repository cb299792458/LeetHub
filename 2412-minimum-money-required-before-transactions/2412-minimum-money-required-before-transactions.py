class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        prof = [t for t in transactions if t[1]>t[0]]
        loss = [t for t in transactions if t[1]<=t[0]]
        
        # lowest money right before last gain
        loss.sort(key = lambda t: t[1])
        
        money = 0
        for cost, gain in loss[:-1]:
            money -= cost
            money += gain
            
        if loss:
            money -= loss[-1][0]
        if not prof:
            return -money
        
        lowest = money
        
        if loss:
            money += loss[-1][1]
        money -= max(t[0] for t in prof)
                     
        lowest = min(lowest, money)
        return -lowest
