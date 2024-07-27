class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10 ** 20
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        prices = defaultdict(lambda: defaultdict(lambda: INF))
        
        for c in alphabet:
            prices[c][c] = 0
        
        for (old, new, price) in zip(original, changed, cost):
            prices[old][new] = min(prices[old][new], price)
            
        for a in alphabet:
            for b in alphabet:
                for c in alphabet:
                    prices[b][c] = min(prices[b][c], prices[b][a] + prices[a][c])
        
        res = sum(prices[s][t] for (s,t) in zip(source,target))
        return res if res < INF else -1